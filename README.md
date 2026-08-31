# Python - Environment & First Programs

    Novice
    By: Javier Valenzani
    Weight: 1
    Your score will be updated as you progress.

## Introduction & Context

Python can execute code in two primary ways:

- Interactively, using the interpreter (REPL).
- By executing a script file.

Professional software development requires understanding both execution modes, how tools are installed, and how environments influence behavior.

This project builds a structured mental model:

- How the interpreter evaluates expressions and statements.
- How a script differs from interactive execution.
- How development tools are installed using pip.
- Why global installations can create conflicts.
- How virtual environments isolate dependencies.

## Learning Objectives

By the end of this project, you should be able to:

- Distinguish between expressions and statements in the interpreter.
- Predict when output will appear automatically in interactive mode.
- Create a portable, executable Python script.
- Install and use a development tool via pip.
- Explain the difference between global installations and isolated environments.
- Demonstrate dependency isolation using venv.

## Resources

- [Python Tutorial — Using the Interpreter](https://docs.python.org/3/tutorial/interpreter.html)

- [Python Standard Library — venv](https://docs.python.org/3/library/venv.html)

- [pip User Guide (overview)](https://pip.pypa.io/en/stable/user_guide/)

- [pycodestyle documentation](https://pycodestyle.pycqa.org/en/latest/)

### General Requirements

- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:

  - #!/usr/bin/env python3

- Every Python file must:
    - Be executable.
    - End with a newline.
    - Be PEP8 compliant (pycodestyle 2.7.x).
- Output must match expected formatting exactly.
- No external libraries are allowed unless explicitly requested.
