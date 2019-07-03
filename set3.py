import re
vowel = ['a','e','i','o','u']
str = input()
if re.match(r'[a-z]', str , re.I):
   if str in vowel:
      print("Vowel")
   else:
      print("Constant")
 else:
     print("invalid")
  
