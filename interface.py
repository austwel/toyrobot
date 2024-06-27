from core import ToyRobot, Direction
from typing import Self

class cli(object):
    def __init__(self) -> None:
        self.toy_robot = ToyRobot()
        
        command = None
        while(command != 'quit'):
            command = input('> ').lower().strip()
            self.parse(command)
            
    def parse(self, user_input: str):
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
            
    def place(self, arguments: list[str]):
        try:
            if len(arguments) == 1:
                x, y, dir = arguments[0].split(',')
            elif len(arguments) == 3:
                x, y, dir = arguments
            else: return
            self.toy_robot.place((int(x), int(y)), Direction[dir.upper()])
        except Exception: ...
        
    def move(self):
        self.toy_robot.move()
        
    def left(self):
        self.toy_robot.left()
        
    def right(self):
        self.toy_robot.right()
        
    def report(self):
        location, direction = self.toy_robot.report()
        if direction is None: return
        print(f'Output: {location[0]},{location[1]},{direction}')
        
    def help(self):
        print('PLACE X,Y,FACING     Will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.\n' + \
              '                     The origin (0,0) can be considered to be the SOUTH WEST most corner.\n' + \
              '                     The first valid command to the robot is a PLACE command, after that, any sequence of\n' + \
              '                     commands may be issued, in any order, including another PLACE command.\n' + \
              'MOVE                 Will move the toy robot one unit forward in the direction it is currently facing.\n' + \
              'LEFT                 Will rotate the robot 90 degrees counter-clockwise without changing the position of the robot.\n' + \
              'RIGHT                Will rotate the robot 90 degrees clockwise without changing the position of the robot.\n' + \
              'REPORT               Will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.')
        
    def quit(self):
        return
        
    def invalid(self, message):
        print(f"'{message}' is not recognised. Type 'help' for help.")
            
class visualiser_cli(cli):
    buffer: str = ''
    
    def __init__(self) -> None:
        self.toy_robot = ToyRobot()
        
        command = None
        while(command != 'quit'):
            self.display()
            command = input('> ').lower().strip()
            self.parse(command)
            
    def display(self):
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
            
        if self.buffer != '':
            visualisation += self.buffer
            self.buffer = ''
        
        print(visualisation)
        
    def report(self):
        location, direction = self.toy_robot.report()
        if direction is None: return
        self.buffer = f'Output: {location[0]},{location[1]},{direction}'
        
    def help(self):
        self.buffer = 'PLACE X,Y,FACING     Will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.\n' + \
                      '                     The origin (0,0) can be considered to be the SOUTH WEST most corner.\n' + \
                      '                     The first valid command to the robot is a PLACE command, after that, any sequence of\n' + \
                      '                     commands may be issued, in any order, including another PLACE command.\n' + \
                      'MOVE                 Will move the toy robot one unit forward in the direction it is currently facing.\n' + \
                      'LEFT                 Will rotate the robot 90 degrees counter-clockwise without changing the position of the robot.\n' + \
                      'RIGHT                Will rotate the robot 90 degrees clockwise without changing the position of the robot.\n' + \
                      'REPORT               Will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.'
                      
    def quit(self):
        print('\033c')
                      
    def invalid(self, message):
        self.buffer = f"'{message}' is not recognised. Type 'help' for help."
            
if __name__ == '__main__':
    visualiser_cli()