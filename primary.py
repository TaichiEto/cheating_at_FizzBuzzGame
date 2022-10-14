while True:
  try:
    i = int(input("i=?"))
    if i % 15 == 0:
      print("fizz buzz")
    elif i % 3 == 0:
      print("fizz")
    elif i % 5 == 0:
      print("buzz")
    else:
      print(i)
  except ValueError:
    #整数以外の値が入力された際の処理
    print ("ERROR")
