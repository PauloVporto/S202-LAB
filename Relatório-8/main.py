from database import Database
from game_database import GameDatabase

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.227.9.12:7687", "neo4j", "assistance-learning-punches")
db.drop_all()

# Criando uma instância da classe GameDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player("Ana")
game_db.create_player("Carlos")
game_db.create_player("Beatriz")

# Criando algumas partidas e associando jogadores a elas
game_db.create_match("1", ["Ana", "Carlos"], 180)
game_db.create_match("2", ["Ana", "Beatriz"], 210)
game_db.create_match("3", ["Carlos", "Beatriz"], 250)

# Atualizando o nome de um jogador
game_db.update_player("Beatriz", "Bianca")

# Deletando um jogador e uma partida
game_db.delete_player("Carlos")
game_db.delete_match("2")

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(game_db.get_players())
print("Partidas de Ana:")
print(game_db.get_player_matches("Ana"))
print("Partidas de Bianca:")
print(game_db.get_player_matches("Bianca"))

# Fechando a conexão com o banco de dados
db.close()
