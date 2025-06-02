import pandas as pd
import random

# Create a class to create a proper Move object
class Move:
    def __init__(self, name, move_type, power):
        self.name = name
        self.type = move_type
        self.power = power

# Create a class to create a proper Pokemon object
class Pokemon:
    def __init__(self, name, p_type, hp, attack, defense, speed, moves):
        self.name = name
        self.type = p_type
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves
        self.status = None  # saves the fainted status of pokemon. Optional: status effects in the future

    # Handles the damage that is taken from the pokemon and checks if it fainted
    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)
        if self.hp == 0:
            self.status = 'fainted'

    # Can check if the pokemon is fainted
    def is_fainted(self):
        return self.hp <= 0


def load_pokemon_and_moves(pokemon_csv, moves_csv):
    pokemon_df = pd.read_csv(pokemon_csv)
    moves_df = pd.read_csv(moves_csv)

    # Group moves by type
    type_to_moves = {}
    for _, row in moves_df.iterrows():
        m = Move(row['name'], row['type'], row['power'])
        type_to_moves.setdefault(row['type'], []).append(m)

    # Create Pokémon objects with 4 random moves of matching type
    pokemons = []
    for _, row in pokemon_df.iterrows():
        moves = type_to_moves.get(row['Type 1'], [])
        selected_moves = random.sample(moves, 4) if len(moves) >= 4 else moves
        p = Pokemon(
            name = row['Name'],
            p_type = row['Type 1'],
            hp = row['HP'],
            attack = row['Attack'],
            defense = row['Defense'],
            speed = row['Speed'],
            moves = selected_moves
        )
        pokemons.append(p)

    return pokemons