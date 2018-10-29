def func(P,Q):
    n = 6;
    i = 1;
    while(i<P):
        n = n*6
        i = i+1
        n = n+Q
        while(n>Q):
            n = n - Q
    return n;

print(func(17,5))
print(func(25,8))
