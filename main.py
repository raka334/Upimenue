# This is the main file where the code will be added and we can easily contribute here 
a = input("Enter your upi address")
b = input ("Enter your price ")
c= input("Enter your Name")
print(f"upi://pay?pa={a}&pn={c}&cu=INR&am={b}")