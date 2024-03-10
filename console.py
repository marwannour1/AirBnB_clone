#!/usr/bin/python3
""" This module contains the console class for the console. """


import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """ Create a new instance of BaseModel, save it
        (to the JSON file) and print the id """
        if not arg:
            print("** class name missing **")
        else:
            if arg == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] == "BaseModel":
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file) """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] == "BaseModel":
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints all string representation of all instances based
        or not on the class name """
        if not arg:
            for key, value in storage.all().items():
                print(value)
        else:
            args = arg.split()
            if args[0] == "BaseModel":
                for key, value in storage.all().items():
                    print(value)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file) """

        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] == "BaseModel":
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in storage.all():
                        if len(args) < 3:
                            print("** attribute name missing **")
                        elif len(args) < 4:
                            print("** value missing **")
                        else:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
