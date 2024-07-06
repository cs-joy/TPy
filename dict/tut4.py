def histogram(s):
    my_dict = dict()
    for c in s:
        if c not in my_dict:
            my_dict[c] = 1
        else:
            my_dict[c] += 1
    return my_dict

print(histogram('hello'))