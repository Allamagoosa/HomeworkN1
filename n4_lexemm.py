#!/usr/bin/python
"""Test=================================
>>> walker("any")
>>> walker("so")
>>> walker("so")
{'any':1, 'so':2}
"""

w = {}

def walker(word):
    if word in w: 
        w[word] += 1
    else:
        w[word] = 1
    
def clean_word(word):
    word = word.lower()
    last = len(word)-1
    if word[last] >= 'A' and word[last] <= 'z':
        walker(word) #Hash
    else:
        if word[last] == "\n" : 
	    walker(word[0:last-1]) #Hash
        else: 
	    walker(word[:last]) #Hash  
          
f = open("Christie.txt", "r")
for line in f:
    words = line.split(' ')
    for item in words:
        if item.isalpha() and len(item) > 3:    # isalpha Slishkom grubo, nado zamenatt?
            clean_word(item)
f.close()
print w['train']

if __name__ == "__main__":
    import doctest
    doctest.testmod()
