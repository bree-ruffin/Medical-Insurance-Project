# create the initial variables below
# age of the individual in years
age = 28
#0 for female, 1 for male
sex = 0
#individual's body mass index
bmi = 26.2
# number of children the individual has
num_of_children = 3
# 0 for a non-smoker, 1 for a smoker 
smoker = 0
# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# insurance string
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age += 4

#new insurance quote
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# difference between the original quote and adjusted 
change_in_insurance_cost = new_insurance_cost - insurance_cost

#the difference 
print("The change in cost of insurance after increasing the age by 4 years is " + str(new_insurance_cost) + " dollars")
# BMI Factor
#reset age factor
age = 28 
# increased bmi by 3.1
bmi += 3.1
# redefined new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# differnece between original and new cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
# print difference statement
print("The change in estimated insurance cost after increasing BMI by 3.1 is  " + str(change_in_insurance_cost) + " dollars.")


# Male vs. Female Factor
#reseting bmi to original 
bmi = 26.2
# changing sex
sex = 1
#adjusted insurance quote
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# difference bewtween original price quote and adjusted
change_in_insurance_cost = new_insurance_cost - insurance_cost
# print adjusted statement 
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars")

# smoker vs. non smoker
#reseting gender
sex = 0
#adjusting smoker
smoker = 1
#adjusting insurance quote 
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
#difference between original price quote and adjusted
change_in_insurance_cost = new_insurance_cost - insurance_cost
#print adjusted statement
print("The change in estimated cost for being a smoker instead of a nonsmoker is " + str(change_in_insurance_cost) + " dollars")

# Having children vs. not having children
smoker = 0
#adjusting number of children
num_of_children = 0
#adjusting insurance quote 
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
#difference between original price quote and adjusted
change_in_insurance_cost = new_insurance_cost - insurance_cost
#print adjusted statement
print("The change in estimated cost after decreasing the amount of children is " + str(change_in_insurance_cost) + " dollars")

