
from asyncio.windows_events import NULL


while True:
  
  str_i = input("i=?")
  if not str_i:
    print("数字いれろや!")
    
  else:
    

    i = int(str_i)

    #fizz buzz ゲームもどき
    
    if i % 15 == 0:
      print("fizz buzz")
    elif i % 3 == 0:
      print("fizz")
    elif i % 5 == 0:
      print("buzz")
    
    else:
    

      print(i)
