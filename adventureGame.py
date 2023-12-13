print("Kyle Sanders and Joey Ceresoli")

def loadGame():
    game = {
        "Start": ["You are driving down the middle of the road in the desert when your car breaks down. What do you do?", "Call for help", "Call", "Check engine for problem", "Check"], 
        "Call": ["You pull out your phone to try to call someone. However, there is no cell service.", "Give up", "End1", "Check engine for problem", "Check"], 
        "End1": ["You give and die.", "Start over", "Start", "Quit", "Quit"], 
        "Check": ["You open up the hood and it is on fire! What do you do?", "Try to fix it", "Fix", "Run away", "Run"], 
        "Fix": ["You try to fix it and it blows up. You Die.", "Start over", "Start", "Quit", "Quit"], 
        "Run": ["You get out just in time before it blows up. ", "Try to get your stuff in the car", "Stuff", "Walk down the road", "Walk"], 
        "Stuff": ["You look in the car and find thaat you didn't bring much and that what you did bring is on fire.", "Walk down the road", "Walk", "Wait on the road", "Wait"], 
        "Walk": ["You walk down the road and you see a car on the side of the road, and a gas station that looks run down.", "Walk to the car", "Car", "Walk to the gas station", "Station"], 
        "Station": ["You walk to the gas station and see that it is deserted. A coyote jumps out and attacks you. You die.", "Start Over", "Start", "Quit", "Quit"], 
        "Car": ["You walk to the car and he gives you a ride. You win", "Start Over", "Start", "Quit", "Quit"]
        }
    return game
def playNode(game, currentNode):
    while currentNode != "end":
        (desc, menuA, nodeA, menuB, nodeB) = game[currentNode]

        print(desc)
        print("1:", menuA)
        print("2:", menuB)

        userChoice = input("Enter your choice: ")

        if userChoice == "1":
            currentNode = nodeA
        elif userChoice == "2":
            currentNode = nodeB
        else:
            print("Invalid choice. Please choose 1 or 2.")
    print("game over.")

def main():
    game = loadGame()
    currentNode = "Start"
    playNode(game, currentNode)

if __name__ == "__main__":
    main()
    

    
