

DROP SCHEMA alarm_share CASCADE;
CREATE SCHEMA alarm_share;

CREATE TABLE alarm_share.person(
    name VARCHAR(100), 
    PRIMARY KEY(name)
);

CREATE TABLE alarm_share.alarm(
    ID bigserial,
    stop_time TIMESTAMP,
    name_sender VARCHAR(100),
    name_recipient VARCHAR(100),
    PRIMARY KEY(name_sender, name_recipient),
    FOREIGN KEY(name_recipient) REFERENCES alarm_share.person(name)
);
