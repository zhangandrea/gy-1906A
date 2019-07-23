# # 按照扑克牌的规则，现在有6张牌，只要5张
# # 黑桃（S）红桃（H）方块（D）梅花（C）
# # 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# # 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# # [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# # ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# # ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# def juge_3_2():
#     a = input('请输入牌型')
#     a = a.replace("''",'"')
#     # print(a)
#     a=a[2:-2]
#     # print(a)
#     a_li = a.split('" , "')
#     # print(a_li)
#     s = {}
#     for i in a_li:
#         j = i [1:]
#         # print(j)
#         if(j not in s):
#             s[j]=1
#         else:
#             s[j]+=1
#     # print(s)
#     q1 = 0
#     q2 = 0
#     for m in s:
#         if  (s[m] == 3):
#             q1 = 1
#         if (s[m]==2):
#             q2 = 1
#     if(q1==1  and q2 ==1):
#         print('3带2')
#     else:
#         print("炸")
#
# juge_3_2()
# juge_3_2()
# juge_3_2()
#
#
#
# def en_3(a):
#     # a = input("打牌：")
#     # a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
#     a = a.replace("''",'"')
#     a=a[2:-2]
#     a_li = a.split('" , "')
#     s = {}
#     for i in a_li:
#         j = i [1:]
#         if(j not in s):
#             s[j]=1
#         else:
#             s[j]+=1
#     q1 = 0
#     q2 = 0
#     for m in s:
#         if  (s[m] == 3):
#             q1 = 1
#         if (s[m]==2):
#             q2 = 1
#     if(q1==1  and q2 ==1):
#            print("3带2")
#     else:
#            print("没有")
#
# with open("D:\\softwaredata\\pycarm\\zhs_1\\shaz\\dma04\\rui_1.txt",'r') as f:
#     lines = f.readlines()
#     for io in lines :
#         io = io.replace('\n','')
#         print(io)
#         en_3(io)
