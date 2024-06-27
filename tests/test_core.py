import unittest
from core import ToyRobot, Direction

class TestPlacement(unittest.TestCase):
    def setUp(self):
        self.toyrobot = ToyRobot()
    
    def test_place(self):
        self.toyrobot.place((2, 1), Direction.EAST)
        self.assertEqual(self.toyrobot._location, (2, 1))
        self.assertEqual(self.toyrobot._direction, Direction.EAST)
        
    def test_replace(self):
        self.toyrobot.place((2,1), Direction.EAST)
        self.toyrobot.place((4,2), Direction.SOUTH)
        self.assertEqual(self.toyrobot._location, (4, 2))
        self.assertEqual(self.toyrobot._direction, Direction.SOUTH)
        
    def test_invalidplace(self):
        self.toyrobot.place((8,16), Direction.WEST)
        self.assertNotEqual(self.toyrobot._location, (8,16))
        self.assertNotEqual(self.toyrobot._direction, Direction.WEST)
    
class TestMovement(unittest.TestCase):
    def setUp(self):
        self.toyrobot = ToyRobot()
        self.toyrobot.place((1,1), Direction.EAST)
        
    def test_move(self):
        self.toyrobot.move()
        self.assertEqual(self.toyrobot._location, (2,1))
        
    def test_left(self):
        self.toyrobot.left()
        self.assertEqual(self.toyrobot._direction, Direction.NORTH)
        
    def test_right(self):
        self.toyrobot.right()
        self.assertEqual(self.toyrobot._direction, Direction.SOUTH)
        
    def test_wander(self):
        self.toyrobot.left()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.right()
        self.toyrobot.right()
        self.toyrobot.move()
        self.toyrobot.left()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot._location, (2,2))
    
class TestBoundaries(unittest.TestCase):
    def setUp(self):
        self.toyrobot = ToyRobot()
        self.toyrobot.place((2,2), Direction.EAST)
        
    def test_rightwall(self):
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot._location, (4,2))
        
    def test_leftwall(self):
        self.toyrobot.left()
        self.toyrobot.left()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot._location, (0,2))
        
    def test_ceiling(self):
        self.toyrobot.left()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot._location, (2,4))
        
    def test_floor(self):
        self.toyrobot.right()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.toyrobot.move()
        self.assertEqual(self.toyrobot._location, (2,0))
    
if __name__ == '__main__':
    unittest.main()