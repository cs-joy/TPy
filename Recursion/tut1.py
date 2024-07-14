def countdown(n):
    if n <= 0:
        print('Warm Welcome!')
    else:
        print(n)
        countdown(n - 1)

countdown(10)