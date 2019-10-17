  
# To-do list program
the_list = []

def show_help():
    print("What do you want to add to the list?")
    print("""
Enter 'done' to end the program.
Enter 'show' to see your current list.
""")
    
def show_list():
    print("Here is your to-do list:")
    
    for item in the_list:
        print(item)
        
def add_to_list(new_item):
    the_list.append(new_item)
    print("Added {}. Your list now has {} items.".format(new_item, len(the_list)))
    
show_help()

while True:
    new_item = input("> ")
    
    if new_item == 'done':
        break
    elif new_item == 'show':
        show_list()
        continue
    add_to_list(new_item)

show_list()
