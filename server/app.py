"""API for toyrobot
"""

import os
from flask import Flask, session, request, jsonify
from dotenv import load_dotenv
from toyrobot.core import ToyRobot, Direction
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route("/", methods=['GET'])
def index():
    """Hello world-like route to check if service is running.

    Returns:
        tuple[str, int]: HTTP Response
    """
    return "Hello, World!", 200

@app.route("/place", methods=['POST'])
def place():
    """Place the robot in a new state, take parameters 'x', 'y' and 'direction'
    to determine location and facing status.

    Returns:
        tuple[str, int]: HTTP Response
    """
    robot = ToyRobot()

    try:
        location = (request.args.get('x', type=int), request.args.get('y', type=int))
    except ValueError:
        return "Location parameters invalid", 400

    try:
        direction = Direction[request.args.get('direction').upper()]
    except (KeyError, AttributeError):
        return "Direction parameter invalid", 400

    if robot.place(location, direction):
        session['robot_state'] = robot.dump_state()
        return "Success", 200
    return "Bad Request", 400

@app.route("/move", methods=['POST'])
def move():
    """Move the current state's robot forward one increment.

    Returns:
        tuple[str, int]: HTTP Response
    """
    if 'robot_state' in session:
        robot = ToyRobot(session['robot_state'])
        status = robot.move()
        session['robot_state'] = robot.dump_state()
        return "Moved" if status else "Ignored", 200
    return "Bad Request", 400

@app.route("/left", methods=['POST'])
def left():
    """Rotate the current robot to the left.

    Returns:
        tuple[str, int]: HTTP Response
    """
    if 'robot_state' in session:
        robot = ToyRobot(session['robot_state'])
        robot.left()
        session['robot_state'] = robot.dump_state()
        return "Success", 200
    return "Bad Request", 400

@app.route("/right", methods=['POST'])
def right():
    """Rotate the current robot to the right.

    Returns:
        tuple[str, int]: HTTP Response
    """
    if 'robot_state' in session:
        robot = ToyRobot(session['robot_state'])
        robot.right()
        session['robot_state'] = robot.dump_state()
        return "Success", 200
    return "Bad Request", 400

@app.route("/report", methods=['GET'])
def report():
    """Return a json object of the current robot state information.

    Returns:
        tuple[str, int]: HTTP Response
    """
    if 'robot_state' in session:
        robot = ToyRobot(session['robot_state'])
        response = {'location': robot.location, 'direction': str(robot.direction)}
        return jsonify(response), 200
    return "Bad Request", 400
