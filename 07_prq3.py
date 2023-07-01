text=input('Enter a text\n')
if('make money online'in text):
    spam=True
elif('click this'in text):
    spam=True
elif('make money'in text):
    spam=True
elif('subscribe now'in text):
    spam=True
else:
    spam=False

if(spam):
    print('this is a spam')
else:
    print('this is not a spam')