class Engine:

    def __init__(self, name: str, power: int, eng_type: int):
        self.name = name
        self.power = power
        self.eng_type = eng_type

    def __repr__(self) -> str:
        return str(self.name)
