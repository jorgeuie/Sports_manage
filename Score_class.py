class TennisScore:
    POINTS = {0: "0", 1: "15", 2: "30", 3: "40"}

    def __init__(self, sets_to_win=3):
        self.player1_points = 0
        self.player2_points = 0
        self.player1_games = 0
        self.player2_games = 0
        self.player1_sets = 0
        self.player2_sets = 0
        self.sets_to_win = sets_to_win
        self.match_over = False

    def _check_game_winner(self):
        if self.player1_points >= 4 and self.player1_points >= self.player2_points + 2:
            print("Player 1 wins the game!")
            self.player1_games += 1
            self._reset_points()
            self._check_set_winner()
        elif self.player2_points >= 4 and self.player2_points >= self.player1_points + 2:
            print("Player 2 wins the game!")
            self.player2_games += 1
            self._reset_points()
            self._check_set_winner()

    def _check_set_winner(self):
        if (self.player1_games >= 6 and self.player1_games >= self.player2_games + 2):
            print("Player 1 wins the set!")
            self.player1_sets += 1
            self._reset_games()
            self._check_match_winner()
        elif (self.player2_games >= 6 and self.player2_games >= self.player1_games + 2):
            print("Player 2 wins the set!")
            self.player2_sets += 1
            self._reset_games()
            self._check_match_winner()

    def _check_match_winner(self):
        if self.player1_sets == self.sets_to_win:
            print(f"Player 1 wins the match {self.player1_sets} to {self.player2_sets}!")
            self.match_over = True
        elif self.player2_sets == self.sets_to_win:
            print(f"Player 2 wins the match {self.player2_sets} to {self.player1_sets}!")
            self.match_over = True

    def add_point(self, player_number):
        if self.match_over:
            print("The match is over.")
            return
        if player_number == 1:
            self.player1_points += 1
        elif player_number == 2:
            self.player2_points += 1
        else:
            print("Invalid player number.")
            return
        self._check_game_winner()

    def _reset_points(self):
        self.player1_points = 0
        self.player2_points = 0

    def _reset_games(self):
        self.player1_games = 0
        self.player2_games = 0

    def get_current_game_score(self):
        if self.player1_points >= 3 and self.player2_points >= 3:
            if self.player1_points == self.player2_points:
                return "Deuce"
            elif self.player1_points > self.player2_points:
                return "Advantage P1"
            else:
                return "Advantage P2"
        else:
            p1_score = self.POINTS.get(self.player1_points, "")
            p2_score = self.POINTS.get(self.player2_points, "")
            return f"{p1_score}-{p2_score}"

    def get_score(self):
        game_score = self.get_current_game_score()
        return (f"Sets: P1 {self.player1_sets} - P2 {self.player2_sets} | "
                f"Games: P1 {self.player1_games} - P2 {self.player2_games} | "
                f"Points: {game_score}")


class FootballScore:
    def __init__(self):
        self.team1_goals = 0
        self.team2_goals = 0

    def add_goal(self, team_number):
        if team_number == 1:
            self.team1_goals += 1
            print("Goal for Team 1!")
        elif team_number == 2:
            self.team2_goals += 1
            print("Goal for Team 2!")
        else:
            print("Invalid team number. Use 1 or 2.")

    def get_score(self):
        return f"Team 1: {self.team1_goals} - Team 2: {self.team2_goals}"