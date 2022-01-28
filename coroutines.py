import time


def reader():
    names = ["sagar", 'akash', 'pulkit', 'some name', 'skillf']
    time.sleep(5)
    while True:
        name = (yield)
        if name in names:
            print("name is present")
        else:
            print("name is not present")


a = reader()
next(a)
a.send('saga')
a.send('sagar')
a.send('s')
a.send('aga')
a.send('ga')
a.send('pulkit')
a.send('akash')
a.close()
