import math
# m>n
def euclid(m,n):
    while n > 0:
        r=m%n
        m=n
        n=r
        # print(m,n)
    return m
print(euclid(1633,355))
