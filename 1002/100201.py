def bar(a, b, *args, c=200):
    print(a, b, args, c)

bar(1, 2, 3, 4, 5, 6) # -> 1, 2, (3, 4, 5, 6)

# def foo(a, b, c):
#     pass

# foo(1, 2) # -> Error

# def pos(a, b, c=20):
#     pass

# pos(1, 2) # -> OK