cityBankGraph = [
    [0, 10, 0, 5, 0, 0, 10, 0, 0, 0], # Uttara Branch
    [10, 0, 5, 0, 0, 0, 10, 0, 0, 0], # City Bank Airport
    [0, 5, 0, 0, 0, 5, 0, 0, 0, 0], # City Bank Le Meridien
    [5, 0, 0, 0, 0, 0, 5, 0, 15, 0], # City Bank Beside Uttara Diagnostic
    [0, 0, 0, 0, 0, 15, 0, 30, 5, 0], # City Bank Mirpur 12
    [0, 0, 5, 0, 15, 0, 0, 0, 0, 10], # City Bank Nikunja
    [10, 10, 0, 5, 0, 0, 0, 0, 15, 0], # City Bank Shaheed Sarani
    [0, 0, 0, 0, 30, 0, 0, 0, 0, 25], # City Bank Narayanganj
    [0, 0, 0, 15, 5, 0, 15, 0, 0, 0], # City Bank Pallabi
    [0, 0, 0, 0, 0, 10, 0, 25, 0, 0] # City Bank JFP
]

def find_lowest_value_and_index(lst):
    lowest_value = float('inf')
    lowest_index = None

    for i, value in enumerate(lst):
        if value != 0 and value < lowest_value:
            lowest_value = value
            lowest_index = i

    return lowest_value, lowest_index

totalDistace = 0
branchNumber = 0
visitList = []

for i in range(len(cityBankGraph) - 1):

    current = cityBankGraph[branchNumber]

    for z in visitList:
        current[z] = 0

    visitList.append(branchNumber)
    value = find_lowest_value_and_index(current)

    branchNumber = value[1]
    Distace = value[0]
    totalDistace = totalDistace + Distace

visitList.append(branchNumber)

print('Path', visitList)
print('totalDistace',totalDistace)
