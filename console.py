#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        "Quits console"
        return True

    def do_EOF(self, line):
        "Exits console"
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
