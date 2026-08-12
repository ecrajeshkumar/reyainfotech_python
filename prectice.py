for i in range(3):
    for j in range(3):
        if j == 2:
            break
    else:
        print("Inner Done")
else:
    print("Outer Done")