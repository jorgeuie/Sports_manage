from Player_class import Player, FootballPlayer

from Player_class import Player, FootballPlayer

class Team:
    teams = []

    def __init__(self, description: str, id: int):
        self.players = []
        self.name = description # Renamed to name for consistency
        self.id = id

    def __str__(self):
        return f"Team {self.id}: {self.name} ({len(self.players)} players)"

    @classmethod
    def create_team(cls, description: str):
        team_id = len(cls.teams) + 1
        new_team = cls(description, team_id)
        cls.teams.append(new_team)
        print(f"Team '{description}' created with ID {team_id}.")
        return new_team

    def add_player(self, player):
        if not isinstance(player, FootballPlayer):
            print("Only football players can be added to this team.")
            return
        if len(self.players) >= 15:
            print("Cannot add more players. The team already has 15.")
            return
        if player in self.players:
            print(f"Player {player.name} is already on the team.")
            return
        self.players.append(player)
        print(f"Football player {player.name} added to team '{self.name}'.")

    def add_player_by_id_from_global_list(self, player_id):
        for player in Player.players:
            if player.id == player_id:
                if not isinstance(player, FootballPlayer):
                    print(f"Player with ID {player_id} is not a football player.")
                    return
                self.add_player(player)
                return
        print(f"No player found with ID {player_id}.")

    def show_players(self):
        print(f"\nTeam '{self.name}' (ID: {self.id}) has {len(self.players)} players:")
        if not self.players:
            print(" (Empty)")
        for player in self.players:
            print(f"- {player.name} (Position: {player.position}, ID: {player.id})")
        print()