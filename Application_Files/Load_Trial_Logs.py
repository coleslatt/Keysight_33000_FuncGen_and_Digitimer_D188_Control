import json
from pathlib import Path
from dataclasses import asdict
from datetime import datetime
from Trial_Program import (
    BodyAnnotation,
    PatientBodyLog,
    PatientReport,
    TrialCondition,
    TrialLogEntry,
    ExperimentLog
)

def parse_datetime(value):
    if value in (None, ""):
        return None
    return datetime.fromisoformat(value)


def body_annotation_from_dict(data):
    return BodyAnnotation(
        x=data["x"],
        y=data["y"],
        note=data.get("note", ""),
        created_at=parse_datetime(data.get("created_at")) or datetime.now(),
    )


def patient_body_log_from_dict(data):
    return PatientBodyLog(
        annotations=[
            body_annotation_from_dict(ann)
            for ann in data.get("annotations", [])
        ],
        created_at=parse_datetime(data.get("created_at")) or datetime.now(),
    )


def patient_report_from_dict(data):
    patient_log_data = data.get("patient_log", None)

    if isinstance(patient_log_data, dict):
        patient_log = patient_body_log_from_dict(patient_log_data)
    else:
        patient_log = patient_log_data

    return PatientReport(
        current_intensity_ma=data.get("current_intensity_ma", 0.0),
        patient_log=patient_log,
        current_time=parse_datetime(data.get("current_time")) or datetime.now(),
    )


def trial_condition_from_dict(data):
    return TrialCondition(
        electrode_config=data.get("electrode_config", ""),
        waveform=data.get("waveform", ""),
        polarity=data.get("polarity", ""),
    )


def trial_log_entry_from_dict(data):
    return TrialLogEntry(
        current_time=parse_datetime(data.get("current_time")) or datetime.now(),
        condition=trial_condition_from_dict(data.get("condition", {})),
        displayed_status=data.get("displayed_status", ""),
        patient_reports=[
            patient_report_from_dict(report)
            for report in data.get("patient_reports", [])
        ],
    )


def experiment_log_from_dict(data):
    return ExperimentLog(
        start_time=parse_datetime(data.get("start_time")) or datetime.now(),
        trial_logs=[
            trial_log_entry_from_dict(entry)
            for entry in data.get("trial_logs", [])
        ],
    )

def load_experiment_log_json(path):
    path = Path(path)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    experiment_log = experiment_log_from_dict(data)

    print(f"Loaded experiment log JSON from: {path}")
    return experiment_log


