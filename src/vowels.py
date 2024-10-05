str = input("enter a string: ").lower()
vowels = 0
consonants=0

for ch in str:
    if ch in "aeiou":
        vowels+=1
    else:
        consonants+=1    
   
print(f"Vowels: {vowels} \nConsonants: {consonants}")            

