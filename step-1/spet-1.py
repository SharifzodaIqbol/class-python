def scope_test():
    def do_local():
        spam = "local spam"

    def do_nolocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("after local assignment:", spam)
    do_nolocal()
    print("after nonlocal assignment:", spam)
    do_global()
    print("after global assignment:", spam)
scope_test()
print("In global scope:", spam)
'''
after local assignment: test spam
after nonlocal assignment: nonlocal spam
after global assignment: nonlocal spam
In global scope: global spam
'''