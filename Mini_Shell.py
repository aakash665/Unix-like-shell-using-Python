#!/usr/bin/env python3
import os
import shlex
import shutil
import socket
from datetime import datetime

def cmd_list(args):
    if args:
        print("list: takes no arguments")
        return
    for item in sorted(os.listdir(".")):
        if os.path.isdir(item):
            print(f"[DIR]  {item}")
        else:
            print(f"[FILE] {item}")

def cmd_dirs(args):
    if args:
        print("dirs: takes no arguments")
        return
    dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
    if not dirs:
        print("(no directories)")
    for d in sorted(dirs):
        print(d)

def cmd_date(args):
    if args:
        print("date: takes no arguments")
        return
    print(datetime.now().strftime("%d-%b-%Y").lower())

def cmd_time(args):
    now = datetime.now()
    if not args:
        print(now.strftime("%H:%M:%S"))
    elif args == ["-hours"]:
        print(now.strftime("%H"))
    elif args == ["-mins"]:
        print(now.strftime("%M"))
    elif args == ["-secs"]:
        print(now.strftime("%S"))
    else:
        print("time: usage: time | time -hours | time -mins | time -secs")

def cmd_ipconfig(args):
    if args:
        print("ipconfig: takes no arguments")
        return
    print(socket.gethostbyname(socket.gethostname()))

def cmd_pwd(args):
    if args:
        print("pwd: takes no arguments")
        return
    print(os.getcwd())

def cmd_cat(args):
    if len(args) != 1:
        print("cat: usage: cat <filename>")
        return
    try:
        with open(args[0], "r", encoding="utf-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        print(f"cat: {args[0]}: No such file")

def cmd_head(args):
    if len(args) != 2 or not args[0].startswith("-") or not args[0][1:].isdigit():
        print("head: usage: head -N <filename>")
        return
    n, fname = int(args[0][1:]), args[1]
    try:
        with open(fname, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= n: break
                print(line, end="")
    except FileNotFoundError:
        print(f"head: {fname}: No such file")

def cmd_tail(args):
    if len(args) != 2 or not args[0].startswith("-") or not args[0][1:].isdigit():
        print("tail: usage: tail -N <filename>")
        return
    n, fname = int(args[0][1:]), args[1]
    try:
        with open(fname, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-n:]:
                print(line, end="")
    except FileNotFoundError:
        print(f"tail: {fname}: No such file")

def cmd_cd(args):
    if len(args) != 1:
        print("cd: usage: cd <directory>")
        return
    try:
        os.chdir(args[0])
    except Exception as e:
        print("cd:", e)

def cmd_copy_file(args):
    if len(args) != 2:
        print("copy_file: usage: copy_file <src> <dest>")
        return
    try:
        shutil.copy2(args[0], args[1])
    except Exception as e:
        print("copy_file:", e)

def cmd_remove_file(args):
    if len(args) != 1:
        print("remove_file: usage: remove_file <filename>")
        return
    try:
        os.remove(args[0])
    except FileNotFoundError:
        print(f"remove_file: {args[0]}: No such file")

def cmd_empty_file(args):
    if len(args) != 1:
        print("empty_file: usage: empty_file <filename>")
        return
    open(args[0], "w").close()

def cmd_clear(args):
    if args:
        print("clear: takes no arguments")
        return
    os.system("cls")

def cmd_exit(args):
    if args:
        print("exit: takes no arguments")
        return
    raise SystemExit

COMMANDS = {
    "list": cmd_list, "dirs": cmd_dirs, "date": cmd_date, "time": cmd_time,
    "cat": cmd_cat, "cd": cmd_cd, "head": cmd_head, "tail": cmd_tail,
    "copy_file": cmd_copy_file, "remove_file": cmd_remove_file,
    "empty_file": cmd_empty_file, "ipconfig": cmd_ipconfig,
    "pwd": cmd_pwd, "clear": cmd_clear, "exit": cmd_exit
}

def main():
    while True:
        try:
            raw = input(f"My-shell[{os.path.basename(os.getcwd())}]> ")
            if not raw.strip(): continue
            parts = shlex.split(raw)
            cmd, args = parts[0], parts[1:]
            if cmd in COMMANDS:
                COMMANDS[cmd](args)
            else:
                print(f"{cmd}: invalid command")
        except (EOFError, KeyboardInterrupt):
            print()
        except SystemExit:
            break
        except Exception as e:
            print("error:", e)

if __name__ == "__main__":
    main()
