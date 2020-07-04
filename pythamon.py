#pythamon the text pokemon game
import random, sys
original_stdout = sys.stdout

petHealth = 100
enemyHealth = 100
name      = ""
petName   = ""
petStanima  = 100
petAlive = 0

enemyName = ["Bob", "Dani", "Alex", "Peter"]
potions = 1
potionHealth = 95
gold      = 300
xp = 0
level = 0
inventory = []

moves = ["Bite", "Slash", "Headbutt", "Dig", "Run"]

petAttack1 = random.randint(1, 30)
petAttack2 = random.randint(20, 50)
petAttack3 = random.randint(40, 100)
petAttack4 = random.randint(90, 200)



name = input("Enter your name: ")
petName = input("Enter your pet name: ")

print("\nHello", name + " and", petName)

optionTrue = 0
while optionTrue == 0:

    
    enemyAttack1 = random.randint(1, 50)

    print("You are level: ", level, " with", xp, " xp")
    print("Your pet has", petHealth, " health\n")
    option = int(input("Select Option: \n1. Fight \n2. Check Inventory\n3. Shop\n4. Save\n5. Load\n"))

    if petAlive == 1:
        print("Your pet is unconcious. Please use a potion.\n")
        
    if option == 1:
        print("You are fighting", enemyName[random.randint(1,3)], "\n")

        attackTrue = 0
        while attackTrue == 0:
           
            while petHealth > 0 or enemyHealth > 0:
                enemyAttack1 = random.randint(1, 50)
                petAttack1 = random.randint(1, 30)
                petAttack2 = random.randint(20, 50)
                petAttack3 = random.randint(40, 100)
                petAttack4 = random.randint(90, 200)
                    
                print("Select Move: \n1.",moves[0] + "\n2.",moves[1] + "\n3.",moves[2] + "\n4.",moves[3] + "\n5.",moves[4])
                attack = input()
                    
                    
                if attack == "1":
                    enemyHealth = enemyHealth - petAttack1
                    print("You did ",petAttack1,  " damage to the enemy")
                    print("They are now on", enemyHealth , " health\n...")

                    petHealth = petHealth - enemyAttack1
                    print("They did ",enemyAttack1,  " damage to you")
                    print("You are now on", petHealth , " hp\n")


                    if enemyHealth <=0:
                        print("You have defeated the enemy!\n")
                        gold = gold + random.randint(10, 300)
                        tempxp =  random.randint(100,1000)
                        print("You gained",tempxp, "xp\n")
                        print("You now have", gold, "gold\n")
                        xp = xp + tempxp
                            
                        if  xp > 1000 and xp < 3000:
                            level = 1
                            enemyHealth = 200
                                        
                        elif xp > 3000 and xp < 7000:
                            level = 2
                            enemyHealth = 300
                            petHealth = 200
                            enemyAttack1 = random.randint(10, 100)
                                        
                        elif xp > 7000 and xp < 14000:
                            level = 3
                            enemyHealth = 400
                            petHealth = 250
                                    
                        elif xp > 14000:
                            level = level+1
                            enemyHealth = 500
                            petHealth = petHealth + 100
                            enemyAttack1 = random.randint(20, 100)
                                    
                        attackTrue = 1
                        break
                            

                    elif petHealth <=0:
                        print("Your pet has fainted!\n")
                        print("Visit a shop to buy health potions...\n")
                        petAlive=1
                        attackTrue=1
                        break

                    else:
                        print("Prepare for the next move\n...")
                        attackTrue = 0

                elif attack == "2":
                             enemyHealth = enemyHealth - petAttack2
                             print("You did ",petAttack2,  " damage to the enemy\n")
                             print("They are now on", enemyHealth , " health\n")

                             petHealth = petHealth - enemyAttack1
                             print("They did ",enemyAttack1,  " damage to you\n")
                             print("You are now on", petHealth , " hp\n")

                            
                             if enemyHealth <=0:
                                print("You have defeated the enemy!\n")
                                gold = gold + random.randint(10, 300)
                                tempxp =  random.randint(100,1000)
                                print("You gained",tempxp, "xp\n")
                                print("You now have", gold, "gold\n")
                                xp = xp + tempxp
                                
                                if  xp > 1000 and xp < 3000:
                                    level = 1
                                    enemyHealth = 200
                                        
                                elif xp > 3000 and xp < 7000:
                                    level = 2
                                    enemyHealth = 300
                                    petHealth = 200
                                    enemyAttack1 = random.randint(10, 100)
                                        
                                elif xp > 7000 and xp < 14000:
                                    level = 3
                                    enemyHealth = 400
                                    petHealth = 250
                                            
                                elif xp > 14000:
                                    level = level+1
                                    enemyHealth = 500
                                    petHealth = petHealth + 100
                                    enemyAttack1 = random.randint(20, 100)
                                    
                                attackTrue=1
                                break
                            

                             elif petHealth <=0:
                                print("Your pet has fainted!\n")
                                print("Visit a shop to buy health potions...\n")
                                petAlive=1
                                attackTrue=1
                                break

                             else:
                                print("Prepare for the next move...\n")
                                attackTrue = 0


                elif attack == "3":
                            enemyHealth = enemyHealth - petAttack3
                            print("You did ",petAttack3,  " damage to the enemy\n")
                            print("They are now on", enemyHealth , " health\n")

                            petHealth = petHealth - enemyAttack1
                            print("They did ",enemyAttack1,  " damage to you\n")
                            print("You are now on", petHealth , " hp\n")

                            
                            if enemyHealth <=0:
                                print("You have defeated the enemy!\n")
                                gold = gold + random.randint(10, 300)
                                tempxp =  random.randint(100,1000)
                                print("You gained",tempxp, "xp\n")
                                print("You now have", gold, "gold\n")
                                xp = xp + tempxp
                                if  xp > 1000 and xp < 3000:
                                    level = 1
                                    enemyHealth = 200
                                        
                                elif xp > 3000 and xp < 7000:
                                    level = 2
                                    enemyHealth = 300
                                    petHealth = 200
                                    enemyAttack1 = random.randint(10, 100)
                                        
                                elif xp > 7000 and xp < 14000:
                                    level = 3
                                    enemyHealth = 400
                                    petHealth = 250
                                            
                                elif xp > 14000:
                                    level = level+1
                                    enemyHealth = 500
                                    petHealth = petHealth + 100
                                    enemyAttack1 = random.randint(20, 100)
                                attackTrue=1
                                break
                            

                            elif petHealth <=0:
                                print("Your pet has fainted!\n")
                                print("Visit a shop to buy health potions...\n")
                                petAlive=1
                                attackTrue=1
                                break

                            else:
                                print("Prepare for the next move...\n")
                                attackTrue = 0


                elif attack == "4":
                            enemyHealth = enemyHealth - petAttack4
                            print("You did ",petAttack4,  " damage to the enemy\n")
                            print("They are now on", enemyHealth , " health\n")

                            petHealth = petHealth - enemyAttack1
                            print("They did ",enemyAttack1,  " damage to you\n")
                            print("You are now on", petHealth , " hp\n")

                            
                            if enemyHealth <=0:
                                print("You have defeated the enemy!\n")
                                gold = gold + random.randint(10, 300)
                                tempxp =  random.randint(100,1000)
                                print("You gained",tempxp, "xp\n")
                                print("You now have", gold, "gold\n")
                                xp = xp + tempxp
                                if  xp > 1000 and xp < 3000:
                                    level = 1
                                    enemyHealth = 200
                                        
                                elif xp > 3000 and xp < 7000:
                                    level = 2
                                    enemyHealth = 300
                                    petHealth = 200
                                    enemyAttack1 = random.randint(10, 100)
                                        
                                elif xp > 7000 and xp < 14000:
                                    level = 3
                                    enemyHealth = 400
                                    petHealth = 250
                                            
                                elif xp > 14000:
                                    level = level+1
                                    enemyHealth = 500
                                    petHealth = petHealth + 100
                                    enemyAttack1 = random.randint(20, 100)
                                attackTrue=1
                                break
                            

                            elif petHealth <=0:
                                print("Your pet has fainted!\n")
                                print("Visit a shop to buy health potions...\n")
                                petAlive=1
                                attackTrue=1
                                break

                            else:
                                print("Prepare for the next move...\n")
                                attackTrue = 0



                elif attack == "5":
                                print("You ran away!\n")
                                attackTrue=1
                                break

                if not attack:
                            print("Select a valid move\n")
                    

    elif option == 2:
                print("Your inventory: ", inventory, potions, "potion(s)", gold, "gold/n")
                usePotion = int(input("If you have a potion would you like to use it?\n1. Yes\n2. No\n"))
                if usePotion == 1:
                    if potions <=0:
                        print("No potions left! Purchase some at the store.\n")
                    else:
                        petHealth = petHealth + potionHealth
                        print("You are now on", petHealth, "health\n")
                        potions=potions-1
                    
                        if petHealth> 0:
                            petAlive = 0
                            attackTrue = 0
                
    elif option == 3:
                print("Welcome to the shop, you have", gold, "gold\n")
                proceed = int(input("Would you like to purchase a health potion for 200 gold?\n1. Yes\n2. No\n"))
                if proceed == 1:
                    if gold > 200:
                        print("Thank you for your purchase!\nVisit your inventory to use potions")
                        potions = potions+1
                        gold = gold - 200
                    else:
                        print("Not enough gold...\n")
                    
                    
                elif proceed == 2:
                    print("Come again soon!\n")

    elif option == 4:
        fileName = input("Name Save: ")
        print("\nSaving game...\n")
        file = open(fileName + '.txt', 'w')
        with file as fw:
            sys.stdout = fw
            print(name)
            print(petName)
            print(level)
            print(gold)
            print(potions)
            print(xp)
            sys.stdout = original_stdout
            print("File saved\n")
        fw.close()

    elif option == 5:
        fileName = input("Enter the save name you wish to load\n")
        with open(fileName + '.txt', 'r') as file:
            name = file.readline()
            print("Name: ", name)
            petName = file.readline()
            print("\nPet name: ", petName)
            level = file.readline()
            print("\nLevel: ", level)
            gold = file.readline()
            print("\nGold: ", gold)
            potions = file.readline()
            print("\nPotions: ", potions)
            xp = file.readline()
            print("\nXP: ", xp)
            gold = int(gold)
            xp = int(xp)
        file.close()
        
        
                    
