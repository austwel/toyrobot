from enum import Enum

class Direction(Enum):
    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)

    def clockwise(self):
        members = list(self.__class__)
        index = members.index(self) + 1
        return members[index % len(members)]

    def counterclockwise(self):
        members = list(self.__class__)
        index = members.index(self) - 1
        return members[index % len(members)]

    def __str__(self) -> str:
        return self.name

class ToyRobot(object):
    _location: tuple[int, int] = None
    _direction: Direction = None
    
    def __init__(self, width: int = 5, height: int = 5) -> None:
        self.WIDTH = width
        self.HEIGHT = height
        
    def place(self, location: tuple[int, int], direction: Direction) -> bool:
        if not 0 <= location[0] < self.WIDTH or not 0 <= location[1] < self.HEIGHT:
            return False
        self._location, self._direction = location, direction
        return False
        
    def move(self) -> bool:
        if self._direction == None: return
        new_location = tuple(map(lambda a, b: a + b, self._location, self._direction.value))
        if not 0 <= new_location[0] < self.WIDTH or not 0 <= new_location[1] < self.HEIGHT:
            return False
        self._location = new_location
        return True
        
    def left(self) -> None:
        if self._direction == None: return
        self._direction = Direction.counterclockwise(self._direction)
        
    def right(self) -> None:
        if self._direction == None: return
        self._direction = Direction.clockwise(self._direction)
    
    def report(self) -> tuple[tuple[int, int], Direction]:
        return self._location, self._direction