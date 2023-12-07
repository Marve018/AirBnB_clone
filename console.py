#!/usr/bin/python3

"""
    A prog that contains the entry point of the
    command interpreter
"""
import cmd
from models import classes
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """Representing the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Command to quit the program"""
        return True

    def do_EOF(self, line):
        """Command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when the enter key is pressed without a command"""
        pass

    def help_quit(self):
        """Message printed for the do_quit method"""
        print("program quitted")

    def help_EOF(self):
        """Message printed for the do_EOF method"""
        print("program exitted")

    def default(self, line):
        """Message printed when the command is unknown"""
        print("input a valid command")

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        arg = shlex.split(line)
        if not (line):
            print("** class name missing **")
            return

        try:
            exs_clss = classes[line]
        except Exception:
            print("** class doesn't exist **")
            return
        else:
            instance = classes[line]()
            instance.save()
            print(instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
