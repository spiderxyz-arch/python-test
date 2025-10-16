def translator(phrase):
   translation="" 
   for letter in phrase:
     if letter in "aeiou":
         translation  = translation + "M"
     elif letter in "AEIOU":
        tranlastion  = translation + "m"

     else:
         translation = translation + letter
   return translation

print(translator(input("Enter your phrase:"))) 