# Laddar nödvändiga verktyg för att bygga spelet
import PySimpleGUI as sg  # Används för att skapa spelets utseende
import random  # Används för att blanda frågor och svar
from european_capitals import european_capitals  # Här finns alla frågor och svar

def create_window():
    # Väljer ett utseende för spelet
    sg.theme('Reddit')

    # Planerar hur allt i spelet ska se ut och var det ska vara
    layout = [
        # Visar text till spelaren
        [sg.Text('Vilken är huvudstaden i följande land?', font=('Helvetica', 16), justification='center')],
        # Här visas själva frågan
        [sg.Text('', font=('Helvetica', 16), key='-QUESTION-', size=(None, 1), justification='center')],
        # Lista för spelaren att välja svar från
        [sg.Listbox([], size=(20, 4), key='-CHOICE-', font=('Helvetica', 14), enable_events=True)],
        # Knappar för att svara och gå vidare
        [sg.Button('Svara', font=('Helvetica', 14), bind_return_key=True), sg.Button('Nästa', font=('Helvetica', 14))]
    ]

    # Gör fönstret redo och visar det
    return sg.Window('Gissa Huvudstaden', layout, finalize=True, element_justification='c')

def update_question(window, europeiska_huvudstader, question_number):
    # Tar fram frågan och det rätta svaret
    question, correct_answer = europeiska_huvudstader[question_number]
    
    # Väljer fel svar för att blanda med det rätta
    wrong_answers = random.sample([answer for q, answer in europeiska_huvudstader if answer != correct_answer], 3)

    # Blandar alla svar
    choices = wrong_answers + [correct_answer]
    random.shuffle(choices)

    # Visar nya frågan och svarsalternativ
    window['-CHOICE-'].update(choices)
    window['-QUESTION-'].update(question)

    # Kommer ihåg det rätta svaret för att kunna kolla om spelaren gissar rätt
    return correct_answer

def main():
    # Gör frågorna i olika ordning varje gång
    random.shuffle(european_capitals)
    score = 0  # Håller koll på poängen
    question_number = 0  # Startar med första frågan
    window = create_window()  # Öppnar spelet
    correct_answer = update_question(window, european_capitals, question_number)  # Visar första frågan

    while True:
        event, values = window.read()  # Väntar på att spelaren gör något

        if event in (sg.WIN_CLOSED, 'Avsluta'):  # Om spelet stängs ner
            break

        if event == 'Svara' and values['-CHOICE-']:  # Om spelaren svarar
            user_choice = values['-CHOICE-'][0]
            if user_choice == correct_answer:  # Kollar om svaret är rätt
                sg.popup('Rätt!', 'Du får en poäng!', font=('Helvetica', 14))
                score += 1
            else:
                sg.popup('Fel!', f'Rätt svar var {correct_answer}.', font=('Helvetica', 14))

        if event == 'Nästa' or user_choice == correct_answer:  # Går vidare till nästa fråga
            question_number += 1
            if question_number < len(european_capitals):
                correct_answer = update_question(window, european_capitals, question_number)
            else:
                sg.popup(f'Du fick {score} poäng!', font=('Helvetica', 14))  # Spelet är slut, visar poäng
                break

    window.close()  # Stänger spelet när allt är klart

if __name__ == "__main__":
    main()  # Startar spelet
