CREATE TABLE DIM_DATE (
    DateKey int NOT NULL IDENTITY(1,1),
    first_air_date varchar(50),
    first_air_Day varchar(50),
    first_air_Month varchar(50),
    first_air_Year varchar(50),
    first_air_Quarter varchar(50),
    first_air_MonthName varchar(20),
    first_air_DayOfWeek varchar(20),
    WeekdayInd int,
);
GO

CREATE TABLE DIM_GENRE (
    GenreKey int NOT NULL IDENTITY(1,1),
    genres_id varchar(50) NOT NULL,
    genres varchar(100),
    primary_genre varchar(50),
    genre_count int,
);
GO

CREATE TABLE DIM_SHOW (
    ShowKey int NOT NULL IDENTITY(1,1),
    show_id varchar(50) NOT NULL,
    show_name nvarchar(100) NOT NULL,
    show_type varchar(50) NOT NULL,
    show_status varchar(50) NOT NULL,
    in_production varchar(50) NOT NULL,
    availableTranslations varchar(50),
    origin_country nvarchar(100),
    origin_Region varchar(50),
    origin_Continent varchar(50),
    ActiveInd smallint NOT NULL DEFAULT 1
);
GO

CREATE TABLE DIM_LANGUAGE (
    LanguageKey int NOT NULL IDENTITY(1,1),
    language_id varchar(50) NOT NULL,
    original_language varchar(10),
    original_languageName varchar(50),
    spoken_languages nvarchar(100),
    ActiveInd smallint NOT NULL DEFAULT 1
);
GO

alter table DIM_DATE add primary key (DateKey);
alter table DIM_GENRE add primary key (GenreKey);
alter table DIM_SHOW add primary key (ShowKey);
alter table DIM_LANGUAGE add primary key (LanguageKey);
GO
