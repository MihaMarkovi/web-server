import requests
from datetime import datetime
from .models import Player, Match


def get_player_data():
    url_players = "https://lunaroapitest.gq/api/players"
    response_players = requests.get(url_players)
    data_players = response_players.json()

    for player in data_players:
        identity_player = player['id']
        players = Player.objects.filter(id=identity_player)
        if players.count() == 0:
            name = player['name']
            rank = player['rank']
            p = Player(id=identity_player, name=name, rank=rank)
            p.save()
        else:
            p = Player.objects.get(id=identity_player)
            p.rank = player['rank']
            p.save()


def get_match_data():
    url_match = "https://lunaroapitest.gq/api/matches"
    response_match = requests.get(url_match)
    data_match = response_match.json()

    for match in data_match:
        identity_match = match['id']
        matches = Match.objects.filter(id=identity_match)
        if matches.count() == 0:
            player_a = match['player_a']
            player_b = match['player_b']
            score_a = match['score_a']
            score_b = match['score_b']
            ping_a = match['ping_a']
            ping_b = match['ping_b']
            delta_a = match['delta_a']
            delta_b = match['delta_b']
            time = datetime.fromtimestamp(int(match['epoch']) / 1000)
            m = Match(id=identity_match, player_a=Player.objects.get(id=player_a),
                      player_b=Player.objects.get(id=player_b), score_a=score_a, score_b=score_b, ping_a=ping_a, ping_b=ping_b,
                      delta_a=delta_a, delta_b=delta_b, time=time)
            m.save()
