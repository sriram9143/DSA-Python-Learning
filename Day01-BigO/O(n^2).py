# |    /
# |   /
# |  /
# | /
# |______________
# ^Operations >N



def print_items(n):
    for i in range(n): #n
        for j in range(n): #n
            print(i,j)

    for k in range(n):
        print(k)

# n*n => n^2 + n => n^2 (here n*2 dominates 2n and 2 is constant)
print_items(2) 

