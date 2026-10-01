gx = 100

def func1():
    print(gx)

def func2():
    global gx
    gx = 200
    print(gx)

func1()
func2()
print(gx)


gx = 100

def func1():
    global gx
    print(gx)

func1()
