def UpiLInkGenerator(upi_address="don't know yet", price=0, name="mohit",res="message"):    
# This is the main file where the code will be added and we can easily contribute here 
    address = upi_address
    cost = price
    nme = name
    return f"upi://pay?pa={upi_address}&pn={name}&cu=INR&tn={res}&am={cost}"
def resources():
    while(True):
        i=1
        name = input(f"Enter {i} product \t")
        price = int(input(f"Enter the price of {name}\t"))
        if(price==0):
            break;
        link = UpiLInkGenerator("dwivedimohit2001-1@oksbi",price,"mohit",name)
        with open("file1.txt","a") as f:
            f.write(link)
            f.write("\n")
        i+=1
if __name__ == "__main__":
    resources()