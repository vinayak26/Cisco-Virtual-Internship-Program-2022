Info=[]
def DtH(n):
    return hex(int(n))
def DtO(n):
    return oct(int(n))
def DtB(n):
    return bin(int(n)).replace("0b","")
for i in range(10):
    IP=input("Enter IPv4 address\n")
    IP=IP.split(".")
    if(len(IP)!=4):
        print("Invalid IP address")
        continue
    for i in IP:
        if(int(i)<0 or int(i)>255):
            print("Invalid IP address")
            break
    else:
        IPd=".".join(IP)
        IPb=list(map(DtB,IP))
        IPb=".".join(IPb)
        IPo=list(map(DtO,IP))
        IPo=".".join(IPo)
        IPh=list(map(DtH,IP))
        IPh=".".join(IPh)
        Info=[IPd,IPb,IPo,IPh]
        with open("conversion.txt","a+") as f:
            f.write(str(Info)+"\n")
        Info=[]

with open("conversion.txt","r") as f:
    OP=f.readlines()
    for i in range(10):
        print("The "+i+1+" IP address in Decimal Binary Octal and Hexadecimal is"+str(OP[i]))