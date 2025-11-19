def getMaxEXP(level):
    return 5 * level

def End(N, M, Player, Map, Turn, Status, Items, Reason, visitedBox, killMonsters):
    for i in range(N):
        for j in range(M):
            v = Map[i][j]
            if (i, j) in visitedBox:
                v = '.'
            if (i, j) in killMonsters:
                v = '.'
            if Player[0] == i and Player[1] == j:
                if Reason == 'WIN' or Reason == 'CONTINUE999':
                    v = '@'
            print(v, end='')
        print('\n', end='')
    if Status["HP"] < 0:
        Status["HP"] = 0
    print(f"Passed Turns : {Turn}")
    print(f'LV : {Status["Level"]}')
    print(f'HP : {Status["HP"]}/{Status["MaxHP"]}')
    print(f'ATT : {Status["Damage"]}+{Items["Sword"]}')
    print(f'DEF : {Status["Armor"]}+{Items["Armor"]}')
    print(f'EXP : {Status["Exp"]}/{getMaxEXP(Status["Level"])}')
    if Reason == "WIN":
        print("YOU WIN!")
    elif Reason == "CONTINUE999":
        print("Press any key to continue.")
    else:
        print(f'YOU HAVE BEEN KILLED BY {Reason}..')
    exit()

N, M = map(int, input().split())
Map = [list(input()) for i in range(N)]
Command = list(input())

Player = [0, 0]
StartPoint = (0, 0)
K = 0
L = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == '@':
            Player = [i, j]
            StartPoint = (i, j)
            Map[i][j] = '.'
        elif Map[i][j] == '&' or Map[i][j] == 'M':
            K += 1
        elif Map[i][j] == 'B':
            L += 1

Monsters = {}
for i in range(K):
    R, C, S, W, A, H, E = input().split()
    Monsters[(int(R)-1, int(C)-1)] = {
        "Name": S,
        "Damage": int(W),
        "Defense": int(A),
        "MaxHP" : int(H),
        "Exp" : int(E)
    }

ItemBox = {}
for i in range(L):
    R, C, T, S = input().split()
    ItemBox[(int(R)-1, int(C)-1)] = {
        "Type": T,
        "Value": S
    }

Items = {
    "Sword": 0,
    "Armor": 0,
    "HR": False,
    "RE": False,
    "CO": False, 
    "EX": False,
    "DX": False,
    "HU": False,
    "CU": False,
    "Acc": 0
}

Status = {
    "MaxHP": 20,
    "HP": 20,
    "Damage": 2,
    "Armor": 2,
    "Exp": 0,
    "Level": 1
}

visitedBox = []
killMonsters = []

turn = 0
for MoveDir in Command:
    # 이동
    if MoveDir == 'L':
        if 0 <= Player[1]-1 < M and Map[Player[0]][Player[1]-1] != '#':
            Player[1] -= 1
    if MoveDir == 'R':
        if 0 <= Player[1]+1 < M and Map[Player[0]][Player[1]+1] != '#':
            Player[1] += 1
    if MoveDir == 'U':
        if 0 <= Player[0]-1 < N and Map[Player[0]-1][Player[1]] != '#':
            Player[0] -= 1
    if MoveDir == 'D':
        if 0 <= Player[0]+1 < N and Map[Player[0]+1][Player[1]] != '#':
            Player[0] += 1
            
    if Player[0] < 0:
        Player[0] = 0
    if Player[1] < 0:
        Player[1] = 0
    if Player[0] >= N:
        Player[0] = N-1
    if Player[1] >= M:
        Player[1] = M-1
    # 이동 끝
    turn += 1

    x, y = Player
    if Map[x][y] == 'B':
        if (x,y) in visitedBox:
            continue
        I = ItemBox[(x, y)]
        Type = I["Type"]
        Value = I["Value"]
        if Type == 'O':
            if Items["Acc"] < 4:
                if Items[Value] == False:
                    Items["Acc"] += 1
                    Items[Value] = True
        if Type == 'W':
            Items["Sword"] = int(Value)
        if Type == 'A':
            Items["Armor"] = int(Value)
        visitedBox.append((x, y))
    elif Map[x][y] == '^':
        if Items["DX"] == True:
            Status["HP"] -= 1
        else:
            Status["HP"] -= 5
        if Status["HP"] <= 0:
            if Items["RE"] == True:
                Status["HP"] = Status["MaxHP"]
                Player[0] = StartPoint[0]
                Player[1] = StartPoint[1]
                Items["RE"] = False
                Items["Acc"] -= 1
                RE = True
            else:
                End(N, M, Player, Map, turn, Status, Items, "SPIKE TRAP", visitedBox, killMonsters)
                break
    elif Map[x][y] == '&' or Map[x][y] == 'M':
        if (x,y) in killMonsters:
            continue
        Monster = Monsters[(x, y)]
        Monster_Name = Monster["Name"]
        Monster_Damage = Monster["Damage"]
        Monster_Defense = Monster["Defense"]
        Monster_MaxHP = Monster["MaxHP"]
        Monster_HP = Monster["MaxHP"]
        Monster_Exp = Monster["Exp"]

        if Items["HU"] == True:
            if Map[x][y] == 'M':
                Status["HP"] = Status["MaxHP"]

        cur = 1 # 1 p 2 m
        k = 1
        RE = False
        while True:
            if cur == 1:
                PlayerDamage = Status["Damage"] + Items["Sword"]
                if k == 1:
                    if Items["CO"] == True:
                        if Items["DX"] == True:
                            PlayerDamage = PlayerDamage * 3
                        else:
                            PlayerDamage = PlayerDamage * 2
                    k = 2
                Monster_HP -= max(1, PlayerDamage - Monster_Defense)
                cur = 2
                if Monster_HP <= 0:
                    break
            else:
                E = True
                if k == 2:
                    if Items["HU"] == True:
                        if Map[x][y] == 'M':
                            E = False
                    k = 3
                if E == True:
                    Status["HP"] -= max(1, Monster_Damage - (Status["Armor"] + Items["Armor"]))
                cur = 1
                if Status["HP"] <= 0:
                    if Items["RE"] == True:
                        Status["HP"] = Status["MaxHP"]
                        Player[0] = StartPoint[0]
                        Player[1] = StartPoint[1]
                        Items["RE"] = False
                        Items["Acc"] -= 1
                        RE = True
                    else:
                        End(N, M, Player, Map, turn, Status, Items, Monster_Name, visitedBox, killMonsters)
                    break
        if RE == False:
            # 몬스터 잡음
            killMonsters.append((x, y))
            if Items["HR"] == True:
                Status["HP"] += 3
                if Status["MaxHP"] < Status["HP"]:
                    Status["HP"] = Status["MaxHP"]

            if Items["EX"] == True:
                Monster_Exp = int(Monster_Exp * 1.2)

            Status["Exp"] += Monster_Exp
            if Status["Exp"] >= getMaxEXP(Status["Level"]):
                Status["Level"] += 1
                Status["Exp"] = 0
                Status["Armor"] += 2
                Status["Damage"] += 2
                Status["MaxHP"] += 5
                Status["HP"] = Status["MaxHP"]

            if Map[x][y] == 'M':
                End(N, M, Player, Map, turn, Status, Items, "WIN", visitedBox, killMonsters)


if Status["HP"] > 0:
    End(N, M, Player, Map, turn, Status, Items, "CONTINUE999", visitedBox, killMonsters)

# for i in Map:
#     print(i)

# print(Player)
# print(Command)
# print(Monsters)
# print(ItemBox)
        