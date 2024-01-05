CREATE TABLE FACT_SHOW_POPULARITY(
    ShowKey int NOT NULL,
    DateKey int,
    LanguageKey int,
    GenreKey int,
    popularity numeric(10, 2) NULL,
    number_of_seasons int NOT NULL,
    number_of_episodes int NOT NULL,
    FOREIGN KEY (ShowKey) REFERENCES DIM_SHOW(ShowKey),
    FOREIGN KEY (DateKey) REFERENCES DIM_DATE(DateKey),
    FOREIGN KEY (LanguageKey) REFERENCES DIM_LANGUAGE(LanguageKey),
    FOREIGN KEY (GenreKey) REFERENCES DIM_GENRE(GenreKey)
);
GO
