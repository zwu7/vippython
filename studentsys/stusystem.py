def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in range(8):
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 录入学生信息
            elif choice == 3:
                delete()  # 录入学生信息
            elif choice == 4:
                modify()  # 录入学生信息
            elif choice == 5:
                sort()  # 录入学生信息
            elif choice == 6:
                total()  # 录入学生信息
            elif choice == 7:
                show()  # 录入学生信息


def menu():
    print('=' * 20 + '学生信息管理系统' + '=' * 21)
    print('-' * 24 + '功能菜单' + '-' * 24)
    print('\t' * 5 + '1. 录入学生信息')
    print('\t' * 5 + '2. 查找学生信息')
    print('\t' * 5 + '3. 删除学生信息')
    print('\t' * 5 + '4. 修改学生信息')
    print('\t' * 5 + '5. 排序')
    print('\t' * 5 + '6. 统计学生总人数')
    print('\t' * 5 + '7. 显示所有学生信息')
    print('\t' * 5 + '0. 退出系统')
    print('-' * 55)


def insert():
    pass


def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    main()