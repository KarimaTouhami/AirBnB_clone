#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""Enter of CMD"""


class HBNBCommand(cmd.Cmd):
    """Implementation of CMD of AirBNB"""
    prompt = '(hbnb) '

    def do_quit(self, cmd):
        """Exit the program"""
        return True

    def do_EOF(self, cmd):
        """Exit the program"""
        return True

    def do_pass(self, cmd):
        """Do Nothing"""
        pass

    def do_create(self, cmd):
        """Creates a new instance of BaseModel"""
        if not cmd:
            print("** class name missing **")
        elif cmd not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[cmd]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, cmd):
        """Prints the string representation of an
        instance based on the class name and id
        """
        if len(cmd) == 0:
            print("** class name missing **")
        else:
            parts = cmd.split()
            if parts[0] not in globals():
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                class_name = parts[0]
                obj_id = parts[1]
                key = f"{class_name}.{obj_id}"
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, cmd):
        '''
        Deletes an instance based on the class name and id
        '''
        if len(cmd) == 0:
            print("** class name missing **")
        else:
            parts = cmd.split()
            if parts[0] not in globals():
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                class_name = parts[0]
                obj_id = parts[1]
                key = f"{class_name}.{obj_id}"
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        '''
        all Prints all string representation of all instances
        based or not on the class name and id
        '''

        parts = arg.split()
        if len(parts) < 1:
            print(storage.all())
        else:
            if parts[0] not in globals():
                print("** class doesn't exist **")
            else:
                for key in storage.all():
                    if parts[0] == key.split('.')[0]:
                        print(storage.all()[key])

    def do_update(self, args):
        '''
        Updates an instance based on the class name
        '''

        vargs = args.split()
        if len(vargs) < 1:
            print("** class name missing **")
        elif vargs[0] not in globals():
            print("** class doesn't exist **")
        elif len(vargs) < 2:
            print("** instance id missing **")
        elif f"{vargs[0]}.{vargs[1]}" not in storage.all():
            print("** no instance found **")
        elif len(vargs) < 3:
            print("** attribute name missing **")
        elif len(vargs) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(vargs[0], vargs[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                if vargs[2] in ("created_at", "updated_at", "id"):
                    print("** can't update **")
                    return
                obj = storage.all()[key]
                setattr(obj, vargs[2], vargs[3])
                storage.save()


if __name__ == '__main__':
    """Entry Point"""
    HBNBCommand().cmdloop()
