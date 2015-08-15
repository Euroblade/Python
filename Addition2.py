"""
Your code was good I just enhanced it a bit for you so you can keep calling
the input statements which let you choose any numbers to summarize.
Also added a for loop so you can consistently add numbers until you close the
program yourself.

"""


while True:
    print "Choose two numbers in order to summarize them."
    x = input("Choose your first number please.")
    y = input("Choose your second number please.")
    def summarize(x,y):
        result = x,y
        return sum(result)
    number = summarize(x,y)
    print "the sum of {0} and {1} is {2}".format(y,x,number)
    print "-----------------------------"
