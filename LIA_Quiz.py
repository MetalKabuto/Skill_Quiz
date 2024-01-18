import PySimpleGUI as sg
sg.set_options(font=("Arial Bold", 16))

main_menu_layout = [
    #Row1
    [sg.Text("Quiz Titel", background_color="#555555")],
    #Reveals the game_layout and hides the main menu on click. Row 2.
    [sg.Button(button_text="Start", size=(10, 1), button_color="#FFFFFF on #150B3F", key="-GAMEWINDOW-")],
    #Row3
    [sg.Button(button_text="Inställningar", size=(10, 1), button_color="#FFFFFF on #150B3F", key="-SETTINGS-")],
    #Row4
    [sg.Button(button_text="Expansion1?", size=(10, 1), button_color="#FFFFFF on #150B3F")],
    #Row5
    [sg.Button(button_text="Stäng av", size=(10, 1), button_color="#FFFFFF on #150B3F", key="-QUIT-")]
]

game_layout = [
    #Row 1
    #For button_color, first code is text color, second is background
    [sg.Button(button_text="Ledtråd", button_color="#000000 on #00AA00" ),
    #Text elements match the window background
    sg.Text("Fråga X av Y ", size=(15,1), background_color="#555555"), 
    sg.Text("Timer:  ", size=(15,1), background_color="#555555"),
    #Reveals the main_menu_layout and hides the game on click.
    #TODO: Remove the placeholder button that goes back to the main menu from the game once its no longer needed.
    sg.Button(button_text="MainMenu", button_color="#000000 on #FFFFFF", key="-PLACEHOLDERMENU-"  ),
    sg.Button(button_text="Hjälp", button_color="#000000 on #03a5fc", key="-HELPSCREEN-")],
   
    #Row2
    #If you make the width bigger than the window size, it doesn't 'spill over'. It stays in the window instead. Height doesn't work that way tough.
    #disabled=True makes it impossible to write in the multiline, but you can still select the text which is not ideal.
    #TODO: Can't figure out a way to disable/hide the scrollbar.
    [sg.Multiline("Fråga här! \nRad 2 av texten" , size=(720,15), background_color="#150B3F", text_color="#FFFFFF", disabled=True)],
   
    #Row3
    #default_text needs to be removed manually when typing. Keeping it for now to show what the box is for.
    #expand_x och y makes the elements expand in size until they reach another element. At least I think so.
    [sg.Input(expand_x=True, expand_y=True, default_text="Skriv svar här"),
    sg.Button(expand_x=True, expand_y=True, button_text="Skicka Svar" ) ],
    
    #Row 4
    [sg.Multiline("Ledtråd 1 ", size=(20,10), background_color="#00AA00", disabled=True),
    sg.Multiline("Ledtråd 2 ", size=(20,10), background_color="#00AA00", disabled=True),
    sg.Multiline("Ledtråd 3 ", size=(20,10), background_color="#00AA00", disabled=True)]
]

