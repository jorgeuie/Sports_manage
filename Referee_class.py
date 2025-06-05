class Referee:
    referees = []

    def __init__(self, name, role, id=None):
        self.name = name
        self.role = role
        self.id = id

    def __str__(self):
        return f"Referee {self.name}, Role: {self.role}, ID: {self.id}"

    @classmethod
    def create_referee(cls, name, role):
        referee_id = len(cls.referees) + 1
        new_referee = cls(name, role, referee_id)
        cls.referees.append(new_referee)
        print(f"Referee '{name}' created with ID {referee_id}.")
        return new_referee

    @classmethod
    def show_referees(cls):
        if not cls.referees:
            print("No referees registered.")
        for referee in cls.referees:
            print(referee)

    @classmethod
    def edit_referee(cls):
        try:
            referee_id = int(input("Enter the ID of the referee to edit: "))
            for referee in cls.referees:
                if referee.id == referee_id:
                    referee.name = input("Enter the new name: ")
                    referee.role = input("Enter the new role: ")
                    print(f"Referee {referee_id} updated successfully.")
                    return
            print(f"Referee with ID {referee_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a number for the ID.")

    @classmethod
    def eliminate_referee(cls):
        try:
            referee_id = int(input("Enter the ID of the referee to eliminate: "))
            for referee in cls.referees:
                if referee.id == referee_id:
                    cls.referees.remove(referee)
                    print(f"Referee {referee_id} eliminated successfully.")
                    return
            print(f"Referee with ID {referee_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a number for the ID.")