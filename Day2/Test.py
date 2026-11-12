print("Welcome to the tip calculator!");

bill_amount = float(input("What was the total bill? $"));
tip = int(input("How much tip would you like to give? 10%, 12%, or 15% "));
number_people = int(input("How many people to split? "));

total_tip = (bill_amount * tip) / 100;
total_bill = bill_amount + total_tip;
each_person_pay = round(total_bill / number_people, 2);

print(f"Each person should pay: ${each_person_pay}");