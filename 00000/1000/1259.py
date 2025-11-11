while True:
    A = input()
    if A == "0":
        break
    print("yes" if A == A[::-1] else "no")