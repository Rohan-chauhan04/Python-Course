sub1=int(input('enter marks in first subject  '))
sub2=int(input('enter marks in second subject  '))
sub3=int(input('enter marks in third subject   '))
if(sub1<33 or sub2<33 or sub3<33):
    print('you are fail')
elif(sub1+sub2+sub3)/3<40:
    print('you are fail')
else:
    print('you are pass')
