import copy


def create_inventory():
    # extra nested field added (supplier_rating)
    inventory = [
        {"item": "Laptop", "details": {"price": 50000, "stock": 10, "supplier_rating": 4.5}},
        {"item": "Phone", "details": {"price": 20000, "stock": 25, "supplier_rating": 4.2}},
        {"item": "Tablet", "details": {"price": 30000, "stock": 15, "supplier_rating": 4.8}}
    ]
    return inventory


def apply_discount(data):
    # using target_index without passing as parameter (as per rule)
    for i in range(len(data)):
        if i == target_index:
            # reduce price by 10%
            price = data[i]["details"]["price"]
            data[i]["details"]["price"] = int(price * 0.9)

            # reduce stock
            data[i]["details"]["stock"] -= 2

    return data


def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i]["details"] != modified[i]["details"]:
            changed += 1
        else:
            unchanged += 1

    return changed, unchanged


# -------- main --------

roll_input = input("Enter your full roll number: ")

# extract digits from roll number
num_str = ""
for ch in roll_input:
    if ch.isdigit():
        num_str += ch

if num_str == "":
    print("Invalid input")
    exit()

roll_number = int(num_str)

inventory = create_inventory()

# backup to detect actual changes
backup = copy.deepcopy(inventory)

# copies
shallow_copy = inventory.copy()
deep_copy = copy.deepcopy(inventory)

# roll rule
target_index = roll_number % len(inventory)

# apply changes
apply_discount(shallow_copy)
apply_discount(deep_copy)

# compare results
shallow_result = compare_data(backup, shallow_copy)
deep_result = compare_data(backup, deep_copy)

# check if original got affected
original_check = compare_data(backup, inventory)


# -------- output --------

print("\n--- Pristine Backup (Before any operations) ---")
print(backup)

print("\n--- Original Inventory (After operations) ---")
print(inventory)

print("\n--- Shallow Copy Result ---")
print(shallow_copy)

print("\n--- Deep Copy Result ---")
print(deep_copy)

print("\n--- Differences Observed ---")

if original_check[0] > 0:
    print("Original inventory got changed due to shallow copy.")
else:
    print("Original inventory is safe.")

print("\nTuple Summary (changed, unchanged):")
print("Shallow:", shallow_result)
print("Deep:", deep_result)


print("\n--- Explanation ---")
print("Shallow copy only copies the outer list, inner dictionaries are shared.")
print("So when we change shallow copy, original also gets affected.")
print("Deep copy creates full separate copy, so original remains unchanged.")