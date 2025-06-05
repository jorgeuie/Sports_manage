Made by Jorge Garcia Fernandez ER-1936 and Manuel Mora Rivas ER-1937

# Sport_system


This project is a simple Python-based console application designed to manage sports entities like players, teams, referees, and contests. It allows for creating, viewing, editing, and deleting these entities, and even simulating score management for tennis and football matches.

Player and Subclasses (Player, TennisPlayer, FootballPlayer)
The core idea was to represent different types of players while avoiding code duplication for common attributes and behaviors.

Player (Base Class): This class serves as the abstract base for any type of player. It holds common attributes like name, age, and a unique id.
Decision: A base class is crucial because all players, regardless of their sport, share these fundamental characteristics. It also centralizes common operations like create_player, show_players, edit_player, and eliminate_player, preventing redundant code in subclasses. The players class attribute (a list) acts as a global registry for all players, making it easy to access them by ID across the application.
TennisPlayer (Subclass): Inherits from Player and adds specific attributes relevant to tennis.
Decision: Tennis players have a ranking that's unique to their sport. By creating a subclass, we extend the base Player functionality without cluttering the Player class with sport-specific details. The sport attribute is added to clearly identify the player's discipline.
FootballPlayer (Subclass): Also inherits from Player and includes attributes specific to football.
Decision: Similar to TennisPlayer, football players have a position. Subclassing allows for this specialization while still benefiting from the generic player management features of the base class. The sport attribute similarly marks them as football players.
Referee Class (Referee)
Referees are distinct entities from players and teams, having their own set of attributes and management needs.

Decision: A standalone Referee class is used because referees have a name, role, and id, but they don't share the same hierarchical relationship or specialized attributes as players or teams. It centralizes all referee-related operations, including creation, listing, editing, and removal. The referees class attribute provides a global list for easy access and management, similar to the players list.
Team Class (Team)
Teams are collections of players and are primarily relevant to team sports like football.

Decision: A Team class is necessary to group FootballPlayer objects. It holds a name and id, and crucially, a list of players that belong to that team. The design ensures that only FootballPlayer instances can be added to a team, enforcing sport-specific rules. The teams class attribute provides a global registry for all created teams. Methods like add_player and add_player_by_id_from_global_list allow for flexible team roster management.
Score Classes (TennisScore, FootballScore)
Scorekeeping logic is often complex and highly dependent on the specific sport's rules.

Decision: Separate TennisScore and FootballScore classes are used to encapsulate the unique scoring rules of each sport. This composition approach (Contest has a Score) avoids a monolithic Contest class that would otherwise be burdened with intricate scoring logic for multiple sports.
TennisScore: Models points, games, and sets, including rules for "Deuce" and "Advantage." It tracks the match_over status.
FootballScore: A simpler model that only tracks goals.
Benefit: This design promotes modularity and extensibility. If a new sport were to be added, you would simply create a new Score subclass without modifying existing score logic or the Contest class significantly.
Contest Class (Contest)
This class orchestrates matches or competitions between players or teams, integrating various other components of the system.

Decision: The Contest class acts as the central hub for defining and managing sports events. It's designed to be flexible, supporting both individual player contests (like tennis) and team contests (like football).
It uses a sport attribute to dynamically assign the correct Score object (e.g., TennisScore or FootballScore), demonstrating polymorphism in action.
It manages participants (players for tennis, teams for football) and assigns a referee.
The contests class attribute keeps a global list of all ongoing or past competitions.
Methods like add_participant, add_team, add_player_by_id, add_team_by_id, add_referee_by_id, preview_match, and manage_score provide a comprehensive interface for setting up and running a competition.


## Design patterns

We used different design patterns like Factory Method (for creating objects), Strategy (for interchangeable behaviors), Facade (for simplifying complex systems), Singleton (used as a global registry for managing shared data), and Composite (for building hierarchical structures).

# Factory method 
Category: Creational.

Where it's used: In the Player, TennisPlayer, and FootballPlayer classes, specifically in the create_player class methods.

How it's used: The base Player class and its subclasses (TennisPlayer, FootballPlayer) provide a static method (@classmethod) to create objects. The client code (the menus) doesn't need to know how a new TennisPlayer(...) is instantiated with all its arguments. It simply calls TennisPlayer.create_player(name, age, ranking). This delegates the responsibility of instantiation to the classes themselves.

# Strategy pattern
Category: Behavioral.

Where it's used: In the Contest class, which uses TennisScore or FootballScore objects.

How it's used: The Contest class needs to manage scoring, but the algorithm for doing so varies drastically between tennis and football. Instead of having a giant if/else block within Contest to handle each case, this responsibility is delegated to a separate object (a "strategy"). When a "tennis" Contest is created, it's assigned an instance of TennisScore. If it's "football," it's assigned FootballScore. From that point on, Contest simply uses the common interface (get_score(), add_point()/add_goal()) of the strategy object it holds.

# Facade pattern
Category: Structural.

Where it's used: menu system (main_menu, player_menu, tournament_menu, etc.).

How it's used: The underlying system (creating players, adding them to teams, creating matches, grouping them into tournaments) has complex logic and many interdependencies. The Facade pattern provides a unified, high-level interface that simplifies the use of this system. The user doesn't need to know which methods to call or in what order; they simply navigate through simple options like "Create player" or "Play tournament match." The menu handles orchestrating the correct calls to the system objects.

# Singleton pattern
Category: Creational.

Where it's used: In the use of class lists like Player.players, Team.teams, Contest.contests, and Tournament.tournaments.

How it's used: While not the classic Singleton implementation that restricts creation to a single object, the purpose is the same: to provide a single global access point to a shared resource.  Player.players acts as a centralized registry of all created players. Any part of the program that needs to find a player by their ID can access this global list without needing to pass it as a parameter everywhere.

# Composite Pattern
Category: Structural.

Where it's used: Primarily in the Team class and its relationship with FootballPlayer objects.

How it's used:
The Composite pattern allows you to compose objects into tree-like structures to represent hierarchies where both individual elements and collections of elements can be treated uniformly.

In the project, the Team class uses Composition to manage its players:

Component (Common Interface):

The Player class, and specifically its subclass FootballPlayer, conceptually acts as the "Component." It defines the basic attributes (name, age, id) and behavior expected of any individual participant in a team.

Leaf (Individual Object):

A FootballPlayer object is a "Leaf." It's an individual, atomic unit within the team that does not contain other players. 

Composite (Container Object):

A Team object is the "Composite." It contains a collection (a list, self.players) of FootballPlayer "Leaf" objects.
The Team class provides methods like add_player (to add a Leaf) and show_players (to interact with its contained Leaves). This allows you to manage the entire group of players (the team) as a single, cohesive unit.