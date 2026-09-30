def constantTC_formula(n):
    operation = 0
    total = n*(n+1)/2
    operation+=1
    return total,n, operation 
def linearTC_1loop(n):
    total = 0
    operation = 0
    for i in range(1, n+1, 1):
        operation +=1
        total +=i
    return total,n, operation
n = int(input("enter your interger till what u want to sum:"))

print(constantTC_formula(n))
print(linearTC_1loop(n))