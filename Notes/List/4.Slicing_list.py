# Slicing Lists
# You can also take slices of lists to get new lists containing subsets of elements:
my_list=[1,2,3,4,5,6]
print("Slicing Lists")
sub_list = my_list[1:4]  # Gets elements from index 1 to 3
print("sub_list = my_list[1:4]",sub_list) # [2,3,4]
sub_list = my_list[0:]
print("sub_list = my_list[0:]",sub_list) # [1, 2, 3, 4, 5, 6]
# sub_list = my_list[::0] # slice step cannot be zero
# print("sub_list = my_list[1:4]",sub_list)
sub_list = my_list[-1]
print("sub_list = my_list[-1]",sub_list) # 6
sub_list = my_list[-1:]
print("sub_list = my_list[-1:]",sub_list) # [6]
sub_list = my_list[-1::]
print("sub_list = my_list[-1::]",sub_list) # [6]
sub_list = my_list[::-1]
print("sub_list = my_list[::-1]",sub_list) # [6, 5, 4, 3, 2, 1]
sub_list = my_list[:-1]
print("sub_list = my_list[:-1]",sub_list) # [1, 2, 3, 4, 5]
sub_list=my_list[0]==my_list[0:1]
print("sub_list = my_list[0]==my_list[0:1]",sub_list) # False