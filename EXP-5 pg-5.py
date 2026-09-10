def set_operations(a,b):
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference (A-B):", a - b)
    print("Difference (B-A):", b - a)
    print("Symmetric Difference:", a ^ b)
    print("A is subset of B:", a.issubset(b))
    print("B is subset of A:", b.issubset(a))
    print("A is superset of B:", a.issuperset(b))
    print("B is superset of A:", b.issuperset(a))
    print("A and B are disjoint:", a.isdisjoint(b))

m = int(input("Enter number of elements in first set: "))
a=set()
b=set()
for i in range(m):
    x = int(input("Enter element: "))
    a.add(x)
n = int(input("Enter number of elements in second set: "))
for i in range(n):
    y= int(input("Enter element: "))
    b.add(y)
set_operations(a, b)
