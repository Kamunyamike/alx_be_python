#Global scope
x = "Mike"

#local scope
def outer():
    x = "Mike"
    print(x)
    def inner():
        x = "Mike"
        print(x)
    inner()
outer()
print(x)