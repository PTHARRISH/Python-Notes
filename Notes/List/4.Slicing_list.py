# Slicing Lists
# You can also take slices of lists to get new lists containing subsets of elements:
my_list=[1,2,3,4,5,6]
print("------------------------------------------------------------------------------------------")
print("----------------------------------Slicing Lists-------------------------------------------")
print("------------------------------------------------------------------------------------------")
print("Original List : ",my_list)
print("------------------------------------------------------------------------------------------")
sub_list = my_list[0:5:1]  # Gets elements from index 0 to 4
print("sub_list = my_list[0:5:1]",sub_list," # Gets elements from index 0 to 4") # [1, 2, 3, 4, 5]
print("------------------------------------------------------------------------------------------")
sub_list = my_list[0:-5:1]  # Gets elements from index 0
print("sub_list = my_list[0:-5:1]",sub_list," # Gets elements from index 0") # [1]
print("------------------------------------------------------------------------------------------")
sub_list = my_list[0:5:-1]  # Print empty list
print("sub_list = my_list[0:5:-1]",sub_list," # Print empty list") # []
print("------------------------------------------------------------------------------------------")
sub_list = my_list[0:-5:-1]  # Print empty list
print("sub_list = my_list[0:-5:-1]",sub_list," # Print empty list") # []
print("------------------------------------------------------------------------------------------")
sub_list = my_list[5:0:1]  # Print empty list
print("sub_list = my_list[5:0:1]",sub_list," # Print empty list") # []
print("------------------------------------------------------------------------------------------")
sub_list = my_list[5:0:-1]  # Gets elements from index 5 to 1
print("sub_list = my_list[5:0:-1]",sub_list," # Gets elements from index 5 to 1") # [6, 5, 4, 3, 2]
print("------------------------------------------------------------------------------------------")
sub_list = my_list[-5:0:1]  # Print empty list
print("sub_list = my_list[-5:0:1]",sub_list," # Print empty list") # []
print("------------------------------------------------------------------------------------------")
sub_list = my_list[-5:0:-1]  # Gets elements from index -5
print("sub_list = my_list[-5:0:-1]",sub_list," # Gets elements from index -5") # [2]
print("------------------------------------------------------------------------------------------")
sub_list = my_list[1:4]  # Gets elements from index 1 to 3
print("sub_list = my_list[1:4]",sub_list," # Gets elements from index 1 to 3") # [2,3,4]
print("------------------------------------------------------------------------------------------")
sub_list = my_list[0:] # Gets all element from 0 to end
print("sub_list = my_list[0:]",sub_list," # Gets all element from 0 to end") # [1, 2, 3, 4, 5, 6]
print("------------------------------------------------------------------------------------------")
# sub_list = my_list[::0] # slice step cannot be zero
# print("sub_list = my_list[1:4]",sub_list)
# print("------------------------------------------------------------------------------------------")
sub_list = my_list[-1] # Print negative element -1 is last element
print("sub_list = my_list[-1]",sub_list," # Print negative element -1 is last element") # 6
print("------------------------------------------------------------------------------------------")
sub_list = my_list[-1:] # Print negative element -1 is last element to end
print("sub_list = my_list[-1:]",sub_list," # Print negative element -1 is last element to end") # [6]
print("------------------------------------------------------------------------------------------")
sub_list = my_list[-1::] # Print negative element -1 is last element to end step is 1
print("sub_list = my_list[-1::]",sub_list," # Print negative element -1 is last element to end step is 1") # [6]
print("------------------------------------------------------------------------------------------")
sub_list = my_list[::-1] # Print all elements in reverse order because list step -1  
print("sub_list = my_list[::-1]",sub_list," # Print all elements in reverse order because list step -1") # [6, 5, 4, 3, 2, 1]
print("------------------------------------------------------------------------------------------")
sub_list = my_list[:-1] # Print elements from begining to -2 ( before to last number -2 )
print("sub_list = my_list[:-1]",sub_list," # Print elements from begining to -2") # [1, 2, 3, 4, 5]
print("------------------------------------------------------------------------------------------")
sub_list=my_list[0]==my_list[0:1] # Both is not same list
print("sub_list = my_list[0]==my_list[0:1]",sub_list," # Both is not same list") # False
print("------------------------------------------------------------------------------------------")
