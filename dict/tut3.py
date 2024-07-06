dept = {'3984984579834': 'Science', '3409845864': 'Business', '4903805834069': 'Arts'}

# check length of the dictionary
print('length = ', len(dept))

'''
the `in` operator works on dictionaries, too; it tells you whether something appear 
as a `key` in the dictionary (appearing as a value isn't good enough)
'''
# using `key`
print('3984984579834' in dept) # should be True

# but when we using the `value` insted of `key`
print('Business' in dept) # should be False which isn't correct info


'''
To see whether something appear as a value in a dictionary, we can use the method `values()`,
which return a collection of values, and then us the `in` operator:::
'''
# getting all values from the dept
vals = dept.values()

#\
print('Business' in vals) # should be True, now
