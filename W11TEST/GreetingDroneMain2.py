from djitellopy import tello
from time import sleep
import cv2

# isMoving = False

# def isMoving():
#     return isMoving

def moveDrone():
    # we have tested this block of code during previous testing session
    donna = tello.Tello()
    donna.connect()
    print(donna.get_battery())

    donna.takeoff()
    donna.move_up(50)  # avoid tables and people
    sleep(2)

    donna.rotate_clockwise(90)
    donna.move_forward(50)
    donna.rotate_counter_clockwise(90)
    donna.move_forward(70)
    donna.rotate_clockwise(90)
    sleep(2)

    donna.move_forward(300)
    sleep(2)
    # we have tested this block of code during previous testing session

    # code left to be tested
    donna.rotate_counter_clockwise(90)
    donna.move_forward(200)
    sleep(2)

    donna.rotate_clockwise(90)
    donna.move_forward(100)
    sleep(2)

    donna.rotate_clockwise(90)
    donna.move_forward(200)
    sleep(2)

    donna.rotate_counter_clockwise(90)
    donna.move_forward(250)
    sleep(2)

    donna.rotate_clockwise(90)
    donna.move_forward(200)
    donna.rotate_clockwise(180)
    donna.move_down(100)
    donna.land();
    # code left to be tested