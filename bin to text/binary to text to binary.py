"""
Title:
        Text To binary program
        And
        Binary To Text Program

Author:
        Shreyas Om
"""


def numtobin(n):  #To Change A Number To Binary
    s=""
    while n>0:
        r=n%2
        n=n//2
        s=str(r)+s
    return(s)



def bintonum(b):   #To Change A Binary String To Number
    n=0
    fn=0
    while len(list(b))!=0:
        fn=fn+((2**n)*(int(b[-1])))
        b=b[:-1]
        n=n+1
    return fn



def texttobin(file_name):   #To change text to binary
    fn=file_name
    
    f=open(fn,"r")    #Taking Data from the file to list fd
    d=f.read()
    fd=list(d)
    f.close()
    
    f=open(fn,"w")    #Removing existing data from the file
    f.close()
    
    f=open(fn,"a")    #Adding converted data to file
    for i in fd:
        f.write(numtobin(ord(i)))
        f.write(" ")
        
    print("task done") 
    f.close()



def bintotext(file_name):      # To Change binary to text
    fn=file_name
    
    f=open(fn,"r")      #Taking data from the file
    d=f.read()
    d=d.split(" ")
    f.close()
    
    f=open(fn,"w")      #Removing existing data from the file
    f.close()
    
    f=open(fn,"a")      # Adding converted data to file
    for i in d:
        f.write(chr(bintonum(i)))
    f.close()
    print("task done")