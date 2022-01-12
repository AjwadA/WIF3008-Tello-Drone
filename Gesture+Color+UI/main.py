import PySimpleGUI as sg  # Part 1 - The import
import detect_and_move as colorDetect
import gestures as gestureDetect
from djitellopy import tello

# donna = tello.Tello()
# donna.connect()
# print()
sg.theme('DarkPurple1')


# a = donna.get_battery()

a=50

layout = [[sg.Text("Welcome, you will be greeted by our drone")],
          [sg.Text("Drone Battery Percentage "+str(a)+"%")],
          [sg.Button('Color Recognition')],
          [sg.Button('Gesture Recognition')],
          [sg.Cancel()]]
window = sg.Window('Event Greeter', layout, size=(480,320))

while True:
    event, values = window.read()
    if event == "Color Recognition":
        colorDetect.color()
    if event == "Gesture Recognition":
        gestureDetect.gesture()
    if event == "Cancel" or event == sg.WINDOW_CLOSED:
        break
window.close()


