for testcase in range(int(input())):
    S = input()

    if S == '.':
        break

    stack = []
    ans = 'YES'
    for i in range(len(S)):
        s = S[i]
        if s == '(':
            stack.append('(')
        if s == ')':
            if len(stack) == 0:
                ans = 'NO'
                break

            if stack[-1] == '(':
                stack.pop()
            else:
                ans = 'NO'
                break

    if len(stack) > 0:
        ans = 'NO'

    print(ans)

