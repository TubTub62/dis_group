from flask import render_template, request
from flask import Blueprint
from steamStats import app, conn
from ..sql import *
import re

stats = Blueprint('stats', __name__)

PYTHONUNBUFFERED=0

@stats.route("/")
def base():
    return render_template("base.html")

@stats.route("/table")
def table():
    
    ### Following lines query and gather all game data from db
    all_games_query = query_game_all(conn)
    
    games = []
    for game in all_games_query:
        
        game_name = game[0]
        game_id = game[1]

        cost_q = query_costs(conn, game_id)[0]
        dates_q = query_dates(conn, game_id)[0]
        
        prices_pkeys = [cost_q[1], cost_q[2]]
        update_release_pkeys = [dates_q[1], dates_q[2]]

        prices_q = query_prices(conn, prices_pkeys[0], prices_pkeys[1])[0]
        update_release_q = query_update_release(conn, update_release_pkeys[0], update_release_pkeys[1])[0]

        game_dict = {
            'steam_id': game_id,
            'name': game_name,
            'current_price': prices_q[0],
            'release_price': prices_q[1],
            'last_update': update_release_q[0],
            'release_date': update_release_q[1]
        }

        games.append(game_dict)
        

    ends_with_2 = 'ends_with_2' in request.args
    no_price_update = 'no_price_update' in request.args
    all_caps = 'all_caps' in request.args

    
    filtered_games = []
    for game in games:
        match = True

        if ends_with_2 and not re.search(r"2$", game["name"]):
            match = False

        if no_price_update and (game['last_update'] != game['release_date']):
            match = False
        
        if all_caps and not re.match(r"^[A-Z\s]+$", game["name"]):
            match = False

        if match:
            filtered_games.append(game)

    sort_by = request.args.get('sort_by')

    if sort_by == 'name':
        filtered_games.sort(key=lambda x: x['name'].lower())
    elif sort_by == 'release_price':
        filtered_games.sort(key=lambda x: x['release_price'])
    elif sort_by == 'current_price':
        filtered_games.sort(key=lambda x: x['current_price'])

    return render_template("table.html", games=filtered_games, filters={'ends_with_2': ends_with_2,'no_price_update': no_price_update,'all_caps': all_caps})

if __name__ == "__main__":
    table()