settings_layout = [
    #Row 1, Text has no size, that way it only uses the necessary space for the text and will align horizontally.
    [sg.Text("Antal Frågor", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 2
    [sg.Button(button_text="-", button_color="#150B3F", size=(2,1)),
    sg.Text("X", background_color="#FFFFFF", text_color="#000000"),
    sg.Button(button_text="+", button_color="#150B3F", size=(2,1))],
    #Row 3, Text
    [sg.Text("Svårighetsgrad", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 4, Difficulty
    #TODO: Have a different background color for the currently selected difficulty.
    [sg.Button(button_text="Ålder 1", button_color="#150B3F"),
    sg.Button(button_text="Ålder 2", button_color="#150B3F"),
    sg.Button(button_text="Ålder 3", button_color="#150B3F"),
    sg.Button(button_text="Ålder 4", button_color="#150B3F")],
    #Row 5, Text
    [sg.Text("Tidstillägg per ledtråd:", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 6, Time penalty for using a hint
    [sg.Button(button_text="-", button_color="#150B3F", size=(2,1)),
    sg.Text("X", background_color="#FFFFFF", text_color="#000000"),
    sg.Button(button_text="+", button_color="#150B3F", size=(2,1))],
    #Row 7, back to main menu.
    [sg.Button(button_text="Tillbaka", button_color="#FFFFFF on #150B3F", key="-MAINMENU-" )]
]

#Since you can only change opacity for the entire window with pysimplegui, appearance doesn't match the wireframe with the dimmed background.
help_layout = [
    #Row 1. Button is on its own row to place it above the text in the layout.
    [sg.Button(button_text="Tillbaka", button_color="#FFFFFF on #150B3F", key="-EXITHELP-" )],
    #Row 2
    [sg.Multiline("Hjälptext här! \nRad 2 av texten" , size=(720,25), background_color="#03a5fc", text_color="#000000", disabled=True)],
    #Row 3, reserved for eventual images. Images should be GIF or PNG only according to pysimplegui.
    [sg.Image()]
]

#Found how to stack layouts here https://stackoverflow.com/questions/59500558/how-to-display-different-layouts-based-on-button-clicks-in-pysimple-gui-persis first answer
program_layout = [
    #-COL1- is visible on startup, since the main menu is there.
    #Columns have to be in a list, otherwise the program crashes on startup.
    #Need to set each columns background_color to match the windows background. Otherwise it will use the default blue for the column.
    #pad attempts to center the elements vertically a bit.
    #TODO: Can set element justification and alignment here?
    [
        sg.Column(main_menu_layout, key="-COL1-", background_color="#555555", element_justification="center", pad=(0,125)),
        sg.Column(game_layout, visible=False, key="-COL2-", background_color="#555555"),
        sg.Column(settings_layout, visible=False, key="-COL3-", background_color="#555555", element_justification="center", pad=(0,125)),
        #element_justification="right" makes the button stick to the right side of the screen, like in the wireframe.
        sg.Column(help_layout, visible=False, key="-COL4-", background_color="#555555", element_justification="right")
    ]
]

#Settings for the program window.
window = sg.Window("Game Window", program_layout, size=(800, 800), background_color="#555555", element_justification="center", element_padding=10)

#Makes the program loop, otherwise it closes down upon clicking any button.
while True:
    #layout2 används istället för layout, vilket betyder att man kan 'skriva över' innehållet i fönstret för att ändra vy.
    #window = sg.Window('Game Window', layout2, size=(800, 800), element_justification="center", element_padding=10)
    #TODO: Check if the preset event == 'Exit' is needed. If it isn't, delete it.
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit" or event == "-QUIT-":
        break
    print (event, values)
   
    #Probably a better way to shift between the menus, but it works for now.
    #COL1 = Main menu, 2 = Game view, 3 = Settings, 4 = Help screen
    #TODO: Remove if for placeholder once it's no longer needed.
    if event == "-PLACEHOLDERMENU-":
        window["-COL2-"].update(visible=False)
        window["-COL1-"].update(visible=True)
    if event == "-GAMEWINDOW-":
        window["-COL1-"].update(visible=False)
        window["-COL2-"].update(visible=True)
    #Settings menu can only be accessed from the main menu, so only those layouts need to be adjusted.
    if event == "-SETTINGS-":
        window["-COL1-"].update(visible=False)
        window["-COL3-"].update(visible=True)
    if event == "-MAINMENU-":
        window["-COL1-"].update(visible=True)
        window["-COL3-"].update(visible=False)
    #Ifs for the help view
    if event == "-HELPSCREEN-":
        window["-COL2-"].update(visible=False)
        window["-COL4-"].update(visible=True)
    if event == "-EXITHELP-":
        window["-COL2-"].update(visible=True)
        window["-COL4-"].update(visible=False)
window.close()