parents = list(map(int, input().split()))
line = int(input())

for i in range(line):
    child = list(map(int, input().split()))
    if child[0] > parents[0]:
        print("You Lose!")
    elif child[0] < parents[0]:
        print("You Win!")
    elif child[0] == parents[0] and child[1]:
        print("You Win!")
    else:
        print("You Lose!")
