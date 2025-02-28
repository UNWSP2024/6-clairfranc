# Claire Francis, Feb 27, 2025, Week6_program_3.py
# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
STATE_SALES_TAX = .05
COUNTY_SALES_TAX = .025

def add_tax(state, county):
    return state + county

def calculate_monthly_tax_report():

    total_sales_for_month = float(input("Enter total sales for the month here: "))
    state_sales_tax = total_sales_for_month * STATE_SALES_TAX
    county_sales_tax = total_sales_for_month * COUNTY_SALES_TAX


    print(f'State sales tax: ${state_sales_tax:,.2f}.')
    print(f'County sales tax: ${county_sales_tax:,.2f}.')
    print(f'Total sales tax: ${float(add_tax(state_sales_tax, county_sales_tax)):,.2f}.')

if __name__ == '__main__':
    calculate_monthly_tax_report()




