class Ship:

    def __init__(self, name: str, weapon_name: str, hull_name: str, engine_name: str):
        self.name = name
        self.weapon_name = weapon_name
        self.hull_name = hull_name
        self.engine_name = engine_name

    def __repr__(self) -> str:
        return str(self.name)
