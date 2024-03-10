class Income():

    def __init__(self, rental=0, misc=0):
        self.rental = rental
        self.misc = misc

    def total_income(self):
        self.rental = float(input("Enter the total monthly payment received for all rental units: "))
        self. misc = float(input("Enter the total monthly payment received for all miscellaneous fees: "))
        total = self.rental + self.misc


class Expenses():
    
    def __init__(self, taxes=0, insurance=0, vacancy=0, repairs=0, capex=0, mortgage=0, others=0):
        self.taxes = taxes
        self.insurance = insurance
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.mortgage = mortgage
        self.others = others
    
    def total_expenses(self):
        self.taxes = float(input("Enter the total monthly amount paid for taxes: "))
        self.insurance = float(input("Enter the total monthly amount paid for insurance: "))
        self.vacancy = float(input("Enter the total monthly amount reserved for potential vacancies: "))
        self.repairs = float(input("Enter the total monthly amount reserved for repairs: "))
        self.capex = float(input("Enter the total monthly amount reserved for capex: "))
        self.mortgage = float(input("Enter the total monthly amount paid for mortgage: "))
        self.others = float(input("Enter the total monthly amount paid for miscellaneous: "))


class Cashflow():
    
    def __init__(self, Income=0, Expenses=0):
        self.income = Income
        self.expenses = Expenses

    def remainder(self):
        remainder = Income - Expenses



class ROI():
    
    def __init__(self, investment =0, cashflow=0):
        self.investment = investment
        self.cashflow = cashflow
        self.properties = {}

    def annual_percentage(self):
        self.cashflow = float(input("Enter your total annual cashflow: "))
        self.investment = float(input("Enter your total amount invested: "))
        prop_name = input("Enter the property name: ")
        annual = (self.cashflow / self.investment) * 100
        print(f"Your annual return on investement is {annual}%")
        self.properties[prop_name] = annual
        print(f"Your current properties: {self.properties}")

    def ROI_calculator(self):
        while True:
            rentals = input("Press S to start ROI calculator. Remember to input data required in numerical form only. No special characters. If you are finished with all properties, press Q to quit program. ").upper()
            if rentals == 'S':
                Income()
                Expenses()
                Cashflow()
                ROI()
            elif rentals == 'Q':
                break
            else:
                print("Please enter a valid option: S to start, Q to quit. Thank you. ")


buhay = ROI()
buhay.ROI_calculator()