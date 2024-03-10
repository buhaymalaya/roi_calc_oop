class ROI():
    
    def __init__(self, investment=0, profit=0, total_inc=0, total_exp=0):
        self.investment = investment
        self.profit = profit
        self.properties = {}
        self.total_inc = total_inc
        self.total_exp = total_exp

    def total_income(self):
        rental = float(input("Enter the total monthly payment received for all rental units: "))
        misc = float(input("Enter the total monthly payment received for all miscellaneous fees: "))
        self.total_inc = rental + misc
        print(f"Your total monthly income is ${self.total_inc}. ")

    def total_expenses(self):
        taxes = float(input("Enter the total monthly amount paid for taxes: "))
        insurance = float(input("Enter the total monthly amount paid for insurance: "))
        vacancy = float(input("Enter the total monthly amount reserved for potential vacancies: "))
        repairs = float(input("Enter the total monthly amount reserved for repairs: "))
        capex = float(input("Enter the total monthly amount reserved for capex: "))
        mortgage = float(input("Enter the total monthly amount paid for mortgage: "))
        others = float(input("Enter the total monthly amount paid for miscellaneous: "))
        self.total_exp = taxes + insurance + vacancy + repairs + capex + mortgage + others
        print(f"Your total monthly expense is ${self.total_exp}. ")

    def cashflow(self):
        self.profit = self.total_inc - self.total_exp
        print(f"Your total cashflow per month is ${self.profit}. ")


    def annual_percentage(self):
        self.investment = float(input("Enter your total amount invested (downpayment, closing costs, repairs, etc): "))
        prop_name = input("Enter the property name: ")
        year_profit = self.profit * 12
        annual = (year_profit / self.investment) * 100
        print(f"Your annual return on investment for {prop_name} is {annual}%")
        self.properties[prop_name] = annual
        print(f"Your current properties: {self.properties}")

    def ROI_calculator(self):
        while True:

            rentals_user = input("Press S to start ROI calculator. Remember to input data required in numerical form only. No special characters. Once finished with all properties, press Q to quit program. ").upper()

            if rentals_user == 'S':
                self.total_income()
                self.total_expenses()
                self.cashflow()
                self.annual_percentage()

            elif rentals_user == 'Q':
                print("Thank you for using the ROI calculator!")
                break

            else:
                print("Please enter a valid option: S to start, Q to quit. Thank you. ")


buhay = ROI()
buhay.ROI_calculator()