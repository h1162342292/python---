import random
import pickle
def open_data():#读取数据
    try:
        with open("user.txt","rb") as f:
            return pickle.load(f)
    except IOError as e:
            return False
    except Exception as e:
        raise e
def update_data(user_data):#更新数据
    try:
        with open("user.txt","wb") as f:
            pickle.dump(user_data,f)
            return True
    except IOError as e:
            return False
    except Exception as e:
        raise e
class BankMan(object):#银行人员
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
    def new_user(self,person):#创建用户
        person.IDcard = random.randint(100000,1000000)
        person.LOCK = False
        user_data = open_data() if open_data() else {}
        if person.IDcard in user_data.keys():
            print("卡号已存在")
            return False
        user_data[person.IDcard] = [person.name,person.id,person.passwd,person.tel,person.money,person.LOCK]
        res = update_data(user_data)
        if not res:
            print("建户失败")
        print("建户成功!!!您的卡号为%d"%person.IDcard)
    def del_user(self,IDcard):#删除用户
        user_data = open_data() if open_data() else {}
        for i in user_data.keys():
            if IDcard == str(i):
                user_data.pop(i)
                break
        update_data(user_data)
        print("销户成功")
    def see_money(self,IDcard):#查看余额
        user_data = open_data() if open_data() else {}
        for i in user_data.keys():
            if IDcard == str(i):
                return f"您的余额为{user_data[i][4]}"
    def deposit(self,IDcard,money):#存款
        user_data = open_data()
        user_data[IDcard][4] += money
        update_data(user_data)
        print("存款成功！")
        print(f"您的余额为{user_data[IDcard][4]}")
    def withdrawals(self,IDcard,money):#取款
        user_data = open_data()
        user_data[IDcard][4] -= money
        update_data(user_data)
        print("取款成功！")
        print(f"您的余额为{user_data[IDcard][4]}")
    def transfer(self,ID1,ID2,money):#转账
        user_data = open_data()
        user_data[ID1][4] -= money
        user_data[ID2][4] += money
        update_data(user_data)
        print("转账成功！")
        print("您的余额为%d" % user_data[ID1][4])
    def unlock(self,IDcard):#解锁
        user_data = open_data()
        if user_data[IDcard][5] == True:
            user_data[IDcard][5] = False
            update_data(user_data)
            print("解锁成功")
        else:
            print("没锁解个屁")
    def user_msg(self,IDcard):#用户信息
        user_data = open_data() if open_data() else {}
        for i in user_data.keys():
            if IDcard == str(i):
                return f"卡号:{i}\t姓名:{user_data[i][0]}\t身份证号:{user_data[i][1]}\t密码:{user_data[i][2]}\t电话:{user_data[i][3]}\t余额:{user_data[i][4]}\t锁状态:{user_data[i][5]}"
    def update_user_msg(self,IDcard):#修改用户信息
        user_data = open_data() if open_data() else {}
        while True:
            choice = input("请选择你要修改的信息 0-用户名，1-手机号，其他退出")
            if choice == "0":
                user_name = input("请输入用户名")
                user_data[IDcard][0] = user_name
                update_data(user_data)
                print("当前姓名为%s"%user_data[IDcard][0])
                print("修改成功")
                break
            elif choice == "1":
                user_tel = input("请输入手机号")
                user_data[IDcard][3] = user_tel
                update_data(user_data)
                print("当前电话为%s" % user_data[IDcard][3])
                print("修改成功")
                break
            else:
                break
    def __str__(self):
        return f"name:{self.name},passwd:{self.passwd}"
    __repr__ = __str__
