import PySimpleGUI as sg
password = False

sg.ChangeLookAndFeel("SystemDefault")

text = sg.Text("Input", background_color="#2196F3", text_color="white")

input_field = sg.InputText(justification="center", focus=True)

if password:
    input_field = sg.InputText(
        password_char="*", justification="center", focus=True
    )

submit_button = sg.Submit(button_color=("white", "#0069C0"))

layout = [[text], [input_field], [submit_button]]

window = sg.Window(
    "SDG",
    layout,
    icon="icon.ico",
    no_titlebar=True,
    background_color="#2196F3",
    element_justification="center",
    use_default_focus=False,
    keep_on_top=True
)
_, values = window.Read()
window.Close()
value = values[0]
