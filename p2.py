#比较输入字符串长度的大小#

w1 = input('请输入第一个字符串：')
w2 = input('请输入第二个字符串：')
# 通过max函数实现返回最大值
print('其中字符最长的长度为：',max(len(w1),len(w2)))