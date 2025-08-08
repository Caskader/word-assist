import json


class Token:
    """
    Represents a token (word) with its index and the words it prompts.
    """
    def __init__(self, index_of_token):
        """
        Initializes a Token object.

        Args:
            index_of_token (int): The unique index of the token.
        """
        self.index_of_token = index_of_token
        self.words_prompted = {}  # Dictionary to store prompted words and their frequencies

    def add_prompted_word(self, index: int, frequency: int):
        """
        Adds a prompted word to the token's list of prompted words.

        Args:
            index (int): The index of the prompted word.
            frequency (int): The frequency of the prompted word.
        """
        if index in self.words_prompted:
            self.words_prompted[index] += frequency  # Increment frequency if word already exists
        else:
            self.words_prompted[index] = frequency  # Add word with its frequency if it doesn't exist
    def get_prompted_word_length(self)->int:
        a = 0
        for i in self.words_prompted:
            a+= self.words_prompted[i]
        return a

def data_extrractor(words: list) -> tuple[dict[int, Token], dict[str, int]]:
    """
    Extracts data from a list of words, creating tokens and indexing them.

    Args:
        words (list): A list of words to process.
    """
    print("Extracting data from words...")

    indexed_words = {}  # Dictionary to store words and their corresponding indices
    Tokens = {}  # Dictionary to store tokens, with index as keys
    pointed_index = 0  # The index to be assigned to the next new word

    i = 0
    while i < len(words) - 1:
        word = words[i]
        next_word = words[i + 1]

        # If the word is not already indexed
        if word not in indexed_words:
            new_token = Token(pointed_index)  # Create a new token
            indexed_words[word] = pointed_index  # Store the word and its index
            Tokens[pointed_index] = new_token  # Store the token
            pointed_index += 1  # Increment the index for the next word
        else:
            new_token = Tokens[indexed_words[word]]  # Retrieve the existing token

        # Process the next word
        if next_word not in indexed_words:
            new_next_token = Token(pointed_index)  # Create a new token for the next word
            indexed_words[next_word] = pointed_index  # Store the next word and its index
            Tokens[pointed_index] = new_next_token  # Store the new token
            pointed_index += 1  # Increment the index
            new_token.add_prompted_word(indexed_words[next_word], 1)  # Add the next word as a prompted word to the current token
        else:
            new_token.add_prompted_word(indexed_words[next_word], 1)  # Add the next word as a prompted word to the current token

        i += 1
    print("Data extraction completed.")
    return Tokens, indexed_words  # Return the tokens and indexed words


def word_extract() -> list[str]:
    """
    This function extracts words from a text file, ignoring certain characters.
        It reads lines from 'data/sample.txt', splits them into words, and filters out unwanted characters.
    """
    print("Extracting words from the file...")

    f = open('data/training_data.txt', 'r')
    lines = f.readlines()

    ignoring_characters = ['!', '@', '#', '$', '%', '^', '?', '&', '*', '(', '_', '+', '-', '=', '>', '<', '|', ':', ';', '/', '~', '`', '[', ']', '\\', '"', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n', '\t']
    discard_word = False  # Flag to indicate if the word should be discarded
    words = []
    for line in lines:
        for word in line.split(" "):
            wordl = ""

            for letter in list(word):  # Convert word to list of characters
                # Check if the letter is not in the ignoring characters
                if letter == '.':
                    discard_word = True
                if letter not in ignoring_characters:
                    wordl += letter
            wordl.lower()  # Convert the word to lowercase
            if not discard_word:
                words.append(wordl)
            else:
                discard_word = False   
            if wordl == "":
                words.remove(wordl)
    f.close()
    print("Words extracted successfully.")
    return words

def save_data(Tokens: list[Token], indexed_words: dict[str, int]):
    print("Saving data to 'data/knowledge.json'...")

    # creating data
    data = {"indexed_words": indexed_words}



    # Loop through each token and store its prompted words


    for i in Tokens:
        token = Tokens[i]
        data[token.index_of_token] = {
            "prompted_words": token.words_prompted
        }

    f = open('data/knowledge.json', 'w')
    json.dump(data, f)
    f.close()
    print("Data saved successfully.")
    return True


def load_data(file_path: str) -> tuple[list[Token], dict[str, int]]:
    """
    Loads data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        tuple[list[Token], dict[str, int]]: A tuple containing:
            - tokens (list[Token]): A list of Token objects.
            - indexed_words (dict[str, int]): A dictionary of words and their corresponding indices.
    """
    indexed_words = {}
    tokens = []
    print(f"Loading data from {file_path}...")
    f = open(file_path, 'r')
    data = json.load(f)
    f.close()

    for key in data:
        if key == "indexed_words":
            indexed_words = data[key]
            
        else:
            token_data = data[key]
            token = Token(int(key))
            token.words_prompted = token_data['prompted_words']
            tokens.append(token)
    print("Data loaded successfully.")
    return tokens ,indexed_words

# def main():
#     words = word_extract()
#     tokens,i = data_extrractor(words)
#     save_data(tokens,i)
#     # t,i=load_data('data/knowledge.json')
    
# main()