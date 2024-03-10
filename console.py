#!/usr/bin/python3
""" This module contains the console class for the console. """


import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
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

            new_instance = None
            if arg == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

            elif arg == "User":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)

            elif arg == "Place":
                new_instance = Place()
                new_instance.save()
                print(new_instance.id)

            elif arg == "City":
                new_instance = City()
                new_instance.save()
                print(new_instance.id)

            elif arg == "State":
                new_instance = State()
                new_instance.save()
                print(new_instance.id)

            elif arg == "Amenity":
                new_instance = Amenity()
                new_instance.save()
                print(new_instance.id)

            elif arg == "Review":
                new_instance = Review()
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
            if args[0] in ("BaseModel", "User", "Place", "City", "State",
                           "Amenity", "Review"):
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
            if args[0] in ("BaseModel", "User", "Place", "City", "State",
                           "Amenity", "Review"):
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
            if args[0] in ("BaseModel", "User", "Place", "City", "State",
                           "Amenity", "Review"):
                for key, value in storage.all().items():
                    if args[0] in key:
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
            if args[0] in ("BaseModel", "User", "Place", "City", "State",
                           "Amenity", "Review"):
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

    def default(self, arg):
        """ Default method for the console """
        args = arg.split(".")
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                count = 0
                for key in storage.all().keys():
                    if args[0] in key:
                        count += 1
                print(count)
            elif args[1][0:5] == "show(":
                new_arg = args[1][5:-1]
                new_arg = args[0] + " " + new_arg.replace(",",
                                                          " ").replace("\"",
                                                                       " ")
                self.do_show(new_arg)
            elif args[1][0:8] == "destroy(":
                new_arg = args[1][8:-1]
                new_arg = args[0] + " " + new_arg.replace(",",
                                                          " ").replace("\"",
                                                                       " ")
                self.do_destroy(new_arg)
                return
            elif args[1][0:7] == "update(":
                new_arg = args[1][7:-1]
                new_arg = args[0] + " " + new_arg.replace(",",
                                                          " ").replace("\"",
                                                                       " ")
                self.do_update(new_arg)
            else:
                print("*** Unknown syntax: {}".format(arg))
                return False
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False


if __name__ == '__main__':

    HBNBCommand().cmdloop()
