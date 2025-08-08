import random

from training import load_data

(tokens,indexed_words) = load_data('data/knowledge.json')

def predict_word(input_word:str):

    input_word = input_word.lower()

    index_of_word = indexed_words[input_word]
    if index_of_word is None:
        raise ValueError(f"Word '{input_word}' not found in indexed words.")
    # getting predictions
    token = tokens[index_of_word]
    length_of_words_prompted = token.get_prompted_word_length()

    random_number = random.randint(0,length_of_words_prompted)
    chosen_word_index = 0
    for i in token.words_prompted :
        frequncy = token.words_prompted[i]

        if random_number > frequncy:
            random_number -= frequncy
        else:
            chosen_word_index = i
            break
    return chosen_word_index

def get_word_from_index(index: int) -> str:
    """
    Retrieves the word associated with a given index from the indexed_words dictionary.

    Args:
        index (int): The index of the word to retrieve.

    Returns:
        str: The word associated with the index.
    """


    for word in indexed_words:
        
        index2 = indexed_words[word]

        if index == str(index2):
            
            return word
    return None  # Return None if the index is not found

def main():
    input_word = input("Enter a word to predict the next word: ")
    index = predict_word(input_word)
    predicted_word = get_word_from_index(index)
    print(f"{input_word} {predicted_word}")

