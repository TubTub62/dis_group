from flask import render_template, request
from steamStats import app
from flask import Blueprint

stats = Blueprint('stats', __name__)



@stats.route("/")
def base():
    return render_template("base.html")

@stats.route("/table")
def table():
    # get steam games data here?
    games = [ # temp data
        {
            'steam_id': 252490,
            'name': 'Rust',
            'current_price': 39.99,
            'release_price': 18.99,
            'last_update': 'Dec 14 2013',
            'release_date': 'Sep 22 2021'
        },
        {
            'steam_id': 730,
            'name': 'Counter-Strike 2',
            'current_price': 0,
            'release_price': 7.34,
            'last_update': 'Nov 1 2012',
            'release_date': 'Dec 6 2018'
        },
        {
            'steam_id': 570,
            'name': 'Dota 2',
            'current_price': 0,
            'release_price': 0,
            'last_update': 'Jul 9 2013',
            'release_date': 'Jul 9 2013'
        },
        {
            'steam_id': 2622380,
            'name': 'ELDEN RING NIGHTREIGN',
            'current_price': 39.99,
            'release_price': 39.99,
            'last_update': 'Feb 12 2025',
            'release_date': 'Feb 12 2025'
        },
        {
            'steam_id': 553850,
            'name': 'HELLDIVERS™ 2',
            'current_price': 39.99,
            'release_price': 39.99,
            'last_update': 'Sep 22 2023',
            'release_date': 'Sep 22 2023'
        }
    ]
    ends_with_2 = 'ends_with_2' in request.args
    no_price_update = 'no_price_update' in request.args

    
    filtered_games = []
    for game in games:
        match = True

        if ends_with_2 and not game['name'].strip().endswith('2'): #this filtering should be done by regex not this
            match = False

        if no_price_update and (game['last_update'] != game['release_date']):
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

    return render_template("table.html", games=filtered_games, filters={'ends_with_2': ends_with_2,'no_price_update': no_price_update})




@app.errorhandler(404)
def not_found():
    print("WTF")
    return "Page not found", 404