import pickle

t = [1, 2, 3]

print(pickle.dumps(t))

s = pickle.dumps(t)
t2 = pickle.loads(s)

print(t2)

# although the new object has the same value as the old, it is not (in general) the same object:
print(t == t2)

print(t is t2)