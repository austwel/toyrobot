"""API for toyrobot
"""

import os
import json
from flask import Flask, session, request, jsonify
from dotenv import load_dotenv
from toyrobot.core import ToyRobot, Direction
load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


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
        if location[0] is None or location[1] is None:
            raise ValueError
    except ValueError:
        return {"message": "Location Parameters invalid"}, 400

    try:
        direction = Direction[request.args.get('direction').upper()]
    except (KeyError, AttributeError):
        direction = Direction.EAST

    if robot.place(location, direction):
        state = robot.dump_state()
        session['robot_state'] = state
        return {"message": "Success", "state": json.loads(state)}, 200
    return {"message": "Bad Request"}, 400

@app.route("/move", methods=['POST'])
def move():
    """Move the current state's robot forward one increment.

    Returns:
        tuple[str, int]: HTTP Response
    """
    if 'robot_state' in session:
        robot = ToyRobot(session['robot_state'])
    elif 'state' in request.args:
        robot = ToyRobot({
            'location': {
                'x': request.args.get('state', str)[0],
                'y': request.args.get('state', str)[1],
            },
            'direction': request.args.get('state', str)[2:]
        })
    else:
        return {"message": "Bad Request"}, 400
    status = robot.move()
    state = robot.dump_state()
    session['robot_state'] = state
    return {"message": "Moved", "state": json.loads(state)} \
    if status else {"message": "Ignored", "state": json.loads(state)}, 200

@app.route("/left", methods=['POST'])
def left():
    """Rotate the current robot to the left.

    Returns:
        tuple[str, int]: HTTP Response
    """
    if 'robot_state' in session:
        robot = ToyRobot(session['robot_state'])
    elif 'state' in request.args:
        robot = ToyRobot({
            'location': {
                'x': request.args.get('state', str)[0],
                'y': request.args.get('state', str)[1],
            },
            'direction': request.args.get('state', str)[2:]
        })
    else:
        return {"message": "Bad Request"}, 400
    robot.left()
    state = robot.dump_state()
    session['robot_state'] = state
    return {"message": "Success", "state": json.loads(state)}, 200

@app.route("/right", methods=['POST'])
def right():
    """Rotate the current robot to the right.

    Returns:
        tuple[str, int]: HTTP Response
    """
    if 'robot_state' in session:
        robot = ToyRobot(session['robot_state'])
    elif 'state' in request.args:
        robot = ToyRobot({
            'location': {
                'x': request.args.get('state', str)[0],
                'y': request.args.get('state', str)[1],
            },
            'direction': request.args.get('state', str)[2:]
        })
    else:
        return {"message": "Bad Request"}, 400
    robot.right()
    state = robot.dump_state()
    session['robot_state'] = state
    return {"message": "Success", "state": json.loads(state)}, 200

@app.route("/report", methods=['GET'])
def report():
    """Return a json object of the current robot state information.

    Returns:
        tuple[str, int]: HTTP Response
    """
    if 'robot_state' in session:
        robot = ToyRobot(session['robot_state'])
    elif 'state' in request.args:
        robot = ToyRobot({
            'location': {
                'x': request.args.get('state', str)[0],
                'y': request.args.get('state', str)[1],
            },
            'direction': request.args.get('state', str)[2:]
        })
    else:
        return {"message": "Bad Request"}, 400
    state = robot.dump_state()
    response = {'location': robot.location, 'direction': str(robot.direction), "state": json.loads(state)}
    return jsonify(response), 200
