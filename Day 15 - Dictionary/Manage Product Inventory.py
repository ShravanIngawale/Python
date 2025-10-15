# current inventory
inventory = {
    "Laptop": 20,
    "Mouse": 50,
    "Keyboard": 30
}

# Safely check stock of 'Monitor'
monitor_stock = inventory.get("Monitor", 0)
print("Monitor stock:", monitor_stock)
# will print 0 because 'Monitor' key does not exist yet

# Add 'Monitor' to inventory
inventory.update({"Monitor": 15})
print("\nInventory after adding monitor:", inventory)

# Remove 'Mouse' from inventory
removed_mouse_stock = inventory.pop("Mouse")
print("\nRemoved Mouse stock was:", removed_mouse_stock)
print("Inventory after removing Mouse:", inventory)

# Backup the inventory
inventory_backup = inventory.copy()

print("\nInventory Items:")
for key, value in inventory.items():
    print(f"{key}: {value}")