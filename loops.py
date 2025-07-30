try:
    for counter in range(1,10, 2):
        print(counter)
        print("Looping through the range in reverse order")
except Exception as e:
    print("An error occurred:", e)

    for x in range(10, 0, -1):
        if x==3:
            continue
        else:
            if x==5:
                break
        print(x)
        print("Looping through the range in reverse order")