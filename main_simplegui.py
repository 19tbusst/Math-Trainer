import PySimpleGUI as sg

layout = [[sg.Text("hi")]]

window = sg.Window("title", layout)

while True:
    event, values = window.read()