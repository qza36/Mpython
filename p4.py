# 判断输入的数字是否为奇数
n = int(input('请输入数字：'))
n2 = n % 2 == 1 # 一个数%2若结果为1则是奇数，结果为0则为偶数
print('是否为奇数：',n2)