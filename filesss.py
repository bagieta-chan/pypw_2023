
from string import punctuation
from collections import Counter

def file_lines(filepath: str)->str:

    with open(filepath, encoding= "utf-8") as file:
        for line in file:
            yield line.replace("\n","")


def delete_punctuation(text: str)-> str:
    result = ""
    for letter in text:
        if letter not in punctuation:
            result += letter
    return result

def words_count(input_text: str) -> dict:
    text = delete_punctuation(input_text)
    splitted_text = (text.lower()).split()
    return Counter(splitted_text).most_common(3)

def letters_count(input_text: str) -> dict:
    return Counter(text.replace(" ","")).most_common(5)

with open("text2.txt", "r", encoding= "utf-8") as file:

    result = file.read()
    text = delete_punctuation(result)
    with open("result.txt","w",encoding= "utf-8") as f:
        print(letters_count(text),file = f)




