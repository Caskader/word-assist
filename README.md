# Word Prediction Machine

## Overview

This project implements a simple word prediction model. It analyzes a text file, extracts words, and builds a model that predicts the next word based on the preceding word. The model uses a dictionary of tokens (words) and their associated indices, along with a record of which words each token prompts (i.e., which words follow it in the text).

## Project Structure

The project consists of the following files:

-   `training/__init__.py`: Contains the core logic for training the word prediction model.
-   `prediction_machine/__init__.py`: Contains the logic for predicting the next word.
-   `data/knowledge.json`: Stores the trained model data (tokens and indexed words).
-   `data/training_data.txt`: The text file used for training the model.

## Training the Model

The training process involves the following steps:

1.  **Extracting Words:** The `word_extract()` function in `training/__init__.py` reads the text from `data/training_data.txt`, splits it into words, removes punctuation and numbers, and converts the words to lowercase.
2.  **Data Extraction:** The `data_extrractor()` function in `training/__init__.py` processes the extracted words, creating tokens and indexing them. It builds two dictionaries:
    -   `indexed_words`: Maps each unique word to a unique index.
    -   `Tokens`: Stores `Token` objects, where each `Token` represents a word and its associated data (index and prompted words).
3.  **Saving Data:** The `save_data()` function in `training/__init__.py` saves the trained model data (the `indexed_words` and `Tokens` dictionaries) to `data/knowledge.json`.

## Predicting Words

The prediction process involves the following steps:

1.  **Loading Data:** The `load_data()` function in `training/__init__.py` loads the trained model data from `data/knowledge.json` into memory.
2.  **Predicting Word:** The `predict_word()` function in `prediction_machine/__init__.py` takes an input word and predicts the next word based on the trained model. It retrieves the token associated with the input word, selects a random word from the token's prompted words, and returns the predicted word.
3.  **Getting Word from Index:** The `get_word_from_index()` function in `prediction_machine/__init__.py` retrieves the actual word from the `indexed_words` dictionary, given its index.

## Usage

1.  **Training:**
    -   Ensure that `data/training_data.txt` contains the text you want to use for training the model.
    -   Run the `training/__init__.py` file directly. This will extract the words, train the model, and save the data to `data/knowledge.json`.
2.  **Prediction:**
    -   Run the `prediction_machine/__init__.py` file. This will load the trained model data and use the `predict_word()` function to predict the next word.

## Code Explanation

### `training/__init__.py`

-   **`Token` Class:** Represents a word (token) in the model.
    -   `__init__(self, index_of_token)`: Initializes a new `Token` object with its index.
    -   `add_prompted_word(self, index: int, frequency: int)`: Adds a prompted word (the word that follows this token) to the token's list of prompted words.
    -   `get_prompted_word_length(self) -> int`: Returns the total frequency of all prompted words for this token.
-   **`word_extract() -> list[str]`:** Extracts words from the training data file, removing punctuation and converting to lowercase.
-   **`data_extrractor(words: list) -> tuple[dict[int, Token], dict[str, int]]`:** Creates the `Tokens` and `indexed_words` data structures from a list of words.
-   **`save_data(Tokens: list[Token], indexed_words: dict[str, int]) -> bool`:** Saves the `Tokens` and `indexed_words` to a JSON file.
-   **`load_data(file_path: str) -> tuple[list[Token], dict[str, int]]`:** Loads the `Tokens` and `indexed_words` from a JSON file.

### `prediction_machine/__init__.py`

-   **`predict_word(input_word: str)`:** Predicts the next word given an input word, using the loaded `Tokens` and `indexed_words`.
-   **`get_word_from_index(index: int) -> str`:** Retrieves the word associated with a given index from the `indexed_words` dictionary.

## Dependencies

-   Python 3.x
-   `json` module (built-in)

## Notes

-   The quality of the word predictions depends on the size and content of the training data.
-   The model is relatively simple and does not account for context beyond the immediately preceding word.
-   The `random` module is used to select a predicted word from the