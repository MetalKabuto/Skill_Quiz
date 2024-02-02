import PySimpleGUI as sg
import random
import time
sg.set_options(font=("Arial Bold", 16))

#Global variables that handle some UI elements. Have to be above the places they're used, so put them up top.
question_number = 1
max_questions = 10
#Used to determine the penalty for using a hint
hint_penalty = 15

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
    [sg.Button(button_text="Ledtråd", button_color="#000000 on #00AA00", key="-HINTBUTTON-" ),
    #Text elements match the window background
    sg.Text(f"Fråga {question_number} av {max_questions}", size=(15,1), background_color="#555555", key="-GAMEQUESTIONS-"), 
    sg.Text("Tid:  ", size=(15,1), background_color="#555555", key="-GAMETIMER-"),
    #Reveals the main_menu_layout and hides the game on click.
    #TODO: Remove the placeholder button that goes back to the main menu from the game once its no longer needed.
    sg.Button(button_text="MainMenu", button_color="#000000 on #FFFFFF", key="-PLACEHOLDERMENU-"  ),
    sg.Button(button_text="Hjälp", button_color="#000000 on #03a5fc", key="-HELPSCREEN-")],
   
    #Row2
    #disabled=True makes it impossible to write in the multiline, but you can still select the text which is not ideal.
    #TODO: no_scrollbar=True to get rid of scrollbars if they're not needed
    [sg.Multiline("Fråga här! \nRad 2 av texten" , size=(720,15), background_color="#150B3F", text_color="#FFFFFF", key="-QUESTIONBOX-" , disabled=True)],
   
    #Row3
    #default_text needs to be removed manually when typing. Keeping it for now to show what the box is for.
    #expand_x och y makes the elements expand in size until they reach another element. At least I think so.
    [sg.Input("Skriv svar här", expand_x=True, expand_y=True, key="-ANSWERBOX-"),
    sg.Button(expand_x=True, expand_y=True, button_text="Skicka Svar", key="-SUBMIT_ANSWER-") ],
    
    #Row 4
    [sg.Text("Ledtråd 1 \n rad 2", size=(20,10), text_color="#00AA00", background_color="#00AA00", key="-HINTBOX1-"),
    sg.Text("Ledtråd 2 ", size=(20,10), text_color="#00AA00", background_color="#00AA00", key="-HINTBOX2-"),
    sg.Text("Ledtråd 3 ", size=(20,10), text_color="#00AA00", background_color="#00AA00", key="-HINTBOX3-")]
]

