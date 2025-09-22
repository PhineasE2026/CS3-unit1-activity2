# Data Collection Drills

# PART A: Lists
my_list = ['h','a','l','l','s']
print(my_list) #['c', 'l', 'o', 'c', 'k']
my_list.append('!')
print(my_list) #['c', 'l', 'o', 'c', 'k', '!']
print(len(my_list)) #6
print(my_list[4:6]) #returns k and !
print(my_list[4:]) #it's the same because the list ends at index 6 anyway
print(my_list[-2:]) #also the same because it -2 loops back to 4
my_list.remove('l') #removed only the first l
print(my_list)
del my_list[0] #first index was removed
print(my_list)
last_item = my_list.pop()
print(last_item) #prints final index
print(my_list) #prints list with final index removed
print(my_list[2]) #prints third index (s)
print('!' in my_list) #false because it was popped
my_list.sort(reverse=True) #reverses list order
print(my_list)
print(sorted(my_list)) #alphabetical
print(my_list)

# PART B: Tuples
my_tuple = ('ultraviolet','infrared','visible light')
print(my_tuple) #prints values of tuple
print(my_tuple[0]) #ultraviolet
print(my_tuple[-1]) #visible light, loops back to final index
#my_tuple[1] = 'microwave' gives an error because tuples are immutable
one_item = ('hello',)
print(one_item) #prints exact statement
colors = ('red','red','red','red','blue','red')
print(colors.count('red')) #5 counts of red
print(colors.index('blue')) # fifth value which is index 4

# PART C: Sets
my_set = {'kiwi', 'cherry', 'mango'}
print(my_set) #order doesnt match what is typed, sets dont have an order
my_set.add('watermelon')
print(my_set) #added watermelon in random order
my_set.add('honeydew')
print(my_set) #added honeydew in random order
my_set.remove('kiwi') # removes kiwi no particular order
print(my_set)
# my_set.discard('pear') gives an error because discard takes exactly one argument and zero are given
tropical = {'coconut','dragonfruit','durian'}
all_fruits = my_set.union(tropical)
print(all_fruits) # combines both sets still with no particular order

# PART D: Dictionaries
my_dict = {'name': 'Slopak', 'age': 237, 'grade': 'N/A'}
print(my_dict) # prints all values
print(my_dict['age']) # prints 237
# print(my_dict['school']) keyError
my_dict['grade'] = '1st'
print(my_dict) # the grade changes to 1st
my_dict['school'] = 'Central Park'
print(my_dict) # adds the school key
