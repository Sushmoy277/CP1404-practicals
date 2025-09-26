Menu = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Name: ")
print(Menu)
choice = input(">>>  ")
while choice != 'Q':
   if choice == 'H':
       print(f"Hello {name}")
   elif choice == 'G':
       print(f"Goodbye {name}")
   else:
       print("Invalid choice")
   print(Menu)
   choice = input(">>>")
print("Finished")