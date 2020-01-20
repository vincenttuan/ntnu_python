# def f(n):
#     if n < 2:
#         return n
#     return f(n-1) + f(n-2)

def f(n):
    return n if n < 2 else f(n-1) + f(n-2)

print(f(6))
