sk1={}
sk2={}
sk3={}
l=int(input("the damn legnth bro  "))
for i in range(l) :
    v1=int(input("feed me with a number for sk1  ")) 
    v2=int(input("feed me with a number for sk2  "))  
    k1=input("Caractère bro pour sk1")
    k2=input("Caractère bro pour sk2")
    sk1[k1]=v1
    sk2[k2]=v2
    if k1==k2 :
        v3=v1+v2
        sk3[k1]=v3
    else :
        sk3[k1]=v1
        sk3[k2]=v2    

print(sk1,sk2,sk3)
    
