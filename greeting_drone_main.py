from djitellopy import tello
from time import sleep
# import cv2


def moveDrone():
  # move all to here
  return "nothing";



donna = tello.Tello()
donna.connect()
print(donna.get_battery())

donna.streamon()

# # To get continuous frame we use while loop
# while True:
#     img = donna.get_frame_read().frame
#     # img = cv2.resize(img, (360, 240)) #resize for faster processing
#     cv2.imshow("Donna's view", img) # window
#     cv2.waitKey(1) # delay to avoid the frame shutdown before we see it
#     # break while loop here when detecting motion

donna.takeoff()
donna.move_up(100) # avoid tables and people
donna.flip_back()
sleep(2)

donna.rotate_clockwise(90)
donna.move_forward(50)
donna.rotate_counter_clockwise(90)
donna.move_forward(50)
donna.rotate_clockwise(90)
donna.flip_forward()
sleep(2)

donna.move_forward(300)
sleep(2)

donna.rotate_counter_clockwise(90)
donna.move_forward(200)
sleep(2)

donna.rotate_clockwise(90)
donna.move_forward(100)
sleep(2)

donna.rotate_clockwise(90)
donna.move_forward(200)
sleep(2)

donna.flip_left()
donna.rotate_counter_clockwise(90)
donna.move_forward(250)
sleep(2)

donna.flip_right()
donna.rotate_clockwise(90)
donna.move_forward(200)
donna.rotate_clockwise(180)
donna.flip_back()
donna.move_down(100)
donna.land()

# donna.send_rc_control(200, 0, 0, 0) # velocity (-100 - 100): left-right, forward-backward, up-down, yaw


# (Fitri) Down here is the last code I have on my laptop after we tested the other day
# ############################################
donna.takeoff()
donna.move_up(50) # avoid tables and people
# donna.flip_back()
sleep(2)

donna.rotate_clockwise(90)
donna.move_forward(50)
donna.rotate_counter_clockwise(90)
donna.move_forward(70)
donna.rotate_clockwise(90)
# donna.flip_forward()
sleep(2)

donna.move_forward(350)
sleep(2)

donna.rotate_counter_clockwise(90)
donna.move_forward(200)
sleep(2)

donna.rotate_clockwise(90)
donna.move_forward(100)
sleep(2)

donna.rotate_clockwise(90)
donna.move_forward(200)
sleep(2)

# donna.flip_left()
donna.rotate_counter_clockwise(90)
donna.move_forward(250)
sleep(2)

# donna.flip_right()
donna.rotate_clockwise(90)
donna.move_forward(200)
donna.rotate_clockwise(180)
# donna.flip_back()
donna.move_down(100)
donna.land()
# ############################################