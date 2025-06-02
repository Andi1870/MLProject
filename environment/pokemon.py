import pandas as pd
import random

class Move:
    def __init__(self, name, move_type, power):
        self.name = name
        self.type = move_type
        self.power = power

class Pokemon:
    def __init__(self, name, p_type, hp, attack, speed, moves):
        self.name = name
        self.type = p_type
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.moves = moves  # list of Move objects

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
        moves = type_to_moves.get(row['type1'], [])
        selected_moves = random.sample(moves, 4) if len(moves) >= 4 else moves
        p = Pokemon(
            name=row['name'],
            p_type=row['type1'],
            hp=row['hp'],
            attack=row['attack'],
            speed=row['speed'],
            moves=selected_moves
        )
        pokemons.append(p)

    return pokemons
