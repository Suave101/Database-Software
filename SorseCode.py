print('Welcome to Project Mesenger')
o = 1
while o == 1:
    yn = input('Leave a message, or read messages? (L/R)')
    if yn == 'R':
        with open('Launch_Code.txt') as f:
            rd = f.readlines()
        print(rd)
    elif yn == 'L':
        with open("Launch_Code.txt", "w") as f:
            f.write("{}".format(input('Message: ')))
    else:
        print('Invalid Input')
        if input('Do you want to continue?(Y/N)') == 'N':
            o = 0