settings_layout = [
    #Row 1, Text has no size, that way it only uses the necessary space for the text and will align horizontally.
    [sg.Text("Antal Frågor", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 2
    [sg.Button(button_text="-", button_color="#150B3F", size=(2,1), key="-SUBQUESTION-"),
    sg.Text(f"{max_questions}", background_color="#FFFFFF", text_color="#000000", key="-MAXQUESTIONDISPLAY-"),
    sg.Button(button_text="+", button_color="#150B3F", size=(2,1), key="-ADDQUESTION-")],
    #Row 3, Text
    [sg.Text("Svårighetsgrad", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 4, Difficulty
    #TODO: Have a different background color for the currently selected difficulty.
    [sg.Button(button_text="Ålder 1", button_color="#150B3F", key="-DIFF1-"),
    sg.Button(button_text="Ålder 2", button_color="#150B3F", key="-DIFF2-"),
    sg.Button(button_text="Ålder 3", button_color="#150B3F", key="-DIFF3-"),
    sg.Button(button_text="Ålder 4", button_color="#150B3F", key="-DIFF4-")],
    #Row 5, Text
    [sg.Text("Tidstillägg per ledtråd:", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 6, Time penalty for using a hint
    [sg.Button(button_text="-", button_color="#150B3F", size=(2,1), key="-SUBPENALTY-"),
    sg.Text(f"{hint_penalty}s", background_color="#FFFFFF", text_color="#000000", key="-PENALTYDISPLAY-"),
    sg.Button(button_text="+", button_color="#150B3F", size=(2,1), key="-ADDPENALTY-")],
    #Row 7, back to main menu.
    [sg.Button(button_text="Tillbaka", button_color="#FFFFFF on #150B3F", key="-MAINMENU-" )]
]

#Since you can only change opacity for the entire window with pysimplegui, appearance doesn't match the wireframe with the dimmed background.
help_layout = [
    #Row 1. Button is on its own row to place it above the text in the layout.
    [sg.Button(button_text="Tillbaka", button_color="#FFFFFF on #150B3F", key="-EXITHELP-" )],
    #Row 2
    [sg.Multiline("Hjälptext här! \nRad 2 av texten" , size=(720,5), background_color="#03a5fc", text_color="#000000", disabled=True, no_scrollbar = True, key="-HELPTEXT-")],
    #Row 3, reserved for eventual images. Images should be GIF or PNG only according to pysimplegui.
    [sg.Image(source="", key="-HELPIMAGE-")]
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
#text = str, solution = str, hints = str (for now), cipher = str, selected = bool, default to False, q_id = int, difficulty = 1-4
class Question:
    def __init__(self, text, solution, hint1, hint2, hint3, cipher, selected, q_id, difficulty):
        self.text = text
        self.solution = solution
        self.hint1 = hint1
        self.hint2 = hint2
        self.hint3 = hint3
        self.cipher = cipher
        self.selected = selected
        self.q_id = q_id
        self.difficulty = difficulty


#Empty hints should be given the value "" to work with functions.
#Questions cipher attributes must match one of the objects in the cipher_list to make help functions work
#TODO: For now, all questions of the same type have the same difficulty. Add more questions to flesh out the difficulty options, so that all types can be found in all diccifulties.
#Caesar questions
caesar_q1 = Question("Dekryptera ordet: ern \nnyckel = 3", "bok", "Byt ut bokstäverna mot de 3 steg bakåt i alfabetet.", "", "", "caesar", False, 0, 1)
caesar_q2 = Question("Dekryptera ordet: mdxy \nnyckel = 5", "häst", "Byt ut bokstäverna mot de 5 steg bakåt i alfabetet.", "", "", "caesar", False, 1, 1)
caesar_q3 = Question("Dekryptera ordet: hveoi \nnyckel = 4", "drake", "Byt ut bokstäverna mot de 4 steg bakåt i alfabetet.", "", "", "caesar", False, 2, 1)
caesar_q4 = Question("Dekryptera ordet: mrughq \nnyckel = 3", "jorden", "Byt ut bokstäverna mot de 3 steg bakåt i alfabetet.", "", "", "caesar", False, 3, 1)
caesar_q5 = Question("Dekryptera ordet: hexsv \nnyckel = 4", "dator", "Byt ut bokstäverna mot de 4 steg bakåt i alfabetet.", "", "", "caesar", False, 4, 1)
caesar_q6 = Question("Dekryptera ordet: uwtlwfrrjwnsl \nnyckel = 5", "programmering", "Byt ut bokstäverna mot de 5 steg bakåt i alfabetet.", "", "", "caesar", False, 5, 1)
caesar_q7 = Question("Dekryptera ordet: doir \nnyckel = 4", "öken", "Byt ut bokstäverna mot de 4 steg bakåt i alfabetet.", "", "", "caesar", False, 6, 1)
caesar_q8 = Question("Dekryptera ordet: bghovwhq \nnyckel = 3", "ädelsten", "Byt ut bokstäverna mot de 3 steg bakåt i alfabetet.", "", "", "caesar", False, 7, 1)
#SCOUT questions
scout_q1 = Question("Dekryptera ordet med SCOUT: Tu Cc Cc Co Ss", "uggla", "Byt ut paren mot bokstaven där koordinaterna möts.", "", "", "scout", False, 8, 2)
scout_q2 = Question("Dekryptera ordet med SCOUT: Tt Us Co Ss", "ödla", "Byt ut paren mot bokstaven där de möts.", "", "", "scout", False, 9, 2)
scout_q3 = Question("Dekryptera ordet med SCOUT: Su Cu Ts Ou Uc Us Ts Uo Uu", "president", "Byt ut paren mot bokstaven där de möts.", "", "", "scout", False, 10, 2)
scout_q4 = Question("Dekryptera ordet med SCOUT: Ou Pu Tt So Ts", "spöke", "Byt ut paren mot bokstaven där de möts.", "", "", "scout", False, 11, 2)
scout_q5 = Question("Dekryptera ordet med SCOUT: Ts Co Ts Sc Ss Uo Uu", "elefant", "Byt ut paren mot bokstaven där de möts.", "", "", "scout", False, 12, 2)
scout_q6 = Question("Dekryptera ordet med SCOUT: Cs Ct Uu Ts", "byte", "Byt ut paren mot bokstaven där de möts.", "", "", "scout", False, 13, 2)
scout_q7 = Question("Dekryptera ordet med SCOUT: Uo Ut Uu St Ts Cu So", "nätverk", "Byt ut paren mot bokstaven där de möts.", "", "", "scout", False, 14, 2)
scout_q8 = Question("Dekryptera ordet med SCOUT: Cs Uc Co", "bil", "Byt ut paren mot bokstaven där de möts.", "", "", "scout", False, 15, 2)
scout_q9 = Question("Dekryptera ordet med SCOUT: Us Ts Os Uc Oo Ss Co", "decimal", "Byt ut paren mot bokstaven där de möts.", "", "", "scout", False, 16, 2)
#Hex questions. TODO: Ska svaret vara stor eller liten bokstav? De har olika hexvärden.
hex_q1 = Question("Vilken bokstav blir hextalet: 44 \nSvara med stor bokstav!", "D", "Bokstaven ligger mellan A och I.", "", "", "hexadecimal", False, 17, 3)
hex_q2 = Question("Vilken bokstav blir hextalet: 59 \nSvara med stor bokstav!", "Y", "Bokstaven är en av de 5 sista.", "", "", "hexadecimal", False, 18, 3)
hex_q3 = Question("Vilken bokstav blir hextalet: 4c \nSvara med stor bokstav!", "L", "Bokstaven ligger mellan H och Q.", "", "", "hexadecimal", False, 19, 3)
hex_q4 = Question("Vilken bokstav blir hextalet: 4a \nSvara med stor bokstav!", "J", "Bokstaven är en av de 10 första.", "", "", "hexadecimal", False, 20, 3)
hex_q5 = Question("Vilken bokstav blir hextalet: 55 \nSvara med stor bokstav!", "U", "Bokstaven ligger mellan S och Z.", "", "", "hexadecimal", False, 21, 3)
hex_q6 = Question("Översätt ordet från hextal: 42 (c3 84) 53 54 \nSvara med stora bokstäver!", "BÄST", "Ordet börjar med B.", "(c3 84) är en bokstav.", "", "hexadecimal", False, 22, 3)
hex_q7 = Question("Översätt ordet från hextal: 53 4b (c3 96) 4c 44 \nSvara med stora bokstäver!", "SKÖLD", "Ordet börjar med S.", "(c3 96) är en bokstav.", "", "hexadecimal", False, 23, 3)
#Binary questions
bin_q1 = Question("Vilken bokstav blir det binära talet: 01 00 10 10 \nSvara med stor bokstav!", "J", "Bokstaven kommer efter D.", "De första 5 siffrorna är 01 00 1_ __", "", "binary", False, 24, 4)
bin_q2 = Question("Vilken bokstav blir det binära talet: 01 00 11 11 \nSvara med stor bokstav!", "O", "Bokstaven kommer före R.", "De första 5 siffrorna är 01 00 1_ __", "", "binary", False, 25, 4)
bin_q3 = Question("Vilken bokstav blir det binära talet: 01 00 11 01 \nSvara med stor bokstav!", "M", "Bokstaven kommer efter I.", "De första 5 siffrorna är 01 00 1_ __", "", "binary", False, 26, 4)
bin_q4 = Question("Vilken bokstav blir det binära talet: 01 00 10 11 \nSvara med stor bokstav!", "K", "Boktaven kommer före O.", "De första 5 siffrorna är 01 00 1_ __", "", "binary", False, 27, 4)
bin_q5 = Question("Översätt ordet från binär kod: (01 01 00 11) (01 01 01 00) (01 00 01 01) (01 00 11 10) \nSvara med stora bokstäver!", "STEN", "Ordet börjar med S.", "Ordet slutar med N.", "", "binary", False, 28, 4)
bin_q6 = Question("Översätt ordet från binär kod: (01 01 01 00) (01 01 00 10) (11 00 00 11 10 00 01 00) (01 00 01 00) \nSvara med stora bokstäver!", "TRÄD", "Ordet börjar med T.", "(11 00 00 11 10 00 01 00) är en bokstav.", "Andra bokstaven är R.", "binary", False, 29, 4)

#List to loop through to check the available questions.
question_list = [
    caesar_q1, caesar_q2, caesar_q3, caesar_q4, caesar_q5, caesar_q6, caesar_q7, caesar_q8,
    scout_q1, scout_q2, scout_q3, scout_q4, scout_q5, scout_q6, scout_q7, scout_q8, scout_q9,
    hex_q1, hex_q2, hex_q3, hex_q4, hex_q5, hex_q6, hex_q7,
    bin_q1, bin_q2, bin_q3, bin_q4, bin_q5, bin_q6
]
used_question_list = []
selected_questions_list = []
selected_difficulty = 0

class Cipher:
    def __init__(self, cipher, help_text, help_image):
        self.cipher = cipher
        self.help_text = help_text
        self.help_image = help_image

#Folder called _internal is added to the project to simulate installing the game through pyinstaller, which creates a _internal folder to put the images into.
cipher1 = Cipher("caesar", "Caesarchiffer används genom att byta ut bokstäverna i ett ord mot en anna bokstav ett visst antal steg framåt i alfabetet.", 
                 "_internal\help_image\caesar_help.png")
cipher2 = Cipher("scout", "Bokstäverna är placerade i ett rutnät som används för att dekryptera ett ord eller en mening. " + 
                 "Ett par, EX Ut, ska bytas ut mot bokstaven i rutnätet där U och t möts. OBS: Inga ord använder Q, W, X.", "_internal\help_image\scout_help.png")
cipher3 = Cipher("hexadecimal", "Hexadecimal är ett system som använder sig av siffrorna 0-9 och bokstäverna a-f.\n" +
                 "Varje siffra och bokstav har ett värde från 0 till 15. Hex-tal kan i sin tur konverteras till binära tal eller ASCII tecken.", "_internal\help_image\hex_help.png")
#FIXME: For some reason the program can't read image files that have \b in them, so for now the file has B instead.
cipher4 = Cipher("binary", "Binära tal är en sträng av 8 stycken ettor och nollor.\n" +
                 "Bokstäver kan skrivas med dessa strängar. Å, Ä och Ö skrivs som två tal efter varann, eftersom de inte finns i engelska alfabetet.", "_internal\help_image\Binary_help.png")

#List containing all the ciphers used for the questions. Might not be needed?
cipher_list = [cipher1, cipher2, cipher3, cipher4]

#Is called when you press a difficulty button. 
def difficulty_select():
    global selected_difficulty
    global selected_questions_list
    if event == "-DIFF1-":
        #Empties the list of items, in case you press the button multiple times.
        selected_questions_list = []
        selected_difficulty = 1
        for x in question_list:
            if x.difficulty == 1:
                selected_questions_list.append(x)
                print("selected")
    elif event == "-DIFF2-":
        selected_questions_list = []
        selected_difficulty = 2
        for x in question_list:
            if x.difficulty == 2:
                selected_questions_list.append(x)
                print("selected")
    elif event == "-DIFF3-":
        selected_questions_list = []
        selected_difficulty = 3
        for x in question_list:
            if x.difficulty == 3:
                selected_questions_list.append(x)
                print("selected")
    elif event == "-DIFF4-":
        selected_questions_list = []
        selected_difficulty = 4
        for x in question_list:
            if x.difficulty == 4:
                selected_questions_list.append(x)
                print("selected")
    

#FIXME: Think you can remove global for lists? cipher_help_list works even tough i didn't declare global first.
def pick_help_text(list_name):
    global active_question0
    #Checks the active questions cipher value to decide what help-items to show.
    if active_question.cipher == "caesar":
        window["-HELPTEXT-"].update(f"{cipher_list[0].help_text}")
        window["-HELPIMAGE-"].update(f"{cipher_list[0].help_image}")
    elif active_question.cipher == "scout":
        window["-HELPTEXT-"].update(f"{cipher_list[1].help_text}")
        window["-HELPIMAGE-"].update(f"{cipher_list[1].help_image}")
    elif active_question.cipher == "hexadecimal":
        window["-HELPTEXT-"].update(f"{cipher_list[2].help_text}")
        window["-HELPIMAGE-"].update(f"{cipher_list[2].help_image}")
    elif active_question.cipher == "binary":
        window["-HELPTEXT-"].update(f"{cipher_list[3].help_text}")
        window["-HELPIMAGE-"].update(f"{cipher_list[3].help_image}")


                

#Globals used to check if hints have text or not
hint1_exists = False
hint2_exists = False
hint3_exists = False

#TODO: Make hintboxes invisible if they're empty? Right now they shift to a darker shade of green.
#Put the text-values inside the hintbox elements. Also changes background and text color to indicate if the hint is available or not.
#In other words, if there is no hint 2 or 3, the box becomes a darker shade. Text color is set to match the lighter shade if a hint is in the box to make it unreadable.
def set_hints(list_name):
    global active_question
    global selected_difficulty
    global hint1_exists
    global hint2_exists
    global hint3_exists  
    for x in list_name:
        if x.q_id == active_question.q_id:
            #Questions always have at least one hint, so it always updates hintbox1
            window["-HINTBOX1-"].update(f"{x.hint1}")
            hint1_exists = True
            #If the object has a hint2 value, it gets put into the box with the same color as the background to make the text invisible
            if x.hint2 != "":
                window["-HINTBOX2-"].update(f"{x.hint2}")
                window["-HINTBOX2-"].update(background_color="#00AA00")
                window["-HINTBOX2-"].update(text_color="#00AA00")
                hint2_exists = True
                if x.hint3 != "":
                    window["-HINTBOX3-"].update(f"{x.hint3}")
                    window["-HINTBOX3-"].update(background_color="#00AA00")
                    window["-HINTBOX3-"].update(text_color="#00AA00")
                    hint3_exists = True
                else:
                    window["-HINTBOX3-"].update("")
                    window["-HINTBOX3-"].update(background_color="#004400")
                    break
            #If hint2 is empty, then hint3 is also always empty and gets darkened at the same time.
            else:
                window["-HINTBOX2-"].update("")
                window["-HINTBOX2-"].update(background_color="#004400")
                #Updates box3 even if the second hint is empty.
                #Otherwise, if the game starts with a question that only has 1 hint, box3 will be light green like it has a hint when it doesn't.
                window["-HINTBOX3-"].update("")
                window["-HINTBOX3-"].update(background_color="#004400")
                break

#Globals to verify hint-text visibility
hint1_visible = False
hint2_visible = False
hint3_visible = False

#Changes the text-color of the next hint so that it becomes readable.
#FIXME: While loop might not be needed?
def reveal_hint():
    new_hint = False
    global hint1_visible
    global hint2_visible
    global hint3_visible
    global hint1_exists
    global hint2_exists
    global hint3_exists
    while new_hint == False:
        if hint1_visible == False and hint1_exists == True:
            window["-HINTBOX1-"].update(text_color="#FFFFFF")
            #Adds time to timer here
            add_time_penalty()
            hint1_visible = True
            new_hint = True
        elif hint2_visible == False and hint2_exists == True:
            window["-HINTBOX2-"].update(text_color="#FFFFFF")
            #Adds time to timer here
            add_time_penalty()
            hint2_visible = True
            new_hint = True
        elif hint3_visible == False and hint3_exists == True:
            window["-HINTBOX3-"].update(text_color="#FFFFFF")
            #Adds time to timer here
            add_time_penalty()
            hint3_visible = True
            new_hint = True
        #If all hints have been revealead, break the loop without doing anything
        else:
            break
        
#Resets the hint_visible variables so they work for the next question.
def hide_hints():
    global hint1_visible
    global hint2_visible
    global hint3_visible
    global hint1_exists
    global hint2_exists
    global hint3_exists
    hint1_visible = False
    hint2_visible = False
    hint3_visible = False
    hint1_exists = False
    hint2_exists = False
    hint3_exists = False
    #There is always a hint1, so text_color is changed to the element background one here to hide it.
    window["-HINTBOX1-"].update(text_color="#00AA00")

#Function had to be placed outside of the Question class, since the question lists are 'list' objects and not 'Question'.
#Placing the function like this means it can be called without doing 'object_name.pick_Question'.
def pick_Question(placeholder_name):
    #Gets the list length as a value. Subtract 1 since random.randint is inclusive, and len() returns the wrong number.
    #EG: If the list has 3 elements, len() would return 3. Since list indexes start at 0 and go to len()-1, it wouldn't work without subtracting 1 initially for the question_list_length variable.
    question_list_length = len(placeholder_name)-1
    #used_question_list is used to break the while loop if you run out of new questions. This means the game doesn't freeze if you use all questions in the list.
    global used_question_list
    #new_question is used to break the while loop once a new question has been chosen
    next_question = False
    while next_question == False:
        #Breaks the loop if you run out of unique questions.
        #In other words, if all questions have been chosen and the function is called again, nothing happens. Before, the program would freeze cause of the while loop.
        if len(used_question_list) == len(placeholder_name):
            break
        #Generates a random number between and including 0 until the length of the list
        random_question = random.randint(0, question_list_length)
        #Checks that the question's id matches the random number
        if placeholder_name[random_question].selected == False:
            #If everything checks out, the question is added to the display.
            window["-QUESTIONBOX-"].update(placeholder_name[random_question].text)
            placeholder_name[random_question].selected = True
            next_question = True
            #The currently selected question is put inside the global variable 'active_question' for use in other functions.
            global active_question
            active_question = placeholder_name[random_question]
            used_question_list.append(placeholder_name[random_question])
            
                

def new_question():
    global selected_difficulty
    #If you haven't altered the difficulty, the game will pick from all questions in the program.
    if selected_difficulty == 0:
        pick_Question(question_list)
        pick_help_text(question_list)
        set_hints(question_list)
    #If you have changed difficulty, it picks a question from the list that gets generated.
    else:
        pick_Question(selected_questions_list) 
        pick_help_text(selected_questions_list)
        set_hints(selected_questions_list)

def check_Answer():
    #active_question from 'pick_Question' is used so you don't have to loop through every question in the game when checking the answer
    global active_question
    #The global question variables are used to update UI elements
    global question_number
    #Found out how to use 'values' to fetch elements here: https://www.reddit.com/r/learnpython/comments/f4t73m/didnt_understand_the_key_concept_in_pysimplegui/
    answer = values["-ANSWERBOX-"]
    global selected_difficulty
    #TODO: solution is case sensitive. Make function that transforms capital letters into small ones?
    if answer == active_question.solution:
        print("japp")
        #Updates the question counter at the top of the window
        question_number += 1
        window["-GAMEQUESTIONS-"].update(f"Fråga {question_number} av {max_questions}")
        #hide_hints needs to be first to change the global variables.
        #This is because set_ makes some variables True, when hide_ makes all of them False again.
        hide_hints()
        #Picks a new question on correct answer
        new_question()
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
    #Updates the display in the settings view
    window["-MAXQUESTIONDISPLAY-"].update(max_questions)
        
def set_Penalty_Time():
    global hint_penalty
    if event == "-SUBPENALTY-":
        hint_penalty -= 1
    elif event == "-ADDPENALTY-":
        hint_penalty += 1
    #Had to use string interpolation in order to keep the s after the time
    window["-PENALTYDISPLAY-"].update(f"{hint_penalty}s")

#Global variables used to compare the clock at the start of the game and once you submit your answer
timer_start = 0
total_time = 0
total_penalty = 0

#Sets the timer_start variable to the current system time. Function is called once you press the 'start' button on the main menu.
def start_Timer():
    global timer_start
    timer_start = time.time()

#Updates the timer to be 'current system time' - 'system time at match start'. Gives the elapsed time in seconds.
#NOTE: Make the time whole numbers instead of rounding?
def update_Timer():
    global timer_start
    global total_time
    global total_penalty
    total_time = round((time.time() - timer_start),2) 
    window["-GAMETIMER-"].update(f"Tid: {total_time + total_penalty}")
        
def add_time_penalty():
    global hint_penalty
    global total_penalty
    total_penalty += hint_penalty

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
        new_question()
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
    #Ifs that change the max_question amount
    if event == "-SUBQUESTION-" or event == "-ADDQUESTION-":
        set_Max_Questions()
    #Ifs that change the time penalty using a hint
    if event == "-SUBPENALTY-" or event == "-ADDPENALTY-":
        set_Penalty_Time()
    #Reveals the next hint. Also adds a time penalty
    if event == "-HINTBUTTON-":
        reveal_hint()
        update_Timer()
    #Sets the difficulty variable to 1,2,3,4 depending on button press.
    if event == "-DIFF1-" or "-DIFF2-" or "-DIFF3-" or "-DIFF4-":
        difficulty_select()
    #Ends the game once you answer enough questions.
    #TODO: Some sort of result screen instead of just closing the program
    if question_number == max_questions+1:
        #Updates the total_time variable in order to get the completion time for the match.
        update_Timer()
        print(f"Du vann! Din slutliga tid är: {total_time}")
        break
window.close()