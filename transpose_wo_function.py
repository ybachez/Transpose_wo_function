aList = [  [99, 85, 98],
           [98, 57, 78],
           [92, 77, 76],
           [94, 32, 11],
           [99, 34, 22]
        ]

# this defines layout of new transpose matrix list triple line
result = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

# iterate through rows
for x in range(len(aList)):
    # iterate through columns
    for y in range(len(aList[0])):
        result[y][x] = aList[x][y]

for r in result:
    print(r)
