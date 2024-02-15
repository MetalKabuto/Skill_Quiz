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
    #Text elements background match the window background
    sg.Text(f"Fråga {question_number} av {max_questions}", size=(15,1), background_color="#555555", key="-GAMEQUESTIONS-"), 
    sg.Text("Tid:  ", size=(25,1), background_color="#555555", key="-GAMETIMER-"),
    #Reveals the main_menu_layout and hides the game on click.
    #TODO: Remove the placeholder button that goes back to the main menu from the game once its no longer needed.
    #sg.Button(button_text="MainMenu", button_color="#000000 on #FFFFFF", key="-PLACEHOLDERMENU-"  ),
    sg.Button(button_text="Hjälp", button_color="#000000 on #03a5fc", key="-HELPSCREEN-")],
    #Row2
    #disabled=True makes it impossible to write in the multiline.
    [sg.Multiline("Fråga här! \nRad 2 av texten" , size=(100,5), background_color="#150B3F", text_color="#FFFFFF", key="-QUESTIONBOX-" , disabled=True, no_scrollbar=True)],
    #Row 3
    [sg.Image(source="", key="-THUMBIMAGE-")],
    #Row 4
    #default_text needs to be removed manually when typing. Keeping it for now to show what the box is for.
    [sg.Input("Skriv svar här", expand_x=True, expand_y=True, key="-ANSWERBOX-"),
    sg.Button(expand_x=True, expand_y=True, button_text="Skicka Svar", key="-SUBMIT_ANSWER-") ],
    #Row 5
    [sg.Text("Ledtråd 1 \n rad 2", size=(18,10), text_color="#00AA00", background_color="#00AA00", key="-HINTBOX1-"),
    sg.Text("Ledtråd 2 ", size=(18,10), text_color="#00AA00", background_color="#00AA00", key="-HINTBOX2-"),
    sg.Text("Ledtråd 3 ", size=(18,10), text_color="#00AA00", background_color="#00AA00", key="-HINTBOX3-")]
]

