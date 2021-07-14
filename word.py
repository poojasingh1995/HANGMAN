import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    # """
    # words_list=["navgurukul","learning","kindness"]
    
    # print("losding word list from file...")
    WORDLIST_FILENAME="words.txt"
    inFile=open(WORDLIST_FILENAME,"r")
    line=inFile.readline()
    words_list = line.split()
    # print("  ",len(words_list),"words loaded.\n")
    return words_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    words_list = load_words()
    secret_word = random.choice(words_list)
    secret_word= secret_word.lower()

    return secret_word
choose_word()