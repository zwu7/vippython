import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择\n'))
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
    student_list = []
    while True:
        id = input('请输入ID（如1001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break

        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入：')
            continue
        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y':
            continue
        else:
            break

    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕！！！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for iterm in student:
                    d = dict(eval(iterm))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学员信息')


def show_student(lst):
    if len(lst) == 0:
        print('每有查询到学生信息，无数据显示！！！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))))


def delete():
    while True:
        student_id = input('请输入要删除的学生的id：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        dict(eval(item))  # 将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'ID为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除之后要重新显示所有学生信息
            answer = input('是否继续删除？y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return

    student_id = input('请输入要修改的学员的ID: ')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for iterm in student_old:
            d = dict(eval(iterm))
            if d['id'] == student_id:
                print('找到学生信息，可以修改其相关信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['python'] = input('请输入Python成绩：')
                        d['java'] = input('请输入Java成绩：')
                    except:
                        print('您的输入有误，请重新输入！！！')
                        continue
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！！！')
            else:
                wfile.write(str(d) + '\n')
    answer = input('是否继续修改其他学生的信息？y/n\n')
    if answer == 'y':
        modify()


def sort():
    pass


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息......')


def show():
    pass


if __name__ == '__main__':
    main()
