""" 🌟 Exercise 1: Student Grade Summary """

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

#Calculate the average grade for each student.
student_averages = {}
student_letter_grades = {}

for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    student_averages[student] = average

    #Assign a letter grade based on the average.
    if average >= 90:
        student_letter_grades[student] = "A"
    elif average >= 80:
        student_letter_grades[student] = "B"
    elif average >= 70:
        student_letter_grades[student] = "C"
    elif average >= 60:
        student_letter_grades[student] = "D"
    else:
        student_letter_grades[student] = "F"

#Calculate and print the class average.
class_average = sum(student_averages.values()) / len(student_averages)
print(f"Class average: {class_average:.2f}")

#Print each student's name, average and letter grade.
for student, average in student_averages.items():
    print(f"{student}: {average:.2f}, Grade: {student_letter_grades[student]}")


""" 🌟 Exercise 2: Advanced Data Manipulation and Analysis """

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

#Calculate the total sales for each product.
total_sales = {}

for sale in sales_data:
    product = sale["product"]
    total_price = sale["price"] * sale["quantity"]

    if product not in total_sales:
        total_sales[product] = 0

    total_sales[product] += total_price

print("\nTotal sales for each product:")
print(total_sales)

#Calculate the total amount spent by each customer.
customer_spending = {}

for sale in sales_data:
    customer = sale["customer_id"]

    if customer not in customer_spending:
        customer_spending[customer] = 0

    customer_spending[customer] += sale["price"] * sale["quantity"]

print("\nCustomer spending:")
print(customer_spending)

#Add the total_price field to each transaction.
for sale in sales_data:
    sale["total_price"] = sale["price"] * sale["quantity"]

print("\nUpdated sales data:")
for sale in sales_data:
    print(sale)

#Find transactions greater than $500 and sort from highest to lowest.
high_value_transactions = [sale for sale in sales_data if sale["total_price"] > 500]
high_value_transactions.sort(key=lambda sale: sale["total_price"], reverse=True)

print("\nHigh-value transactions:")
for sale in high_value_transactions:
    print(sale)

#Count purchases for each customer. Each transaction is one purchase.
customer_purchases = {}

for sale in sales_data:
    customer = sale["customer_id"]

    if customer not in customer_purchases:
        customer_purchases[customer] = 0

    customer_purchases[customer] += 1

loyal_customers = []

for customer, purchases in customer_purchases.items():
    if purchases > 1:
        loyal_customers.append(customer)

print("\nCustomers with more than one purchase:")
print(loyal_customers)


## BONUS

#Count transactions and units sold for each product.
product_transactions = {}
product_quantities = {}

for sale in sales_data:
    product = sale["product"]

    if product not in product_transactions:
        product_transactions[product] = 0
        product_quantities[product] = 0

    product_transactions[product] += 1
    product_quantities[product] += sale["quantity"]

#Calculate average transaction value, not average price per unit.
average_transaction_values = {}

print("\nAverage transaction value for each product:")
for product, revenue in total_sales.items():
    average = revenue / product_transactions[product]
    average_transaction_values[product] = average
    print(f"{product}: ${average:.2f}")

#Find the most popular product based on quantity sold.
most_popular_product = max(product_quantities, key=product_quantities.get)
print(f"\nMost popular product: {most_popular_product}")
print(f"Quantity sold: {product_quantities[most_popular_product]}")

#Explain how the results could help with marketing.
print("\nMarketing insights:")
print("Headphones sold the most units. Try offering them in bundles with phones or laptops.")
print("Laptops generated the most revenue and had the highest average transaction value.")
print("Try targeted laptop promotions and measure whether they increase sales.")
print("Customer 2 spent the most. A personalised offer could encourage another purchase.")
print("All three customers made repeat purchases. Try a loyalty reward for returning customers.")
print("These are only seven transactions. Use more data to check whether these patterns continue.")
