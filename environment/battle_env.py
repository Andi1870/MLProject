class Battle_Environment:
    def __init__(self, teamA, teamB):
        
        # Initailizes the Teams
        self.teamA = teamA
        self.teamB = teamB

        # Sets the first Pokemon of both teams as starters
        self.active_A = 0
        self.active_B = 0

        # Assigns correct hp value to each Pokemon
        self.hp_A = [p.hp for p in teamA]
        self.hp_B = [p.hp for p in teamB]

        self.done = False
    

    def get_hp_bucket(self, hp, max_hp):
        if hp == 0:
            return 0
        elif hp <= max_hp * 0.5:
            return 1
        else:
            return 2


    def get_state(self):
        A_pokemon = self.teamA[self.active_A]
        B_pokemon = self.teamB[self.active_B]

        A_hp_bucket = self.get_hp_bucket(self.hp_A[self.active_A], A_pokemon.hp)
        B_hp_bucket = self.get_hp_bucket(self.hp_B[self.active_B], B_pokemon.hp)

        # Return a tuple representing the state
        return (self.active_A, A_hp_bucket, self.active_B, B_hp_bucket)


    # For debugging to know how much hp is left and if battle is done
    def render(self):
        A_pokemon = self.teamA[self.active_A]
        B_pokemon = self.teamB[self.active_B]

        print(f"Team A: {A_pokemon.name} HP: {self.hp_a[self.active_a]:.1f}/{A_pokemon.hp}")
        print(f"Team B: {B_pokemon.name} HP: {self.hp_b[self.active_b]:.1f}/{B_pokemon.hp}")
        print(f"Battle done: {self.done}")


    # Resets the batlle environment
    def reset(self):

        self.active_A = 0
        self.active_B = 0
        self.hp_A = [p.hp for p in self.teamA]
        self.hp_B = [p.hp for p in self.teamB]
        self.done = False

        return self.get_state()