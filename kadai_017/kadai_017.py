class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}さんは大人です。")
        else:
            print(f"{self.name}さんは大人ではありません。")

human_data = [
    ("花子", 19), 
    ("一郎", 23), 
    ("二郎", 21), 
    ("三郎", 19), 
    ("四郎", 17), 
    ("五郎", 15)
]

humans = [] 

for name, age in human_data:
    human = Human(name, age)
    humans.append(human)

for human in humans:
    human.check_adult()

