totalBranch = [1, 2, 3, 4, 5, 6, 7, 8, 9]
minValue = 100
cityBankGraph = [
    [0, 10, 0, 5, 0, 0, 10, 0, 0, 0],
    [10, 0, 5, 0, 0, 0, 10, 0, 0, 0],
    [0, 5, 0, 0, 0, 5, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 5, 0, 15, 0],
    [0, 0, 0, 0, 0, 15, 0, 30, 5, 0],
    [0, 0, 5, 0, 15, 0, 0, 0, 0, 10],
    [10, 10, 0, 5, 0, 0, 0, 0, 15, 0],
    [0, 0, 0, 0, 30, 0, 0, 0, 0, 25],
    [0, 0, 0, 15, 5, 0, 15, 0, 0, 0],
    [0, 0, 0, 0, 0, 10, 0, 25, 0, 0]
]
totalDistace = 0
for i in cityBankGraph:
    minValue = min(value for j, value in enumerate(i) if j in totalBranch and value != 0)
    totalDistace = totalDistace + minValue
    print(totalBranch)
    print(i.index(minValue))
    totalBranch.remove(i.index(minValue))
    
    print(f"Minimum Value in the row: {minValue}")
    
print(totalDistace)