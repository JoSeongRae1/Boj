while True:
    S = input()

    if S == '.':
        break

    stack = []
    ans = 'yes'
    for i in range(len(S)):
        s = S[i]
        if s == '(':
            stack.append('(')
        if s == ')':
            if len(stack) == 0:
                ans = 'no'
                break

            if stack[-1] == '(':
                stack.pop()
            else:
                ans = 'no'
                break
            
        if s == '[':
            stack.append('[')
        if s == ']':
            if len(stack) == 0:
                ans = 'no'
                break

            if stack[-1] == '[':
                stack.pop()
            else:
                ans = 'no'
                break

    if len(stack) > 0:
        ans = 'no'

    print(ans)