settings_layout = [
    #Row 1
    [sg.Text("Antal Frågor", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 2
    [sg.Button(button_text="-", button_color="#150B3F", size=(2,1), key="-SUBQUESTION-"),
    sg.Text(f"{max_questions}", background_color="#FFFFFF", text_color="#000000", key="-MAXQUESTIONDISPLAY-"),
    sg.Button(button_text="+", button_color="#150B3F", size=(2,1), key="-ADDQUESTION-")],
    #Row 3, Text
    [sg.Text("Svårighetsgrad", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 4, Difficulty
    [sg.Button(button_text="Lätt", button_color="#150B3F", size=(5,1), key="-DIFF1-"),
    sg.Button(button_text="Medel", button_color="#150B3F", size=(5,1), key="-DIFF2-"),
    sg.Button(button_text="Svår", button_color="#150B3F", size=(5,1), key="-DIFF3-")],
    #Row 5, Text
    [sg.Text("Tidstillägg per ledtråd:", background_color="#555555", text_color="#FFFFFF", font=("Arial Bold", 16, "underline"))],
    #Row 6, Time penalty for using a hint
    [sg.Button(button_text="-", button_color="#150B3F", size=(2,1), key="-SUBPENALTY-"),
    sg.Text(f"{hint_penalty}s", background_color="#FFFFFF", text_color="#000000", key="-PENALTYDISPLAY-"),
    sg.Button(button_text="+", button_color="#150B3F", size=(2,1), key="-ADDPENALTY-")],
    #Row 7, back to main menu.
    [sg.Button(button_text="Tillbaka", button_color="#FFFFFF on #150B3F", key="-MAINMENU-" )]
]

help_layout = [
    #Row 1
    [sg.Button(button_text="Tillbaka", button_color="#FFFFFF on #150B3F", key="-EXITHELP-" )],
    #Row 2
    [sg.Multiline("Hjälptext här! \nRad 2 av texten" , size=(720,5), background_color="#03a5fc", text_color="#000000", disabled=True, no_scrollbar = True, key="-HELPTEXT-")],
    #Row 3. Images should be GIF or PNG only according to pysimplegui.
    [sg.Image(source="", key="-HELPIMAGE-")]
]

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

#Class used to create the questions as objects.
#text = str, solution = str, hints = str, cipher = str, selected = bool, default to False, q_id = int, difficulty = 1-4
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
#Easy questions
caesar_q1 = Question("Dekryptera ordet: ern \nnyckel = 3", "bok", "Någonting man kan läsa. En _.", "", "", "caesar", False, 0, 1)
caesar_q2 = Question("Dekryptera ordet: mdxy \nnyckel = 5", "häst", "Ett djur som man rider på.", "", "", "caesar", False, 1, 1)
caesar_q3 = Question("Dekryptera ordet: hveoi \nnyckel = 4", "drake", "Ett populärt monster.", "", "", "caesar", False, 2, 1)
caesar_q4 = Question("Dekryptera ordet: hexsv \nnyckel = 4", "dator", "En teknisk pryl.", "", "", "caesar", False, 3, 1)
caesar_q5 = Question("Dekryptera ordet: doir \nnyckel = 4", "öken", "Ett varmt ställe med mycket sand.", "", "", "caesar", False, 4, 1)

scout_q1 = Question("Dekryptera ordet med SCOUT: \nTu Cc Cc Co Ss", "uggla", "En fågel som kommer fram på natten.", "", "", "scout", False, 5, 1)
scout_q2 = Question("Dekryptera ordet med SCOUT: \nTt Us Co Ss", "ödla", "En sorts djur.", "", "", "scout", False, 6, 1)
scout_q3 = Question("Dekryptera ordet med SCOUT: \nOu Su Tt So Ts", "spöke", "'Jag tror det finns ett _ på min vind.'", "", "", "scout", False, 7, 1)
scout_q4 = Question("Dekryptera ordet med SCOUT: \nTo Ou Uu", "ost", "Görs av mjölk.", "", "", "scout", False, 8, 1)
scout_q5 = Question("Dekryptera ordet med SCOUT: \nCs Uc Co", "bil", "Ett fordon med fyra hjul.", "", "", "scout", False, 9, 1)

hex_q1 = Question("Vilken bokstav blir hextalet: 44 \nSvara med stor bokstav!", "D", "Bokstaven ligger mellan A och I.", "", "", "hexadecimal", False, 10, 1)
hex_q2 = Question("Vilken bokstav blir hextalet: 59 \nSvara med stor bokstav!", "Y", "Bokstaven är en av de 5 sista.", "", "", "hexadecimal", False, 11, 1)
hex_q3 = Question("Vilken bokstav blir hextalet: 4c \nSvara med stor bokstav!", "L", "Bokstaven ligger mellan H och Q.", "", "", "hexadecimal", False, 12, 1)
hex_q4 = Question("Vilken bokstav blir hextalet: 4a \nSvara med stor bokstav!", "J", "Bokstaven är en av de 10 första.", "", "", "hexadecimal", False, 13, 1)
hex_q5 = Question("Vilken bokstav blir hextalet: 55 \nSvara med stor bokstav!", "U", "Bokstaven ligger mellan S och Z.", "", "", "hexadecimal", False, 14, 1)

bin_q1 = Question("Vilken bokstav blir det binära talet: \n01 00 10 10 \nSvara med stor bokstav!", "J", "De första 6 siffrorna är 01 00 10 __", "Bokstaven kommer efter D.", "", "binary", False, 15, 1)
bin_q2 = Question("Vilken bokstav blir det binära talet: \n01 00 11 11 \nSvara med stor bokstav!", "O", "De första 6 siffrorna är 01 00 11 __", "Bokstaven kommer före R.", "", "binary", False, 16, 1)
bin_q3 = Question("Vilken bokstav blir det binära talet: \n01 00 11 01 \nSvara med stor bokstav!", "M", "De första 6 siffrorna är 01 00 11 __", "Bokstaven kommer efter I.", "", "binary", False, 17, 1)
bin_q4 = Question("Vilken bokstav blir det binära talet: \n01 00 10 11 \nSvara med stor bokstav!", "K", "De första 6 siffrorna är 01 00 10 __", "Boktaven kommer före O.", "", "binary", False, 18, 1)
bin_q5 = Question("Vilken bokstav blir det binära talet: \n01 01 00 00 \nSvara med stor bokstav!", "P", "De första 6 siffrorna är 01 01 00 __", "Boktaven kommer före X.", "", "binary", False, 19, 1)
#Medium questions
caesar_q6 = Question("Dekryptera ordet: mrughq \nnyckel = 3", "jorden", "En särskild planet.", "", "", "caesar", False, 20, 2)
caesar_q7 = Question("Dekryptera ordet: uwtlwfrrjwnsl \nnyckel = 5", "programmering", "Vad handlar lägret om?", "", "", "caesar", False, 21, 2)
caesar_q8 = Question("Dekryptera ordet: jpöktper \nnyckel = 4", "flygplan", "Åker mellan länder.", "", "", "caesar", False, 22, 2)
caesar_q9 = Question("Dekryptera ordet: ohjhqg \nnyckel = 3", "legend", "En historia från länge sedan är en _.", "", "", "caesar", False, 23, 2)
caesar_q10 = Question("Dekryptera ordet: bghovwhq \nnyckel = 3", "ädelsten", "Någonting värdefullt som används i smycken. En _.", "", "", "caesar", False, 24, 2)

scout_q6 = Question("Dekryptera ordet med SCOUT: \nSu Cu Ts Ou Uc Us Ts Uo Uu", "president", "Ordet börjar med P.", "Den högsta politikern är en _.", "", "scout", False, 25, 2)
scout_q7 = Question("Dekryptera ordet med SCOUT: \nTs Co Ts Sc Ss Uo Uu", "elefant", "Ordet börjar med E.", "Ett djur med stora öron.", "", "scout", False, 26, 2)
scout_q8 = Question("Dekryptera ordet med SCOUT: \nUo Ut Uu St Ts Cu So", "nätverk", "Ordet börjar med N.", "Datorer kommunicerar genom ett _.", "", "scout", False, 27, 2)
scout_q9 = Question("Dekryptera ordet med SCOUT: \nUs Ts Os Uc Oo Ss Co", "decimal", "Ordet börjar med D.", "'Avrunda till en _.'", "", "scout", False, 28, 2)
scout_q10 = Question("Dekryptera ordet med SCOUT: \nTu Uo Us Ts Cu Co Uc Cc", "underlig", "Ordet börjar med U.", "'En _ varelse.'", "", "scout", False, 29, 2)

hex_q6 = Question("Översätt ordet från hextal: 42 (c3 84) 53 54 \nSvara med stora bokstäver!", "BÄST", "Ordet börjar med B.", "Någonting kan inte vara bättre, det är _.", "", "hexadecimal", False, 30, 2)
hex_q7 = Question("Översätt ordet från hextal: 53 4b (c3 96) 4c 44 \nSvara med stora bokstäver!", "SKÖLD", "Ordet börjar med S.", "'En _ av järn.'.", "", "hexadecimal", False, 31, 2)
hex_q8 = Question("Översätt ordet från hextal: 4c 4f 47 49 4b \nSvara med stora bokstäver!", "LOGIK", "Ordet börjar med L.", "Viktigt vid programmering.", "", "hexadecimal", False, 32, 2)
hex_q9 = Question("Översätt ordet från hextal: 52 45 53 41 \nSvara med stora bokstäver!", "RESA", "Ordet börjar med R.", "Att åka någonstans.", "", "hexadecimal", False, 33, 2)
hex_q10 = Question("Översätt ordet från hextal: 54 45 47 45 4c \nSvara med stora bokstäver!", "TEGEL", "Ordet börjar med T.", "'Ett hus av _ tål starka vindar.'", "", "hexadecimal", False, 34, 2)

bin_q6 = Question("Vilka bokstäver blir de binära talen:\n(01 00 01 01) (01 00 11 11) \nSkriv med stora bokstäver utan mellanrum!", "EO", "Andra bokstaven är O.", "", "", "binary", False, 35, 2)
bin_q7 = Question("Vilka bokstäver blir de binära talen:\n(01 01 01 01) (01 01 00 10) \nSkriv med stora bokstäver utan mellanrum!", "UR", "Första bokstaven är U.", "", "", "binary", False, 36, 2)
bin_q8 = Question("Vilka bokstäver blir de binära talen:\n(01 00 00 01) (01 01 10 00) \nSkriv med stora bokstäver utan mellanrum!", "AX", "Andra bokstaven är X.", "", "", "binary", False, 37, 2)
bin_q9 = Question("Vilka bokstäver blir de binära talen:\n(01 00 11 00) (01 01 01 00) \nSkriv med stora bokstäver utan mellanrum!", "LT", "Första bokstaven är L.", "", "", "binary", False, 38, 2)
bin_q10 = Question("Vilka bokstäver blir de binära talen:\n(01 01 10 01) (01 00 10 00) \nSkriv med stora bokstäver utan mellanrum!", "YH", "Första bokstaven är Y.", "", "", "binary", False, 39, 2)
#Hard questions
caesar_q11 = Question("Dekryptera ordet: du_hwd \nnyckel = 3", "arbeta", "Ordet rimmar på 'leta'", "", "", "caesar", False, 40, 3)
caesar_q12 = Question("Dekryptera ordet: osrwx_k \nnyckel = 4", "konstig", "Den gömda bokstaven är en vokal.", "", "", "caesar", False, 41, 3)
caesar_q13 = Question("Dekryptera ordet: iw_pzq_ \nnyckel = 5", "drakula", "En känd figur med vassa tänder.", "", "", "caesar", False, 42, 3)
caesar_q14 = Question("Dekryptera ordet: cy_l_j \nnyckel = 3", "övning", "'X' ger färdighet.", "", "", "caesar", False, 43, 3)
caesar_q15 = Question("Dekryptera ordet: vsw__vdh \nnyckel = 4", "rostbröd", "Någonting man äter.", "", "", "caesar", False, 44, 3)

scout_q11 = Question("Dekryptera ordet med SCOUT: \nSo Ut Uo Cc __ Cu", "kängor", "Någonting man har på fötterna.", "", "", "scout", False, 45, 3)
scout_q12 = Question("Dekryptera ordet med SCOUT: \nCc __ __ Oo Co Uc Cc Uu", "grumligt", "'Vattnet är _, det är svårt att se någonting.'.", "", "", "scout", False, 46, 3)
scout_q13 = Question("Dekryptera ordet med SCOUT: \nCo To __ __ Uo Us Ts", "lovande", "Synonym till bra. 'Det ser _ ut.'", "", "", "scout", False, 47, 3)
scout_q14 = Question("Dekryptera ordet med SCOUT: \n__ Ct Os __ Co Uc Uo Cc", "kyckling", "En fågelart som finns på bondgårdar.", "", "", "scout", False, 48, 3)
scout_q15 = Question("Dekryptera ordet med SCOUT: \nOt Uo Cc __ Ou __", "ångest", "En jobbig känsla.", "", "", "scout", False, 49, 3)

hex_q11 = Question("Översätt ordet från hextal: 54 52 59 46 46 45 4c \nSvara med stora bokstäver!", "TRYFFEL", "Ordet börjar med T.", "En sorts svamp.", "", "hexadecimal", False, 50, 3)
hex_q12 = Question("Översätt ordet från hextal: 53 4b 52 (c3 84) 43 4b \nSvara med stora bokstäver!", "SKRÄCK", "Ordet börjar med S.", "En obehaglig känsla.", "", "hexadecimal", False, 51, 3)
hex_q13 = Question("Översätt ordet från hextal: 52 49 47 47 41 44 \nSvara med stora bokstäver!", "RIGGAD", "Ordet börjar med R.", "'Matchen var inte rättvis, den var _.'.", "", "hexadecimal", False, 52, 3)
hex_q14 = Question("Översätt ordet från hextal: 4b 4c 49 53 54 45 52 \nSvara med stora bokstäver!", "KLISTER", "Ordet börjar med K.", "Fäster ihop grejer.", "", "hexadecimal", False, 53, 3)
hex_q15 = Question("Översätt ordet från hextal: 50 52 41 4b 54 49 53 4b 54 \nSvara med stora bokstäver!", "PRAKTISKT", "Ordet börjar med P.", "Någonting som är användbart är _.", "", "hexadecimal", False, 54, 3)

bin_q11 = Question("Översätt ordet från binär kod: \n(01 01 00 11) (01 01 01 00) (01 00 01 01) (01 00 11 10) \nSvara med stora bokstäver!", "STEN", "Ordet börjar med S.", "Kan hittas på stranden.", "", "binary", False, 55, 3)
bin_q12 = Question("Översätt ordet från binär kod: \n(01 01 01 00) (01 01 00 10) (11 00 00 11 10 00 01 00) (01 00 01 00) \nSvara med stora bokstäver!", "TRÄD", "Ordet börjar med T.", "'Pengar växer inte på _.'", "", "binary", False, 56, 3)
bin_q13 = Question("Översätt ordet från binär kod: \n(01 00 11 11) (01 01 00 10) (01 00 11 01) \nSvara med stora bokstäver!", "ORM", "Ordet börjar med O.", "Ett slingrigt djur.", "", "binary", False, 57, 3)
bin_q14 = Question("Översätt ordet från binär kod: \n(01 01 00 10) (01 00 01 01) (01 01 00 11) (01 00 00 01) \nSvara med stora bokstäver!", "RESA", "Ordet börjar med R.", "Att åka någonstans.", "", "binary", False, 58, 3)
bin_q15 = Question("Översätt ordet från binär kod: \n(01 00 01 01) (01 01 01 10) (01 00 10 01) (01 00 01 11) (01 01 01 00) \nSvara med stora bokstäver!", "EVIGT", "Ordet börjar med E.", "Någonting som aldrig tar slut varar för _.", "", "binary", False, 59, 3)

#List containing all the questions in the program.
question_list = [
    caesar_q1, caesar_q2, caesar_q3, caesar_q4, caesar_q5, caesar_q6, caesar_q7, caesar_q8, caesar_q9, caesar_q10,
    caesar_q11, caesar_q12, caesar_q13, caesar_q14, caesar_q15,
    scout_q1, scout_q2, scout_q3, scout_q4, scout_q5, scout_q6, scout_q7, scout_q8, scout_q9, scout_q10,
    scout_q11, scout_q12, scout_q13, scout_q14, scout_q15,
    hex_q1, hex_q2, hex_q3, hex_q4, hex_q5, hex_q6, hex_q7, hex_q8, hex_q9, hex_q10,
    hex_q11, hex_q12, hex_q13, hex_q14, hex_q15,
    bin_q1, bin_q2, bin_q3, bin_q4, bin_q5, bin_q6, bin_q7, bin_q8, bin_q9, bin_q10,
    bin_q11, bin_q12, bin_q13, bin_q14, bin_q15
]
#Used questions get appended here to prevent them from being chosen again.
used_question_list = []
#List that gets questions for the chosen difficulty.
custom_question_list = []
selected_difficulty = 0

class Cipher:
    def __init__(self, cipher, help_text, help_image, thumb_image):
        self.cipher = cipher
        self.help_text = help_text
        self.help_image = help_image
        self.thumb_image = thumb_image

#Folder called _internal is added to the project to simulate installing the game through pyinstaller, which creates a _internal folder to put the images into.
caesar_cipher = Cipher("caesar", "Caesarchiffer används genom att byta ut bokstäverna i ett ord mot en anna bokstav ett visst antal steg framåt i alfabetet.", 
                 "_internal\help_image\caesar_help.png", "_internal\help_image\caesar_thumb.png")
scout_cipher = Cipher("scout", "Bokstäverna är placerade i ett rutnät som används för att dekryptera ett ord eller en mening. " + 
                 "Ett par, EX: Ut, ska bytas ut mot bokstaven i rutnätet där U och t möts. OBS: Inga ord använder Q, W, X, Z.", 
                 "_internal\help_image\scout_help.png", "_internal\help_image\scout_thumb.png")
hex_cipher = Cipher("hexadecimal", "Hexadecimal är ett system som använder sig av siffrorna 0-9 och bokstäverna a-f.\n" +
                 "Varje siffra och bokstav har ett värde från 0 till 15. Hex-tal kan i sin tur konverteras till binära tal eller ASCII tecken.",
                 "_internal\help_image\hex_help.png", "_internal\help_image\hex_thumb.png")
#FIXME: For some reason the program can't read image files that have \b in them, so for now the file has B instead.
bin_cipher = Cipher("binary", "Binära tal är en sträng av 8 stycken ettor och nollor.\n" +
                 "Bokstäver kan skrivas med dessa strängar. Å, Ä och Ö skrivs som två tal efter varandra, eftersom de inte finns i engelska alfabetet.",
                 "_internal\help_image\Binary_help.png", "_internal\help_image\Binary_thumb.png")

#List containing all the ciphers used for the questions.
cipher_list = [caesar_cipher, scout_cipher, hex_cipher, bin_cipher]

def difficulty_select():
    global selected_difficulty
    global custom_question_list
    if event == "-DIFF1-":
        #Changes button_color to show the selection.
        change_button_color()
        #Empties the list of items, in case you press the button multiple times.
        custom_question_list = []
        selected_difficulty = 1
        for x in question_list:
            if x.difficulty == 1:
                custom_question_list.append(x)
    #Same code as the above 'if', with some changed values.
    elif event == "-DIFF2-":
        change_button_color()
        custom_question_list = []
        selected_difficulty = 2
        for x in question_list:
            if x.difficulty == 2:
                custom_question_list.append(x)
    elif event == "-DIFF3-":
        change_button_color()
        custom_question_list = []
        selected_difficulty = 3
        for x in question_list:
            if x.difficulty == 3:
                custom_question_list.append(x)

#Highlights the selected difficulty by changing to a brighter color.
def change_button_color():
    if event == "-DIFF1-":
        #Changes background_color to show the selection.
        window["-DIFF1-"].update(button_color="#150BFF")
        window["-DIFF2-"].update(button_color="#150B3F")
        window["-DIFF3-"].update(button_color="#150B3F")
    elif event == "-DIFF2-":
        window["-DIFF1-"].update(button_color="#150B3F")
        window["-DIFF2-"].update(button_color="#150BFF")
        window["-DIFF3-"].update(button_color="#150B3F")
    elif event == "-DIFF3-":
        window["-DIFF1-"].update(button_color="#150B3F")
        window["-DIFF2-"].update(button_color="#150B3F")
        window["-DIFF3-"].update(button_color="#150BFF")

def pick_help_text(list_name):
    global active_question
    #Checks the active questions cipher value to decide what help-items to show.
    if active_question.cipher == "caesar":
        window["-HELPTEXT-"].update(f"{cipher_list[0].help_text}")
        window["-HELPIMAGE-"].update(f"{cipher_list[0].help_image}")
        window["-THUMBIMAGE-"].update(f"{cipher_list[0].thumb_image}")
    elif active_question.cipher == "scout":
        window["-HELPTEXT-"].update(f"{cipher_list[1].help_text}")
        window["-HELPIMAGE-"].update(f"{cipher_list[1].help_image}")
        window["-THUMBIMAGE-"].update(f"{cipher_list[1].thumb_image}")
    elif active_question.cipher == "hexadecimal":
        window["-HELPTEXT-"].update(f"{cipher_list[2].help_text}")
        window["-HELPIMAGE-"].update(f"{cipher_list[2].help_image}")
        window["-THUMBIMAGE-"].update(f"{cipher_list[2].thumb_image}")
    elif active_question.cipher == "binary":
        window["-HELPTEXT-"].update(f"{cipher_list[3].help_text}")
        window["-HELPIMAGE-"].update(f"{cipher_list[3].help_image}")
        window["-THUMBIMAGE-"].update(f"{cipher_list[3].thumb_image}")

#Globals used to check if hints have text or not
hint1_exists = False
hint2_exists = False
hint3_exists = False

#Puts the text-values inside the hintbox elements. Also changes background and text color to indicate if the hint is available or not.
#In other words, if there is no hint 2 or 3, the box becomes a darker shade. Text color is set to match the lighter shade if a hint is in the box to make it unreadable.
def set_hints(list_name):
    global active_question
    global hint1_exists
    global hint2_exists
    global hint3_exists  
    for x in list_name:
        if x.q_id == active_question.q_id:
            #Questions always have at least one hint, so it always updates hintbox1
            window["-HINTBOX1-"].update(f"{x.hint1}")
            #text_color is changed to the element background here to hide it if the previous questions hint1 was revealed.
            window["-HINTBOX1-"].update(text_color="#00AA00")
            hint1_exists = True
            #If the object has a hint2 value, it gets put into the box.
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
def reveal_hint():
    global hint1_visible
    global hint2_visible
    global hint3_visible
    global hint1_exists
    global hint2_exists
    global hint3_exists
    if hint1_visible == False and hint1_exists == True:
        window["-HINTBOX1-"].update(text_color="#FFFFFF")
        #Adds time to timer here
        add_time_penalty()
        hint1_visible = True
    elif hint2_visible == False and hint2_exists == True:
        window["-HINTBOX2-"].update(text_color="#FFFFFF")
        add_time_penalty()
        hint2_visible = True
    elif hint3_visible == False and hint3_exists == True:
        window["-HINTBOX3-"].update(text_color="#FFFFFF")
        add_time_penalty()
        hint3_visible = True
        
#Resets the 'hint' global variables so they work for the next question.
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

def pick_Question(list_name):
    #Gets the list length as a value. Subtract 1 since random.randint is inclusive, and len() returns the wrong number.
    #EG: If the list has 3 elements, len() would return 3. Since list indexes start at 0 and go to len()-1, it wouldn't work without subtracting 1 initially for the question_list_length variable.
    question_list_length = len(list_name)-1
    #used_question_list is used to break the while loop if you run out of new questions. This means the game doesn't freeze if you use all questions in the list.
    global used_question_list
    next_question = False
    while next_question == False:
        if len(used_question_list) == len(list_name):
            break
        random_question = random.randint(0, question_list_length)
        #Checks that the question hasn't been chosen before
        if list_name[random_question].selected == False:
            window["-QUESTIONBOX-"].update(list_name[random_question].text)
            list_name[random_question].selected = True
            next_question = True
            #The currently selected question is put inside the global variable 'active_question' for use in other functions.
            global active_question
            active_question = list_name[random_question]
            used_question_list.append(list_name[random_question])
            
def new_question():
    global selected_difficulty
    #If you haven't altered the difficulty, the game will pick from all questions in the program.
    if selected_difficulty == 0:
        pick_Question(question_list)
        pick_help_text(question_list)
        set_hints(question_list)
    #If you have changed difficulty, it picks a question from the list for that difficulty.
    else:
        pick_Question(custom_question_list) 
        pick_help_text(custom_question_list)
        set_hints(custom_question_list)

def check_Answer():
    #active_question from 'pick_Question' is used so you don't have to loop through every question in the game when checking the answer
    global active_question
    #The global variables are used to update UI elements
    global question_number
    global selected_difficulty
    answer = values["-ANSWERBOX-"]
    #TODO: solution is case sensitive. Make function that transforms capital letters into small ones?
    if answer == active_question.solution:
        #Updates the question counter at the top of the window
        question_number += 1
        window["-GAMEQUESTIONS-"].update(f"Fråga {question_number} av {max_questions}")
        #Empties the inputbox
        window["-ANSWERBOX-"].update("")
        #hide_hints needs to be first to change the global variables.
        #This is because set_hints makes some variables True, when hide_hints makes all of them False again.
        hide_hints()
        #Picks a new question on correct answer and runs set_hints
        new_question()

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
    total_time = round((time.time() - timer_start),1) 
    window["-GAMETIMER-"].update(f"Tid: {total_time + total_penalty}")

#Updates the variable containing the total penalty time for that session.
def add_time_penalty():
    global hint_penalty
    global total_penalty
    total_penalty += hint_penalty

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "-QUIT-":
        break
    #COL1 = Main menu, 2 = Game view, 3 = Settings, 4 = Help screen
    #TODO: Remove if for placeholder once it's no longer needed.
    #if event == "-PLACEHOLDERMENU-":
    #    window["-COL2-"].update(visible=False)
    #    window["-COL1-"].update(visible=True)
    if event == "-GAMEWINDOW-":
        window["-COL1-"].update(visible=False)
        window["-COL2-"].update(visible=True)
        new_question()
        start_Timer()
    if event == "-SUBMIT_ANSWER-":
        check_Answer()
        update_Timer()
    if event == "-SETTINGS-":
        window["-COL1-"].update(visible=False)
        window["-COL3-"].update(visible=True)
    if event == "-MAINMENU-":
        window["-COL1-"].update(visible=True)
        window["-COL3-"].update(visible=False)
    if event == "-HELPSCREEN-":
        window["-COL2-"].update(visible=False)
        window["-COL4-"].update(visible=True)
    if event == "-EXITHELP-":
        window["-COL2-"].update(visible=True)
        window["-COL4-"].update(visible=False)
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
    if event == "-DIFF1-" or "-DIFF2-" or "-DIFF3-":
        difficulty_select()
    #Ends the game once you answer enough questions.
    #TODO: Some sort of result screen instead of just closing the program
    if question_number == max_questions+1:
        #Updates the total_time variable in order to get the completion time for the match.
        update_Timer()
        print(f"Du vann! Din slutliga tid är: {total_time}")
        #Added 'input' as a lazy way to let the player see their end-time when running the program as an exe. Otherwise, the window closes too fast.
        input("Tryck på enter för att stänga av programmet.")
        break
window.close()