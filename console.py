#!/usr/bin/python3
"""Create the cmd interpreter"""


import cmd, sys
import models
from models.base_model import BaseModel
from models import storage


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
        else:
            cls_name = cls.split()[0]
            if cls_name in self.cmd_classes and issubclass(self.cmd_classes[cls_name], BaseModel):
                new_instance = self.cmd_classes[cls_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **") 
        
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
            temp_key = arr[0] + "." + arr[1]
            temp_obj = storage.all()
            if temp_key not in temp_obj:
                print("** no instance found **")
            else:
                print(temp_obj[temp_key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()