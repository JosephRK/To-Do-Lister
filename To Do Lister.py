lst1=[]
def main():
    while True:
        choice = input("Grocery List Manager\n"   
                       "(A) Add Item\n"
                       "(R) Remove Item\n"
                       "(D) Display List\n"
                       "(E) Exit\n"
                       "Enter your choice (1-4): ")
        if choice == "(A)":
            (gro)=input("\nEnter the item to add:")
            lst1.append(gro)
        elif choice == "(R)":
            lst1.remove(input("\nEnter the item to remove:"))
        elif choice == "(D)":
            print(*lst1, sep='\n')
        elif choice == "(E)":
            break
        else:
            print("Invalid choice")
main()