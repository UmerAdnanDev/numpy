#Vectorization allows performing arithmatic operation 50 - 100 times 
#faster in array then using list comprehension or loops

# without it
list1 = [1,2,3,4,5]
cube = [x**3 for x in list1]
print(cube)
list2 = [6,7,8,9,10]
sum = [x+y for x,y in zip(list1,list2)] # zip is a function
print(sum)
list3 =[[1,2],[3,4]]
difference = [x-y for x,y in list3]
print(difference)
