import PySimpleGUI as sg
import time

sg.ChangeLookAndFeel("SystemDefault")
text = sg.Text("Soli Deo Glory", background_color="#2196F3", text_color="white")
ok_button = sg.OK(button_color=("white", "#0069C0"))
layout = [[text], [ok_button]]
window = sg.Window(
    "SDG",
    layout,
    no_titlebar=True,
    background_color="#2196F3",
    element_justification="center",
    use_default_focus=False,
    keep_on_top=False
)
_, values = window.Read()
window.Close()
