str = input("Please enter a string: ")
vowels = 0
consonants = 0
for i in str:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels+1
    else:
        consonants = consonants+1
print("The number of vowels:", vowels)
print("The number of consonants:", consonants)