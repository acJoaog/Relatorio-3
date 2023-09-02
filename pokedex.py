from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database : Database):
        self.database = database

    def pokemons_evolucao_ate_21(self) :
        pokemons = self.database.collection.find({"next_evolution.1.num": {"$lte": "020"}})
        writeAJson(pokemons, "PokemonsEvolucaoAte21")
        
    def pokemons_tipo_fogo(self):
        pokemons = self.database.collection.find({"$or": [{"type":"Fire"}]})
        writeAJson(pokemons, "PokemonsTipoFogo")

    def pokemons_uma_fraqueza(self):
        pokemons = self.database.collection.find({"weaknesses": {"$size": 1}})
        writeAJson(pokemons, "PokemonsUmaFraqueza")

    def pokemons_fracos_contra_gelo(self):
        pokemons = self.database.collection.find({"weaknesses": "Ice"})
        writeAJson(pokemons, "PokemonsFracosContraGelo")

    def pokemons_sem_multiplier(self):
        pokemons = self.database.collection.find({"multipliers": {"$exists": False}})
        writeAJson(pokemons, "PokemonsSemMultiplier")

    