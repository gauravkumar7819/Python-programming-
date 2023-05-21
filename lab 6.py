
try:
    with open(r"C:\Users\anike\OneDrive\Desktop\2nd\Ancient Indias Documentary_360p.mp4","rb") as anni:
        data=anni.read()
        try:
            with open(r"C:\Users\anike\OneDrive\Desktop\Python\science.txt","w") as file:
                file.write(str(data))
            with open(r"C:\Users\anike\OneDrive\Desktop\pooopy.bin","wb") as file:
                file.write(data)
            with open(r"C:\Users\anike\OneDrive\Desktop\pooopy.bin","rb") as file:
                wp=file.read()
            with open(r"C:\Users\anike\OneDrive\Desktop\pooopy.mp4","wb") as file:
                file.write(wp)
        except:
            print("data not written")




except:print("cant read")
else:print("done bro")
finally:print("thanku and get out")