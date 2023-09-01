def resources():
    while(True):
        name = input("Enter first product \t")
        price = int(input(f"Enter the price of {name}\t"))
        if(price==0):
            break;
resources()