bankman1 = BankMan("张三","123456")
bankman2 = BankMan("李四","123456")
bankman3 = BankMan("王五","123456")
bankman4 = BankMan("赵六","123456")
Dict1 = {}#存放银行人员的字典
Dict1[bankman1.name] = bankman1.passwd
Dict1[bankman2.name] = bankman2.passwd
Dict1[bankman3.name] = bankman3.passwd
Dict1[bankman4.name] = bankman4.passwd
class Person(object):#普通用户
    IDcard = None
    LOCK = None
    def __init__(self,name,id,passwd,tel,money=0):
        self.name = name
        self.id = id
        self.passwd =passwd
        self.tel = tel
        self.money = money
    def see_money(self,IDcard):#查看余额
        user_data = open_data() if open_data() else {}
        for i in user_data.keys():
            if IDcard == i:
                return f"您的余额为{user_data[i][4]}"
    def deposit(self,IDcard,money):#存款
        user_data = open_data()
        user_data[IDcard][4] += money
        update_data(user_data)
        print("存款成功！")
        print(f"您的余额为{user_data[IDcard][4]}")
    def withdrawals(self,IDcard,money):#取款
        user_data = open_data()
        user_data[IDcard][4] -= money
        update_data(user_data)
        print("取款成功！")
        print(f"您的余额为{user_data[IDcard][4]}")
    def transfer(self,ID1,ID2,money):#转账
        user_data = open_data()
        user_data[ID1][4] -= money
        user_data[ID2][4] += money
        update_data(user_data)
        print("转账成功！")
        print("您的余额为%d" % user_data[ID1][4])
