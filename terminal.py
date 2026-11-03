import login
import message

if(__name__ == "__main__"):
    exit()

print("███╗░░██╗████████╗███████╗██╗░░░██╗    ███╗░░░███╗███████╗░██████╗░██████╗███████╗███╗░░██╗░██████╗░███████╗██████╗░")
print("████╗░██║╚══██╔══╝██╔════╝╚██╗░██╔╝    ████╗░████║██╔════╝██╔════╝██╔════╝██╔════╝████╗░██║██╔════╝░██╔════╝██╔══██╗")
print("██╔██╗██║░░░██║░░░█████╗░░░╚████╔╝░    ██╔████╔██║█████╗░░╚█████╗░╚█████╗░█████╗░░██╔██╗██║██║░░██╗░█████╗░░██████╔╝")
print("██║╚████║░░░██║░░░██╔══╝░░░░╚██╔╝░░    ██║╚██╔╝██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗")
print("██║░╚███║░░░██║░░░██║░░░░░░░░██║░░░    ██║░╚═╝░██║███████╗██████╔╝██████╔╝███████╗██║░╚███║╚██████╔╝███████╗██║░░██║")
print("╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░    ╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝ \n")

def terminal():
    print("\n$ ", end="")
    eingabe = input()
    
    
    if(eingabe == "help"):
        print("help     Shows you all commands\n" \
              "login    Set a username. If left blank the username will be set to \"Anonymous\"\n" \
              "logout   Removes the set username back to \"Anonymous\"\n" \
              "send     Send a message to the selectet channel\n" \
              "channel  Set's the cannel for the messages\n")

        terminal()
    
    elif(eingabe == "login"):
        print("Username: ", end="")
        login.username = input()
        print(f"You are now logged in as {login.username}")
        terminal()
    
    elif(eingabe == "logout"):
        login.username = "Anonymous"
        print("You are now logged out")
        terminal()
    
    elif(eingabe == "send"):
        print("Message: ", end="")
        message.send(message=input())
        print("Message send\n")
        terminal()

    elif(eingabe == "channel"):
        print("Feature not avaliable")
        terminal()

    else:
        print("Wrong input. Type in \"help\" to see all the commands")
        terminal()


terminal()