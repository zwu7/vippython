def find_answer(question):
    with open('reply.txt', 'r', encoding='gbk') as file:
        while True:
            line = file.readline()
            if not line:  # if line == '', 到文件末尾退出
                break
            # 字符串的分割
            keyword = line.split('|')[0]
            reply = line.split('|')[0]
            if keyword in question:
                return reply


if __name__ == '__main__':
    question = input('Hi，您好，小秘在此等主人很久了，有什么烦恼快和小米说吧')
    while True:
        if question == 'bye':
            print('小主再见')
            break
        # 开始在文件中查找
        reply = find_answer(question)
        if not reply:  # 如果回复的是false，not false == True:
            question = input('小蜜不知道你在说什么，您可以问一些关于订单、物流、账户、支付等问题，（退出请输入bye）')
        else:
            print(reply)
            question = input('小主，您还可以继续问一些关于订单、物流、账户、支付的问题（退出请输入bye）')
