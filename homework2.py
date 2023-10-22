
def name_sender(foo):

    def wrapper(*args, **kwargs):
       with open("text.txt", "r") as file:
            text = str(file.read())
