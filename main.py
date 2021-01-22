def factOrSum(x, word):
    if word == "factorial": 
        total = 1
        for i in range (1, x+1):
            total = total * i
          
    else: 
        total = 0
        for i in range (1, x+1):
            total = total + i
    
    return total 

print(factOrSum(3, "sum"))
