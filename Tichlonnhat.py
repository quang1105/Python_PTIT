n = int(input())
a = sorted([int(x) for x in input().split()])
print(max(a[0] * a[1], max(a[-1] * a[-2], max(a[0] * a[1] * a[-1], a[-1] * a[-2] * a[-3]))))