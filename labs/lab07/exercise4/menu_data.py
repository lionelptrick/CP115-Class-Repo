import random

restaurant_name = "Yellow Brick Road"
restaurant_location = "Jalan Dungun, Bukit Damansara, 50490 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur"
menu_items = "1. Caesar Salad\n2. Classic Cheeseburger\n3. Beef Tagliatelle"

name_upper = restaurant_name.upper()
name_lower = restaurant_name.lower()
location_length = len(restaurant_location)

daily_special_number = random.randint(1, 3)
customer_number = random.randint(100, 999)


