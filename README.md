# Keysight_33000_FuncGen_and_Digitimer_D188_Control
A simple package for controlling a Keysight 33000 Series Function Generator and a Digitimer D188, for lab use in stimulation studies.

## Installation

1. Using Windows Powershell, clone the repo with:
```
git clone https://github.com/coleslatt/Keysight_33000_FuncGen_and_Digitimer_D188_Control.git
```

2. In Powershell, navigate to your repo directory with (replace with your own path):
```
cd "C:\your\path\to\Keysight_33000_FuncGen_and_Digitimer_D188_Control"
```

3. Run setup script with:
```
.\setup_env.ps1
```
## Usage

1. Activate python using:
```
.\.venv\Scripts\python.exe
```

2. Then, run:
```
from FuncGen_Selector_Function import func_gen_control_stateful as fg
```

3. Now, we can make update the state of the function generator with commands like:
```
fg(freq=30)
```



