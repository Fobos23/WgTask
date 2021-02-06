class Hull:

    def __init__(self, name: str, armor: int, hull_type: int, capacity: int):
        self.name = name
        self.armor = armor
        self.hull_type = hull_type
        self.capacity = capacity

    def __repr__(self) -> str:
        return str(self.name)
