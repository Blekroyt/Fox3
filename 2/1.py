#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from Packet.add import add
from Packet.list import list
from Packet.select import select
from Packet.help import help

def main():
    spisok = []
    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            sp = add()
            spisok.append(sp)
        elif command == "list":
            list(spisok)
        elif command.startswith("select"):
            name = input("Введите имя человека ")
            select(spisok, name)
        elif command == "help":
            help()
        else:
            print(f"неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()