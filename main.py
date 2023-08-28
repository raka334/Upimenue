def UpiLInkGenerator(upi_address="don't know yet", price=0, name="unknown"):    
# This is the main file where the code will be added and we can easily contribute here 
    address = upi_address
    cost = price
    nme = name
    return f"upi://pay?pa={upi_address}&pn={nme}&cu=INR&am={cost}"


if __name__ == "__main__":
    link = UpiLInkGenerator(nupurkaushiknk@oksbi,600,"Nupar")
    print(link)