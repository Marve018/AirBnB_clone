#!/usr/bin/python3

"""
    A prog that contains the entry point of the
    command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Representing the command interpreter"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        classes = {"BaseModel": BaseModel}

        if line not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[line]()
        new_instance.save()
        print(new_instance.id)


    def do_show(self, line):
        """
            Prints the string representation of an
            instance based on class name and ID
        """
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        classes = {"BaseModel": BaseModel}  # Add other classes here as needed

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])
        

    def do_destroy(self, line):
        """Deletes an instance based on class name and ID"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        classes = {"BaseModel": BaseModel}

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """
            Prints all string representations of
            instances based or not on class name
        """
        classes = {"BaseModel": BaseModel}

        if line not in classes and line:
            print("** class doesn't exist **")
            return

        instances = [str(value) for key, value in storage.all().items()
                     if not line or value.__class__.__name__ == line]

        print(instances)

    
    def do_update(self, line):
        """
            Updates an instance based on class name and
            ID by adding or updating an attribute
        """
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        classes = {"BaseModel": BaseModel}

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** attribute name missing **")
            return

        if len(args) < 5:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attr_name = args[3]
        attr_value = args[4].strip('"')

        if hasattr(instance, attr_name):
            attr_value = type(getattr(instance, attr_name))(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")


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
