import io
import zipfile
import pandas as pd


def main():
    main_df = pd.read_csv(io.StringIO(zipfile.ZipFile("dataset/RLCS 2021-22 Dataset.zip")
                                      .read("main.csv")
                                      .decode("utf-8")))
    return main_df


def players_db():
    players_db_df = pd.read_csv(
        io.StringIO(zipfile.ZipFile("dataset/RLCS 2021-22 Dataset.zip").read("players_db.csv").decode("utf-8")))
    return players_db_df


def matches_by_teams():
    matches_by_teams_df = pd.read_csv(
        io.StringIO(zipfile.ZipFile("dataset/RLCS 2021-22 Dataset.zip").read("matches_by_teams.csv").decode("utf-8")))
    # Filtro para dejar solo las columnas necesarias
    matches_by_teams_df_fil = matches_by_teams_df.filter(['color',
                                                          'team_id',
                                                          'team_name',
                                                          'team_region',
                                                          'core_shots',
                                                          'core_goals',
                                                          'core_saves',
                                                          'core_assists',
                                                          'core_score',
                                                          'boost_amount_collected',
                                                          'boost_amount_stolen',
                                                          'boost_time_zero_boost',
                                                          'movement_total_distance',
                                                          'movement_time_supersonic_speed',
                                                          'movement_time_boost_speed',
                                                          'movement_time_slow_speed',
                                                          'movement_time_ground',
                                                          'movement_time_low_air',
                                                          'movement_time_high_air',
                                                          'positioning_time_defensive_half',
                                                          'positioning_time_offensive_half',
                                                          'demo_inflicted',
                                                          'demo_taken',
                                                          'score',
                                                          'winner'])
    return matches_by_teams_df_fil


def games_by_teams_df():
    games_by_teams_df = pd.read_csv(
        io.StringIO(zipfile.ZipFile("dataset/RLCS 2021-22 Dataset.zip").read("games_by_teams.csv").decode("utf-8")))
    return games_by_teams_df


def matches_by_players():
    matches_by_players_df = pd.read_csv(
        io.StringIO(zipfile.ZipFile("dataset/RLCS 2021-22 Dataset.zip").read("matches_by_players.csv").decode("utf-8")),
        low_memory=False)
    matches_by_players_df_fil = matches_by_players_df.filter(['match_id',
                                                              'team_id',
                                                              'team_region',
                                                              'player_id',
                                                              'player_tag',
                                                              'core_shots',
                                                              'core_goals',
                                                              'core_saves'
                                                              'core_assists',
                                                              'core_score',
                                                              'boost_amount_collected',
                                                              'boost_amount_stolen',
                                                              'boost_time_zero_boost',
                                                              'movement_total_distance',
                                                              'movement_time_supersonic_speed',
                                                              'movement_time_boost_speed',
                                                              'movement_time_slow_speed',
                                                              'movement_time_ground',
                                                              'movement_time_low_air',
                                                              'movement_time_high_air',
                                                              'positioning_time_defensive_half',
                                                              'positioning_time_offensive_half',
                                                              'demo_inflicted',
                                                              'demo_taken',
                                                              'score',
                                                              'winner'])
    return matches_by_players_df_fil


def games_by_players_df():
    games_by_players_df = pd.read_csv(
        io.StringIO(zipfile.ZipFile("dataset/RLCS 2021-22 Dataset.zip").read("games_by_players.csv").decode("utf-8")),
        low_memory=False)
    return games_by_players_df


""" with zipfile.ZipFile("dataset/RLCS 2021-22 Dataset.zip") as z:
    games_by_players_df = pd.read_csv(io.StringIO(z.read("games_by_players.csv").decode("utf-8")), low_memory=False) ok
    games_by_teams_df = pd.read_csv(io.StringIO(z.read("games_by_teams.csv").decode("utf-8"))) ok
    main_df = pd.read_csv(io.StringIO(z.read("main.csv").decode("utf-8"))) ok
    matches_by_players_df = pd.read_csv(io.StringIO(z.read("matches_by_players.csv").decode("utf-8"))) ok
    matches_by_teams_df = pd.read_csv(io.StringIO(z.read("matches_by_teams.csv").decode("utf-8")))
    players_db_df = pd.read_csv(io.StringIO(z.read("players_db.csv").decode("utf-8"))) """
