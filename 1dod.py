x = input("wprowadz litere: ")
if len(x)>1 or len(x)==0:
    print("blad")
    exit()
if ord('a')<= x <=ord('z'):
    print("litera jest małą")
elif ord('A') <= x <=ord('Z'):
    print("li   tera jest duza")
else:
    print('to nie jest litera')