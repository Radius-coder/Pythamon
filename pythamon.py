#pythamon the text pokemon game
import random, sys
from encryptor import encryption
from encryptor import decryption

original_stdout = sys.stdout

petHealth = 100
petMaxHealth = 100
petMana = 100
enemyHealth = 100
name      = ""
petName   = ""
petStamina  = 100
petAlive = 0

enemyName = ["Bob", "Dani", "Alex", "Peter", "Tyler", "Charlie", "Ryan", "Chris", "Jordan", "Tom"]
potions = 1
potionRegen = 95
mPotions = 1
mPotionRegen = 100
net = 1
netPower = random.randint(1, 10)
gold      = 400
price = 0
xp = 0
level = 0
collection = []

moves = ["Bite", "Slash", "Magic 25", "Magic 50", "Capture", "Run"]

petAttack1 = random.randint(1, 30)
petAttack2 = random.randint(20, 50)
petAttack3 = random.randint(40, 100)
petAttack4 = random.randint(90, 200)



name = input("Enter your name: ")
petName = input("Enter your pet name: ")

collection.append(petName)

print("\nHello", name + " and", petName)

optionTrue = 0
while optionTrue == 0:
    
    if  xp > 1000 and xp < 3000:
                    level = 1
                    
    elif xp > 3000 and xp < 7000:
                    level = 2
                   
    elif xp > 7000 and xp < 14000:
                    level = 3
                    
    elif xp > 14000:
                    level = level+1
                    
                    
    
    netPower = random.randint(1, 10)
                                

    if petMana > 100:
        petMana = 100
    print("You are level: ", level, " with", xp, " xp")
    print("Your pet has", petHealth, "health and have", petMana, "mana remaining!\n")
    option = int(input("Select Option: \n1. Fight \n2. Check Inventory\n3. Shop\n4. Save\n5. Load\n6. Pythamex\n0. Quit\n"))

    if petAlive == 1:
        print("Your pet is unconcious. Please use a potion.\n")
        
    if option == 1:
        currentEnemy = enemyName[random.randint(1,9)]
        print("You are fighting", currentEnemy , "\n")
        
        if level == 2:
            enemyHealth = 150
        elif level == 3:
            enemyHealth = 200
        elif level >3:
            enemyHealth+=75
        else:
            enemyHealth = 100
            
        attackTrue = 0
        while attackTrue == 0:
           
            while petHealth > 0 or enemyHealth > 0:
                    
                print("Select Move: \n1.",moves[0] + "\n2.",moves[1] + "\n3.",moves[2] + "\n4.",moves[3] + "\n5.",moves[4] + "\n6.",moves[5])
                attack = input()
                    
                    
                if attack == "1":
                    if xp > 3000 and xp < 7000:
                        enemyAttack1 = random.randint(10, 100)
                    elif xp > 14000:
                        enemyAttack1 = random.randint(20, 100)
                    else:
                        enemyAttack1 = random.randint(1, 50)
                        
                    petAttack1 = random.randint(1, 30)
                    enemyHealth = enemyHealth - petAttack1
                    print("You did ",petAttack1,  " damage to the enemy")
                    if enemyHealth <=0:
                        print("You have defeated the enemy!\n")
                        gold = gold + random.randint(10, 300)
                        tempxp =  random.randint(100,1000)
                        print("You gained",tempxp, "xp\n")
                        print("You now have", gold, "gold\n")
                        xp = xp + tempxp
                        attackTrue = 1
                        break
                    else:
                        print("They are now on", enemyHealth , " health\n...")

                    petHealth = petHealth - enemyAttack1
                    print("They did ",enemyAttack1,  " damage to you")
                    print("You are now on", petHealth , " hp\n")                            
                            

                    if petHealth <=0:
                        print("Your pet has fainted!\n")
                        print("Visit a shop to buy health potions...\n")
                        petAlive=1
                        attackTrue=1
                        break

                    else:
                        print("Prepare for the next move\n...")
                        attackTrue = 0

                elif attack == "2":
                    if xp > 3000 and xp < 7000:
                        enemyAttack1 = random.randint(10, 100)
                    elif xp > 14000:
                        enemyAttack1 = random.randint(20, 100)
                    else:
                        enemyAttack1 = random.randint(1, 50)

                    petAttack2 = random.randint(20, 50)
                    enemyHealth = enemyHealth - petAttack2
                    print("You did ",petAttack2,  " damage to the enemy\n")
                    if enemyHealth <=0:
                        print("You have defeated the enemy!\n")
                        gold = gold + random.randint(10, 300)
                        tempxp =  random.randint(100,1000)
                        print("You gained",tempxp, "xp\n")
                        print("You now have", gold, "gold\n")
                        xp = xp + tempxp
                        attackTrue=1
                        break
                    else:
                            print("They are now on", enemyHealth , " health\n")
                            petHealth = petHealth - enemyAttack1
                            print("They did ",enemyAttack1,  " damage to you\n")
                            print("You are now on", petHealth , " hp\n")

                            
                            if petHealth <=0:
                                print("Your pet has fainted!\n")
                                print("Visit a shop to buy health potions...\n")
                                petAlive=1
                                attackTrue=1
                                break

                            else:
                                print("Prepare for the next move...\n")
                                attackTrue = 0


                elif attack == "3":
                    if xp > 3000 and xp < 7000:
                        enemyAttack1 = random.randint(10, 100)
                    elif xp > 14000:
                        enemyAttack1 = random.randint(20, 100)
                    else:
                        enemyAttack1 = random.randint(1, 50)
                    if petMana <25:
                        print("Not enough mana! Select a different move\n")
                    else:
                            petMana-=25
                            petAttack3 = random.randint(40, 100)
                            enemyHealth = enemyHealth - petAttack3
                            print("You did ",petAttack3,  " damage to the enemy\n")
                            if enemyHealth<=0:
                                print("The enemy has fainted!\n")
                                gold = gold + random.randint(10, 300)
                                tempxp =  random.randint(100,1000)
                                print("You gained",tempxp, "xp\n")
                                print("You now have", gold, "gold\n")
                                xp = xp + tempxp
                                attackTrue=1
                                break
                            else:
                                print("They are now on", enemyHealth , " health\n")

                            petHealth = petHealth - enemyAttack1
                            print("They did ",enemyAttack1,  " damage to you\n")
                            
                      

                            if petHealth <=0:
                                print("Your pet has fainted!\n")
                                print("Visit a shop to buy health potions...\n")
                                petAlive=1
                                attackTrue=1
                                break

                            else:
                                print("You are now on", petHealth , " health and have", petMana, "mana remaining!\n")
                                
                                print("Prepare for the next move...\n")
                                attackTrue = 0


                elif attack == "4":
                    if xp > 3000 and xp < 7000:
                        enemyAttack1 = random.randint(10, 100)
                    elif xp > 14000:
                        enemyAttack1 = random.randint(20, 100)
                    else:
                        enemyAttack1 = random.randint(1, 50)
                    if petMana <50:
                        print("Not enough mana! Select a different move\n")
                    else:
                            petMana-=50
                            petAttack4 = random.randint(90, 200)
                            enemyHealth = enemyHealth - petAttack4
                            print("You did ",petAttack4,  " damage to the enemy\n")
                            if enemyHealth<=0:
                                print("The enemy has fainted!\n")
                                gold = gold + random.randint(10, 300)
                                tempxp =  random.randint(100,1000)
                                print("You gained",tempxp, "xp\n")
                                print("You now have", gold, "gold\n")
                                xp = xp + tempxp
                                attackTrue=1
                                break
                            else:
                                print("They are now on", enemyHealth , " health\n")

                            petHealth = petHealth - enemyAttack1
                            print("They did ",enemyAttack1,  " damage to you\n")
                            print("You are now on", petHealth , " hp\n")

                            if petHealth <=0:
                                print("Your pet has fainted!\n")
                                print("Visit a shop to buy health potions...\n")
                                petAlive=1
                                attackTrue=1
                                break

                            else:
                                print("Prepare for the next move...\n")
                                attackTrue = 0


                elif attack == "5":
                    if net <1:
                        print("Buy a net from the shop to use\n")
                        attackTrue=0
                    else:
                        net-=1
                        print("You throw the net...\n")
                        if netPower > 8:
                            print("Congratulations this monster has been caught!\n")
                            collection.append(currentEnemy)
                            gold = gold + random.randint(10, 300)
                            tempxp =  random.randint(100,1000)
                            print("You gained",tempxp, "xp\n")
                            print("You now have", gold, "gold\n")
                            xp = xp + tempxp
                            attackTrue=1
                            break
                            
                        else:
                            print("Capture failed, better luck next time.\n")
                            netPower = random.randint(1, 10)
                            print("Prepare for the next move...\n")
                            attackTrue = 0  


                elif attack == "6":
                                print("You ran away!\n")
                                attackTrue=1
                                break

                if not attack:
                            print("Select a valid move\n")
                    

    elif option == 2:
                print("Your inventory: \n", potions, "Health potion(s)\n", mPotions, "Magic Potion(s)\n", net, "Capture net(s)\n",  gold, "Gold\n")
                if potions > 0 or mPotions > 0:
                    proceed = int(input("Would you like to use:\n1. Health Potion\n2. Magic Potion\n3. Go back\n"))
                    if proceed == 1:
                        if potions <=0:
                            print("No potions left! Purchase some at the store.\n")
                        else:
                            if level == 0:
                                petMaxHealth = 100
                            elif level == 1:
                                petMaxHealth = 150
                            elif level ==2:
                                petMaxHealth = 200
                            elif level == 3:
                                petMaxHealth = 250
                            elif level > 3:
                                petMaxHealth += 50
                            if petHealth >= petMaxHealth:
                                petHealth = petMaxHealth
                                print("Pet at full health...\n")
                            else:
                                petHealth = petHealth + potionRegen
                                print("You are now on", petHealth, "health\n")
                                potions=potions-1

                                if petHealth >= petMaxHealth:
                                    petHealth = petMaxHealth
                    
                                if petHealth> 0:
                                    petAlive = 0
                                    attackTrue = 0
                            
                            
                    elif proceed == 2:
                        if mPotions <= 0:
                            print("No potions left! Purchase some at the store.\n")
                        else:
                            if petMana >= 100:
                                petMana = 100
                                print("Pet mana already full...\n")
                            else:
                                petMana=petMana+mPotionRegen
                                print("You now have", petMana, "magic\n")
                                mPotions-=1

                                if petMana >= 100:
                                    petMana = 100
                else:
                    print("No useable items...\n")

                        
                
    elif option == 3:
                print("Welcome to the shop, you have", gold, "gold\n")
                proceed = int(input("What would you like to buy?\n1. Health Potion - 100\n2. Magic Potion - 200\n3. Capture net - 450\n4. Move learner- 1000\n5. Leave shop\n"))
                if proceed == 1:
                    quantity = int(input("How many would you like?: \n"))
                    price = 100*quantity
                    if gold >= price:
                        print("Thank you for your purchase!\nVisit your inventory to use potions\n")
                        potions = potions+quantity
                        gold = gold - price
                    else:
                        print("Not enough gold...\n")

                elif proceed == 2:
                    quantity = int(input("How many would you like?: \n"))
                    price = 200 * quantity
                    if gold >= price:
                        print("Thank you for your purchase!\nVisit your inventory to use potions\n")
                        mPotions = mPotions+quantity
                        gold = gold - price

                    else:
                        print("Not enough gold...\n")

                elif proceed == 3:
                    quantity = int(input("How many would you like?: \n"))
                    price = 450 * quantity
                    if gold >= price:
                        print("Thank you for your purchase!\nCapture nets can be used in battle\n")
                        net +=quantity
                        gold = gold - price

                elif proceed == 4:
                    quantity = int(input("How many would you like?: \n"))
                    price = 1000 * quantity
                    if gold >= price:
                        print("TEST")
                elif proceed == 5:
                    print("Come again soon!\n")

    elif option == 4:
        fileName = input("Name Save: ")
        print("\nSaving game...\n")
        #variables have to be converted to string before it gets encrypted
        level = str(level)
        gold = str(gold)
        xp = str(xp)
        potions = str(potions)
        mPotions = str(mPotions)
        net = str(net)
        
        
        eLevel = encryption(level)
        eGold = encryption(gold)
        eXp = encryption(xp)
        ePotions = encryption(potions)
        eMPotions = encryption(mPotions)
        eNet = encryption(net)
        file = open(fileName + '.txt', 'w')
        with file as fw:
            sys.stdout = fw
            print(name)
            print(petName)
            print(eLevel)
            print(eGold)
            print(eXp)
            print(ePotions)
            print(eMPotions)
            print(eNet)
            print(collection)
            sys.stdout = original_stdout
            print("File saved\n")
        fw.close()

        #convert back to integers to avoid errors

        level = int(level)
        gold = int(gold)
        xp = int(xp)
        potions = int(potions)
        mPotions = int(mPotions)
        net = int(net)

    elif option == 5:
        fileName = input("Enter the save name you wish to load\n")
        with open(fileName + '.txt', 'r') as file:
            name = file.readline()
            print("Name: ", name)
            petName = file.readline()
            print("Pet name: ", petName)
            level = file.readline()
            level = decryption(level)
            print("Level: ", level)
            gold = file.readline()
            gold = decryption(gold)
            print("Gold: ", gold)
            xp = file.readline()
            xp = decryption(xp)
            print("XP: ", xp)
            potions = file.readline()
            potions = decryption(potions)
            print("Health Potions: ", potions)
            mPotions = file.readline()
            mPotions = decryption(mPotions)
            print("Mana Potions: ", mPotions)
            net = file.readline()
            net = decryption(net)
            print("Capture Nets: ", net)
            collection = file.readline()
            print("Collection: ", collection)
            level = int(level)
            gold = int(gold)
            xp = int(xp)
            potions = int(potions)
            mPotions = int(mPotions)
            net = int(net)
        file.close()

    elif option == 6:
                print("Your collection: \n", collection)
               
        
    elif option == 0:
        answer = int(input("Are you sure you want to quit...\n1. Yes\n2. No\n"))
        if answer == 1:
            optionTrue=1
            break
        else:
            optionTrue=0

    else:
        print("Enter a valid choice.\n")
        optionTrue=0
                    
