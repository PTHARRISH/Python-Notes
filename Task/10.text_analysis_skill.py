paragraph=input("enter the paragraph: ")
space_removed=paragraph.replace(" ","")
words=[x for x in paragraph.split(" ")]
dict1={}
for i in words:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1

print("There are ",len(space_removed)," letters in the paragraph")
print("There are ",len(words)," letters in the paragraph")
print("There are ",dict1," are the words repeated these times")
