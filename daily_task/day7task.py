
inventory=[]
def add_item(item):
    inventory.append(item)

def count_items(items):
    if not items:
        return 0
    return 1 + count_items(items[1:])

def main():
    add_item( "dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    show_items=lambda x:print(f"Item in stock : {x} ")
    for item in inventory:
      show_items(item)

    total_items=count_items(inventory)
    print(f"Total items in stock: {total_items}")

main()
