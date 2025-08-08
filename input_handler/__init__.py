import prediction_machine
import os

def start_input_channel():
    """
    Initializes the input channel for the application.
    This function sets up necessary configurations and prepares
    the input handling system to start receiving user inputs.
    """
    print("Input channel started. ")
    # Additional setup code can be added here if needed.
    print("enter the word for prediction, press enter to predict:  ")
    text = ""
    ignoring_characters = ['!', '@', '#', '$', '%', '^', '?', '&', '*', '(', '_', '+', '-', '=', '>', '<', '|', ':', ';', '.', '/', '~', '`', '[', ']', '\\', '"', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n', '\t']
    while(True):
        command = input()
        command = command.strip()  # Remove leading/trailing spaces

        # Use a string comprehension to filter out ignoring characters
        command = ''.join(c for c in command if c not in ignoring_characters)

        command = command.lower()  # Convert the command to lowercase
        text +=" "+ command + " "
        
        a = text.split(" ")[-2]

        prediction = prediction_machine.get_word_from_index(prediction_machine.
        predict_word(text.split(" ")[-2]))
        text += prediction

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        
        print(text)