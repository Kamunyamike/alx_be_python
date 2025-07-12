#Global scope
x = "XGlobal"

#Local scope
def outer():
    global x
    x = "Outer_X"
    print(x)
    def inner():
        x = "Inner_X"
        print(x)
    inner()
outer()
print(x)


#The LEGB rule applied in the sense that the code executed first begins with the local scope,
# where the outer scope is first printed out then the function thet is enclosed within the local scope is executed.
#Finally, the Global scope is executed but having redefined its narrative, it nolonger functions as an independent variable but as a redefined tool.
#The execution therefore borrows a LEGB rule.