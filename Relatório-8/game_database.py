class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, match_id, player_ids, total_score):
        query = "CREATE (:Match {id: $match_id, total_score: $total_score})"
        parameters = {"match_id": match_id, "total_score": total_score}
        self.db.execute_query(query, parameters)

        for player_id in player_ids:
            self.add_player_to_match(player_id, match_id)

    def add_player_to_match(self, player_id, match_id):
        query = """
        MATCH (p:Player {name: $player_id}), (m:Match {id: $match_id})
        MERGE (p)-[:PARTICIPATES_IN]->(m)
        """
        parameters = {"player_id": player_id, "match_id": match_id}
        self.db.execute_query(query, parameters)

    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name, p.id AS id"
        results = self.db.execute_query(query)
        return [(result["name"], result["id"]) for result in results]

    def get_player_matches(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})-[:PARTICIPATES_IN]->(m:Match)
        RETURN m.id AS match_id, m.total_score AS total_score
        """
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [(result["match_id"], result["total_score"]) for result in results]

    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)
