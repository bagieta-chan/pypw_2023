
from string import punctuation
from collections import Counter
text = ""
with open("text.txt", "r") as file:
    text = str(file.read())


def delete_punctuation(text: str)-> str:
    result = ""
    for letter in text:
        if letter not in punctuation:
            result += letter
    return result

def words_count(input_text: str) -> dict:
    text = delete_punctuation(input_text)
    splitted_text = (text.lower()).split()
    return Counter(splitted_text).most_common()

print(words_count(text))