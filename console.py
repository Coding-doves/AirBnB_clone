#!/usr/bin/python3
"""For Hbnb console Definition."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Definition of Hbnb command line interpreter.
    commands are handled using do_ + command method names.
    """

    prompt = "(hbnb) "
    __mod_list = ['BaseModel']

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing when emptyline is inputed."""
        pass

    def do_EOF(self, arg):
        """Print new line and quit when ctrl d is hit."""
        print("")
        return True

    def do_create(self, arg):
        '''
         Creates a new instance of BaseModel, saves it
         (to the JSON file) and prints the id

        '''
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.__mod_list:
            print("** class doesn't exist **")
            return
        else:
            if arg in HBNBCommand.__mod_list:
                if arg == 'BaseModel':
                    new_inst = BaseModel()
                    new_inst.save()
                    print(new_inst.id)
                    return

    def do_show(self, argv):
        '''
        Prints the string representation of an instance base
        on the class name and id.

        '''

        string = shlex.split(argv)
        obj_dict = storage.all()
        if len(string) == 0:
            print("** class name missing **")
        elif string[0] not in HBNBCommand.__mod_list:
            print("** class doesn't exist **")
        elif len(string) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(string[0], string[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            obj = obj_dict["{}.{}".format(string[0], string[1])]
            print(obj)

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        (save the change into the JSON file).

        '''
        string = shlex.split(arg)
        obj_dict = storage.all()
        if len(string) == 0:
            print("** class name missing **")
        elif string[0] not in HBNBCommand.__mod_list:
            print("** class doesn't exist **")
        elif len(string) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(string[0], string[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(string[0], string[1])]
            storage.save()

    def do_update(self):
        '''
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)

        '''

    def do_all(self, arg):
        '''
        Prints all string representation of all instances based
        or not on the class name.

        '''
        string = shlex.split(arg)
        if len(string) > 0:
            if string[0] not in HBNBCommand.__mod_list:
                print("** class doesn't exist **")
            else:
                instances = []
                for obj in storage.all().values():
                    if string[0] == obj.__class__.__name__:
                        instances.append(obj.__str__())
                print(instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
