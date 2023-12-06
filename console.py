#!/usr/bin/python3

"""
    A prog that contains the entry point of the
    command interpreter
"""
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
