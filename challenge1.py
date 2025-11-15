num = int(input("Enter a number : "))
if num <=0:
  print('enter a positive number')
else:
  n=num
  sum=0
  count=0 
  while n > 0:
    count  +=1
    n//=10
  # print(count)
  
  n = num
  while n > 0:
    number=n%10
    sum= sum + number ** count
    n = n//10 
    

  # print(number)
  # print(sum)
  if num == sum:
    print (num,'is armstrong')
  else:
    print (num, 'is not armstrong ')


