startingnumber = int(input("enter a starting number"))
endingnumber = int(input("enter a ending number"))
print(f"prime number between {startingnumber} and {endingnumber} are")
for i in range (startingnumber,endingnumber+1):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i)