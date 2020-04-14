product_price = float(input("Insert the product's price: "))
category = int(input("Insert the product's category: \n1 - Cleaning\n2 - Food"
                     "\n3 - Clothing\n\tPlease insert category's number\n\t:"))

if product_price <= 25:
    if category == 1:
        new_product_price = product_price + 0.05
        tax = (8 * new_product_price) / 100
    elif category == 2:
        situation = input(
            "Insert the product's situation: \nR  - If it needs cooling\nN - If it doesn't needs cooling\n\t:")
        if situation.upper() == "R":
            new_product_price = product_price + 0.08
            tax = (5 * new_product_price) / 100
        else:
            new_product_price = product_price + 0.08
            tax = (8 * new_product_price) / 100
    elif category == 3:
        new_product_price = product_price + 0.1
        tax = (8 * new_product_price) / 100
    else:
        print("This category doesn't exist")
else:
    if category == 1:
        new_product_price = product_price + 0.12
        tax = (8 * new_product_price) / 100
    elif category == 2:
        situation = input(
            "Insert the product's situation: \nR  - If it needs cooling\nN - If it doesn't needs cooling\n\t:")
        if situation.upper() == "R":
            new_product_price = product_price + 0.15
            tax = (5 * new_product_price) / 100
        else:
            new_product_price = product_price + 0.15
            tax = (8 * new_product_price) / 100
    elif category == 3:
        new_product_price = product_price + 0.18
        tax = (8 * new_product_price) / 100
    else:
        print("This category doesn't exist")

if new_product_price <= 50:
    classification = "Cheap"
elif 50 < new_product_price < 120:
    classification = "Normal"
else:
    classification = "Expensive"

print("Price: ", new_product_price, "\nTax: ", tax, "\nClassification:", classification)