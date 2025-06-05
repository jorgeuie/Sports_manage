from Player_class import Player, TennisPlayer
from Team_class import Team
from Referee_class import Referee
from Score_class import TennisScore, FootballScore

class Contest:
    contests = []

    def __init__(self, sport, referee=None):
        self.id = len(Contest.contests) + 1
        self.sport = sport.lower()
        self.name = f"Competition of {self.sport.capitalize()} (ID: {self.id})"
        self.players = []  # For tennis
        self.teams = []    # For football
        self.referee = referee
        self.score = None
        Contest.contests.append(self)

        if self.sport == "tennis":
            self.score = TennisScore()
        elif self.sport == "football":
            self.score = FootballScore()
        else:
            raise ValueError("Sport not supported")

    def add_participant(self, player):
        if self.sport != "tennis":
            print("This sport does not support individual players.")
            return
        if not isinstance(player, TennisPlayer):
            print(f"Player {player.name} is not a tennis player.")
            return
        if len(self.players) < 2:
            self.players.append(player)
            print(f"Player '{player.name}' added to the competition.")
        else:
            print("There are already two players in the tennis match.")
            

    def add_player_by_id(self, player_id):
        found_player = None
        for p in Player.players:
            if p.id == player_id:
                found_player = p
                break
        if found_player:
            self.add_participant(found_player)
        else:
            print(f"No player found with ID {player_id}.")

    def add_team(self, team):
        if self.sport != "football":
            print("This sport does not support teams.")
            return
        if len(self.teams) < 2:
            self.teams.append(team)
            print(f"Team '{team.name}' added to the competition.")
        else:
            print("There are already two teams in the football match.")
            
    
    def add_team_by_id(self, team_id):
        found_team = None
        for t in Team.teams:
            if t.id == team_id:
                found_team = t
                break
        if found_team:
            self.add_team(found_team)
        else:
            print(f"No team found with ID {team_id}.")
            
    
    def add_referee_by_id(self, referee_id):
        found_referee = None
        for r in Referee.referees:
            if r.id == referee_id:
                found_referee = r
                break
        if found_referee:
            self.referee = found_referee
            print(f"Referee '{self.referee.name}' assigned to the competition.")
        else:
            print(f"No referee found with ID {referee_id}.")

    def preview_match(self):
        print(f"\n--- SUMMARY: {self.name} ---")
        print(f"Sport: {self.sport.capitalize()}")
        if self.referee:
            print(f"Referee: {self.referee.name}")
        else:
            print("No referee assigned.")
        
        if self.sport == "tennis":
            print("Players:")
            if not self.players: print(" (None)")
            for i, player in enumerate(self.players):
                print(f"   - Player {i+1}: {player.name} (Ranking: {player.ranking})")
        elif self.sport == "football":
            print("Teams:")
            if not self.teams: print(" (None)")
            for i, team in enumerate(self.teams):
                print(f"   - Team {i+1}: {team.name} ({len(team.players)} players)")

    
    def manage_score(self):
        if self.score is None:
            print("This competition does not have a scoring system.")
            return

        print(f"\n--- SCORE MANAGEMENT: {self.name} ---")
        
        if self.sport == "tennis":
            while True:
                print("\n" + self.score.get_score())
                if self.score.match_over: break
                print("1. Add point to Player 1")
                print("2. Add point to Player 2")
                print("3. Exit score management")
                choice = input("Option: ")
                if choice == "1":
                    self.score.add_point(1)
                elif choice == "2":
                    self.score.add_point(2)
                elif choice == "3":
                    break
                else:
                    print("Invalid option.")

        elif self.sport == "football":
            while True:
                print("\n" + self.score.get_score())
                print("1. Add goal to Team 1")
                print("2. Add goal to Team 2")
                print("3. Exit score management")
                choice = input("Option: ")
                if choice == "1":
                    self.score.add_goal(1)
                elif choice == "2":
                    self.score.add_goal(2)
                elif choice == "3":
                    break
                else:
                    print("Invalid option.")