def main():
    login = True
    while login:
        user = input("请选择登陆类型(0--银行人员，1--普通用户,其他--退出)")
        if user == "0":
            man_name = input("请输入员工姓名")
            while True:
                if man_name not in Dict1.keys():
                    print("查无此员工")
                    break
                else:
                    man_passwd = input("请输入密码")
                    if Dict1[man_name] == man_passwd:
                        print("员工%s登陆成功"%man_name)
                        # 建户【0】 销户【1】 查看余额【2】 存款【3】 取款【4】
                        # 转账【5】  解锁【6】 用户信息【7】 修改用户信息【8】
                        # 退出登录【9】
                        man = BankMan(man_name, man_passwd)
                        choice = input("请选择你想要进行的操作: 0建户 1销户 2查看余额 3存款 4取款 5转账 6解锁 7用户信息 8修改用户信息 9退出登陆")
                        if choice == "0":
                            user_name = input("请输入姓名")
                            user_id = input("请输入身份证号")
                            user_passwd = input("请输入密码")
                            user_tel = input("请输入电话号码")
                            p = Person(name=user_name,id=user_id,passwd=user_passwd,tel=user_tel,)
                            man.new_user(person=p)
                            break
                        if choice == "1":
                            user_IDcard = input("请输入你需要注销的卡的卡号")
                            man.del_user(user_IDcard)
                            break
                        if choice == "2":
                            user_IDcard = input("请输入卡号")
                            res = man.see_money(user_IDcard)
                            print(res)
                            break
                        if choice == "3":
                            n = True
                            user_data = open_data() if open_data() else {}
                            print(user_data.keys())
                            user_IDcard = int(input("请输入卡号"))
                            while n:
                                if user_IDcard in user_data.keys():
                                    user_money = int(input("请输入存款金额"))
                                    man.deposit(user_IDcard,user_money)
                                    n = False
                                else:
                                    print("卡号不存在")
                                    user_IDcard = int(input("请重新输入卡号"))
                            if n == False:
                                break
                        if choice == "4":
                            n = True
                            user_data = open_data() if open_data() else {}
                            print(user_data.keys())
                            user_IDcard = int(input("请输入卡号"))
                            while n:
                                if user_IDcard in user_data.keys():
                                    user_money = int(input("请输入取款金额"))
                                    if 0<user_money<user_data[user_IDcard][4]:
                                        man.withdrawals(user_IDcard,user_money)
                                        n = False
                                    else:
                                        print("没钱取毛线")
                                else:
                                    print("卡号不存在")
                                    user_IDcard = int(input("请重新输入卡号"))
                            if n == False:
                                break
                        if choice == "5":
                            n = True
                            user_data = open_data() if open_data() else {}
                            print(user_data.keys())
                            user_IDcard1 = int(input("请输入你的卡号"))
                            while n:
                                if user_IDcard1 in user_data.keys():
                                    user_IDcard2 = int(input("请输入你要转账的卡号"))
                                    while True:
                                        if user_IDcard2 in user_data.keys():
                                            user_money = int(input("请输入转账金额"))
                                            if 0<user_money<user_data[user_IDcard1][4]:
                                                man.transfer(user_IDcard1,user_IDcard2,user_money)
                                                n = False
                                                break
                                            else:
                                                print("没钱转个屁")
                                        else:
                                            print("所转账户不存在")
                                            break
                                else:
                                    print("你的账户不存在")
                                    n = False
                            if n == False:
                                break
                        if choice == "6":
                            n = True
                            user_data = open_data() if open_data() else {}
                            user_IDcard = int(input("请输入卡号"))
                            while n:
                                if user_IDcard in user_data.keys():
                                    user_id = input("请输入身份证号")
                                    while True:
                                        if user_data[user_IDcard][1] == user_id:
                                            man.unlock(user_IDcard)
                                            n = False
                                            break
                                        else:
                                            user_id = input("请重新输入身份证号")
                                else:
                                    user_IDcard = int(input("请重新输入卡号"))
                            if n == False:
                                break
                        if choice == "7":
                            user_IDcard = input("请输入你要查看的用户的卡号")
                            res = man.user_msg(user_IDcard)
                            print(res)
                            break
                        if choice == "8":
                            n = True
                            user_data = open_data() if open_data() else {}
                            user_IDcard = int(input("请输入卡号"))
                            while n:
                                if user_IDcard in user_data.keys():
                                    user_id = input("请输入身份证号")
                                    while True:
                                        if user_data[user_IDcard][1] == user_id:
                                            man.update_user_msg(user_IDcard)
                                            n = False
                                            break
                                        else:
                                            user_id = input("请重新输入身份证号")
                                else:
                                    user_IDcard = int(input("请重新输入卡号"))
                            if n == False:
                                break
                        if choice == "9":
                            login = False
                            break
        elif user == "1":
            num = 0
            person_data = open_data() if open_data() else {}
            person_IDcard = int(input("请输入卡号"))
            while True:
                if person_IDcard in person_data.keys() :
                    if person_data[person_IDcard][5] == False:
                        person_passwd = input("请输入密码")
                        while num <2:
                            if person_data[person_IDcard][2] == person_passwd:
                                print("登录成功")
                                break
                            else:
                                num += 1
                                person_passwd = input("请重新输入密码")
                        if num == 2:
                            person_data[person_IDcard][5] = True
                            update_data(person_data)
                            print("卡已锁死，请找银行人员解锁")
                            break
                    else:
                        print("卡已锁死，请找银行人员解锁")
                        break
                    person = Person(person_data[person_IDcard][0], person_data[person_IDcard][1],
                                    person_data[person_IDcard][2], person_data[person_IDcard][3],person_data[person_IDcard][4])
                    person.IDcard = person_IDcard
                    person.LOCK = person_data[person_IDcard][5]
                    choice = input("请选择你想要进行的操作:  0查看余额 1存款 2取款 3转账 4退出登陆")
                    if choice == "0":
                        res = person.see_money(person_IDcard)
                        print(res)
                        break
                    if choice == "1":
                        person_money = int(input("请输入存款金额"))
                        person.deposit(person_IDcard,person_money)
                        break
                    if choice == "2":
                        person_money = int(input("请输入取款金额"))
                        if 0< person_money <= person_data[person_IDcard][4]:
                            person.withdrawals(person_IDcard, person_money)
                            break
                        else:
                            print("没钱取毛线")
                            break
                    if choice == "3":
                        n = True
                        print(person_data.keys())
                        person_IDcard1 = int(input("请输入你需要转的卡号"))
                        while n:
                            if person_IDcard1 in person_data.keys():
                                person_money = int(input("请输入转账金额"))
                                if 0 < person_money < person_data[person_IDcard][4]:
                                    person.transfer(person_IDcard, person_IDcard1, person_money)
                                    n = False
                                    break
                                else:
                                    print("没钱转个屁")
                            else:
                                print("所转账户不存在")
                                n = False
                                break
                        if n == False:
                            break
                    if choice == "4":
                        login = False
                        break
                else:
                    print("卡号不存在")
                    break
        else:
            print("输入错误!!!退出系统!!!")
            login = False
if __name__ == '__main__':
    main()
