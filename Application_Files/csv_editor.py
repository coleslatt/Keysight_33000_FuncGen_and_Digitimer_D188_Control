"""Small, reusable CSV editor dialogs for the stimulation interface."""

from __future__ import annotations

import csv
import io
from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets


def read_numeric_csv_file(path: Path, *, allow_negative: bool = True) -> list[float]:
    """Read a headerless, one-column numeric CSV and validate every row."""
    with Path(path).open("r", newline="", encoding="utf-8-sig") as csv_file:
        rows = list(csv.reader(csv_file))

    if not rows:
        raise ValueError("CSV is empty.")

    values: list[float] = []
    for row_number, row in enumerate(rows, start=1):
        if len(row) != 1:
            raise ValueError(
                f"Row {row_number} must contain exactly one column."
            )

        cell = row[0]
        if not cell.strip():
            raise ValueError(f"Row {row_number} is blank.")
        if cell != cell.strip():
            raise ValueError(
                f"Row {row_number} contains leading or trailing spaces."
            )

        try:
            value = float(cell)
        except ValueError as exc:
            raise ValueError(
                f"Row {row_number} must contain a numeric value."
            ) from exc

        if not allow_negative and value < 0:
            raise ValueError(f"Row {row_number} must be greater than or equal to 0.")
        values.append(value)

    return values


class CsvValueTable(QtWidgets.QTableWidget):
    """One-column table with spreadsheet-like paste and delete behavior."""

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.matches(QtGui.QKeySequence.Paste):
            self._paste_clipboard()
            return
        if event.key() in (QtCore.Qt.Key_Delete, QtCore.Qt.Key_Backspace):
            for item in self.selectedItems():
                item.setText("")
            return
        super().keyPressEvent(event)

    def _paste_clipboard(self) -> None:
        text = QtWidgets.QApplication.clipboard().text()
        if not text:
            return

        # Excel and other spreadsheet applications place tab-separated rows on
        # the clipboard. Also accept a regular one-column comma-separated block.
        lines = text.rstrip("\r\n").splitlines()
        values: list[str] = []
        for line in lines:
            row = next(csv.reader([line], delimiter="\t" if "\t" in line else ","))
            if len(row) != 1:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Cannot Paste",
                    "Paste one column of values at a time.",
                )
                return
            values.append(row[0])

        start_row = self.currentRow()
        if start_row < 0:
            start_row = self.rowCount()
        while self.rowCount() < start_row + len(values):
            self.insertRow(self.rowCount())
        for offset, value in enumerate(values):
            self.setItem(start_row + offset, 0, QtWidgets.QTableWidgetItem(value))


