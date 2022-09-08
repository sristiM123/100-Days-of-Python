#Write your code below this line 👇
def prime_checker(number):
  prime=True
  for a in range (1, number):
    if (number%a==0):
      prime=False
  if prime:
    print("this a prime number")
  else:
    print("this is not prime number")
    
#Write your code above this line 👆
 
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
