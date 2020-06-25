s = input()

vowels = "AEIOUY"

flag = False

for _ in range(len(s)):

        if (int(s[0])+int(s[1]))%2==0 and (int(s[3])+int(s[4]))%2==0 and (int(s[4])+int(s[5]))%2==0 and (int(s[-1])+int(s[-2]))%2==0:
            flag = True

ans = 'valid' if (flag and s[2] not in vowels) else 'invalid'

print(ans)

