#!/usr/bin/python3
"""Create the cmd interpreter"""


import cmd
import sys
import models
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """cmd prompt with handling the EOF and quit
        an empty line + ENTER shouldnt execute anything
        code should not be executed when imported"""

    prompt = '(hbnb) '
    cmd_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
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
        else:
            cls_name = cls.split()[0]
            if cls_name in self.cmd_classes and issubclass(self.cmd_classes[cls_name], BaseModel):  # noqa
                new_instance = self.cmd_classes[cls_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""  # noqa
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
        """Prints all string representation of all instances based or not on the class name  # noqa
            Ex: $ all BaseModel or $ all"""

        if not cls:
            print([str(obj) for obj in storage.all().values()])

        elif cls not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")

        else:
            print([str(obj) for obj in storage.all().values() if isinstance(obj, HBNBCommand.cmd_classes[cls])])  # noqa

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or updating attribute  # noqa
            Usage: update <class name> <id> <attribute name> "<attribute value>" """  # noqa
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
