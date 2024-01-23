import PySimpleGUI as sg
import random
import time
sg.set_options(font=("Arial Bold", 16))

#Global variables that handle some UI elements. Have to be above the places they're used, so put them up top.
question_number = 1
max_questions = 10

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
    sg.Text(f"Fråga {question_number} av {max_questions}", size=(15,1), background_color="#555555", key="-GAMEQUESTIONS-"), 
    sg.Text("Timer:  ", size=(15,1), background_color="#555555", key="-GAMETIMER-"),
    #Reveals the main_menu_layout and hides the game on click.
    #TODO: Remove the placeholder button that goes back to the main menu from the game once its no longer needed.
    sg.Button(button_text="MainMenu", button_color="#000000 on #FFFFFF", key="-PLACEHOLDERMENU-"  ),
    sg.Button(button_text="Hjälp", button_color="#000000 on #03a5fc", key="-HELPSCREEN-")],
   
    #Row2
    #disabled=True makes it impossible to write in the multiline, but you can still select the text which is not ideal.
    #TODO: Can't figure out a way to disable/hide the scrollbar.
    [sg.Multiline("Fråga här! \nRad 2 av texten" , size=(720,15), background_color="#150B3F", text_color="#FFFFFF", key="-QUESTIONBOX-" ,disabled=True)],
   
    #Row3
    #default_text needs to be removed manually when typing. Keeping it for now to show what the box is for.
    #expand_x och y makes the elements expand in size until they reach another element. At least I think so.
    [sg.Input("Skriv svar här", expand_x=True, expand_y=True, key="-ANSWERBOX-"),
    sg.Button(expand_x=True, expand_y=True, button_text="Skicka Svar", key="-SUBMIT_ANSWER-") ],
    
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
    [sg.Button(button_text="-", button_color="#150B3F", size=(2,1), key="-SUBQUESTION-"),
    sg.Text(f"{max_questions}", background_color="#FFFFFF", text_color="#000000", key="-MAXQUESTIONDISPLAY-"),
    sg.Button(button_text="+", button_color="#150B3F", size=(2,1), key="-ADDQUESTION-")],
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
    [
        sg.Column(main_menu_layout, key="-COL1-", background_color="#555555", element_justification="center", pad=(0,125)),
        sg.Column(game_layout, visible=False, key="-COL2-", background_color="#555555"),
        sg.Column(settings_layout, visible=False, key="-COL3-", background_color="#555555", element_justification="center", pad=(0,125)),
        sg.Column(help_layout, visible=False, key="-COL4-", background_color="#555555", element_justification="right")
    ]
]

#Settings for the program window.
window = sg.Window("Game Window", program_layout, size=(800, 800), background_color="#555555", element_justification="center", element_padding=10)

#Class used to create the questions as objects.
#text = str, solution = str, hints = str (for now), cipher = str, image = str path to the image, cipher_image = same as image, selected = bool, default to False, q_id = int
class Question:
    def __init__(self, text, solution, hints, cipher, image, cipher_image, selected, q_id):
        self.text = text
        self.solution = solution
        self.hints = hints
        self.cipher = cipher
        self.image = image
        self.cipher_image = cipher_image
        self.selected = selected
        self.q_id = q_id

#Placeholder values while testing question functions
question1 = Question("Question1 value \nLine 2 test", "Solution here", "Hints here", "Cipher here", "image path here", "cipher image path here", False, 0)
question2 = Question("Question2 value \nLine fghgfhgfhgfh", "Solution here", "Hints here", "Cipher here", "image path here", "cipher image path here", False, 1)
question3 = Question("Question3 value \nLine asdasdasdasd", "Solution here", "Hints here", "Cipher here", "image path here", "cipher image path here", False, 2)

#List to loop through to check the available questions.
question_list = [question1, question2, question3]
used_question_list = []


