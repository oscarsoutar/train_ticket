timeUp = [9, 11, 13, 15]
originalTicketsUp = [480, 480, 480, 480]
ticketsUp = [480, 480, 480, 480]
moneyUp = [0, 0, 0, 0]
finalPassengersUp = [0, 0, 0, 0]

timeDown = [10, 12, 14, 16]
originalTicketsDown = [480, 480, 480, 640]
ticketsDown = [480, 480, 480, 640]
moneyDown = [0, 0, 0, 0]
finalPassengersDown = [0, 0, 0, 0]

separateTotal = []
totalPassenger = 0

price = 25
timeAvailUp = False
timeAvailDown = False
seatAvailUp = False
seatAvailDown = False
moreTicket = False
confirmInput = False
mostSales = False

while moreTicket == False:
    print "Times and seats available for going up the mountain:"
    for i in range(len(timeUp)):
        if ticketsUp[i] > 0:
            print str(ticketsUp[i]) + " seats available " + str(timeUp[i]) + ":00"
        else:
            print "Closed"

    print "Times and seats available for going down the mountain:"

    for i in range(len(timeDown)):
        if ticketsDown[i] > 0:
            print str(ticketsDown[i]) + " seats available " + str(timeDown[i]) + ":00"
        else:
            print "Closed"

    while timeAvailUp == False:
        amountOfPassengers = input("Enter number of tickets going up: ")
        timeUpEnt = input("Select a time going up: (9:00 = 9)(11:00 = 11)(13:00 = 13)(15:00 = 15)")
        if timeUpEnt == 9 or timeUpEnt == 11 or timeUpEnt == 13 or timeUpEnt == 15:
            for i in range(len(timeUp)):
                if timeUp[i] == timeUpEnt:
                    IndexUp = i
                    timeAvailUp = True
        else:
            print("Time enter is invalid...")

    while seatAvailUp == False:
            if amountOfPassengers <= ticketsUp[IndexUp]:
                seatAvailUp = True
            elif ticketsUp[IndexUp] != 0:
                print "Sorry, there are only " + str(ticketsUp[IndexUp]) + " seats available"
            else:
                print("Sorry, There are no seats available for " + str(timeUp[IndexUp]) + ":00")

    while timeAvailDown == False:
        timeDownEnt = input("Select a time going down: (10:00 = 10)(12:00 = 12)(14:00 = 14)(16:00 = 16)")
        if timeDownEnt == 10 or timeDownEnt == 12 or timeDownEnt == 14 or timeDownEnt == 16:
            for i in range(len(timeDown)):
                if timeDown[i] == timeDownEnt:
                    IndexDown = i
            if timeDown[IndexDown] < timeUp[IndexUp]:
                print("Time going down cannot be before the time going up")
            else:
                timeAvailDown = True
        else:
            print("Time enter is invalid...")

    while seatAvailDown == False:
        if amountOfPassengers <= ticketsDown[IndexDown]:
            seatAvailDown = True
        elif ticketsDown[IndexDown] != 0:
            print "Sorry, there are only " + str(ticketsDown[IndexDown]) + " seats available"
        else:
            print"Sorry, There are no seats available for " + str(timeDown[IndexDown]) + ":00"

    originalUpPrice = int(moneyUp[IndexUp]) + int(amountOfPassengers * price)
    originalDownPrice = int(moneyDown[IndexDown]) + int(amountOfPassengers * price)

    discount = int(amountOfPassengers / 10)
    if amountOfPassengers >= 10 and amountOfPassengers <= 80:
        if discount >= 1:
            ticketsAfterDiscount = amountOfPassengers - discount

    moneyTotal = str((moneyDown[IndexDown] + (amountOfPassengers * price)) + (moneyUp[IndexUp] + (amountOfPassengers * price)))
    discountedTotal = str((discount * price) * 2)
    if discount >= 1:
        print "Price: $" + moneyTotal
        print "Discount: -$" + discountedTotal

    print "Total Value: $" + str(int(moneyTotal) - int(discountedTotal))
    while confirmInput == False:
        confirmPurchase = raw_input("Would you like to purchase the ticket? (Y/N)").upper()
        if confirmPurchase == "Y":
            ticketsUp[IndexUp] = ticketsUp[IndexUp] - amountOfPassengers
            moneyUp[IndexUp] = int(originalUpPrice) - (int(discountedTotal) / 2)
            ticketsDown[IndexDown] = ticketsDown[IndexDown] - amountOfPassengers
            moneyDown[IndexDown] = int(originalDownPrice) - (int(discountedTotal) / 2)
            print "Purchase Successful!"

            for i in range(len(ticketsUp)):
                print "train at " + str(timeUp[i]) + ":00 had " + str(originalTicketsUp[i] - ticketsUp[i]) + " sales and made $" + str(moneyUp[i])
                print "train at " + str(timeDown[i]) + ":00 had " + str(originalTicketsDown[i] - ticketsDown[i]) + " sales and made $" + str(moneyDown[i])

            totalPassenger = totalPassenger + amountOfPassengers
            print "total passengers: " + str(totalPassenger)

            finalMoney = sum(moneyUp) + sum(moneyDown)
            print "total money earned: $" + str(finalMoney)

            separateTotal.append([[timeUp[IndexUp], amountOfPassengers, int(moneyUp[IndexUp])], [timeDown[IndexDown], amountOfPassengers, int(moneyDown[IndexDown])]])
            print "every purchase today: " + str(separateTotal)
            confirmInput = True

            finalPassengersUp[IndexUp] = finalPassengersUp[IndexUp] + amountOfPassengers
            finalPassengersDown[IndexDown] = finalPassengersDown[IndexDown] + amountOfPassengers
            maxPassengerUp = max(finalPassengersUp)
            maxPassengerDown = max(finalPassengersDown)
            maxIndexUp = finalPassengersUp.index(max(finalPassengersUp))
            maxIndexDown = finalPassengersDown.index(max(finalPassengersDown))
            if maxPassengerUp > maxPassengerDown:
                print str(timeUp[maxIndexUp]) + ":00"
            elif maxPassengerUp < maxPassengerDown:
                print str(timeDown[maxIndexDown]) + ":00"
            else:
                print "Both " + str(timeUp[maxIndexUp]) + ":00 and " + str(timeDown[maxIndexDown]) + ":00 have equal passengers"


        elif confirmPurchase == "N":
            confirmInput = True
            break
        else:
            print "please enter either (Y/N)"

    buyAgain = raw_input("Would you like to purchase more tickets? (Y/N)").upper()
    if buyAgain == "Y":
        timeAvailUp = False
        timeAvailDown = False
        seatAvailUp = False
        seatAvailDown = False
        moreTicket = False
        confirmInput = False
        mostSales = False

    elif buyAgain == "N":
        print "Thank you for using our service!"
        moreTicket = True
    else:
        print "please enter either (Y/N)"