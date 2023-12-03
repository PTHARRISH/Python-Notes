def reversed_sentence(s):
    words=""
    reversed_word=""
    for i in s:
        if i!=" ": # if word is not a space means it add in words
            words+=i
        else:
            reversed_word=' '+words+reversed_word # i is space it add space + word + reversed_word and store reversed word
            words='' # it will remove words and make empty string
    reversed_word=words+reversed_word # it will use for if condition words (line 6 after this will add reversed word) 
    return reversed_word

print(reversed_sentence(input('Enter the sentence to reverse: ')))