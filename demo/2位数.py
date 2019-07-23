
def f():
    return'{m1}欠{m2}{mon}'.format(mon=money,m1=hm1,m2=hm2)
print(f("海南哥",'蚝哥','一个海南岛'))

def buy_coffee(cash=100,cups=1):
    print('去咖啡店')
    cup_num = cups
    print('告诉服务员',cup_num,'杯咖啡')
    print('服务员告诉你要',cup_num*30,'钱')
    money=cash
    print('你给服务员',money,'钱')
    print('服务员找零',money-cup_num*30,'，给你',cup_num,'杯咖啡')
buy_coffees()
buy_coffees(100,2)