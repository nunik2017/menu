print "Welcome to menu Program!"

menuList = {}

while True:
    dish = raw_input("Enter dish name: ")
    dishPrice = float(raw_input("Enter dish price as ($.$$): "))
    menuList[dish] = dishPrice

    another = raw_input("Do you want to enter another dish? (yes/no): ")

    if (another.lower() == "no".lower()):
        print "Your dishes have been updated and saved!"
        break

print "Menu: %s" % menuList

with open("menu.txt", "w+") as menu_file:

    for dish in menuList:
        menu_file.write("%s / %s EUR\n" % (dish, menuList[dish]))

