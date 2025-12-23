name = "harry" #String are immutable

# name[0] = "R" # You cannot do this

a = len(name)
print(a)
print(name.upper(), a)
print(name.lower(), a)
print(name.capitalize(), a)

#strip() ,  #find(), #replace(), 

text = "Apples, Bananas, Pineapples"
print(text.split(","))
print(",".join(['Apples', ' Bananas', ' Pineapples']))

#isalpha(), #isdigit(), #isalnum(), #isspace()