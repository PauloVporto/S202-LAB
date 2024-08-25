from database import Database
from pokedex import Pokedex
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

pokedex = Pokedex(db)

pokedex.get_pokemons_by_type(["Grass", "Fighting"])
pokedex.get_pokemons_by_name('Pikachu')
pokedex.get_pokemons_have_evolution()
pokedex.get_pokemons_spawn_chance_greater_three()
pokedex.get_pokemons_avg_spawns_less_two()