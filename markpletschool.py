import math
a=25
b=1253.59
c='python'

'''print('Hello %s programming.'%c)
print('a = %d'%a)
print('b = %d'%b)
print('%s is easy'%c)
print('%d'%(b-100))
print('b = %f'%b)
print('%d %.2f'%(a,b))
print('You got a new job!? That\'s so exiting')
print('I don\'t have a car')
i=1
sum=0
n=int(input('Put round: '))
for i in range(n+1) :
    #print('I is %d'%i)
    #for sum in range(i):
    print('*'*i)
    i+=1
print('\n')
m=input('*')
j=int(input('Put round of * :'))
#for i in range(j):
print('%s'%m*j)

a=int(input('Enter a :'));b=int(input('Enter b : '));c=int(input('Enter c :'))
sum=(a+b+c)/3
print('AVG = : %.2f'%sum)

weight=int(input('Put your weight : '))
height=int(input('Put your height : '))
print('Your weight is %d and height is %d.'%(weight,height))

str1=input('Put 1 charactor :')
print('You put is %s'%str1)

a=int(input('Input A :'))
b=int(input('Input B :'))
print(a-b)

print('ทดสอบ')

a=int(input('A='))
b=int(input('B='))
print('%d'%(a+b))
#a=str(a)
#b=str(b)
print('%s%s'%(a,b))

midterm=float(input('Score midterm: '))
final=float(input('Score Final: '))
print('Total : %.1f'%(midterm+final))
print('Average : %.1f'%((midterm+final)/2))

width=float(input('Width : '))
height=float(input('Height : '))
depth=float(input('Depth : '))
cal=width*height*depth
minute=cal*15/60
print('Time to fill a pool is %.2f minutes.'%minute)

print('โปรแกรมช่วยคำนวนการตั้งราคาขายสินค้า ต้นทุน 35%')
cost=float(input('ระบุต้นทุนราคาขายเป็นบาท :'))
sell=cost/35*100
print('ราคาขาย ควรอยู่ที่ %.2f บาท'%sell)

n=int(input('Input n round: '))
char1=input('Put char1: ')
char2=input('Put char2: ')
a=n%2
result=(char1+char2)*(n//2)+(char1*a)
print('%s'%result)


a1=int(input('Put numerator of 1 '))
a2=int(input('Put denominator of 1 '))
b1=int(input('Put numerator of 2 '))
b2=int(input('Put denominator of 2 '))
sumation1=(a1*b2)+(b1*a2)
sumation2=a2*b2
print('Sumation of the two faction is %d/%d'%(sumation1,sumation2))

s1=int(input('Enter your exercise time 1 '))
s2=int(input('Enter your exercise time 2 '))
sum=s1+s2
hour=sum//3600
minute=(sum%3600)//60
second=(sum%3600)%60
print('It is %d hours %d minutes and %d seconds'%(hour,minute,second))

#print(abs(-44))
#print(pow(2,3))
#print(math.pi)
x=4
y=math.sqrt(16-4*x)
print(y)

a=1
t=1
u=1
s=(u*t)+(1/2*a*(pow(t,2)))
print(s)

b=4
a=4
c=4
x=-b+(math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
print(x)

a=float(input('Put float num1: '))
b=float(input('Put float num2: '))
print('A is %d and B is %d'%(math.ceil(a),math.ceil(b)))

r=int(input('Enter radius: '))
cal1=math.pi*pow(r,2)
cal2=2*math.pi*r
print('Area of a circle with radius %d is %.2f'%(r,cal1))
print('Circumference of a circle with radius %d is %.2f'%(r,cal2))

a=int(input('Enter A: '))
b=int(input('Enter B: '))
c=a
a=b
b=c
print('A = %d'%a)
print('B = %d'%b)

m=int(input('Month: '))
d=int(input('Day: '))
if m%3==0 and d>21 :
    if m<=3 :
        print('spring')
    elif m<=6 :
        print('summer')
    elif m<=9 :
        print('Fall')
    elif m<=12 :
        print('Winter')
else:
    if m<=3:print('Winter')
    elif m<=6:print('Spring')
    elif m<=9:print('Summer')
    elif m<=12:print('Fall')
    else:print('Something wrong')
    

#ข้อที่12
a=int(input('Put numer 2 digit: '))
b=str(a)
c1=b[0]
c2=b[1]
if c1==c2:
    print('ตัวเลขเหมือนกัน')
else:
    print('ตัวเลขต่างกัน')

#ข้อที่13
a=int(input('Put numer 2 digit: '))
b=str(a)
c1=b[0]
c2=b[1]
#c1=str(a[0])
#c2=str(a[1])
#print('a0=%s'%c1)
#print('a0=%s'%c2)
#print('a0=%s'%c1)
#print('a1=%s'%c2)
print(type(c1))
print(type(c2))
d1=int(c1)
d2=int(c2)
cal=d1-d2
print(type(cal))
if cal>0:
    print('เลขโดดหลักสิบมากกว่าหลักหน่วยอยู่ %d'%cal)
elif cal<0:
    print('เลขโดหลักสิบน่อยกว่าหลักหน่วยอยู่ %d'%cal)
else:
    print('ผลต่างเท่ากับศูนย์')

if c1>c2:
    print('เลขโดดหลักสิบมากกว่าหลักหน่วย')
elif c1<c2:
    print('เลขโดดหลักสิบน้อยหลักหน่วย')
else:
    print('เท่ากัน')


a=int(input('A: '))
b=int(input('B: '))
c=int(input('C: '))
maximum=max(a,b,c)
print('Max is %d'%maximum)

c=int(input('Enter C: '))
f=((9/5)*c)+32
k=c+273.15

func=(input('What fucntion you want to change to (F or f farenhi ) or (K or k Kelvin): '))
if func == 'F' or func =='f':
    print('Farenhigh is %.2f'%f)
elif func =='K' or func =='k':
    print('Kelvin is %.2f'%k)
else:
    print('You put wrong function.')

#BMI
weight=float(input('Enter you weight in Kg.: '))
height=float(input('Enter you height in Mate.: '))
bmi=weight/pow(height,2)
print('Your BMI is %.1f'%bmi)
if bmi < 18.5 :
    print('Underweight')
elif bmi < 25 :
    print('Normal weight')
elif bmi < 30 :
    print('Over weight')
else:
    print('Obesity')

#Discount
price=float(input('Enter your buy: '))
if price >= 1000 :
    if price >=1000 and price<3000:
        dis=0.1
    else:
        dis=0.15
    pay=price-(price*dis)
    print('Amount due after discount is %.2f baht'%pay)

else:
    print('No discount.')

#โปรแกรมร้านอาหาร Japan and Korean
menu=input('Enter you buffet choice [J is Japan] and [K is Korean]')
day=(input('Is today wednesday \(yes or no\)'))
j=1000
k=1500
if menu=='J' or menu=='j':
    if day=='yes':
        dis=0.15
    else:
        dis=0
    pay=j-j*dis
    print('Your payment is %.2f baht'%pay)
elif menu=='K' or menu=='k':
    if day=='yes':
        dis=0.15
    else:
        dis=0
    pay = k - k*dis
    print('Your payment is %.2f baht' % pay)
else:
    print('You put wrong menu')

#โปรแกรมร้านค้า
tv=6000
dvd=1500
audio=3000
btv=int(input('How many Tvs: '))
bdvd=int(input('How many Dvds: '))
baudio=int(input('How many Audios: '))
stv=tv*btv
sdvd=dvd*bdvd
saudio=audio*baudio
sum=stv+sdvd+saudio
dis=0
total=sum-sum*dis
if sum >= 24000:
    dis=0.2
    total = sum - sum * dis

print('Total price is %.2f baht'%sum)
print('Your payment is %.2f baht'%total)


i=-30
while True:
    if i<=30 :
        print(abs(i))
        i+=10
        continue
    break

i=int(input('Round : '))
j=0
while True:
    if j<=i:
        print(j)
        j+=1
    else:
        i = int(input('Round : '))
        j=0
    continue



summ=0
stack=[]
while True:
    p=int(input('Put number: '))
    if p>0:
        summ+=p
        stack.append(p)
    else:
        print('Total is %.2f' % summ)
        print(stack)
        maxx=max(stack)
        print('Max is %d'%maxx)
        break
    continue

a=int(input('Put num: '))
b=str(a)
print('%s'%b[2])
print('%s'%b[1])
print('%s'%b[0])

j=0
while True:
    i=int(input('put num: '))
    if i>0:
        if i%2>0:
           j+=1
        continue

    else:
        print('odd is %d' % j)

first=0
see=1
i=int(input('Put height of building: '))
first=i
while True:
    j=int(input('Put height of building: '))
    if j>-1 :
        if first < j:
            see+=1
            print('see = %d'%see)
    else:
        print('See is %d'%see)
        break

#คำนวนคะแนนโบว์ลิง
i=1
r=0
score=0
sum_score=0
score_temp=0

while i<11 :
        print('Frame # %d' % i)
        if score_temp <10 and r<2:
            score = int(input('Number of pins dows: '))
            score_temp+=score
            r+=1
            if r==2 and score_temp<10:
                sum_score+=score_temp
                score_temp=0
                r=0
                i+=1
            continue
        else:
            sum_score+=10
            print('Sum_Score = %d'%sum_score)
            score_temp=0
            r=0
            i+=1
        continue

print('Score is %d'%sum_score)

#ตรวจสอบว่าจำนวนที่รับเข้ามาเป็นจำนวนเฉพาะหรือไม่
n=int(input('Put number: '))
ss=''
i=0
j=0
for i in range(n):
    if i%2>0:
        ss+=str(i)+','
        j+=1
print('Number static is %d.'%j)
print('That number is %s'%ss)

#factorial
f=int(input('Put number for make factorial: '))
sum=1
for i in range(f,1,-1):
    sum*=i

print('Factorial is %d'%sum)


#แม่สูตรคููณ1
m=int(input('Input mother: '))
#m+=1
for i in range(2,m+1,1):
    print('Mother %d'%i)
    for j in range(1,13,1):
            mul=i*j
            print('%d x %d = %d'%(i,j,mul))

#แม่สูตรคููณ2
m=int(input('Input mother: '))
print('Mother %d'%m)
for j in range(1,13,1):
    mul=m*j
    print('%d x %d = %d'%(m,j,mul))
    
 #ทดสอบFor   
for i in range(1,101,2):
    print(i)

'''
