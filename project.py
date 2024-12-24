def myfunction(n):
    for i in range(0,n+1):
        print("first loop")
    j=1
    for i in range(j<=n+1):
        print("Second loop")
        j=j*2
    for i in range(0,100):
        print("third loop")
print("Function above will take time:")
print("O(N)+O(log N)+O(100)")