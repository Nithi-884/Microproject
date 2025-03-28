from itertools import permutations


## Getspan functions returns the concerened substings
def getSpan(s,ss):
    spans = []
    start = 0
    while start < len(s):
        index = s.find(ss, start)
        if index == -1:
            break
        spans.append((index, index + len(ss) - 1))
        start = index + 1
    return spans

## Function to reverse the words in the string

def reverse(string1):
    # return string1[::-1]
    list1 = string1.split()
    list1.reverse()
  
    rev = ' '.join(list1)
    return rev

## Remove punctuations

def removePunctuations(string1):
    result = ""
    punctuations = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
                    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
                     '^', '_', '`', '{', '|', '}', '~']
    for char in string1:
        if char not in punctuations:
            result += char
    return result
# new = removePunctuations("This is a [] a . car")
# print(new)

"""
Function to count number of words in a string sentance

"""


def countWords(string1):
    list1 = string1.split()
    count = len(list1)
    return count

# count = countWords("This is a car")
# print(count)


## charecter map function

def charecterMaps(string1):
    dict1 = {}

    for i in string1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    return dict1

# ans = charecterMaps("mississippi i k ")
# print(ans)

## Make title function

def makeTitle(string1):
    return string1.title()

# ans  = makeTitle("nithi")
# print(ans)


def normalizeSpaces(string1):
    list1 = string1.split()
    return " ".join(list1)

# ans = normalizeSpaces("sss   ss d d ss ss")
# print(ans)


# Funtion to transform a string

def transform(string1):
    rev = string1[::-1]
    return rev.swapcase()

# ans = transform("Hello")
# print(ans)

def getPermutations(string1):
    list(string1)
    return permutations(string1)

# ans = getPermutations("Apple")
# print(list(ans))