class NumericCsvEditorDialog(QtWidgets.QDialog):
    """Editor for the headerless, one-column numeric CSVs used by Burst Mode."""

    file_saved = QtCore.Signal(str)

    def __init__(
        self,
        parent: QtWidgets.QWidget | None = None,
        *,
        path: Path | None = None,
        title: str = "CSV Editor",
        column_title: str = "Value",
        allow_negative: bool = True,
        default_directory: Path | None = None,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(500, 600)
        self._path = Path(path) if path else None
        self._allow_negative = allow_negative
        self._default_directory = Path(default_directory or Path.cwd())
        self._dirty = False
        self._loading = False

        layout = QtWidgets.QVBoxLayout(self)

        self.path_label = QtWidgets.QLabel()
        self.path_label.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByMouse
        )
        self.path_label.setWordWrap(True)
        layout.addWidget(self.path_label)

        help_label = QtWidgets.QLabel(
            "Double-click a cell to edit it. You can also paste one column "
            "copied from Excel."
        )
        help_label.setWordWrap(True)
        layout.addWidget(help_label)

        self.table = CsvValueTable(self)
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels([column_title])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems
        )
        self.table.itemChanged.connect(self._mark_dirty)
        layout.addWidget(self.table)

        edit_buttons = QtWidgets.QHBoxLayout()
        add_button = QtWidgets.QPushButton("Add Row")
        insert_button = QtWidgets.QPushButton("Insert Row")
        remove_button = QtWidgets.QPushButton("Remove Selected Rows")
        add_button.clicked.connect(self._add_row)
        insert_button.clicked.connect(self._insert_row)
        remove_button.clicked.connect(self._remove_selected_rows)
        edit_buttons.addWidget(add_button)
        edit_buttons.addWidget(insert_button)
        edit_buttons.addWidget(remove_button)
        edit_buttons.addStretch()
        layout.addLayout(edit_buttons)

        file_buttons = QtWidgets.QHBoxLayout()
        open_button = QtWidgets.QPushButton("Open CSV...")
        save_button = QtWidgets.QPushButton("Save")
        save_as_button = QtWidgets.QPushButton("Save As...")
        close_button = QtWidgets.QPushButton("Close")
        open_button.clicked.connect(self._choose_file)
        save_button.clicked.connect(lambda: self.save())
        save_as_button.clicked.connect(lambda: self.save(save_as=True))
        close_button.clicked.connect(self.close)
        file_buttons.addWidget(open_button)
        file_buttons.addStretch()
        file_buttons.addWidget(save_button)
        file_buttons.addWidget(save_as_button)
        file_buttons.addWidget(close_button)
        layout.addLayout(file_buttons)

        if self._path:
            try:
                self._load(self._path)
            except Exception as exc:
                QtWidgets.QMessageBox.critical(
                    self, "CSV Error", f"Could not open the CSV:\n{exc}"
                )
                self._path = None
                self._set_rows([""])
        else:
            self._set_rows([""])
        self._update_path_label()

    def _set_rows(self, values: list[str]) -> None:
        self._loading = True
        try:
            self.table.setRowCount(len(values))
            for row, value in enumerate(values):
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(value))
        finally:
            self._loading = False
        self._dirty = False

    def _load(self, path: Path) -> None:
        values = read_numeric_csv_file(
            path, allow_negative=self._allow_negative
        )
        self._path = Path(path)
        self._set_rows([str(value) for value in values])
        self._update_path_label()

    def _choose_file(self) -> None:
        path_str, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open CSV",
            str(self._path.parent if self._path else self._default_directory),
            "CSV Files (*.csv);;All Files (*)",
        )
        if not path_str:
            return
        if self._dirty and not self._confirm_discard():
            return
        try:
            self._load(Path(path_str))
        except Exception as exc:
            QtWidgets.QMessageBox.critical(
                self, "CSV Error", f"Could not open the CSV:\n{exc}"
            )

    def _add_row(self) -> None:
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(""))
        self.table.setCurrentCell(row, 0)
        self.table.editItem(self.table.item(row, 0))
        self._dirty = True

    def _insert_row(self) -> None:
        row = self.table.currentRow()
        if row < 0:
            row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(""))
        self.table.setCurrentCell(row, 0)
        self.table.editItem(self.table.item(row, 0))
        self._dirty = True

    def _remove_selected_rows(self) -> None:
        rows = sorted(
            {index.row() for index in self.table.selectedIndexes()}, reverse=True
        )
        if not rows and self.table.currentRow() >= 0:
            rows = [self.table.currentRow()]
        for row in rows:
            self.table.removeRow(row)
        if rows:
            self._dirty = True

    def _mark_dirty(self) -> None:
        if not self._loading:
            self._dirty = True

    def _table_values(self) -> list[str]:
        if self.table.rowCount() == 0:
            raise ValueError("Add at least one row before saving.")

        values: list[str] = []
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            text = item.text() if item else ""
            if not text.strip():
                raise ValueError(f"Row {row + 1} is blank.")
            if text != text.strip():
                raise ValueError(
                    f"Row {row + 1} contains leading or trailing spaces."
                )
            try:
                value = float(text)
            except ValueError as exc:
                raise ValueError(
                    f"Row {row + 1} must contain a numeric value."
                ) from exc
            if not self._allow_negative and value < 0:
                raise ValueError(
                    f"Row {row + 1} must be greater than or equal to 0."
                )
            values.append(text)
        return values

    def save(self, *, save_as: bool = False) -> bool:
        try:
            values = self._table_values()
        except ValueError as exc:
            QtWidgets.QMessageBox.warning(self, "Invalid CSV", str(exc))
            return False

        path = None if save_as else self._path
        if path is None:
            path_str, _ = QtWidgets.QFileDialog.getSaveFileName(
                self,
                "Save CSV",
                str(self._default_directory),
                "CSV Files (*.csv);;All Files (*)",
            )
            if not path_str:
                return False
            path = Path(path_str)
            if path.suffix.lower() != ".csv":
                path = path.with_suffix(".csv")

        output = io.StringIO(newline="")
        writer = csv.writer(output, lineterminator="\n")
        for value in values:
            writer.writerow([value])

        save_file = QtCore.QSaveFile(str(path))
        if not save_file.open(QtCore.QIODevice.OpenModeFlag.WriteOnly):
            QtWidgets.QMessageBox.critical(
                self, "Save Error", f"Could not open the file for writing:\n{path}"
            )
            return False
        save_file.write(output.getvalue().encode("utf-8"))
        if not save_file.commit():
            QtWidgets.QMessageBox.critical(
                self, "Save Error", f"Could not finish saving:\n{path}"
            )
            return False

        self._path = path
        self._dirty = False
        self._update_path_label()
        self.file_saved.emit(str(path))
        return True

    def _update_path_label(self) -> None:
        self.path_label.setText(
            f"File: {self._path}" if self._path else "File: New CSV (not saved)"
        )

    def _confirm_discard(self) -> bool:
        answer = QtWidgets.QMessageBox.question(
            self,
            "Unsaved Changes",
            "Discard the unsaved changes?",
            QtWidgets.QMessageBox.StandardButton.Discard
            | QtWidgets.QMessageBox.StandardButton.Cancel,
            QtWidgets.QMessageBox.StandardButton.Cancel,
        )
        return answer == QtWidgets.QMessageBox.StandardButton.Discard

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if not self._dirty:
            event.accept()
            return

        answer = QtWidgets.QMessageBox.question(
            self,
            "Unsaved Changes",
            "Save changes before closing?",
            QtWidgets.QMessageBox.StandardButton.Save
            | QtWidgets.QMessageBox.StandardButton.Discard
            | QtWidgets.QMessageBox.StandardButton.Cancel,
            QtWidgets.QMessageBox.StandardButton.Save,
        )
        if answer == QtWidgets.QMessageBox.StandardButton.Save:
            event.accept() if self.save() else event.ignore()
        elif answer == QtWidgets.QMessageBox.StandardButton.Discard:
            event.accept()
        else:
            event.ignore()
