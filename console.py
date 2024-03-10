#!/usr/bin/python3
""" This module contains the console class for the console. """

import cmd

class HBNBCommand(cmd.Cmd):
    """ This class contains the console for the HBnB project. """

    prompt = "(hbnb) "
    file = None

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

    def emptyline(self):
        """ Do nothing on empty input """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
