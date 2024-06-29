"""
Module to handle cli implementations of the toy robot demonstration. The base
class 'cli'
"""

from .core import ToyRobot, Direction

class Cli():
    """Implementation of interfacing with the toy robot via command-line.

    Attributes:
        HELP_STRING (str): Constant string literal of the help message

    Args:
        None
    """

    HELP_STRING = \
        'PLACE X,Y,FACING   Will put the toy robot on the table in position X,Y\n' + \
        '                   and facing NORTH, SOUTH, EAST or WEST.\n' + \
        '                   The origin (0,0) can be considered to be the SOUTH\n' + \
        '                   WEST most corner.\n' + \
        '                   The first valid command to the robot is a PLACE\n' + \
        '                   command, after that, any sequence of commands may\n' + \
        '                   be issued, in any order, including another PLACE\n' + \
        '                   command.\n' + \
        'MOVE               Will move the toy robot one unit forward in the\n' + \
        '                   direction it is currently facing.\n' + \
        'LEFT               Will rotate the robot 90 degrees counter-clockwise\n' + \
        '                   without changing the position of the robot.\n' + \
        'RIGHT              Will rotate the robot 90 degrees clockwise without\n' + \
        '                   changing the position of the robot.\n' + \
        'REPORT             Will announce the X,Y and F of the robot.'

    def __init__(self) -> None:
        """
        Inititalise the toy robot object.
        """
        self.toy_robot = ToyRobot()

    def run(self) -> None:
        """
        Parse given commands via standard input.
        """
        command = None
        while command != 'quit':
            command = input('> ').lower().strip()
            self.parse(command)

    def parse(self, user_input: str) -> None:
        """
        Parse the given user input mostly by performing a function on the toy
        robot object.

        Args:
            user_input (str):
                String literal of user inputted text from standard input
        """
        command, *arguments = user_input.split(' ')
        if command == 'place':
            self.place(arguments)
        elif command == 'move':
            self.move()
        elif command == 'left':
            self.left()
        elif command == 'right':
            self.right()
        elif command == 'report':
            self.report()
        elif command == 'help':
            self.help()
        elif command == 'quit':
            self.quit()
        else:
            self.invalid(user_input)

    def place(self, arguments: list) -> None:
        """
        Perform the place function by parsing the user input into a location
        and direction.

        Args:
            arguments (list[str]):
                List of arguments given with the PLACE command. One argument in
                the {X,Y,FACING} format can be parsed along with three arguments
                in the {X Y FACING} format.
        """
        try:
            if len(arguments) == 1:
                x, y, d = arguments[0].split(',')
            elif len(arguments) == 3:
                x, y, d = arguments
            else:
                return
            if d.upper() not in list(Direction.__members__):
                return
            self.toy_robot.place((int(x), int(y)), Direction[d.upper()])
        except KeyError:
            ...

    def move(self) -> None:
        """Move the toy robot forwards in the direction it is currently facing.
        """
        self.toy_robot.move()

    def left(self) -> None:
        """Rotate the toy robot counter-clockwise one step.
        """
        self.toy_robot.left()

    def right(self) -> None:
        """Rotate the toy robot clockwise one step.
        """
        self.toy_robot.right()

    def report(self) -> None:
        """Report the current status of the toy robot to the user.
        """
        location, direction = self.toy_robot.report()
        if direction is None:
            return
        print(f'Output: {location[0]},{location[1]},{direction}')

    def help(self) -> None:
        """Display the help message to the user."""
        print(self.HELP_STRING)

    def quit(self) -> None:
        """Base method for quitting the toy robot demonstration.
        """
        return

    def invalid(self, message: str) -> None:
        """Called when a command was not recognised as being valid.

        Args:
            message (str): A user input string interpreted as a command
        """
        print(f"'{message}' is not recognised. Type 'help' for help.")


class CliVisualiser(Cli):
    """A child of the Cli class which also displays a grid visualisation of the
    toy robot.

    Attributes:
        _buffer: A private string to append after the next cls function
    """
    _buffer: str = ''

    def run(self) -> None:
        command = None
        while command != 'quit':
            self.display()
            command = input('> ').lower().strip()
            self.parse(command)

    def display(self) -> None:
        """Displays the grid visualisation of the toy robot to the user.
        """
        location, direction = self.toy_robot.report()
        visualisation = '\033c'
        for i in range(self.toy_robot.HEIGHT-1, -1, -1):
            for j in range(self.toy_robot.WIDTH):
                if (j, i) == location:
                    visualisation += '^ ' if direction == Direction.NORTH else \
                                     '> ' if direction == Direction.EAST else \
                                     'v ' if direction == Direction.SOUTH else \
                                     '< '
                else:
                    visualisation += '. '
            visualisation += '\n\n'

        if self._buffer != '':
            visualisation += self._buffer
            self._buffer = ''

        print(visualisation)

    def report(self) -> None:
        location, direction = self.toy_robot.report()
        if direction is None:
            return
        self._buffer = f'Output: {location[0]},{location[1]},{direction}'

    def help(self):
        self._buffer = self.HELP_STRING

    def quit(self) -> None:
        print('\033c')

    def invalid(self, message) -> None:
        self._buffer = f"'{message}' is not recognised. Type 'help' for help."


if __name__ == '__main__':
    CliVisualiser().run()
