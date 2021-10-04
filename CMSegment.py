import re
import time

record = open("dict_no_space.txt", "r")

# get all words in dicitonary
thing = record.readlines()
word = set()
for i in thing:
    word.add(i.strip())

# search in dictionary
matching = []
result = []
position = -1
sentence = input("Sentence: ")
start = time.time()
while True:
    thing = ""
    matching.clear()
    letter = re.compile(r'[a-zA-Z]')
    symbol = re.compile(r'[，、。!@$#%^&()-_=+`~{}\[\]|\\:;"\'<>,.?/]')
    for i in range(position+1, len(sentence)):
        thing += sentence[i]
        english = letter.findall(thing)
        punc = symbol.findall(thing)
        if len(english) == 0:
            if thing in word:
                matching.append(thing)
                position = i
        if len(english) == len(thing):
            matching.append(thing)
            position = i
        if len(punc) == len(thing):
            matching.append(thing)
            position = i
    result.append(matching[-1])
    if position == len(sentence)-1:
        break
print(result)
end = time.time()
print(end - start, "seconds")

record.close()