# Class for proccesing of text data
class TextProcessor():
    def __init__(self):
        self.marks = (".", ",", ":", ";", "-", "!", "?" )

# Privat method Checking all symbols for equality with punctuation marks
    def __is_punktuation(self, symbol):
        if symbol in self.marks:
            return False
        else:
            return True

# Public method Removing all punctuatiom markes from a string
    def get_clean_string(self, text):
        clean_text = ''
        for i in text:
            if self.__is_punktuation(i) == False:
                continue
            else:
                clean_text += i
        return clean_text

# Arguments for the first part of my task Class TextProcessor
phrase1 = TextProcessor()
print(phrase1.get_clean_string("It?.,! is s---o ha::rd to st;;;udy Python"))

# One more class with a privat attributes text_processor and clean_string
class TextLoader():
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ''

    @property
    def text_processor(self):
        return self.__text_processor

# Editional property for clean_string
    @property
    def clean_string(self):
        print("There are no punctuation marks in this text")
        return self.__clean_string

# Public method set_clean_text which causes the method of TextProcessor Class
    def set_clean_text(self, text1):
        self.__clean_string = self.__text_processor.get_clean_string(text1)
        return self.__clean_string


phrase2 = TextLoader()
phrase2.set_clean_text("I wa!!!nt to.. be a c:::ool;;; programmer")
print(phrase2.clean_string)

# New class Datainterface with protected attribute
class DataInterface():
    def __init__(self):
        self._attribute = TextLoader()

    # def process_texts(self, list):
    #     c = []
    #     for i in list:
    #         w = self._attribute.set_clean_text(i)
    #         c.append(w)
    #     return c
    def process_text(self, list):
        for i in list:
            print(self._attribute.text_processor.get_clean_string(i))

my_list = ["Python forever", "Python forever", "Python forever"]
phrases3 = DataInterface()
phrases3.process_text(my_list)