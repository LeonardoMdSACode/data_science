def foo (x,y):
    return y(x) + y(x+1)

print(foo(1, lambda x: x*x))