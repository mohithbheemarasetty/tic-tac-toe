n = 3
a = [0] * n
z = 5


def check(order):
    for x in range(order):
        m = 0
        o = 0
        for y in range(order):
            if a[x][y] == 1:
                m += 1
            elif a[x][y] == 2:
                o += 1
            if m == 3:
                return "1"
            if o == 3:
                return "2"
    for y in range(order):
        m = 0
        o = 0
        for x in range(order):
            if a[x][y] == 1:
                m += 1
            elif a[x][y] == 2:
                o += 1
            if m == 3:
                return "1"
            elif o == 3:
                return "2"
    if a[0][0] & a[1][1] & a[2][2] == 1:
        return "1"
    elif a[0][0] & a[1][1] & a[2][2] == 2:
        return "2"
    if a[0][2] & a[1][1] & a[2][0] == 1:
        return "1"
    if a[0][2] & a[1][1] & a[2][0] == 1:
        return "1"


for i in range(n):
    a[i] = [0] * n
print(a[0])
print(a[1])
print(a[2])
wow = dict()
g = 0
ron = 100
while z != 0:
    point = 1
    print("you can only enter at zeros")
    lol = int(input("enter the point player 1 "))
    lol1 = int(input("point 2"))
    if (lol, lol1) in wow.keys():
        print("occupied, try a different position")
        continue
    wow[g] = {(lol, lol1)}
    g += 1
    a[lol][lol1] = point
    well = check(n)
    if well == "1":
        print("player 1 wins!!")
        break
    point = 2
    print(a[0])
    print(a[1])
    print(a[2])
    lol = int(input("enter the point player 2"))
    lol1 = int(input("point 2"))
    if (lol, lol1) in wow.keys():
        print("occupied try a different position")
        continue
    wow[g] = {(lol, lol1)}
    g += 1
    a[lol][lol1] = point
    well = check(n)
    print(a[0])
    print(a[1])
    print(a[2])
    if well == "2":
        print("player 2 wins!!")
        break
    z -= 1
    if z == 1:
        print("it's a draw!!")
        break


