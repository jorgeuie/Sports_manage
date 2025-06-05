class Player:
    players = []

    def __init__(self, name, age, id=None):
        self.name = name
        self.age = age
        self.id = id

    def __str__(self):
        return f"Player {self.name}, Age: {self.age}, ID: {self.id}"

    @classmethod
    def create_player(cls, name, age):
        player_id = len(cls.players) + 1
        new_player = cls(name, age, player_id)
        cls.players.append(new_player)
        return new_player

    @classmethod
    def show_players(cls):
        if not cls.players:
            print("No players registered.")
            return
        for player in cls.players:
            print(player)

    @classmethod
    def edit_player(cls):
        player_id = int(input("Enter the ID of the player you want to edit: "))
        for player in cls.players:
            if player.id == player_id:
                player.name = input("Enter the new name: ")
                player.age = int(input("Enter the new age: "))
                # If it's a specific player type, more things could be edited
                if isinstance(player, TennisPlayer):
                    player.ranking = int(input("Enter the new ranking: "))
                elif isinstance(player, FootballPlayer):
                    player.position = input("Enter the new position: ")
                print(f"Player {player_id} updated successfully.")
                return
        print(f"Player with ID {player_id} not found.")

    @classmethod
    def eliminate_player(cls):
        player_id = int(input("Enter the ID of the player you want to eliminate: "))
        for player in cls.players:
            if player.id == player_id:
                cls.players.remove(player)
                print(f"Player {player_id} deleted successfully.")
                return
        print(f"Player with ID {player_id} not found.")


class TennisPlayer(Player):
    def __init__(self, name, age, ranking, id=None):
        super().__init__(name, age, id)
        self.ranking = ranking
        self.sport = "tennis"

    def __str__(self):
        return f"Tennis Player {self.name}, Age: {self.age}, Ranking: {self.ranking}, ID: {self.id}"

    @classmethod
    def create_player(cls, name, age, ranking):
        player_id = len(Player.players) + 1
        new_tennis_player = cls(name, age, ranking, player_id)
        Player.players.append(new_tennis_player)
        print(f"Tennis player '{name}' created with ID {player_id}.")
        return new_tennis_player


class FootballPlayer(Player):
    def __init__(self, name, age, position, id=None):
        super().__init__(name, age, id)
        if isinstance(position, str):
            self.position = position
            self.sport = "football"
        else:
            raise ValueError("Position must be a string")

    def __str__(self):
        return f"Football Player {self.name}, Age: {self.age}, Position: {self.position}, ID: {self.id}"

    @classmethod
    def create_player(cls, name, age, position):
        player_id = len(Player.players) + 1
        new_football_player = cls(name, age, position, player_id)
        Player.players.append(new_football_player)
        print(f"Football player '{name}' created with ID {player_id}.")
        return new_football_player