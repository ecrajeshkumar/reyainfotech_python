
def count_up_to(n):
    i = 1
    while i <= n:
        print("before yield", i)
        yield i
        print("yield generate value i and return to called function count_up_to and save in num and print value and continue again after yield statement ")
        print("before increment", i)
        i += 1
        print("after increment", i)

for num in count_up_to(5):
    print("inside for", num)



