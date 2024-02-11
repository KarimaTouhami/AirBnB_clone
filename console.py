#!/usr/bin/python3
import cmd

"""Enter of CMD"""


class HBNBCommand(cmd.Cmd):
    """Implementation of CMD of AirBNB"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()  # Print a newline
        return True


if __name__ == '__main__':
    """Entry Point"""
    HBNBCommand().cmdloop()
