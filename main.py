class Siri:
    power = "wired"
    def __init__(self, name, playlist=[]) -> None:
        self.name = name
        self.playlist = playlist
        print(f"{self.name} is recognized")

    def greet(self):
        return f"Hello from {self.name}"
    
    def add_song(self, new_song):
        self.playlist.append(new_song)
    

class Alexa(Siri):
    def __init__(self, name, playlist=[], amazon_account="") -> None:
        super().__init__(name, playlist)
        self.amazon_account = amazon_account
    

kent = Siri('Kent', ['Its five o clock somewhere', 'Barbie Girl'])
tom = Siri("Tom", ['Tequila Talkin'])
drake = Alexa('drake', ["respect"], "655654654654")

print(kent.greet())
print(kent.playlist)
print(tom.playlist)
print(drake.power)

tom.add_song('I will always love you!')
print(tom.playlist)