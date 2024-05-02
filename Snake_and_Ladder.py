import random
snakes = {
        99:2,
        87:60,
        63:45,
        42:30,
        26:9
    }
lader = {
        3:15,
        13:34,
        36:52,
        47:82,
        7:95
    }
def to_win(num_players, player_names, players_position, current_players_index):
    number_to_win=100-players_position[current_players_index]
    print(player_names[current_players_index]," you have to roll ",number_to_win," to win...")
    
    
    
def check_snakes_and_ladder(num_players, player_names, players_position, current_players_index):
    flag=0
    for i in range(players_position[current_players_index]+1,players_position[current_players_index]+7):
        #snakes check:
        if i in snakes:
            print("There's a SNAKE in location: ",i," which will take you to location: ",snakes[i])
            flag=1
        if i in lader:
            print("There's a LADER in location: ",i," which will take you to location: ",lader[i])
            flag=1
    if(flag==0):
        print("There are no snakes and laders on your way till location:",players_position[current_players_index]+6)
        

def play_game(num_players, player_names,players_position):
    completed=[]
    for i in range(num_players):
        players_position.append(0)
    print("players current positions:")
    for i in range(num_players):
        print(player_names[i],":",players_position[i])

    while(1):
        if len(completed) == num_players:
            print("Game Over...\nHope you guys had fun.....")
            break
        for i in range(num_players):
            if i in completed:
                print("completed_players:",len(completed))
                continue
            print(player_names[i]," It's your turn...")
            if(players_position[i]!=0):
                check_snakes_and_ladder(num_players, player_names, players_position, i)
            if(players_position[i]>94):
                to_win(num_players, player_names, players_position, i)
            print(player_names[i]," your current position(before roll) is ---> ", players_position[i])
            print(player_names[i]," press Enter to roll the dice...")
            input()
            rolled_no = random.randint(1, 6)
            print(player_names[i]," rolled ", rolled_no)
            if(players_position[i]+rolled_no>100):
                    print(player_names[i],"your rolled number will take you to position above 100, so roll again.")
                    print("--------------------------------------------------------------------------------------------------")
                    continue
            if(players_position[i]==0):
                if(rolled_no!=1):
                    print(player_names[i]," you have to roll 1 start the game")
                    print("--------------------------------------------------------------------------------------------------")
                else:
                    players_position[i]=players_position[i]+rolled_no
                    print(player_names[i],"'s current position ===>>", players_position[i])
                    print("Don't be happy now, the real game is just about to start ",player_names[i],". Hold tight for the next adventerous 99 locations")
                    print("--------------------------------------------------------------------------------------------------")
            else:
                    players_position[i]=players_position[i]+rolled_no
                    if players_position[i] in snakes:
                        print("Oooo!!, You are bitten by a snake in location: ",players_position[i],", so now you are going to location:",snakes[players_position[i]])
                        players_position[i]= snakes[players_position[i]]
                    if players_position[i] in lader:
                        print("Congrats!! You have stepped on a ladder in location: ",players_position[i],", so now you are going to location:",lader[players_position[i]])
                        players_position[i]= lader[players_position[i]]
                    print(player_names[i],"'s current position ===>>", players_position[i])
                    print("--------------------------------------------------------------------------------------------------")
                    if(players_position[i]==100):
                        print(player_names[i],"You have completed the game congradulations...!!!!")
                        completed.append(i)




def main():
    players_count = int(input("Enter players count:"))
    players_name = []
    players_position=[]
    print("Enter players name:")
    for i in range(players_count):
        temp = input()
        players_name.append(temp)
    print("Players Names:")
    for name in players_name:
        print(name)
    print("Rules:\n1) Player should roll 1 to start the game. \n2) No player is allowed to roll the dice continuously.")
    print("=====================================================================================================")
    play_game(players_count,players_name,players_position)

if __name__ == "__main__":
    main()