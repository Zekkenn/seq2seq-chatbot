file = open("C:/Users/ASUS/Documents/Sebastian/seq2seq-chatbot/data/supreme court dialogs/supreme.conversations.txt", "r")

os.chdir("C:/Users/ASUS/Documents/Sebastian/seq2seq-chatbot/data/twitter")

import data
import os

dt = [ x.split(" +++$+++ ") for x in file.readlines() ]

dt = [ x[-1] for x in dt ]

text = "".join(dt)

f = open("chat.txt", "w")
f.write(cadena)
f.close()
