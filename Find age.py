b_year =int(input("Enter the year of birth :"))
p_year = int(input("Enter the present year :"))
age = p_year - b_year

if age >=13 and age <=19:
    print("Teenage")
elif age >=20 and age <=29:
    print("Twenties")
