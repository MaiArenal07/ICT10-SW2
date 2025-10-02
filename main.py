from pyscript import display 
#Restaurant Ordering System using Python Data types 

#String Data Type 
restaurant_name = "Catacoffee"
owner_name = "Maiah Arenal"

#Integer Data Type
year_since = 2024 

#Float Data Type 
tax_rate = 0.08 

#Boolean Data Type 
has_delivery = True
is_dine_in = True 
is_takeaway = False

#List Data Type 
product_names = ["panacotta", "cookie", "vanilla short cake"]
beverages = ["ice tea", "ube milkshake"]

#Tuple Data Type 
business_hours = ("9:00 AM", "8:00 PM")

#Dictionary Data Types 
menu = {
    "panacotta": 120.00,
    "cookie": 55.00,
    "vanilla short cake": 250.00,
    "ice tea": 30.00,
    "ube milkshake": 100.00
}

#Set Data Types 
common_allergens = {"Nuts","Soy", "Dairy","Wheat", "Gluten"}

#Displaying restaurant Information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist:", target="heading1") 


#Display Menu Items
display(product_names[0], target="prod1")
display(f"₱{menu['panacotta']: .2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['cookie']: .2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['vanilla short cake']: .2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['ice tea']: .2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['ube milkshake']: .2f}", target="price5")

#Display additional info 
display(f"Open: {business_hours[0]} - {business_hours[1]}", target= "openingHours")

#display order type
display(f"Dine-in Available", target="orderType")