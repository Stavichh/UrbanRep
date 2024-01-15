
def test(*args):
    for i, arg in enumerate(args):
        print("нынешний праметр - ", arg, " на позиции", i)


test(6, "damn", "word", True, None)



print()

def rec(n):
    if n == 1:
        return 1
    factorial = rec(n = n-1)
    return n * factorial


print(rec(3))