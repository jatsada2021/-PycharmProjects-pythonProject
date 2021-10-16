def printname(*adult):
    print('Your name is '+adult[0]+'and surname is '+adult[1])

#printname('Tik')
#printname('Khim')
printname('Jatsada','Chamnanprai.')

def addinfo (*data):
    for j in data:
        print(j)

grade=['A','B','C','D']
addinfo(grade)
def putdata (ans):
    if ans == 'y' :
      opn= open("test1",'r+')
      print('')
      print(opn.read())
      inp=input('Write some thing now >>')
      answ=input('Do you want to save ?. y or n')
      if answ == 'y':
            opn.write('\n')
            opn.write(inp)
            print('Add wording successed is '+inp)
      elif ans == 'n':
            print('You just cancled.')
            return()
      else :
           print('Please put correct choice. y or n ')

    elif ans == 'n':
         print('You no to write a file.')
         print('Thank you.')
    else:
        ans=input('You put wrong choice .You want to add some word to file? y or n : ')
        putdata(ans)

ans = input('You want to add some word to file? y or n : ')
putdata(ans)
#Today test to setup a git



