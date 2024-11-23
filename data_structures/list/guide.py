'''
list.append(x)

    Add an item to the end of the list. Similar to a[len(a):] = [x].

list.extend(iterable)

    Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.

list.insert(i, x)

    Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)

    Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])

    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()

    Remove all items from the list. Similar to del a[:].

list.index(x[, start[, end]])

    Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

    The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)

    Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)

    Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()

    Reverse the elements of the list in place.

list.copy()

    Return a shallow copy of the list. Similar to a[:].

An example that uses most of the list methods:
'''

feelings = ['joy', 'anger', 'love', 'shock', 'anger', 'sadness', 'joy', 'fear', 'disgust', 'joy']
# counting copy elements in the list
print(f'\'anger\': {feelings.count('anger')}')
print(f'\'happy\': {feelings.count('happy')}')

# index of an element
print(f'index of \'joy\': {feelings.index('joy')}')

# find next joy starting at position 6
print(feelings.index('joy', 6))

# reversing the list
def list_reverse():
    feelings.reverse()
    return feelings
print(list_reverse())

# insert an element to the list
feelings.append('curiosity')
print(f'after adding new feelings: {feelings}')

# sorting
feelings.sort()
print(feelings)

# removing an element at the given position
feelings.pop(9) # sadness feelings removed :)
print(feelings)

# extending the list
new_list = [1, 2.8, 3]
feelings.extend(new_list)
print(feelings)

# copy the entire list
copied_list = feelings.copy()
print(f'copied_list: {copied_list}')

# clear the list
feelings.clear()
print(f'feelings = {feelings}')


# :) :) :) :) :) :) :) :)
# Using Lists as Queues:
# :) :) :) :) :) :) :) :)
