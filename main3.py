def ontime(n):
    iterations=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iterations+=1
        print(" ")
    print("When n is:",n,"the number of iterations is:",iterations)
ontime(5)
ontime(4)
ontime(3)
print("With every n the number of iterations are squared")
print("O(n^2)")
