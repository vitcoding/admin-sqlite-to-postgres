CREATE SCHEMA IF NOT EXISTS content;
SET search_path TO content, public;

CREATE TABLE IF NOT EXISTS film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created TIMESTAMP WITH TIME ZONE,
    modified TIMESTAMP WITH TIME ZONE
);

CREATE INDEX film_work_title_idx ON film_work (title);
CREATE INDEX film_work_rating_idx ON film_work (rating);
CREATE INDEX film_work_type_idx ON film_work (type);

CREATE TABLE IF NOT EXISTS genre (
    id uuid PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created TIMESTAMP WITH TIME ZONE,
    modified TIMESTAMP WITH TIME ZONE
);

CREATE INDEX genre_name_idx ON genre (name);

CREATE TABLE IF NOT EXISTS genre_film_work (
    id uuid PRIMARY KEY,
    genre_id UUID NOT NULL,
    film_work_id UUID NOT NULL,
    created TIMESTAMP WITH TIME ZONE,
    CONSTRAINT fk_genre_id
        FOREIGN KEY (genre_id)
        REFERENCES genre (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_film_work_id
        FOREIGN KEY (film_work_id)
        REFERENCES film_work (id)
        ON DELETE CASCADE
);

CREATE UNIQUE INDEX 
    film_work_genre_idx 
    ON genre_film_work (film_work_id, genre_id);

CREATE TABLE IF NOT EXISTS person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created TIMESTAMP WITH TIME ZONE,
    modified TIMESTAMP WITH TIME ZONE
);

CREATE INDEX person_full_name_idx ON person (full_name);

CREATE TABLE IF NOT EXISTS person_film_work (
    id uuid PRIMARY KEY,
    person_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
    role TEXT NOT NULL,
    created TIMESTAMP WITH TIME ZONE,
    CONSTRAINT fk_person_id
        FOREIGN KEY (person_id)
        REFERENCES person (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_film_work_id
        FOREIGN KEY (film_work_id)
        REFERENCES film_work (id)
        ON DELETE CASCADE
);

CREATE UNIQUE INDEX 
    film_work_person_idx 
    ON person_film_work (film_work_id, person_id);
