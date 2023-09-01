def UpiLInkGenerator(res="message",price=0,upi_address="don't know yet",  name="mohit"):    
# This is the main file where the code will be added and we can easily contribute here 
    address = upi_address
    cost = price
    nme = name
    return f"upi://pay?pa={upi_address}&pn={name}&cu=INR&tn={res}&am={cost}"
def resources(upi):
    while(True):
        i=1
        name = input(f"Enter {i} product \t")
        price = int(input(f"Enter the price of {name}\t"))
        if(price==0):
            break;
        link = UpiLInkGenerator(name,price,upi,"mohit")

        with open("file1.txt","a") as f:
            f.write(link)
            f.write("\n")
        i+=1
if __name__ == "__main__":
    upi = input("Enter your upi address : \t")
    resources(upi)