# reverse-words-in-a-given-string
# using inbuilt function
string=input()
j=""
a=[]
for i in reversed(string.split(' ')):
    j=j+i+" "
print(j)

# without using inbuilt function
string= input()
word=""
reversed_word=""
for i in string:
    if i!=' ':
        word+=i
    else:
        reversed_word=' '+word+reversed_word
        word=''
reversed_word=word+reversed_word
print(reversed_word)
