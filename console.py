#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


def parse(args):
    list = args.split()
    return list


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {"BaseModel", "User"}

    def do_quit(self, line):
        "Quits console"
        return True

    def do_EOF(self, line):
        "Exits console"
        return True

    def do_create(self, line):
        """Create a new class object and save it"""
        if len(line) == 0:
            print("** class name missing **")
        elif line in self.__classes:
            newbase = BaseModel()
            print(newbase.id)
            newbase.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Shows an instance of a class using the
        class name and id
        """

        args = parse(line)

        objects = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" in objects:
            print(objects[f"{args[0]}.{args[1]}"])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Destroy a class instance using
        the class name and id
        """
        args = parse(line)
        objects = storage.all()

        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" in objects:
            del objects[f"{args[0]}.{args[1]}"]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints a list of strings of all
        class instances
        """
        args = parse(line)
        objects = storage.all()

        if len(args) > 1 and args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            list_objects = []
            for obj in objects.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    list_objects.append(obj.__str__())
                else:
                    list_objects.append(obj.__str__())
            print(list_objects)

    def do_update(self, line):
        """
        update a class instance using
        the class name and id
        """
        args = parse(line)
        attribute = args[2]
        value = args[3].replace('"', "")
        objects = storage.all()

        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")

        if len(args) == 4:
            obj = objects["{}.{}".format(args[0], args[1])]
            if attribute in obj.to_dict().keys():
                cast = type(getattr(obj, attribute))
                setattr(obj, attribute, cast(value))
            else:
                setattr(obj, attribute, value)
                
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
