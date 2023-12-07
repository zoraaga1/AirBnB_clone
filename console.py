#!/usr/bin/python3
"""Create the cmd interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """cmd prompt with handling the EOF and quit
        an empty line + ENTER shouldnt execute anything
        code should not be executed when imported"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Handle EOF signal"""
        return True

    def do_quit(self,line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
