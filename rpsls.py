#coding:gbk
"""
程序目的：Rock-paper-scissors-lizard-Spock
程序作者：张琦
"""

import random


def number_to_name(number):                                                # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    if number == 0:                                                        #将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
        return "石头"
    elif number == 1:
        return "史波克"
    elif number == 2:
        return "纸"
    elif number == 3:
        return "蜥蜴"
    elif number == 4:
        return "剪刀"

    def name_to_number(name):
        if name == "石头":
            return 0
        elif name == "史波克":
            return 1
        elif name == "纸":
            return 2
        elif name == "蜥蜴":
            return 3
        elif name == "剪刀":
            return 4
def rpsls(player_choice):
    comp_number = random.randrange(0, 5)                                    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    m = number_to_name(comp_number)                                         # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    print("--------")                                                       # 输出"-------- "进行分割
    print("您的选择为:"+str(player_choice))                                   # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    print("计算机的选择为："+m)                                                # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
    if comp_number == 0:
        if player_choice == "纸" or player_choice == "史波克":               # 在屏幕上显示计算机选择的随机对象
            print("您赢了")
        elif player_choice == "剪刀" or player_choice == "蜥蜴":
            print("机器赢了")
        elif m == player_choice:
            print("您和计算机出的一样呢")                                      # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
    elif comp_number == 1:
        if player_choice =="纸" or player_choice == "蜥蜴":
            print("您赢了")
        elif player_choice == "石头" or player_choice == "剪刀":
            print("机器赢了")
        elif m == player_choice:
            print("您和计算机出的一样呢")
    elif comp_number == 2:
        if player_choice == "剪刀" or player_choice == "蜥蜴":
            print("您赢了")
        elif player_choice == "剪刀" or player_choice == "蜥蜴":
            print("机器赢了")
        elif m == player_choice:
            print("您和计算机出的一样呢")
    elif comp_number == 3:
        if player_choice == "剪刀" or player_choice == "石头":
            print("您赢了")
        elif player_choice == "纸" or player_choice == "史波克":
            print("机器赢了")
        elif m == player_choice:
            print("您和计算机出的一样呢")
    elif comp_number == 4:
        if player_choice == "石头" or player_choice == "史波克":
            print("您赢了")
        elif player_choice == "纸" or player_choice == "蜥蜴":
            print("机器赢了")
        elif m == player_choice:
            print("您和计算机出的一样呢")



print("欢迎使用RPSLS游戏")
print("----------------")
player_choice=input("请输入你的选择：")
if player_choice == "石头" or player_choice == "剪刀" or player_choice == "纸" or player_choice == "蜥蜴" or player_choice == "史波克":
    print(rpsls(player_choice))
else:
    print("Error:No Correct Name")



