players = [
    {"name": "Kevin Durant", "age": 34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age": 24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age": 32, "position": "Point Guard", "team": "Brooklyn Nets"},
    {"name": "Damian Lillard", "age": 33, "position": "Point Guard", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age": 32, "position": "Power Foward", "team": "Philidelphia 76ers"},
    {"name": "DeMar DeRozan", "age": 32, "position": "Shooting Guard", "team": "Chicago Bulls"}]

# Challenge 1
class Player:
    def __init__(self, players):
        self.name = players["name"]
        self.age = players["age"]
        self.position = players["position"]
        self.team = players["team"]
    # Ninja Bonus
    @classmethod
    def get_team(cls, dict):
        team_list = []
        for i in dict:
            team_list.append(i["team"])
        return team_list

# Challenge 2
kevin = {"name": "Kevin Durant","age": 34,"position": "small forward","team": "Brooklyn Nets"}
jason = {"name": "Jason Tatum","age": 24,"position": "small forward","team": "Boston Celtics"}
kyrie = {"name": "Kyrie Irving","age": 32,"position": "Point Guard","team": "Brooklyn Nets"}
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)

# Challenge 3
new_team = []
for i in players:
    new_team.append(Player(i))

# Ninja Bonus Test Code
# tm_list = Player.get_team(players)
# for i in range(len(players)):
#     print(tm_list[i])