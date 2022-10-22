while True:
    try:
        i_str = input("i=?")
        if i_str == "exit":
            #input "exit" to exit this script
            break
        else:
            i = int(i_str)
    except ValueError:
        print("ERROR")
    else:
      if i % 15 == 0:
        print("fizz buzz")
      elif i % 3 == 0:
        print("fizz")
      elif i % 5 == 0:
        print("buzz")
      else:
        print(i)