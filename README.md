Overview

The Mini Shell Implementation is a Python-based graphical command-line simulator built using Tkinter. It recreates the behavior of a basic Unix-like shell within a graphical interface. This project demonstrates how shell commands are interpreted, executed, and managed internally, while integrating a user-friendly GUI for easier interaction.

This program allows users to execute both built-in and external system commands. Built-in commands include basic file and directory operations such as ls, cd, pwd, mkdir, rmdir, rm, touch, write, cat, and date. External commands are executed using Python’s subprocess module. The shell also supports command history navigation using the arrow keys and provides color-coded output for information, errors, and prompts.

**Features**

GUI-based terminal built using Tkinter

Supports common shell commands: ls, cd, pwd, mkdir, rmdir, rm, touch, write, cat, date, and exit

Executes external system commands via subprocess

Command history navigation using up and down arrow keys

Real-time clock displayed in the title bar

Status bar showing the current working directory

Clear output button for quick screen reset

Color-coded output for better readability

Error handling for invalid commands

**Technologies Used**

Language: Python

Libraries:

tkinter – GUI framework

os – Directory and file operations

subprocess – System command execution

datetime – Date and time display

getpass – User identification

How to Run

Clone the repository:

git clone https://github.com/<your-username>/Mini-Shell-Implementation.git
cd Mini-Shell-Implementation


Run the program:

python main4.py


Type your commands in the input bar and press Enter or click Run.

Example Usage
Welcome user! Terminal started in /home/user
Type commands like ls, cd, pwd, date, mkdir, rm, etc.

user@shell:/home/user$ ls
Documents
Downloads
Desktop

Learning Objectives

Understanding how shells interpret and execute commands

Familiarity with process creation and system calls in Python

Experience with file handling and string parsing

Practical knowledge of Tkinter GUI development

Author

Ananya Patel
