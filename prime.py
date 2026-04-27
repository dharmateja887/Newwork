for i in range(2,101):
    W=True
    for j in range(2,i):
        if i%j==0:
            W=False
    if W:
        print(i)