#Function had to be placed outside of the Question class, since the question lists are 'list' objects and not 'Question'.
#Placing the function like this means it can be called without doing 'object_name.pick_Question'.
def pick_Question(placeholder_name):
    #Gets the list length as a value. Subtract 1 since random.randint is inclusive, and len() returns the wrong number.
    #EG: If the list has 3 elements, len() would return 3. Since list indexes start at 0 and go to len()-1, it wouldn't work without subtracting 1 initially for the question_list_length variable.
    question_list_length = len(placeholder_name)-1
    #used_question_list is used to break the while loop if you run out of new questions. This means the game doesn't freeze if you use all questions in the list.
    global used_question_list
    #new_question is used to break the while loop once a new question has been chosen
    new_question = False
    while new_question == False:
        #Breaks the loop if you run out of unique questions.
        #In other words, if all questions have been chosen and the function is called again, nothing happens. Before, the program would freeze cause of the while loop.
        if len(used_question_list) == len(placeholder_name):
            break
        #Generates a random number between and including 0 until the length of the list
        random_question = random.randint(0, question_list_length)
        for x in placeholder_name:
            #Checks that the question's id matches the random number
            if x.q_id == random_question:
                #Checks the selected value, since questions should only appear once each.
                if x.selected == False:
                    #If everything checks out, the question is added to the display.
                    window["-QUESTIONBOX-"].update(placeholder_name[random_question].text)
                    x.selected = True
                    new_question = True
                    #The currently selected question is put inside the global variable 'active_question' for use in other functions.
                    global active_question
                    active_question = x
                    used_question_list.append(x)
                #If the ID and random number match, but the question has been selected already, it breaks and generates a new number:
                elif x.selected == True:
                    break


def check_Answer():
    #active_question from 'pick_Question' is used so you don't have to loop through every question in the game when checking the answer
    global active_question
    #The global question variables are used to upadte UI elements
    global question_number
    #Found out how to use 'values' to fetch elements here: https://www.reddit.com/r/learnpython/comments/f4t73m/didnt_understand_the_key_concept_in_pysimplegui/
    answer = values["-ANSWERBOX-"]
    #TODO: solution is case sensitive. Make function that transforms capital letters into small ones?
    if answer == active_question.solution:
        print("japp")
        #Updates the question counter at the top of the window
        question_number += 1
        window["-GAMEQUESTIONS-"].update(f"Fråga {question_number} av {max_questions}")
        #Picks a new question on correct answer
        pick_Question(question_list)
    else:
        print("nepp")


def set_Max_Questions():
    global max_questions
    global question_number
    if event == "-SUBQUESTION-":
        max_questions -= 1
        #Updates the question display in the game view
        window["-GAMEQUESTIONS-"].update(f"Fråga {question_number} av {max_questions}")
    elif event == "-ADDQUESTION-":
        max_questions += 1
        #Updates the question display in the game view
        window["-GAMEQUESTIONS-"].update(f"Fråga {question_number} av {max_questions}")

#Global variables used to compare the clock at the start of the game and once you submit your answer
timer_start = 0

#Sets the timer_start variable to the current system time. Function is called once you press the 'start' button on the main menu.
def start_Timer():
    global timer_start
    timer_start = time.time()

#Updates the timer to be 'current system time' - 'system time at match start'. Gives the elapsed time in seconds.
def update_Timer():
    global timer_start
    total_time = round((time.time() - timer_start),2) 
    window["-GAMETIMER-"].update(f"Timer: {total_time}")
        

#Makes the program loop, otherwise it closes down upon clicking any button.
while True:
    #TODO: Check if the preset event == 'Exit' is needed. If it isn't, delete it.
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit" or event == "-QUIT-":
        break
    #print (event, values)
   
    #Probably a better way to shift between the menus, but it works for now.
    #COL1 = Main menu, 2 = Game view, 3 = Settings, 4 = Help screen
    #TODO: Remove if for placeholder once it's no longer needed.
    if event == "-PLACEHOLDERMENU-":
        window["-COL2-"].update(visible=False)
        window["-COL1-"].update(visible=True)
    if event == "-GAMEWINDOW-":
        window["-COL1-"].update(visible=False)
        window["-COL2-"].update(visible=True)
        #TODO: Change when the game picks a new question, instead of just when you change to the game view.
        pick_Question(question_list)
        start_Timer()
        #Makes the initial timer display as 0.0 for testing.
        #update_Timer()
    if event == "-SUBMIT_ANSWER-":
        check_Answer()
        update_Timer()
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
        #Update the timer display, since it's visible again.
        update_Timer()
    #Ifs that change the max_question amount
    if event == "-SUBQUESTION-" or event == "-ADDQUESTION-":
        set_Max_Questions()
        print(max_questions)
        #NOTE: Think the max_questions value inside the textbox is an int? Not sure tough
        window["-MAXQUESTIONDISPLAY-"].update(max_questions)
    #  
    #Ends the game once you answer enough questions.
    #TODO: Some sort of result screen instead of just closing the program
    if question_number == max_questions+1:
        print("Du vann!")
        break
window.close()