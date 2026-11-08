
# Ellie Posada
# Module 11 lab: Customer Dictionary & Lookup
#Reflection Questions
#1.The .get() method is useful when you're not sure if a key exists because it won't cause an error if it's missing I would use bracket notation when I know the key exists.
#2.Exercise 8 reminds me of using a PivotTable in Excel because both can organize and summarize data into categories. Python can be more useful for large datasets because it can automate calculations and handle lots of data efficiently.

#Exericse 1
print("---Exercise 1---")
customer = {
    "name": "Alice",
    "email":"not-alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer) 

#Exercise 2
print("---Exercise 2---")
customer["phone"] = "555-1234"
print(customer)
customer['tier'] = "platinum"
print(customer)
del customer["email"]
print(customer)

#Exercise 3
print("---Exercise 3---")

print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("no email on file")   


#Exercise 4
print("---Exercise 4---")
for key, value in customer.items():
    print(f"{key}: {value}")
for something in customer:
    print(something, customer[something])

#Exercise 5
print("---Exercise 5---")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

print("customer tier:", tier)
print("customer discount:", discount)


#Exercise 6
print("---Exercise 6---")
customers = [
    {"name": "Bob", "tier": "gold", "ytd_spend": 3200},
    {"name": "Carol", "tier": "silver", "ytd_spend": 1500},
    {"name": "David", "tier": "bronze", "ytd_spend": 800}
]
for c in customers:
    tier = c["tier"]
    discount = tier_discounts.get(tier,0)
    discount_amount = 300 * discount
    print(c["name"], tier, discount_amount)


#Exercise 7
print("---Exercise 7---")
Catalog = {
    "Widget A":{"price": 9.99, "Stock": 150},
    "Gadget C":{"price": 49.99, "Stock": 8},

}
for product_name, details in Catalog.items(): 
   if details["Stock"] < 20:
      print(f"LOW STOCK: {product_name} - only {details['Stock']} left")



#Exercise 8
print("---Exercise 8---")
transaction = [
    { "region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "East", "amount": 200}
]    

sales_by_region = {}
for sale in transaction:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(region, sales_by_region[region])

