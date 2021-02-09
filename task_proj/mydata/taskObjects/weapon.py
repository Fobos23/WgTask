class Weapon:

    def __init__(self, name: str, rel_speed: int, rot_speed: int, diam: int, power_vol: int, count: int):
        self.name = name
        self.rel_speed = rel_speed
        self.rot_speed = rot_speed
        self.diam = diam
        self.power_vol = power_vol
        self.count = count

    def __repr__(self) -> str:
        return str(self.name)
