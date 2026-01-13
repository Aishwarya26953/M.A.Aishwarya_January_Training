def count_message(msg, count=0):
    # Each time this function is called,
    # the default value of count starts from 0 again
    count = count + 1
    print("Message:", msg)
    print("Count:", count)
    return count
count_message("Hey")
count_message("Hello")
count_message("Welcome")

#the count is start with 0(default)
#count is not increase because count is integer and integers are immutable in python 