#!/usr/bin/python3
"""For Hbnb console Definition."""
import cmd
import sys
from models import storage
from models.base_model import BaseModel


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
            print ("** class name missing **")
            return
        elif arg not in HBNBCommand.__mod_list:
            print ("** class doesn't exist **")
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

        if len(sys.argv) < 2:
            print("** class name missing **")
            return
        else:
            model = sys.argv[1]

            if model not in HBNBCommand.__mod_list:
                print("** class doesn't exist **")
                return
            elif len(sys.argv) > 3:
                print("** instance id missing **")
                return
            else:
                model_id = sys.argv[2]

                key = f"{model_id}.{model}"

                if key in storage.all():
                    str_rep = storage.all()[key]
                    print(str_rep)
                    return
                else:
                    print("** no instance found **")
                    return

    def do_destroy(self):
        '''
        Deletes an instance based on the class name and id
        (save the change into the JSON file). 

        '''

    def do_update(self):
        '''
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)

        '''

    def do_all(self):
        '''
        Prints all string representation of all instances based
        or not on the class name.

        '''

if __name__ == '__main__':
    HBNBCommand().cmdloop()
