# Análisis preliminar
Este dataset puede tener información más relevante al ser el que guarda lo referente a los encuentros (no a los partidos individuales)([Glosario](../glosario.md)).

## Columnas y tipos (matches_by_teams_df.dtypes)
```text
match_id                               object
color                                  object
team_id                                object
team_slug                              object
team_name                              object
team_region                            object
core_shots                            float64
core_goals                            float64
core_saves                            float64
core_assists                          float64
core_score                            float64
core_shooting_percentage              float64
boost_bpm                             float64
boost_bcpm                            float64
boost_avg_amount                      float64
boost_amount_collected                float64
boost_amount_stolen                   float64
boost_amount_collected_big            float64
boost_amount_stolen_big               float64
boost_amount_collected_small          float64
boost_amount_stolen_small             float64
boost_count_collected_big             float64
boost_count_stolen_big                float64
boost_count_collected_small           float64
boost_count_stolen_small              float64
boost_amount_overfill                 float64
boost_amount_overfill_stolen          float64
boost_amount_used_while_supersonic    float64
boost_time_zero_boost                 float64
boost_time_full_boost                 float64
boost_time_boost_0_25                 float64
boost_time_boost_25_50                float64
boost_time_boost_50_75                float64
boost_time_boost_75_100               float64
movement_total_distance               float64
movement_time_supersonic_speed        float64
movement_time_boost_speed             float64
movement_time_slow_speed              float64
movement_time_ground                  float64
movement_time_low_air                 float64
movement_time_high_air                float64
movement_time_powerslide              float64
movement_count_powerslide             float64
positioning_time_defensive_third      float64
positioning_time_neutral_third        float64
positioning_time_offensive_third      float64
positioning_time_defensive_half       float64
positioning_time_offensive_half       float64
positioning_time_behind_ball          float64
positioning_time_in_front_ball        float64
demo_inflicted                        float64
demo_taken                            float64
score                                 float64
winner                                   bool
dtype: object
```

## Nulos (matches_by_teams_df.isnull().sum())
```text
match_id                                 0
color                                    0
team_id                                  0
team_slug                                0
team_name                                0
team_region                              7
core_shots                            1886
core_goals                            1886
core_saves                            1886
core_assists                          1886
core_score                            1886
core_shooting_percentage              1886
boost_bpm                             1932
boost_bcpm                            1932
boost_avg_amount                      1932
boost_amount_collected                1932
boost_amount_stolen                   1932
boost_amount_collected_big            1932
boost_amount_stolen_big               1932
boost_amount_collected_small          1932
boost_amount_stolen_small             1932
boost_count_collected_big             1932
boost_count_stolen_big                1932
boost_count_collected_small           1932
boost_count_stolen_small              1932
boost_amount_overfill                 1932
boost_amount_overfill_stolen          1932
boost_amount_used_while_supersonic    1932
boost_time_zero_boost                 1932
boost_time_full_boost                 1932
boost_time_boost_0_25                 1932
boost_time_boost_25_50                1932
boost_time_boost_50_75                1932
boost_time_boost_75_100               1932
movement_total_distance               1932
movement_time_supersonic_speed        1932
movement_time_boost_speed             1932
movement_time_slow_speed              1932
movement_time_ground                  1932
movement_time_low_air                 1932
movement_time_high_air                1932
movement_time_powerslide              1932
movement_count_powerslide             1932
positioning_time_defensive_third      1932
positioning_time_neutral_third        1932
positioning_time_offensive_third      1932
positioning_time_defensive_half       1932
positioning_time_offensive_half       1932
positioning_time_behind_ball          1932
positioning_time_in_front_ball        1932
demo_inflicted                        1932
demo_taken                            1932
score                                    0
winner                                   0
dtype: int64
```

La siguiente línea de código, se divide en lo siguiente:
1. Busca los valores nulos dentro del df con el método isnull()
2. Con el método any(axis=1) guarda las posiciones de cada True de isnull
3. Filtra cada posición guardada anteriormente en el df
4. Guarda el resultado en un nuevo df llamado "nulos"
```python
nulos = matches_by_teams_df[matches_by_teams_df.isnull().any(1)]
```

Al verificar manualmente algunas de las filas que están con datos nulos, realmente no existen en la web donde está la base desde donde se realizaría el web scraping, ahora bien, en general en cada columna representaría un 18% (en las que tienen más nulos) que podría afectar en el modelo, por lo tanto, dependiendo de la relación principalmente se rellenarán con la mediana, o de lo contrario se eliminarían

## Limpieza de dataset
Si bien, el dataset cuenta con muchas columnas que se pueden analizar, hay algunas que muestran porcentajes o promedios y realmente no se utilizarían en el modelo y se eliminarán.
Por otro lado, hay columnas que son la suma de otras 2 que muestran un poco más en detalle, por ejemplo, "boost_amount_collected" es la suma de "boost_amount_collected_big" y "boost_amount_collected_small". Si bien con el detalle se podrían hacer un análisis más completo y en detalle con estos datos, realmente no influirían tanto en este modelo, por lo tanto, solo se quedarán las columnas con el total.
Con base en lo anteriormente mencionado, junto con otros factores, se optará por dejar solo las siguientes columnas.
```text
match_id (esto solo se incluirá en el caso que se deba buscar un dato en otro df o en la web)
color
team_id
team_name
team_region
core_shots
core_goals
core_saves
core_assists
core_score
boost_amount_collected
boost_amount_stolen
boost_time_zero_boost
movement_total_distance
movement_time_supersonic_speed
movement_time_boost_speed
movement_time_slow_speed
movement_time_ground
movement_time_low_air
movement_time_high_air
positioning_time_defensive_half
positioning_time_offensive_half
demo_inflicted
demo_taken
score
winner
```

Esta limpieza se realiza en el archivo [datasets.py](../datasets.py) que se utilizará como módulo con el fin de limpiar todos los datos y cargarlos en archivos por separado