#!/usr/bin/python3
"""For Hbnb console Definition."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Definition of Hbnb command line interpreter.
    commands are handled using do_ + command method names.
    """

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
