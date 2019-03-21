'''Tyler Goodrich
3/13/19
This program will take your budget and it will give you the specs of what pc you should build.'''

budget = int(input("Hello lets get started what is your budget?:"))
games = input("List 3 of your favorite PC games:")
for x in games:

    print("   ")
    if budget >= 450 and budget <= 500:
        print("Perfect Budget and Great Choice of games.")
        print("These are your specs, Processer: Intel i3  GPU: Gtx 980  Ram: 4gb ballistix ddr4 Case: Thermaltake CA-1B3-00M1NN-00 Versa")
        print("  ")
        break
        continue

    elif budget >= 501 and budget < 600:
        print("Perfect Budget and Great Choice of games.")
        print("These are your specs, Processer: Intel i5 7700. GPU: Gtx 980. Ram: 4gb ballistix. ddr4 Case:Cooler Master MasterBox Lite 3.1  ")
        print("  ")
        break
        continue
# Prints specs of desired budget PC.

    else:
        print('Budget too low.')
        print("   ")
        break
# If they print something else it says there budget is too low.

price = True

while price:
    print("Congrats!!")
    break
# Prints Congrats after specs.
