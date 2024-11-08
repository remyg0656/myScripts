from cx_Freeze import setup, Executable

build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None


executables = [
    Executable("mouseMove.py", base=base, target_name = 'mouseMove')
]

packages = ["tkinter", "threading", "time", "queue", "mouse", "datetime", "sys"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}

setup(
    name = "MoveMouse",
    options = options,
    version = "1.0",
    description = 'Programme qui permet de faire bouger la souris d un pixel vers la droite toute les 3mins',
    executables = executables
)