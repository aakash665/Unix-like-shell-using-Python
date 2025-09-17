# Unix-like-shell-using-Python

A lightweight custom shell written in Python.  
It provides a set of basic Unix-like commands for working with files, directories, and system information.  

---

## Features  

- List files and directories  
- Show current working directory  
- Read and truncate files  
- Copy, remove, or empty files  
- Display date, time, and IP address  
- Change directory  
- Clear the screen  
- Exit the shell  

---

## Installation  

1. Make sure you have **Python 3.7+** installed.  
2. Clone or download this repository.  
3. Run the shell:  

## Commands  

| Command        | Usage                              | Description                                   |
|----------------|------------------------------------|-----------------------------------------------|
| `list`         | `list`                             | List files and directories in current folder   |
| `dirs`         | `dirs`                             | List only directories                         |
| `date`         | `date`                             | Show current date (`dd-mon-yyyy`)             |
| `time`         | `time` / `time -hours` / `time -mins` / `time -secs` | Show current time or parts of time |
| `pwd`          | `pwd`                              | Show current working directory                |
| `ipconfig`     | `ipconfig`                         | Show local IP address                         |
| `cat`          | `cat <file>`                       | Print file contents                           |
| `head`         | `head -N <file>`                   | Show first N lines of a file                  |
| `tail`         | `tail -N <file>`                   | Show last N lines of a file                   |
| `cd`           | `cd <dir>`                         | Change current directory                      |
| `copy_file`    | `copy_file <src> <dest>`           | Copy a file                                   |
| `remove_file`  | `remove_file <file>`               | Delete a file                                 |
| `empty_file`   | `empty_file <file>`                | Empty (truncate) a file                       |
| `clear`        | `clear`                            | Clear the screen                              |
| `exit`         | `exit`                             | Exit the shell                                |

---



