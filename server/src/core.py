"""Core module for the toy robot demonstration.

This module is commonly used by interfaces to provide the core functionality.
"""

from enum import Enum
import json

class Direction(Enum):
    '''Enum-like implementation of directions, allowing rotation methods'''
    NORTH = (0, 1)
    '''The north direction'''
    EAST = (1, 0)
    '''The east direction'''
    SOUTH = (0, -1)
    '''The south direction'''
    WEST = (-1, 0)
    '''The west direction'''

    def clockwise(self):
        """Rotate the given direction by 90 degrees clockwise.

        Returns:
            Direction: Direction after being rotated
        """
        members = list(self.__class__)
        index = members.index(self) + 1
        return members[index % len(members)]

    def counterclockwise(self):
        """Rotate the given direction by 90 degrees counter-clockwise.

        Returns:
            Direction: Direction after being rotated
        """
        members = list(self.__class__)
        index = members.index(self) - 1
        return members[index % len(members)]

    @staticmethod
    def from_integer(index: int):
        """Get a direction value by serialisable integer index.
        
        Returns:
            Direction: Direction of index given
        """
        members = list(Direction)
        return members[index % len(members)]

    def __str__(self) -> str:
        """Plain string representation of the object for printing.

        Returns:
            str: Plain name for the direction [North, East, South, West]
        """
        return self.name

class ToyRobot():
    """Main toy robot class that handes the functionality.

    Attributes:
        location (tuple[int, int]): 
            Current position of the toy robot (x, y) using the southwest
            corner as the origin.
        direction (Direction): 
            Current cardinal direction the toy robot is facing.
        WIDTH (int):
            Constant defining the maximum x value of the plane on which the toy
            robot sits.
        HEIGHT (int):
            Constant defining the maximum y value of the plane on which the toy
            robot sits.
            
    Args:
        None
    """
    location: tuple = None
    direction: Direction = None
    WIDTH: int = 5
    HEIGHT: int = 5

    def __init__(self, state = None) -> None:
        """Initialise toy robot object

        Args:
            state (json):
            An optional robot state to initialise. Provided in the form
            {'location': {'x': 1, 'y': 2}, 'direction', 0}
        """
        if state is not None:
            robot_state = json.loads(state)
            self.place(
                (robot_state['location']['x'], robot_state['location']['y']),
                Direction[str(robot_state['direction']).upper()]
            )

    def dump_state(self) -> str:
        """Helper function to dump the state into a json format for serialising.

        Returns:
            str: State
        """
        return json.dumps({
            'location': {
                'x': self.location[0],
                'y': self.location[1]
            },
            'direction': str(self.direction)
        })

    def place(self, location: tuple, direction: Direction) -> bool:
        """
        Place the toy robot at the given location, replacing the older
        instance if it exists.    

        Args:
            location (tuple[int, int]):
                Tuple representation of the new location
            direction (Direction):
                Direction the new toy robot should begin facing

        Returns:
            bool: If the placement was valid, safe to ignore.
        """
        if not 0 <= location[0] < self.WIDTH or not 0 <= location[1] < self.HEIGHT:
            return False
        self.location, self.direction = location, direction
        return True

    def move(self) -> bool:
        """Move the robot one measure forwards in the direction it is facing.

        Returns:
            bool: If the movement was valid, safe to ignore.
        """
        if self.direction is None:
            return False
        new_location = tuple(map(lambda a, b: a + b, self.location, self.direction.value))
        if not 0 <= new_location[0] < self.WIDTH or not 0 <= new_location[1] < self.HEIGHT:
            return False
        self.location = new_location
        return True

    def left(self) -> None:
        '''Rotate the robot one rotation to the left.'''
        if self.direction is None:
            return
        self.direction = Direction.counterclockwise(self.direction)

    def right(self) -> None:
        '''Rotate the robot one rotation to the right.'''
        if self.direction is None:
            return
        self.direction = Direction.clockwise(self.direction)

    def report(self) -> tuple:
        """Display the current status of the toy robot.

        Returns:
            tuple[tuple[int, int], Direction]:
                A tuple containing both the current location and current
                direction the toy robot is facing.
        """
        return self.location, self.direction
