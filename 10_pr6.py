mark=int(input('Enter your mark\n'))
if mark>=90:
    grade="A+"
elif mark>=80:
    grade='A'
elif mark>=70:
    grade='B'
elif mark>=60:
    grade='C'
elif mark>=50:
    grade='D'
else:
    grade='F'

print('Your grade is '+grade)
