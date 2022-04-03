import PySimpleGUI as sg
import os.path
import ebooks

sg.theme('dark grey 9')

text_input_column = [
    [
        sg.Text("Enter text to be encoded/decoded here"),
    ], 
    [
        sg.Multiline(key='-TEXT-INPUT-', size=(40, 20)),
    ],
    [
        sg.OK(key='-ACCEPT-TEXT-'),
        sg.Button('Encrypt', size=(6,1), button_color=('white', 'green'), key='_B_'), sg.Button('Exit')
    ]
]

file_list_column = [
    [sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
     sg.FolderBrowse(),],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
]

text_viewer_column = [
    [sg.Multiline(size=(40, 20), key="-BOOK-TEXT-", expand_y=True)],
]

layout = [
    [sg.Column(text_input_column),
     sg.VSeperator(),
     sg.Column(file_list_column),
     sg.VSeperator(),
     sg.Column(text_viewer_column),]
]


window = sg.Window("Book Cipher", icon='../assets/book-icon.png').Layout(layout)
encryptFlag = True
while True:
    event, values = window.read()
    if event == "-ACCEPT-TEXT-":
        if (len(values["-FILE LIST-"]) == 0):
            sg.popup("Select a PDF to read from. ")
        else:
            path = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            if encryptFlag:
                ciphertext = ebooks.encrypt(path, values['-TEXT-INPUT-'])
                result = ciphertext[0]
                if (len(ciphertext[1]) > 0):
                    sg.popup("Warning: Could not find encodings for " + str(ciphertext[1]))
            else:
                result = ebooks.decrypt(path, values['-TEXT-INPUT-'])
            window["-BOOK-TEXT-"].update(result)
    
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
        ]
        window["-FILE LIST-"].update(fnames)
        

    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
        except:
            pass
    
    if event == '_B_':
        encryptFlag = not encryptFlag
        window.Element('_B_').Update(('Decrypt','Encrypt')[encryptFlag], button_color=(('white', ('red', 'green')[encryptFlag])))

window.close()