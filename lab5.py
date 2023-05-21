'''import datetime as t
s=print(t.datetime.now())
import datetime
s=datetime.datetime.now()
print(s+datetime.timedelta(days=2))
f=open("C:\\Users\\anike\\OneDrive\\Desktop\\Python\\abc.txt","w")
f.write("Hello Python Programmming")
f.close'''
import os 
anni=os.listdir(r"C:\Users\anike\OneDrive\Desktop\2nd")

try:
    for i in anni:
        try:    
            f=open(f"C:\\Users\\anike\\OneDrive\\Desktop\\2nd\\{i}","rb")
            x=f.read()
            f2=open(f"C:\\Users\\anike\\OneDrive\\Desktop\\Python\\{i}","wb")
            f2.write(x)
            f.close()
            f2.close()
        except:
            print("Aniket")
except:
    print("fuck")
else:
    print("nice")
