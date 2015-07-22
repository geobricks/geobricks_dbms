CREATE TABLE public.datasources
(
    id SERIAL PRIMARY KEY NOT NULL,
    datasource VARCHAR(64),
    vendor VARCHAR(64),
    db_name VARCHAR(256),
    username VARCHAR(64),
    password VARCHAR(64),
    collection VARCHAR(256)
);

INSERT INTO "datasources" ("datasource", "vendor", "db_name", "username", "password")
VALUES('test_postgresql', 'postgresql', 'geobricks', 'postgres', 'Ce09114238');

INSERT INTO "datasources" ("datasource", "vendor", "db_name", "collection")
VALUES('test_mongodb', 'mongodb', 'test', 'posts');