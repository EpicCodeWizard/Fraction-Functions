import os
while True:
  print("Hello. Thank you for using fraction functions. Please input the corresponding number to the function you want.\n1 - Fraction Adder\n2 - Fraction Subtractor\n3 - Fraction Multiplier\n4 - Fraction Divider\n5 - Fraction Simplifier\n6 - Fraction to Decimal Converter\n7 - Same Repeating Decimal to Fraction Converter")
  try:
    grand = int(input())
  except ValueError:
    print("You have not entered a number.")
    input()
  
  if grand == 1:
    from math import *
    try:
      numerator = int(input("Please input your the numerator of your 1st fraction. "))
      denominator = int(input("Please input your the denominator of your 1st fraction. "))
      numerator2 = int(input("Please input your the numerator of your 2nd fraction. "))
      denominator2 = int(input("Please input your the denominator of your 2nd fraction. "))
    except ValueError:
      print("You have not entered a valid number.")
      input()
    if denominator == 0:
      print("Addition with 0 as the denominator isn't possible.")
      input()
    elif denominator2 == 0:
      print("Addition with 0 as the denominator isn't possible.")
      input()
    goodnum = denominator2 * numerator
    goodden = denominator2 * denominator
    goodnum2 = denominator * numerator2
    goodden2 = denominator * denominator2
    finalnum = goodnum + goodnum2
    finalfrac = str(finalnum) + "/" + str(goodden2) + "."
    print("The unsimplified result is",finalfrac)
    commondivisor = gcd(finalnum,goodden2)
    smallestnum = finalnum/commondivisor
    smallestden = goodden2/commondivisor
    a = str(smallestnum) + "/" + str(smallestden)
    y = a + "."
    print("The simplified result is",y)
    print()
    input()
  
  elif grand == 2:
    from math import *
    try:
      numerator = int(input("Please input your the numerator of your 1st fraction. "))
      denominator = int(input("Please input your the denominator of your 1st fraction. "))
      numerator2 = int(input("Please input your the numerator of your 2nd fraction. "))
      denominator2 = int(input("Please input your the denominator of your 2nd fraction. "))
    except ValueError:
      print("You have not entered a valid number.")
      input()
    if denominator == 0:
      print("Subtraction with 0 as the denominator isn't possible.")
      input()
    elif denominator2 == 0:
      print("Subtraction with 0 as the denominator isn't possible.")
      input()
    goodnum = denominator2 * numerator
    goodden = denominator2 * denominator
    goodnum2 = denominator * numerator2
    goodden2 = denominator * denominator2
    finalnum = goodnum - goodnum2
    finalfrac = str(finalnum) + "/" + str(goodden2) + "."
    print("The unsimplified result is",finalfrac)
    commondivisor = gcd(finalnum,goodden2)
    smallestnum = finalnum/commondivisor
    smallestden = goodden2/commondivisor
    a = str(smallestnum) + "/" + str(smallestden)
    y = a + "."
    print("The simplified result is",y)
    print()
    input()
  
  elif grand == 3:
    from math import *
    try:
      numerator = int(input("Please input your the numerator of your 1st fraction. "))
      denominator = int(input("Please input your the denominator of your 1st fraction. "))
      numerator2 = int(input("Please input your the numerator of your 2nd fraction. "))
      denominator2 = int(input("Please input your the denominator of your 2nd fraction. "))
    except ValueError:
      print("You have not entered a valid number.")
      input()
    answerup = (numerator) * (numerator2)
    answerdown = (denominator) * (denominator2)
    z = str(answerup) + "/" + str(answerdown) + "."
    print("The unsimplified result is",z)
    if answerdown == 0:
      print("Simplification with 0 as the denominator isn't possible.")
      input()
  
    commondivisor = gcd(answerup,answerdown)
    smallestnum = answerup/commondivisor
    smallestden = answerdown/commondivisor
    a = str(smallestnum) + "/" + str(smallestden)
    y = a + "."
    print("The simplified result is",y)
    print()
    input()
  
  elif grand == 4:
    from math import *
    try:
      numerator = int(input("Please input your the numerator of your 1st fraction. "))
      denominator = int(input("Please input your the denominator of your 1st fraction. "))
      numerator2 = int(input("Please input your the numerator of your 2nd fraction. "))
      denominator2 = int(input("Please input your the denominator of your 2nd fraction. "))
    except ValueError:
      print("You have not entered a valid number.")
      input()
    
    answerup = (numerator) * (denominator2)
    answerdown = (denominator) * (numerator2)
    z = str(answerup) + "/" + str(answerdown) + "."
    print("The unsimplified result is",z)
    
  
    if answerdown == 0:
      print("Simplification with 0 as the denominator isn't possible.")
      input()
  
    commondivisor = gcd(answerup,answerdown)
    smallestnum = answerup/commondivisor
    smallestden = answerdown/commondivisor
    a = str(smallestnum) + "/" + str(smallestden)
    y = a + "."
    print("The simplified result is",y)
    print()
    input()
  
  elif grand == 5:
    from math import *
    try:
      numerator = int(input("Please input your numerator. "))
      denominator = int(input("Please input your denominator. "))
    except ValueError:
      print("You have not entered a valid number.")
      input()
  
    if denominator == 0:
      print("Simplifiction by zero is not possible.")
      input()
  
    commondivisor = gcd(numerator,denominator)
    smallestnum = numerator/commondivisor
    smallestden = denominator/commondivisor
    a = str(smallestnum) + "/" + str(smallestden)
    z = a + "."
    print("The simplified fraction is",z)
    print()
    input()
  
  elif grand == 6:
    from math import *
    try:
      numerator = int(input("Please input your numerator. "))
      denominator = int(input("Please input your denominator. "))
    except ValueError:
      print("You have not entered a valid number.")
      input()
    z = str(numerator/denominator) + "."
    print("The decimal of the fraction you entered is",z)
    print()
    input()
  
  elif grand == 7:
    from math import *
    try:
      number = int(input("Please input the two digits or your repeating decimal. Examples:\nFor 0.5757575757 you would input 57.\nFor 0.9999999999 you would input 99.\n"))
    except ValueError:
      print("You have not entered a number.")
      input()
  
    if len(str(number)) != 2:
      print("You have not entered two digits.")
      input()
  
    commondivisor = gcd(number,99)
    smallestnum = number/commondivisor
    smallestden = 99/commondivisor
    a = str(smallestnum) + "/" + str(smallestden)
    z = a + "."
    print("Your fraction is",z)
    print()
    input()
  os.system("clear")
