<details>
<summary> Python - Environment & First Programs </summary>


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


## Task
<details>
<summary> 0. Interpreter Reasoning </summary>

Start the Python interpreter:

    python3

Inside the interpreter:

- Evaluate a mathematical expression.
- Assign a value to a variable.
- Enter the variable name alone.
- Use print() with that variable.
- Evaluate a comparison expression.

Observe carefully:

- When Python displays output automatically.
- When it does not.
- What role print() plays.

Reflect on why the behavior differs between expressions and statements.

</details>


<details>
<summary> 1. Deterministic Script Output</summary>

Create an executable file named structured_output.py that prints exactly:

    Language: Python
    Version: 3
    Pi approx: 3.14
    Computation valid: True

Constraints:

- The float must be derived from a numeric value and formatted to two decimals.
- The boolean must result from evaluating a comparison expression.
- At least one line must use formatted string interpolation.
- No input is allowed.

Execution example:

    ./structured_output.py

The output must match exactly.

    Repo:

        GitHub repository: holbertonschool-core-engineering
        Directory: python_fundamentals/hello_world
        File: structured_output.py
</details>

<details>
<summary>
2. Installing and Using `pycodestyle` with `pip`
</summary>

pip is the standard tool used to install Python packages and development tools.

When you run:

    pip install <package_name>

The package is typically installed globally for that Python installation unless a virtual environment is active.

Install pycodestyle using pip.

After installation, run:

    pycodestyle structured_output.py

If formatting errors are reported, correct your script until no errors remain.

When installing in the sandbox, you may see a warning such as:

    > WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead.

This warning appears because installing packages globally (especially as root) can affect the system Python environment.

On a personal machine, installing tools globally can:

- Create version conflicts.
- Affect other projects unexpectedly.
- Require elevated permissions.

This motivates the use of virtual environments.
</details>
<details>
<summary> 3. Virtual Environment Isolation
</summary>

A virtual environment is an isolated Python setup with its own interpreter and installed packages. The goal is to see, concretely, that installing a tool in one environment does not make it available in another.

The instructions below use Linux commands. On Windows, the process is similar, but activation commands differ.

### Create two environments

From the folder where you want to work, create two virtual environments:

    python3 -m venv alpha_env
    python3 -m venv beta_env

### Confirm activation changes “which Python”

Activate the first environment:

    source alpha_env/bin/activate

Confirm the Python interpreter being used:

    which python3
    python3 --version

Expected behavior:
- which python3 points inside alpha_env/ (a path containing alpha_env/bin/python3).
- The Python version prints normally (for example, Python 3.8.x).

### Install a tool in only one environment

While alpha_env is active, install pycodestyle:

    pip install pycodestyle

You may see a warning like:

>WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

What matters here:

- Packages installed with pip are global to the current Python environment.
- If a virtual environment is active, the installation is isolated to that environment.

Confirm pycodestyle is available:

    pycodestyle --version

Expected behavior:

- A version number is printed (for example, 2.7.x).

### Deactivate and switch environments

Deactivate the current environment:

    deactivate

Confirm you are no longer using the environment interpreter:

    which python3

Expected behavior:

- The path no longer contains alpha_env/.

Now activate the second environment:

    source beta_env/bin/activate

Confirm interpreter location again:

    which python3

Expected behavior:

- which python3 points inside beta_env/.

### Verify isolation

Check whether pycodestyle exists in beta_env:

    pycodestyle --version

Expected behavior:

- The command should fail (for example: command not found) or indicate it is not available.

This difference is the point: pycodestyle was installed only in alpha_env, so it should not appear in beta_env.

### Return to the first environment (switch back)

Deactivate beta_env:

    deactivate

Activate alpha_env again:

    source alpha_env/bin/activate

Confirm pycodestyle is available again:

    pycodestyle --version

Expected behavior:

- A version number is printed again.

</details>
</details>

<details>
<summary> Python - Control Flow </summary>

# Python - Control Flow

    Novice
    By: Javier Valenzani
    Weight: 1
    Your score will be updated as you progress.

## Introduction & Context

Programs become meaningful when they can make decisions and repeat actions. Control flow allows a program to:

- Execute different code depending on conditions.
- Repeat instructions using loops.
- Combine logical conditions to model real scenarios.

This project focuses exclusively on control flow using:

- if, elif, else
- Comparison operators
- Boolean logic
- while loops
- for loops with range()

The activities are adapted from the existing "Python - if/else, loops, functions" project, keeping only those aligned with control flow.

## Learning Objectives

By the end of this project, you should be able to:

- Write conditional statements using if, elif, and else.
- Use comparison and logical operators correctly.
- Control repetition using while and for loops.
- Reason about loop boundaries and iteration ranges.
- Generate formatted output using numeric iteration.
- Combine conditions and loops to produce deterministic output.

## Resources

- [Python Tutorial — Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Tutorial — More on Conditions](https://docs.python.org/3/reference/expressions.html#comparisons)

## General Requirements

- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:

        #!/usr/bin/env python3

- Every Python file must:
    - Be executable.
    - End with a newline.
    - Be PEP8 compliant (pycodestyle 2.7.x).

- No external libraries are allowed.

- No functions are allowed in this project.

- No imports are allowed.

- Output must match expected formatting exactly.

## Tasks

<details>
<summary> 0. Positive anything is better than negative nothing </summary>

Create a script that assigns a random integer to a variable named number. Copy the following line exactly as it is, after the shebang line.

    number = __import__('random').randint(-10, 10)

> The previous line will assign a random integer between -10 and 10 to the number variable. You don't need to focus on this yet.

Using conditional statements, print:

- <number> is positive if the number is greater than 0
- <number> is zero if the number equals 0
- <number> is negative if the number is less than 0

Example:

    spam@camelot:~/$ ./positive_or_negative.py
    -4 is negative
    spam@camelot:~/$ ./positive_or_negative.py
    0 is zero
    spam@camelot:~/$ ./positive_or_negative.py
    -3 is negative
    spam@camelot:~/$ ./positive_or_negative.py
    -10 is negative
    spam@camelot:~/$ ./positive_or_negative.py
    10 is positive

Repo:

    GitHub repository: holbertonschool-core-engineering
    Directory: python_fundamentals/control_flow
    File: positive_or_negative.py
