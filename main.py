from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

pokedex = Pokedex(db)

pokedex.pokemons_evolucao_ate_21()
pokedex.pokemons_fracos_contra_gelo()
pokedex.pokemons_sem_multiplier()
pokedex.pokemons_tipo_fogo()
pokedex.pokemons_uma_fraqueza()