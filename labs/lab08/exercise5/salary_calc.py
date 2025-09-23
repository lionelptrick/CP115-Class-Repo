import employee_data

# Total gross salary
gross_salary = employee_data.basic_salary + (employee_data.overtime_hours * employee_data.overtime_rate)

# Deductions
epf = 0.11 * gross_salary
sosco = 0.005 * gross_salary
eis = 0.002 * gross_salary
medical_insurance = 50
parking = 30

# Total deduction for 11% EPF, 0.5% SOSCO, 0.2% EIS, Medical Insurance and Parking
total_deductions =  epf + sosco + eis + medical_insurance + parking

# Total net salary
net_salary = gross_salary + total_deductions

print("---- PAYSLIP ----")
print(f"Gross Salary: RM{gross_salary}")
print()
print("DEDUCTIONS:")
print(f"EPF (11%): RM{epf}")
print(f"SOSCO (0.05%): RM{epf}")
print(f"EIS (0.02%): RM{eis}")
print(f"Medical Insurance: RM{medical_insurance}")
print(f"Parking: RM{parking}")
print()
print(f"Total Deductions: RM{total_deductions}")
print(f"Net Salary: RM{net_salary}")
print("----------------")




