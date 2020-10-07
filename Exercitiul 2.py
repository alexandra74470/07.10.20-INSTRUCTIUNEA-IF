v1=int(input("introdu varsta primului copil"))
v2=int(input("introdu varst la al doilea copil"))
if v1>v2:
    print("primul copil este mai mare cu",v1-v2,"ani")
elif v1<v2:
    print("al doila copil este mai mare cu",v2-v1,"ani")
else:
    print("copiii au aceeasi varsta")