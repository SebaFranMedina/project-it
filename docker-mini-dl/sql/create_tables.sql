CREATE TABLE dim_city (
    city_key INTEGER PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(10)
);

CREATE TABLE dim_system (
    system_key INTEGER PRIMARY KEY,
    system VARCHAR(200)
);

CREATE TABLE fact_network (
    network_id VARCHAR(100) PRIMARY KEY,
    network_name VARCHAR(200),
    city_key INTEGER,
    system_key INTEGER,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    company TEXT,
    href TEXT,

    CONSTRAINT fk_city
        FOREIGN KEY (city_key)
        REFERENCES dim_city(city_key),

    CONSTRAINT fk_system
        FOREIGN KEY (system_key)
        REFERENCES dim_system(system_key)
);