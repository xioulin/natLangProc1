try:
    name=input('what is your name?')
except EOFError:
    print('this is EOF exception, write name again')
except KeyboardInterrupt:
    print('lala')
else:
    print('hey there')