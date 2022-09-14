# print('hello python')
# a = input("请输入数字")
# b = input("请输入数字")
# c = int(a) * int(b)
# print(c)
for a in range(1,10):
    for b in range(1,a + 1):
        c= a * b
        print(b ,'*', a, '=',c ,'\t',end='')
    print('')