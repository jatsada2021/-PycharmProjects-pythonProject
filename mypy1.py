honda='Accord'
toyota='Yaris'
k=a,b,c='Tik','Kim','Lars'
d=['Red','Blue','Dark']
e=1,2,3
t='Jatsada Chamnanprai'
aa = ["red", "big", "tasty"]
bb = ["apple", "banana", "cherry"]
def showcar():
    z=honda + toyota
    print('I have 2 car is ' + z)

showcar()

print('I have 2 cars is '+honda+' and '+toyota)
print(a+b+c)
print (t.upper())
print(d[0:2])
for i in range(len(d)):
    print('I = ' + str(i))
    print(d[i])

for j in range(2,13):

  print('Mother = ' + str(j))

  for k in range(1,13):

    print(str(j)+'X'+str(k)+'='+ str(j*k))

for l in aa:
    for m in bb:
        print(l,m)




