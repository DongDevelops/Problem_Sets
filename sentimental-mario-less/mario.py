height = input("Height: ")
while True:
    if 0 < height and height < 9:
        for i in height:
            print("#")
    else:
        input("Height: ")