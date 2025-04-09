t = input("Enter the First  Integer :")
s = input("Enter the Second Interger :")
p1 = 0
p2 = 0
while p1 < len(t) and p2 < len(s):
    if t[p1] == s[p2]:
        p1 += 1
        p2 += 1
    else:
        p2 += 1
if len(t) > p1:
    print(False)
else:
    print(True)
