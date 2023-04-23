test = "HelloWorld!"

def stringTest(ind):
    global test
    if test[ind] == 'l':
        print("Doing nothing")
    else:
        test = f"{test[:ind]}L{test[ind+1:]}"
        print(test)


for i in range(len(test)):
    stringTest(i)

input("Press ENTER to quit!")