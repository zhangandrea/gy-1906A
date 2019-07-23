# #a字符串 =赋值符
# import turtle
#
# a=11123
# print(type(a))
#
# #字符串
# b="ihopfja[pk"
# print(type(b))
# print(b)
#
# #列表
# c=[1,2,3,4]
# print(type(c))
#
# #元组
# d = (1,3,5,76)
# print(type(d))
#
# #键值对{}dict 多个键值对中间用,隔开 key和value之间用:隔开
# e = {"姓名":"蚝哥","手机号":"13370018219","性别":"女"}
# print(type(e))
# print(e)
#
# #练习
# # 第一组数据   张三,李四,王五,赵六,钱七
# f = ["张三","李四","王五","赵六","钱七"]
# print(f)
# # 第二组数据    姓名 张三  年龄 18 性别 女  科目 语文 成绩 80
# g = {"姓名":"张三","年龄":"18","性别":"女","科目":"语文","成绩":"80"}
# print(g)
# # 第三组数据   A，2,3,4,5,6,7,8,9，J,Q,K
# h = "A,2,3,4,5,6,7,8,9,J,Q,K"
# print(h)
# # 第四组数据  10000
# i = 10000
# print(i)
# # 第五组数据  学生
# j = "学生"
# print(j)
#
#
# # 小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟
# a = 20
# if(a>=10):
#     print(a,"元可以买红双喜")
# if(a>=25):
#     print(a,"元可以买玉溪")
# if(a>=5):
#     print(a, "元可以买大前门")
#
#
# # 成人票 200 未成年票100 60岁以上的老人票 150 小明今年18岁，去买票应该买那种票？
# age = 18
# if(age>=60):
#     print(age,"买老年票150元")
# elif(age>=18):
#     print(age,"买成人票200元")
# else:
#     print(age,"买未成年票200元" )
#
# # 打印出100以内的奇数 i%2
# for i in range(100):
#  if (i%2 !=0):
#      print(i)
#
#
#
# for i in range(100):
#     print(i)
#
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'X',i,"=",i*j,'\t',end='')
#     print()
#
#
#
# # 求出100以内的质数
# num=[];
# i=2
# for i in range(2,100):
#    j=2
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#       num.append(i)
# print(num)
#
#
#
# #成绩0-59不及格，60-70及格 70-80 良好 80以上是优秀    [90,100,81,84]判断下改组成绩是否全部都是优秀
# for m in [90,100,81,84]:
#     a = 0 #0代表m是不及格,1代表m及格
#     b = 2 #2代表m是良好,3代表m是优秀
#     for m in [90,100,81,84]:
#         if(m>80):
#             b = 3
#             print (m,'是优秀')
#
#
#
# #[1,60,30,90.100,20,70.59.69.71,80,84]
# for i in [1,60,30,90,100,20,70,59,6,97,80,84]:
#     c = 80
#     b = 59
#     a = 60
#     if (i>=c):
#         print(i,'优秀')
#     elif(i<=b):
#         print(i,'不及格')
#     else:
#         print(i,'及格')
#
#
#
# o = 1
# for i  in [81,90,81,90,99,5]:
#     if(i<80):
#         o = 2
# if (o==1):
#             print("优秀")
# else:
#             print("不优秀")


#"01010010001110001001001010101010010101" 计算下几个0 几个1
a = "01010010001110001001001010101010010101"
x = 0 #统计0
y = 0 #统计1
for i in a:
    if(i=="0"):
        x=x+1
    else:
        y=y+1
print ("有",x,"个0,",y,"个1")


#求1+2+3+4...+100
i = 1
while(i<101):
    print(i+i)
    i=i+1


#求1+2+3+4...+100

a=0
for i in range(1,101):
    a = a + i

print(a)


a=0
i=1
while(i<101):
    a = a+i

    i = i+1
print(a)


#求出10的阶乘

a="中华人民共和国成立70年"
print(a[1:5])
print(a[5:7])
print(a[-3:-1])

#按照扑克牌的规则，现在有6张牌，只要5张
#黑桃（S）红桃（H）方块（D）梅花（C）
#牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
#数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
#[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
#["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
#["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
#
# a = '[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'
# a = a[1:-1]
# print(a)
# a_li = a.split(''' , ''')
# print(a_li)
#
#
# a = 'https://guoyasoft.com/dashboard'
# xieyi=a.split('://')[0]
# a = a.split('://')[1]
# print(xieyi)
#
# yuming=a[:a.find('/')]
# print(yuming)
#
# uri=a[a.find('/'):]
# print(uri)
#
#
#
# a = []
# a.append(2)
# a.append('biofdngopajdf')
# print(a)
#
# b=['biogfbanps',65416,'张海世是蚝哥的小弟']
# print(a+b)
#
# a.extend(b)
# print(a)
#
# a.pop(0)
# print(a)
#
# a.pop()
# print(a)
#
# # a = []
# # print(a)
# #
# # a.clear()
# # print(a)
#
# a[0]=0
# print(a)
#
# print(a[0])
#
# print(a[1])
#
# for i in a:
#     print(i)
#
# print(a[1:3])
#
# print(a[::-1])
#
# a={}
# a['姓名']='蚝哥'
# print(a)
# c = {'姓名':'蚝哥'}
# d = {'性别':'女'}
# print(dict(c,**d))
# print(c)
# print(d)
#
# d = {}
# for i in b:
#     c=i[1:]
#     if(c in d):
#         d[c] += 1
#     else:
#         d[c] = 1
# print(d)


# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]

# 第一步：统一符号  对字符串的处理，用replace（）
a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
a = a.replace("''",'"')
print(a)
# 第二步：去掉中括号 字符串截取  [::]
# 第三步：变成list  字符串切片  .split（） 新建一个list变量
# 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
# 第五步：统计相同的数字个数  用字典去统计
# 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
# 如果key对应的数值有3的 v1 = 1，如果没有则为0
# 如果key对应的数值有2的 v2 = 1，如果没有则为0
    a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
    a = a.replace("''",'"')
    print(a)
    a=a[2:-2]
    print(a)
    a_li = a.split('" , "')
    print(a_li)
    s = {}
    for i in a_li:
        j = i [1:]
        print(j)
        if(j not in s):
            s[j]=1
        else:
            s[j]+=1
    print(s)
    q1 = 0
    q2 = 0
    for m in s:
        if  (s[m] == 3):
            q1 = 1
        if (s[m]==2):
            q2 = 1
    if(q1==1  and q2 ==1):
        print('3带2')
    else:
        print("炸")




