
initial_grocery=["milk", "bread", "eggs"]
def add_item(item):
    initial_grocery.insert(0,item)

def remove_last_item():
    initial_grocery.pop()
add_item("butter")
remove_last_item()
print(initial_grocery)

display_list=lambda x:print(f"Item: {x} ")
for x in initial_grocery:
    display_list(x)

def count_characters(items):
    if not items:
        return 0
    return len(items[0])+count_characters(items[1:]) 
print(count_characters(initial_grocery))