class Vendor:
    def __init__(self, name, year, contact, email):
        self.name = name
        self.year = year
        self.contact = contact
        self.email = email
        self.monthly_purchases = []

    def get_purchases(self):
        print(f"Enter monthly purchases for {self.name}:")
        for i in range(1, 13):
            amount = float(input(f"Month {i}: "))
            self.monthly_purchases.append(amount)

    def generate_report(self):
        total_annual = sum(self.monthly_purchases)
        print("\n" + "="*40)
        print("ANNUAL PURCHASE REPORT")
        print("="*40)
        print(f"Vendor: {self.name}")
        print(f"Association Since: {self.year}")
        print(f"Contact: {self.contact}")
        print(f"Email: {self.email}")
        print("-" * 40)
        for i, amt in enumerate(self.monthly_purchases, 1):
            print(f"Month {i}: Rs. {amt}")
        print("-" * 40)
        print(f"Total Annual Billing: Rs. {total_annual}")
        print("="*40)

v_name = input("Vendor Name: ")
v_year = input("Year of Association: ")
v_contact = input("Contact Number: ")
v_email = input("Email ID: ")

vendor_obj = Vendor(v_name, v_year, v_contact, v_email)
vendor_obj.get_purchases()
vendor_obj.generate_report()
