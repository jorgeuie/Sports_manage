from Player_class import Player, FootballPlayer, TennisPlayer
from Team_class import Team
from Referee_class import Referee
from Contest_class import Contest

def setup_initial_data():
    """Creates initial players and teams to test the application."""
    print("Loading initial data...")
    # Football players
    for i in range(1, 23):
        FootballPlayer.create_player(f"Football Player {i}", 25, "Forward")
    
    # Tennis players
    TennisPlayer.create_player("Rafael Nadal", 37, 2)
    TennisPlayer.create_player("Carlos Alcaraz", 21, 1)

    # Teams
    team1 = Team.create_team("Blue Team")
    team2 = Team.create_team("Red Team")

    # Add players to teams
    for i in range(1, 12):
        team1.add_player_by_id_from_global_list(i)
    for i in range(12, 23):
        team2.add_player_by_id_from_global_list(i)
    print("\nInitial data loaded successfully!")

def player_menu():
    while True:
        print("\n--- PLAYER MENU ---")
        print("1. Create Tennis Player")
        print("2. Create Football Player")
        print("3. Show All Players")
        print("4. Edit Player")
        print("5. Delete Player")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")
        try:
            if choice == "1":
                name = input("Name: ")
                age = int(input("Age: "))
                ranking = int(input("Ranking: "))
                TennisPlayer.create_player(name, age, ranking)
            elif choice == "2":
                name = input("Name: ")
                age = int(input("Age: "))
                position = input("Position: ")
                FootballPlayer.create_player(name, age, position)
            elif choice == "3":
                Player.show_players()
            elif choice == "4":
                Player.edit_player()
            elif choice == "5":
                Player.eliminate_player()
            elif choice == "6":
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input. Please enter a number where required.")

def team_menu():
    while True:
        print("\n--- TEAM MENU ---")
        print("1. Create Team")
        print("2. Add Player by ID to a Team")
        print("3. Show Teams and their Players")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")
        try:
            if choice == "1":
                desc = input("Team Name: ")
                Team.create_team(desc)
            elif choice == "2":
                team_id = int(input("Team ID: "))
                player_id = int(input("Player ID to add: "))
                found_team = False
                for team in Team.teams:
                    if team.id == team_id:
                        team.add_player_by_id_from_global_list(player_id)
                        found_team = True
                        break
                if not found_team:
                    print("Team not found.")
            elif choice == "3":
                if not Team.teams:
                    print("No teams created yet.")
                for team in Team.teams:
                    team.show_players()
            elif choice == "4":
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input. Please enter a number where required.")

def referee_menu():
    while True:
        print("\n--- REFEREE MENU ---")
        print("1. Create Referee")
        print("2. Show Referees")
        print("3. Edit Referee")
        print("4. Delete Referee")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Name: ")
            role = input("Role: ")
            Referee.create_referee(name, role)
        elif choice == "2":
            Referee.show_referees()
        elif choice == "3":
            Referee.edit_referee()
        elif choice == "4":
            Referee.eliminate_referee()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

def contest_menu():
    while True:
        print("\n--- CONTEST MENU ---")
        print("1. Create New Contest")
        print("2. Add Participant (player/team) to Contest")
        print("3. Assign Referee to Contest")
        print("4. View Contest Summary")
        print("5. Manage Contest Score")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")

        try:
            if choice == "1":
                sport = input("Sport (tennis/football): ").lower()
                if sport not in ["tennis", "football"]:
                    print("Invalid sport.")
                    continue
                Contest(sport)
                print("Contest created.")
            elif choice in ["2", "3", "4", "5"]:
                if not Contest.contests:
                    print("You must create a contest first.")
                    continue
                
                print("\nAvailable Contests:")
                for c in Contest.contests:
                    print(f"- {c.name}")
                
                comp_id = int(input("Select the Contest ID: "))
                current_contest = next((c for c in Contest.contests if c.id == comp_id), None)

                if not current_contest:
                    print("Invalid contest selection.")
                    continue

                if choice == "2": # Add participant
                    if current_contest.sport == "tennis":
                        player_id = int(input("Tennis player ID: "))
                        current_contest.add_player_by_id(player_id)
                    elif current_contest.sport == "football":
                        team_id = int(input("Football team ID: "))
                        current_contest.add_team_by_id(team_id)
                elif choice == "3": # Assign referee
                    referee_id = int(input("Referee ID: "))
                    current_contest.add_referee_by_id(referee_id)
                elif choice == "4": # View summary
                    current_contest.preview_match()
                elif choice == "5": # Manage score
                    current_contest.manage_score()
            elif choice == "6":
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input. Please enter a number where required.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main_menu():
    setup_initial_data()
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Players")
        print("2. Teams")
        print("3. Referees")
        print("4. Contests")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            player_menu()
        elif choice == "2":
            team_menu()
        elif choice == "3":
            referee_menu()
        elif choice == "4":
            contest_menu()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()