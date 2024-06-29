"""Module providing unit testing capabilities"""
import unittest
import json

from ..src.core import ToyRobot, Direction

class TestInit(unittest.TestCase):
    """
    A class to test initialising the toy robot object.
    """
    def test_initless(self):
        '''Initialise a new toy robot and ensure it has null attributes'''
        toyrobot = ToyRobot()
        self.assertEqual(toyrobot.location, None)
        self.assertEqual(toyrobot.direction, None)

    def test_init(self):
        '''Initialise a new toy robot and ensure it has valid attributes'''
        state = json.dumps({'location': {'x': 1, 'y': 3}, 'direction': 'SOUTH'})
        toyrobot = ToyRobot(state)
        self.assertEqual(toyrobot.location, (1, 3))
        self.assertEqual(toyrobot.direction, Direction.SOUTH)

class TestPlacement(unittest.TestCase):
    """
    A class to test placing the toy robot on the plane.
    """
    def setUp(self):
        '''Initialise a new toy robot object before each test'''
        self.toyrobot = ToyRobot()

    def test_place(self):
        '''Place a robot at (2, 1) and check if it is there'''
        self.toyrobot.place((2, 1), Direction.EAST)
        self.assertEqual(self.toyrobot.location, (2, 1))
        self.assertEqual(self.toyrobot.direction, Direction.EAST)

    def test_replace(self):
        '''Place a robot at (2, 1) and replace it with a robot at (4, 2)'''
        self.toyrobot.place((2, 1), Direction.EAST)
        self.toyrobot.place((4, 2), Direction.SOUTH)
        self.assertEqual(self.toyrobot.location, (4, 2))
        self.assertEqual(self.toyrobot.direction, Direction.SOUTH)

    def test_invalidplace(self):
        '''Place a robot out of bounds at (8, 16) ensure it is ignored'''
        self.toyrobot.place((8, 16), Direction.WEST)
        self.assertNotEqual(self.toyrobot.location, (8, 16))
        self.assertNotEqual(self.toyrobot.direction, Direction.WEST)

class TestMovement(unittest.TestCase):
    """
    A class to test moving the toy robot on the plane.
    """
    def setUp(self):
        '''Place a toy robot at (1, 1) before each test in this class'''
        self.toyrobot = ToyRobot()
        self.toyrobot.place((1, 1), Direction.EAST)

    def test_move(self):
        '''Move the robot one step, ensure it is now at (2, 1)'''
        self.toyrobot.move()
        self.assertEqual(self.toyrobot.location, (2, 1))

    def test_left(self):
        '''
        Spin the robot one step counterclockwise, ensure it is now facing north
        '''
        self.toyrobot.left()
        self.assertEqual(self.toyrobot.direction, Direction.NORTH)

    def test_right(self):
        '''Spin the robot one step clockwise, ensure it is now facing south'''
        self.toyrobot.right()
        self.assertEqual(self.toyrobot.direction, Direction.SOUTH)

    def test_spin(self):
        '''Spin the robot 360 degrees ensuring it returns to facing east'''
        self.toyrobot.left()
        self.toyrobot.left()
        self.toyrobot.left()
        self.toyrobot.left()
        self.assertEqual(self.toyrobot.direction, Direction.EAST)

    def test_wander(self):
        '''Wander the robot around the plane, ensure it stops where it should'''
        self.toyrobot.left()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.right()
        self.toyrobot.right()
        self.toyrobot.move()
        self.toyrobot.left()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot.location, (2, 2))

class TestBoundaries(unittest.TestCase):
    """
    A class to test moving the robot outside the boundaries of the plane.
    """
    def setUp(self):
        '''Place the robot at (2, 2) before each test in this class'''
        self.toyrobot = ToyRobot()
        self.toyrobot.place((2, 2), Direction.EAST)

    def test_rightwall(self):
        '''
        Move the robot forwards towards the east wall, 
        ensure it stops at the end of the plane
        '''
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot.location, (4, 2))

    def test_leftwall(self):
        '''
        Move the robot forwards towards the west wall, 
        ensure it stops at the end of the plane
        '''
        self.toyrobot.left()
        self.toyrobot.left()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot.location, (0, 2))

    def test_ceiling(self):
        '''
        Move the robot forwards towards the north wall, 
        ensure it stops at the end of the plane
        '''
        self.toyrobot.left()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot.location, (2, 4))

    def test_floor(self):
        '''
        Move the robot forwards towards the south wall, 
        ensure it stops at the end of the plane
        '''
        self.toyrobot.right()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot.location, (2, 0))

if __name__ == '__main__':
    unittest.main()
