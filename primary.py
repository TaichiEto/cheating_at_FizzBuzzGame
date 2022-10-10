while True:
  try:
    i = int(input("i=?"))
    if i % 15 == 0:
      print("fizz buzz")
    elif i % 3 == 0:
      print("fizz")
    elif i % 5 == 0:
      print("buzz")1
    else:
      print(i)
  except ValueError:
    print ("エラー：数字以外の文字を入力しないでください。")
