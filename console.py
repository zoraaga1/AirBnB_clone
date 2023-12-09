#!/usr/bin/python3
"""Create the cmd interpreter"""


import cmd, sys
import models
import re
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """cmd prompt with handling the EOF and quit
        an empty line + ENTER shouldnt execute anything
        code should not be executed when imported"""
    prompt = '(hbnb) '
    cmd_classes = {
            "BaseModel": BaseModel,
            }
    
    def cmdloop(self, intro=None):
        """Repeatedly issue a prompt, accept input, parse an initial prefix
    off the received input, and dispatch to action methods, passing them
    the remainder of the line as argument.
    """
        try:
            super().cmdloop(intro)
        except KeyboardInterrupt:
            sys.exit()
    
    
    def do_EOF(self, line):
        """Handle EOF signal"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, cls):
        """Creates new instance; save it to JSON file"""
        if not cls:
            print("** class name missing **")
        elif cls not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.cmd_classes[cls]()
            new_instance.save()
            print(new_instance.id)

        
    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        arr = args.split()
        if len(arr) == 0:
            print("** class name missing **")

        elif len(arr) < 2:
            print("** instance id missing **")

        elif arr[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")

        else:
            tempor_key = arr[0] + "." + arr[1]
            tempor_obj = storage.all()
            if tempor_key not in tempor_obj:
                print("** no instance found **")
            else:
                print(tempor_obj[tempor_key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        save the change into the JSON file"""
        arr = args.split()
        if len(arr) == 0:
            print("** class name missing **")

        elif arr[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        
        elif len(arr) < 2:
            print("** instance id missing **")

        else:
            temporary_key = arr[0] + "." + arr[1]
            temporary_obj = storage.all()
            if temporary_key not in temporary_obj:
                print("** no instance found **")
            else:
                del temporary_obj[temporary_key]
                storage.save()

    def do_all(self, cls):
        """Prints all string representation of all instances based or not on the class name
            Ex: $ all BaseModel or $ all"""
        if not cls:
            print([str(obj) for obj in storage.all().values()])
        elif cls not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all().values() if isinstance(obj, HBNBCommand.cmd_classes[cls])])

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or updating attribute 
            Usage: update <class name> <id> <attribute name> "<attribute value>" """
        arr = args.split()
        if len(arr) < 1:
            print("** class name missing **")

        elif arr[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")

        elif len(arr) < 2:
            print("** instance id missing **")

        elif len(arr) < 3:
            print("** attribute name missing **")

        elif len(arr) < 4:
            print("** value missing **")
        
        else:
            tempor_key = arr[0] + "." + arr[1]
            tempor_obj = storage.all()

            if tempor_key not in tempor_obj:
                print("** no instance found **")
            else:
                setattr(tempor_obj[tempor_key], arr[2], arr[3])
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()