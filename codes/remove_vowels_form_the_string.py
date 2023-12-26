# remove the vowels
# 1. loop
def remove_vowels(sentence):
    vowels=['a','e','i','o','u']
    result=""
    for i in sentence:
        if i.lower() not in vowels:
            result+=""+i
    print(result)

sentence=input("enter the sentence: ")
remove_vowels(sentence)

# 2. list comprehension
def remove_vowels(sentence):
    vowels=['a','e','i','o','u']
    result=[i for i in sentence if i.lower() not in vowels]
    result="".join(result) # list(result) to string conversion
    print(result)

sentence=input("enter the sentence: ")
remove_vowels(sentence)


# 3 using regular expression
import re
def remove_vowels(sentence):
    return re.sub("[AEIOUaeiou]","",sentence)


sentence=input("enter the sentence: ")
print(remove_vowels(sentence))