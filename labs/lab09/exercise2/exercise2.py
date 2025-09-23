employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
total_income = base_salary + (35 * overtime_hours)

if tax_status == "Single":
    if total_income >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18

elif tax_status == "Married":
    if total_income >= 6000:
        tax_rate = 0.20 
    else:
        tax_rate = 0.15

elif tax_status == "Head":
    if total_income >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19

else:
    tax_rate = 0.0

tax_amount = tax_rate * total_income
epf = 0.11 * total_income
sosco = 0.005 * total_income
total_deductions = tax_amount + epf + sosco

net_salary = total_income - total_deductions

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")

