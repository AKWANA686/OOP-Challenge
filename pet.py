class Pet:
    def __init__(self, name: str, hunger: int = 5, energy : int = 5, happiness: int = 5):
        
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []
        
    @property
    def hunger(self) -> int:
        return self._hunger
    
    @hunger.setter
    def hunger(self, value: int):
        self._hunger = max(0, min(10, value))
        
    @property
    def energy(self) -> int:
        return self._energy
        
    @energy.setter
    def energy(self, value: int):
        self._energy = max(0, min(10, value))
       
    @property
    def happiness(self) -> int:
        return self._happiness   
        
    @happiness.setter
    def happiness(self, value: int):
        self._happiness = max(0, min(10, value))
        
    def eat(self) -> None:
        print(f"{self.name} is eating...")
        self.hunger = self.hunger - 3
        self.happiness = self.happiness + 1
        
    def sleep(self) -> None:
        print(f"{self.name} is sleeping...")
        self.energy = self.energy + 5
        
    def play(self) -> None:
        if self.energy <= 0:
            print(f"{self.name} is too tired to play!")
            return
        
        print(f"{self.name} is playing...")
        self.energy = self.energy -2
        self.happiness = self.happiness + 2
        self.hunger = self.hunger + 1
        
    def get_status(self) -> None:
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")
        
    def train(self, trick: str) -> None:
        self.tricks.append(trick.lower())    