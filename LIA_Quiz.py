#Code taken from https://www.tutorialspoint.com/pysimplegui/pysimplegui_window_class.htm and adapted.

from ctypes import alignment
from turtle import color
import PySimpleGUI as psg
psg.set_options(font=('Arial Bold', 16))

game_layout = [
   #Row 1
   #For button_color, first code is text color, second is background
   [psg.Button(button_text="Ledtråd", button_color="#000000 on #00AA00" ),
   #Text elements match the window background
   psg.Text('Fråga X av Y ', size=(15,1), background_color="#555555"), 
   psg.Text('Timer:  ', size=(15,1), background_color="#555555"),
   #Reveals the main_menu_layout and hides the game on click.
   psg.Button(button_text="MainMenu", button_color="#000000 on #FFFFFF", key="-MAINMENU-"  ),
   psg.Button(button_text="Hjälp", button_color="#000000 on #03a5fc")],
   
   #Row2
   #If you make the width bigger than the window size, it doesn't 'spill over'. It stays in the window instead. Height doesn't work that way tough.
   #disabled=True makes it impossible to write in the multiline, but you can still select the text which is not ideal.
   #TODO: Can't figure out a way to disable/hide the scrollbar.
   [psg.Multiline('Fråga här! \nRad 2 av texten' , size=(720,15), background_color="#150B3F", text_color="#FFFFFF", disabled=True)],
   
   #Row3
   #default_text needs to be removed manually when typing. Keeping it for now to show what the box is for.
   #expand_x och y makes the elements expand in size until they reach another element. At least I think so.
   [psg.Input(expand_x=True, expand_y=True, default_text="Skriv svar här"),
    psg.Button(expand_x=True, expand_y=True, button_text="Skicka Svar" ) ],
    
   #Row 4
   [psg.Multiline('Ledtråd 1 ', size=(20,10), background_color="#00AA00"),
    psg.Multiline('Ledtråd 2 ', size=(20,10), background_color="#00AA00"),
    psg.Multiline('Ledtråd 3 ', size=(20,10), background_color="#00AA00"),]
]

main_menu_layout = [
   #Row1
   [psg.Text('Quiz Titel', size=(15,1), background_color="#555555")],
   #Reveals the game_layout and hides the main menu on click. Row 2.
   [psg.Button(button_text="Start", button_color="#000000 on #FFFFFF", key="-GAMEWINDOW-")],
   #Row3
   [psg.Button(button_text="Inställningar", button_color="#000000 on #FFFFFF")],
   #Row4
   [psg.Button(button_text="Expansion1?", button_color="#000000 on #FFFFFF")],
   #Row5
   [psg.Button(button_text="Stäng av", button_color="#000000 on #FFFFFF")]
]

#Found how to stack layouts here https://stackoverflow.com/questions/59500558/how-to-display-different-layouts-based-on-button-clicks-in-pysimple-gui-persis first answer
program_layout = [
   #-COL1- is visible on startup, since the main menu is there.
   #Colums have to be in a list, otherwise the program crashes on startup.
   #Need to set each columns background_color to match the windows background. Otherwise it will use the default blue for the column.
   [
       psg.Column(main_menu_layout, key="-COL1-", background_color="#555555"), psg.Column(game_layout, visible=False, key="-COL2-", background_color="#555555")
   ]
]

#Settings for the program window
window = psg.Window('Game Window', program_layout, size=(800, 800), background_color="#555555", element_justification="center", element_padding=10)

#Makes the program loop, otherwise it closes down upon clicking any button.
while True:
   #layout2 används istället för layout, vilket betyder att man kan 'skriva över' innehållet i fönstret för att ändra vy.
   #window = psg.Window('Game Window', layout2, size=(800, 800), element_justification="center", element_padding=10)
   event, values = window.read()
   if event == psg.WIN_CLOSED or event == 'Exit':
      break
   print (event, values)
   
   #Probably a better way to shift between the menus, but it works for now.
   if event == "-MAINMENU-":
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=True)
   if event == "-GAMEWINDOW-":
        window['-COL1-'].update(visible=False)
        window['-COL2-'].update(visible=True)
window.close()