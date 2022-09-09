n = int(input("Informe um numero :"))
for j in range(1,n+1):
    primo = 0
    for i in range(1,n+1):
        if(j%i==0):
            primo += 1
    if(primo==2):
        print(f"{j}",end='-')