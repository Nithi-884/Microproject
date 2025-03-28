# getSpan, reverse, removePunctuations,countWords,charecterMaps
# ,makeTitle,normalizeSpaces,transform,getPermutations

import stoppackage as s
#1 getSpan
answer = s.getSpan("Mississippi","ss")
print(answer)

#2 reverse
answer = s.reverse("This is a car")
print(answer)

#3 removePunctuations

answer = s.removePunctuations("This [] is , a car .")
print(answer)

# countWords
answer = s.countWords("This is a car")
print(answer)

# charecterMaps
answer = s.charecterMaps("Mississippi")
print(answer)


# makeTitle
answer = s.makeTitle("nithi hello")
print(answer)

# normalizeSpaces
answer = s.normalizeSpaces("This is              a car  aa")
print(answer)

# transform
answer = s.transform("Hello")
print(answer)

# getPermutations

answer = s.getPermutations("apple")
print(list(answer))