DROP SCHEMA steam_stats CASCADE;
CREATE SCHEMA steam_stats;

CREATE TABLE steam_stats.game(
    name VARCHAR(100),
    id bigserial, 
    PRIMARY KEY(id)
);

CREATE TABLE steam_stats.update_release(
    newest_date TIMESTAMP,
    oldest_date TIMESTAMP,
    PRIMARY KEY(newest_date, oldest_date)
);

CREATE TABLE steam_stats.prices(
    newest_price INT,
    oldest_price INT,
    PRIMARY KEY(newest_price, oldest_price)
);

create TABLE steam_stats.dates(
    steam_game_id bigserial,
    newest_date TIMESTAMP,
    oldest_date TIMESTAMP,
    FOREIGN KEY(steam_game_id) REFERENCES steam_stats.game(id),
    FOREIGN KEY(newest_date, oldest_date) REFERENCES steam_stats.update_release(newest_date, oldest_date)

);

CREATE TABLE steam_stats.costs(
    steam_game_id bigserial,
    newest_price INT,
    oldest_price INT,
    FOREIGN KEY(steam_game_id) REFERENCES steam_stats.game(id),
    FOREIGN KEY(newest_price, oldest_price) REFERENCES steam_stats.prices(newest_price, oldest_price)
);