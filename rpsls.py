#coding:gbk
"""
����Ŀ�ģ�Rock-paper-scissors-lizard-Spock
�������ߣ�����
"""

import random


def number_to_name(number):                                                # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    if number == 0:                                                        #������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
        return "ʯͷ"
    elif number == 1:
        return "ʷ����"
    elif number == 2:
        return "ֽ"
    elif number == 3:
        return "����"
    elif number == 4:
        return "����"

    def name_to_number(name):
        if name == "ʯͷ":
            return 0
        elif name == "ʷ����":
            return 1
        elif name == "ֽ":
            return 2
        elif name == "����":
            return 3
        elif name == "����":
            return 4
def rpsls(player_choice):
    comp_number = random.randrange(0, 5)                                    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    m = number_to_name(comp_number)                                         # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    print("--------")                                                       # ���"-------- "���зָ�
    print("����ѡ��Ϊ:"+str(player_choice))                                   # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    print("�������ѡ��Ϊ��"+m)                                                # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    if comp_number == 0:
        if player_choice == "ֽ" or player_choice == "ʷ����":               # ����Ļ����ʾ�����ѡ����������
            print("��Ӯ��")
        elif player_choice == "����" or player_choice == "����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͼ��������һ����")                                      # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
    elif comp_number == 1:
        if player_choice =="ֽ" or player_choice == "����":
            print("��Ӯ��")
        elif player_choice == "ʯͷ" or player_choice == "����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͼ��������һ����")
    elif comp_number == 2:
        if player_choice == "����" or player_choice == "����":
            print("��Ӯ��")
        elif player_choice == "����" or player_choice == "����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͼ��������һ����")
    elif comp_number == 3:
        if player_choice == "����" or player_choice == "ʯͷ":
            print("��Ӯ��")
        elif player_choice == "ֽ" or player_choice == "ʷ����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͼ��������һ����")
    elif comp_number == 4:
        if player_choice == "ʯͷ" or player_choice == "ʷ����":
            print("��Ӯ��")
        elif player_choice == "ֽ" or player_choice == "����":
            print("����Ӯ��")
        elif m == player_choice:
            print("���ͼ��������һ����")



print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
player_choice=input("���������ѡ��")
if player_choice == "ʯͷ" or player_choice == "����" or player_choice == "ֽ" or player_choice == "����" or player_choice == "ʷ����":
    print(rpsls(player_choice))
else:
    print("Error:No Correct Name")



