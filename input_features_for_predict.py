import pandas as pd
import numpy as np
import json
import requests

def input_orgs_info(data):
    with open('../duration_info/orgs_mean.json') as file:
        orgs_mean = json.load(file)
    data['r_org_mean_duration'] = 0
    data['d_org_mean_duration'] = 0
    data['r_org_mean_score'] = 0
    data['d_org_mean_score'] = 0
    data['r_org_mean_deaths'] = 0
    data['d_org_mean_deaths'] = 0
    data['r_org_mean_assists'] = 0
    data['d_org_mean_assists'] = 0
    data['r_org_mean_last_hits'] = 0
    data['d_org_mean_last_hits'] = 0
    data['r_org_mean_denies'] = 0
    data['d_org_mean_denies'] = 0
    data['r_org_mean_gpm'] = 0
    data['d_org_mean_gpm'] = 0
    data['r_org_mean_xpm'] = 0
    data['d_org_mean_xpm'] = 0
    data['r_org_mean_winrate'] = 0
    data['d_org_mean_winrate'] = 0

    data['org_vs_org_mean_winrate'] = 0
    data['org_vs_org_mean_duration'] = 0
    data['org_vs_org_mean_score'] = 0
    data['org_vs_org_mean_deaths'] = 0

    data['r_org_vs_org_mean_assists'] = 0
    data['r_org_vs_org_mean_last_hits'] = 0
    data['r_org_vs_org_mean_denies'] = 0
    data['r_org_vs_org_mean_gpm'] = 0
    data['r_org_vs_org_mean_xpm'] = 0

    data['d_org_vs_org_mean_assists'] = 0
    data['d_org_vs_org_mean_last_hits'] = 0
    data['d_org_vs_org_mean_denies'] = 0
    data['d_org_vs_org_mean_gpm'] = 0
    data['d_org_vs_org_mean_xpm'] = 0

    for index, org in enumerate(orgs_mean):
        if int(org) in data[['r_org', 'd_org']].values:
            data.loc[data['r_org'] == int(org), 'r_org_mean_duration'] = orgs_mean[org]['duration']
            data.loc[data['d_org'] == int(org), 'd_org_mean_duration'] = orgs_mean[org]['duration']

            data.loc[data['r_org'] == int(org), 'r_org_mean_winrate'] = orgs_mean[org]['wins']
            data.loc[data['d_org'] == int(org), 'd_org_mean_winrate'] = orgs_mean[org]['wins']

            data.loc[data['r_org'] == int(org), 'r_org_mean_score'] = orgs_mean[org]['score_mean']
            data.loc[data['d_org'] == int(org), 'd_org_mean_score'] = orgs_mean[org]['score_mean']

            data.loc[data['r_org'] == int(org), 'r_org_mean_deaths'] = orgs_mean[org]['deaths_mean']
            data.loc[data['d_org'] == int(org), 'd_org_mean_deaths'] = orgs_mean[org]['deaths_mean']

            data.loc[data['r_org'] == int(org), 'r_org_mean_assists'] = orgs_mean[org]['assists']
            data.loc[data['d_org'] == int(org), 'd_org_mean_assists'] = orgs_mean[org]['assists']

            data.loc[data['r_org'] == int(org), 'r_org_mean_last_hits'] = orgs_mean[org]['last_hits']
            data.loc[data['d_org'] == int(org), 'd_org_mean_last_hits'] = orgs_mean[org]['last_hits']

            data.loc[data['r_org'] == int(org), 'r_org_mean_denies'] = orgs_mean[org]['denies']
            data.loc[data['d_org'] == int(org), 'd_org_mean_denies'] = orgs_mean[org]['denies']

            data.loc[data['r_org'] == int(org), 'r_org_mean_gpm'] = orgs_mean[org]['gold_per_min']
            data.loc[data['d_org'] == int(org), 'd_org_mean_gpm'] = orgs_mean[org]['gold_per_min']

            data.loc[data['r_org'] == int(org), 'r_org_mean_xpm'] = orgs_mean[org]['xp_per_min']
            data.loc[data['d_org'] == int(org), 'd_org_mean_xpm'] = orgs_mean[org]['xp_per_min']

            for versus in orgs_mean[org]['versus_orgs']:
                if int(versus) in data[['r_org', 'd_org']].values:
                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'org_vs_org_mean_duration'] = \
                        orgs_mean[org]['versus_orgs'][versus]['duration']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'org_vs_org_mean_duration'] = \
                        orgs_mean[org]['versus_orgs'][versus]['duration']

                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'org_vs_org_mean_winrate'] = \
                        orgs_mean[org]['versus_orgs'][versus]['wins']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'org_vs_org_mean_winrate'] = \
                        orgs_mean[org]['versus_orgs'][versus]['wins']

                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'org_vs_org_mean_score'] = \
                        orgs_mean[org]['versus_orgs'][versus]['score_mean']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'org_vs_org_mean_score'] = \
                        orgs_mean[org]['versus_orgs'][versus]['deaths_mean']

                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'org_vs_org_mean_deaths'] = \
                        orgs_mean[versus]['versus_orgs'][org]['score_mean']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'org_vs_org_mean_deaths'] = \
                        orgs_mean[versus]['versus_orgs'][org]['deaths_mean']

                    data.loc[
                        (data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'r_org_vs_org_mean_assists'] = \
                        orgs_mean[org]['versus_orgs'][versus]['r_assists']
                    data.loc[
                        (data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'd_org_vs_org_mean_assists'] = \
                        orgs_mean[org]['versus_orgs'][versus]['d_assists']
                    data.loc[
                        (data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'r_org_vs_org_mean_assists'] = \
                        orgs_mean[versus]['versus_orgs'][org]['r_assists']
                    data.loc[
                        (data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'd_org_vs_org_mean_assists'] = \
                        orgs_mean[versus]['versus_orgs'][org]['d_assists']

                    data.loc[
                        (data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'r_org_vs_org_mean_last_hits'] = \
                        orgs_mean[org]['versus_orgs'][versus]['r_last_hits']
                    data.loc[
                        (data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'd_org_vs_org_mean_last_hits'] = \
                        orgs_mean[org]['versus_orgs'][versus]['d_last_hits']
                    data.loc[
                        (data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'r_org_vs_org_mean_last_hits'] = \
                        orgs_mean[versus]['versus_orgs'][org]['r_last_hits']
                    data.loc[
                        (data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'd_org_vs_org_mean_last_hits'] = \
                        orgs_mean[versus]['versus_orgs'][org]['d_last_hits']

                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'r_org_vs_org_mean_denies'] = \
                        orgs_mean[org]['versus_orgs'][versus]['r_denies']
                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'd_org_vs_org_mean_denies'] = \
                        orgs_mean[org]['versus_orgs'][versus]['d_denies']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'r_org_vs_org_mean_denies'] = \
                        orgs_mean[versus]['versus_orgs'][org]['r_denies']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'd_org_vs_org_mean_denies'] = \
                        orgs_mean[versus]['versus_orgs'][org]['d_denies']

                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'r_org_vs_org_mean_gpm'] = \
                        orgs_mean[org]['versus_orgs'][versus]['r_gold_per_min']
                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'd_org_vs_org_mean_gpm'] = \
                        orgs_mean[org]['versus_orgs'][versus]['d_gold_per_min']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'r_org_vs_org_mean_gpm'] = \
                        orgs_mean[versus]['versus_orgs'][org]['r_gold_per_min']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'd_org_vs_org_mean_gpm'] = \
                        orgs_mean[versus]['versus_orgs'][org]['d_gold_per_min']

                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'r_org_vs_org_mean_xpm'] = \
                        orgs_mean[org]['versus_orgs'][versus]['r_xp_per_min']
                    data.loc[(data['r_org'] == int(org)) & (data['d_org'] == int(versus)), 'd_org_vs_org_mean_xpm'] = \
                        orgs_mean[org]['versus_orgs'][versus]['d_xp_per_min']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'r_org_vs_org_mean_xpm'] = \
                        orgs_mean[versus]['versus_orgs'][org]['r_xp_per_min']
                    data.loc[(data['r_org'] == int(versus)) & (data['d_org'] == int(org)), 'd_org_vs_org_mean_xpm'] = \
                        orgs_mean[versus]['versus_orgs'][org]['d_xp_per_min']
    return data


def input_players_info(data):
    with open('../duration_info/players_mean.json') as file:
        players_mean = json.load(file)

    players_id = set(list(data[[f'r_{i}_player_id' for i in range(1, 6)]].values.ravel()) + list(
        data[[f'd_{i}_player_id' for i in range(1, 6)]].values.ravel()))


    data['r_players_mean_duration'] = 0
    data['d_players_mean_duration'] = 0
    data['r_players_heroes_mean_duration'] = 0
    data['d_players_heroes_mean_duration'] = 0

    data['r_players_mean_winrate'] = 0
    data['d_players_mean_winrate'] = 0
    data['r_players_heroes_mean_winrate'] = 0
    data['d_players_heroes_mean_winrate'] = 0

    data['r_players_mean_score'] = 0
    data['d_players_mean_score'] = 0
    data['r_players_heroes_mean_score'] = 0
    data['d_players_heroes_mean_score'] = 0

    data['r_players_mean_deaths'] = 0
    data['d_players_mean_deaths'] = 0
    data['r_players_heroes_mean_deaths'] = 0
    data['d_players_heroes_mean_deaths'] = 0

    data['r_players_mean_assists'] = 0
    data['d_players_mean_assists'] = 0
    data['r_players_heroes_mean_assists'] = 0
    data['d_players_heroes_mean_assists'] = 0

    data['r_players_mean_last_hits'] = 0
    data['d_players_mean_last_hits'] = 0
    data['r_players_heroes_mean_last_hits'] = 0
    data['d_players_heroes_mean_last_hits'] = 0

    data['r_players_mean_denies'] = 0
    data['d_players_mean_denies'] = 0
    data['r_players_heroes_mean_denies'] = 0
    data['d_players_heroes_mean_denies'] = 0

    data['r_players_mean_gpm'] = 0
    data['d_players_mean_gpm'] = 0
    data['r_players_heroes_mean_gpm'] = 0
    data['d_players_heroes_mean_gpm'] = 0

    data['r_players_mean_xpm'] = 0
    data['d_players_mean_xpm'] = 0
    data['r_players_heroes_mean_xpm'] = 0
    data['d_players_heroes_mean_xpm'] = 0

    heroes_id = set(list(data[[f'r_{i}' for i in range(1, 6)]].values.ravel()) + list(
        data[[f'd_{i}' for i in range(1, 6)]].values.ravel()))

    for index, player in enumerate(players_mean):
        if int(player) in players_id:
            for i in range(1, 6):
                r_player = f'r_{i}_player_id'
                d_player = f'd_{i}_player_id'

                data.loc[data[r_player] == int(player), 'r_players_mean_duration'] += players_mean[player]['duration']
                data.loc[data[d_player] == int(player), 'd_players_mean_duration'] += players_mean[player]['duration']

                data.loc[data[r_player] == int(player), 'r_players_mean_winrate'] += players_mean[player]['wins']
                data.loc[data[d_player] == int(player), 'd_players_mean_winrate'] += players_mean[player]['wins']

                data.loc[data[r_player] == int(player), 'r_players_mean_score'] += players_mean[player]['score_mean']
                data.loc[data[d_player] == int(player), 'd_players_mean_score'] += players_mean[player]['score_mean']

                data.loc[data[r_player] == int(player), 'r_players_mean_deaths'] += players_mean[player]['deaths_mean']
                data.loc[data[d_player] == int(player), 'd_players_mean_deaths'] += players_mean[player]['deaths_mean']

                data.loc[data[r_player] == int(player), 'r_players_mean_assists'] += players_mean[player]['assists']
                data.loc[data[d_player] == int(player), 'd_players_mean_assists'] += players_mean[player]['assists']

                data.loc[data[r_player] == int(player), 'r_players_mean_last_hits'] += players_mean[player]['last_hits']
                data.loc[data[d_player] == int(player), 'd_players_mean_last_hits'] += players_mean[player]['last_hits']

                data.loc[data[r_player] == int(player), 'r_players_mean_denies'] += players_mean[player]['denies']
                data.loc[data[d_player] == int(player), 'd_players_mean_denies'] += players_mean[player]['denies']

                data.loc[data[r_player] == int(player), 'r_players_mean_gpm'] += players_mean[player]['gold_per_min']
                data.loc[data[d_player] == int(player), 'd_players_mean_gpm'] += players_mean[player]['gold_per_min']

                data.loc[data[r_player] == int(player), 'r_players_mean_xpm'] += players_mean[player]['xp_per_min']
                data.loc[data[d_player] == int(player), 'd_players_mean_xpm'] += players_mean[player]['xp_per_min']
            for hero in players_mean[player]['heroes']:
                if int(hero) in heroes_id:
                    for i in range(1, 6):
                        r_hero = f'r_{i}'
                        d_hero = f'd_{i}'
                        r_player = f'r_{i}_player_id'
                        d_player = f'd_{i}_player_id'
                        data.loc[(data[r_player] == int(player)) & (
                                data[r_hero] == int(hero)), 'r_players_heroes_mean_duration'] += \
                            players_mean[player]['heroes'][hero]['duration']
                        data.loc[(data[d_player] == int(player)) & (
                                data[d_hero] == int(hero)), 'd_players_heroes_mean_duration'] += \
                            players_mean[player]['heroes'][hero]['duration']

                        data.loc[(data[r_player] == int(player)) & (
                                data[r_hero] == int(hero)), 'r_players_heroes_mean_winrate'] += \
                            players_mean[player]['heroes'][hero]['wins']
                        data.loc[(data[d_player] == int(player)) & (
                                data[d_hero] == int(hero)), 'd_players_heroes_mean_winrate'] += \
                            players_mean[player]['heroes'][hero]['wins']

                        data.loc[
                            (data[r_player] == int(player)) & (
                                        data[r_hero] == int(hero)), 'r_players_heroes_mean_score'] += \
                            players_mean[player]['heroes'][hero]['score_mean']
                        data.loc[
                            (data[d_player] == int(player)) & (
                                        data[d_hero] == int(hero)), 'd_players_heroes_mean_score'] += \
                            players_mean[player]['heroes'][hero]['score_mean']

                        data.loc[(data[r_player] == int(player)) & (
                                data[r_hero] == int(hero)), 'r_players_heroes_mean_deaths'] += \
                            players_mean[player]['heroes'][hero]['deaths_mean']
                        data.loc[(data[d_player] == int(player)) & (
                                data[d_hero] == int(hero)), 'd_players_heroes_mean_deaths'] += \
                            players_mean[player]['heroes'][hero]['deaths_mean']

                        data.loc[(data[r_player] == int(player)) & (
                                data[r_hero] == int(hero)), 'r_players_heroes_mean_assists'] += \
                            players_mean[player]['heroes'][hero]['assists']
                        data.loc[(data[d_player] == int(player)) & (
                                data[d_hero] == int(hero)), 'd_players_heroes_mean_assists'] += \
                            players_mean[player]['heroes'][hero]['assists']

                        data.loc[(data[r_player] == int(player)) & (
                                data[r_hero] == int(hero)), 'r_players_heroes_mean_last_hits'] += \
                            players_mean[player]['heroes'][hero]['last_hits']
                        data.loc[(data[d_player] == int(player)) & (
                                data[d_hero] == int(hero)), 'd_players_heroes_mean_last_hits'] += \
                            players_mean[player]['heroes'][hero]['last_hits']

                        data.loc[(data[r_player] == int(player)) & (
                                data[r_hero] == int(hero)), 'r_players_heroes_mean_denies'] += \
                            players_mean[player]['heroes'][hero]['denies']
                        data.loc[(data[d_player] == int(player)) & (
                                data[d_hero] == int(hero)), 'd_players_heroes_mean_denies'] += \
                            players_mean[player]['heroes'][hero]['denies']

                        data.loc[
                            (data[r_player] == int(player)) & (
                                        data[r_hero] == int(hero)), 'r_players_heroes_mean_gpm'] += \
                            players_mean[player]['heroes'][hero]['gold_per_min']
                        data.loc[
                            (data[d_player] == int(player)) & (
                                        data[d_hero] == int(hero)), 'd_players_heroes_mean_gpm'] += \
                            players_mean[player]['heroes'][hero]['gold_per_min']

                        data.loc[
                            (data[r_player] == int(player)) & (
                                        data[r_hero] == int(hero)), 'r_players_heroes_mean_xpm'] += \
                            players_mean[player]['heroes'][hero]['xp_per_min']
                        data.loc[
                            (data[d_player] == int(player)) & (
                                        data[d_hero] == int(hero)), 'd_players_heroes_mean_xpm'] += \
                            players_mean[player]['heroes'][hero]['xp_per_min']

    data['r_players_mean_duration'] /= 5
    data['d_players_mean_duration'] /= 5
    data['r_players_heroes_mean_duration'] /= 5
    data['d_players_heroes_mean_duration'] /= 5

    data['r_players_mean_winrate'] /= 5
    data['d_players_mean_winrate'] /= 5
    data['r_players_heroes_mean_winrate'] /= 5
    data['d_players_heroes_mean_winrate'] /= 5

    data['r_players_mean_score'] /= 5
    data['d_players_mean_score'] /= 5
    data['r_players_heroes_mean_score'] /= 5
    data['d_players_heroes_mean_score'] /= 5

    data['r_players_mean_deaths'] /= 5
    data['d_players_mean_deaths'] /= 5
    data['r_players_heroes_mean_deaths'] /= 5
    data['d_players_heroes_mean_deaths'] /= 5

    data['r_players_mean_assists'] /= 5
    data['d_players_mean_assists'] /= 5
    data['r_players_heroes_mean_assists'] /= 5
    data['d_players_heroes_mean_assists'] /= 5

    data['r_players_mean_last_hits'] /= 5
    data['d_players_mean_last_hits'] /= 5
    data['r_players_heroes_mean_last_hits'] /= 5
    data['d_players_heroes_mean_last_hits'] /= 5

    data['r_players_mean_denies'] /= 5
    data['d_players_mean_denies'] /= 5
    data['r_players_heroes_mean_denies'] /= 5
    data['d_players_heroes_mean_denies'] /= 5

    data['r_players_mean_gpm'] /= 5
    data['d_players_mean_gpm'] /= 5
    data['r_players_heroes_mean_gpm'] /= 5
    data['d_players_heroes_mean_gpm'] /= 5

    data['r_players_mean_xpm'] /= 5
    data['d_players_mean_xpm'] /= 5
    data['r_players_heroes_mean_xpm'] /= 5
    data['d_players_heroes_mean_xpm'] /= 5

    return data


def input_heroes_info(data):
    with open('../duration_info/heroes_mean.json') as file:
        heroes_mean = json.load(file)

    heroes_id = set(list(data[[f'r_{i}' for i in range(1, 6)]].values.ravel()) + list(
        data[[f'd_{i}' for i in range(1, 6)]].values.ravel()))

    data['r_hero_mean_duration'] = 0
    data['d_hero_mean_duration'] = 0

    data['r_hero_mean_winrate'] = 0
    data['d_hero_mean_winrate'] = 0

    data['r_hero_mean_score'] = 0
    data['d_hero_mean_score'] = 0

    data['r_hero_mean_deaths'] = 0
    data['d_hero_mean_deaths'] = 0

    data['r_hero_mean_assists'] = 0
    data['d_hero_mean_assists'] = 0

    data['r_hero_mean_last_hits'] = 0
    data['d_hero_mean_last_hits'] = 0

    data['r_hero_mean_denies'] = 0
    data['d_hero_mean_denies'] = 0

    data['r_hero_mean_gpm'] = 0
    data['d_hero_mean_gpm'] = 0

    data['r_hero_mean_xpm'] = 0
    data['d_hero_mean_xpm'] = 0
    for hero in heroes_mean:
        if int(hero) in heroes_id:
            for i in range(1, 6):
                r_hero = f'r_{i}'
                d_hero = f'd_{i}'

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_duration'] += heroes_mean[hero]['duration']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_duration'] += heroes_mean[hero]['duration']

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_winrate'] += heroes_mean[hero]['wins']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_winrate'] += heroes_mean[hero]['wins']

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_score'] += heroes_mean[hero]['score_mean']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_score'] += heroes_mean[hero]['score_mean']

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_deaths'] += heroes_mean[hero]['deaths_mean']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_deaths'] += heroes_mean[hero]['deaths_mean']

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_assists'] += heroes_mean[hero]['assists']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_assists'] += heroes_mean[hero]['assists']

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_last_hits'] += heroes_mean[hero]['last_hits']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_last_hits'] += heroes_mean[hero]['last_hits']

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_denies'] += heroes_mean[hero]['denies']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_denies'] += heroes_mean[hero]['denies']

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_gpm'] += heroes_mean[hero]['gold_per_min']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_gpm'] += heroes_mean[hero]['gold_per_min']

                data.loc[data[r_hero] == int(hero), 'r_hero_mean_xpm'] += heroes_mean[hero]['xp_per_min']
                data.loc[data[d_hero] == int(hero), 'd_hero_mean_xpm'] += heroes_mean[hero]['xp_per_min']

    data['r_hero_mean_duration'] /= 5
    data['d_hero_mean_duration'] /= 5

    data['r_hero_mean_winrate'] /= 5
    data['d_hero_mean_winrate'] /= 5

    data['r_hero_mean_score'] /= 5
    data['d_hero_mean_score'] /= 5

    data['r_hero_mean_deaths'] /= 5
    data['d_hero_mean_deaths'] /= 5

    data['r_hero_mean_assists'] /= 5
    data['d_hero_mean_assists'] /= 5

    data['r_hero_mean_last_hits'] /= 5
    data['d_hero_mean_last_hits'] /= 5

    data['r_hero_mean_denies'] /= 5
    data['d_hero_mean_denies'] /= 5

    data['r_hero_mean_gpm'] /= 5
    data['d_hero_mean_gpm'] /= 5

    data['r_hero_mean_xpm'] /= 5
    data['d_hero_mean_xpm'] /= 5

    return data


def input_five_player_together_info(data):
    with open('../duration_info/five_man_mean.json') as file:
        five_man_mean = json.load(file)

    data['r_five_players_id'] = 0
    data['d_five_players_id'] = 0
    for i in range(data.shape[0]):
        radiant = []
        dire = []
        for j in range(1, 6):
            r = f'r_{j}_player_id'
            d = f'd_{j}_player_id'
            radiant.append(data.loc[i, r])
            dire.append(data.loc[i, d])
        radiant = ''.join(map(str, sorted(radiant)))
        dire = ''.join(map(str, sorted(dire)))
        data.loc[i, 'r_five_players_id'] = radiant
        data.loc[i, 'd_five_players_id'] = dire

    data['r_five_mean_duration'] = 0
    data['d_five_mean_duration'] = 0

    data['r_five_mean_winrate'] = 0
    data['d_five_mean_winrate'] = 0

    data['r_five_mean_score'] = 0
    data['d_five_mean_score'] = 0

    data['r_five_mean_deaths'] = 0
    data['d_five_mean_deaths'] = 0

    data['r_five_mean_assists'] = 0
    data['d_five_mean_assists'] = 0

    data['r_five_mean_last_hits'] = 0
    data['d_five_mean_last_hits'] = 0

    data['r_five_mean_denies'] = 0
    data['d_five_mean_denies'] = 0

    data['r_five_mean_gpm'] = 0
    data['d_five_mean_gpm'] = 0

    data['r_five_mean_xpm'] = 0
    data['d_five_mean_xpm'] = 0

    for five in five_man_mean:
        if five in data[['r_five_players_id', 'd_five_players_id']].values:
            data.loc[data['r_five_players_id'] == five, 'r_five_mean_duration'] = five_man_mean[five]['duration']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_duration'] = five_man_mean[five]['duration']

            data.loc[data['r_five_players_id'] == five, 'r_five_mean_winrate'] = five_man_mean[five]['wins']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_winrate'] = five_man_mean[five]['wins']

            data.loc[data['r_five_players_id'] == five, 'r_five_mean_score'] = five_man_mean[five]['score_mean']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_score'] = five_man_mean[five]['score_mean']

            data.loc[data['r_five_players_id'] == five, 'r_five_mean_deaths'] = five_man_mean[five]['deaths_mean']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_deaths'] = five_man_mean[five]['deaths_mean']

            data.loc[data['r_five_players_id'] == five, 'r_five_mean_assists'] = five_man_mean[five]['assists']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_assists'] = five_man_mean[five]['assists']

            data.loc[data['r_five_players_id'] == five, 'r_five_mean_last_hits'] = five_man_mean[five]['last_hits']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_last_hits'] = five_man_mean[five]['last_hits']

            data.loc[data['r_five_players_id'] == five, 'r_five_mean_denies'] = five_man_mean[five]['denies']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_denies'] = five_man_mean[five]['denies']

            data.loc[data['r_five_players_id'] == five, 'r_five_mean_gpm'] = five_man_mean[five]['gold_per_min']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_gpm'] = five_man_mean[five]['gold_per_min']

            data.loc[data['r_five_players_id'] == five, 'r_five_mean_xpm'] = five_man_mean[five]['xp_per_min']
            data.loc[data['d_five_players_id'] == five, 'd_five_mean_xpm'] = five_man_mean[five]['xp_per_min']
    return data


def input_heroes_stat(data):
    url = 'https://api.opendota.com/api/heroStats'
    heroes_stats = requests.get(url).json()

    heroes = {}
    for hero in heroes_stats:
        heroes[hero['hero_id']] = hero

    data['r_heroes_players_mean_health'] = 0
    data['d_heroes_players_mean_health'] = 0

    data['r_heroes_players_mean_armor'] = 0
    data['d_heroes_players_mean_armor'] = 0

    data['r_heroes_players_mean_mana'] = 0
    data['d_heroes_players_mean_mana'] = 0
    for i in data.index:
        try:
            r_hero_id = list(data.loc[i, [f'r_{i}' for i in range(1, 6)]].values)
            d_hero_id = list(data.loc[i, [f'd_{i}' for i in range(1, 6)]].values)

            r_players_id = list(data.loc[i, [f'r_{i}_player_id' for i in range(1, 6)]].values)
            d_players_id = list(data.loc[i, [f'd_{i}_player_id' for i in range(1, 6)]].values)

            r_stats = get_stats(r_hero_id, r_players_id)
            d_stats = get_stats(d_hero_id, d_players_id)

            data.loc[i, 'r_heroes_players_mean_health'] = r_stats[0]
            data.loc[i, 'd_heroes_players_mean_health'] = d_stats[0]

            data.loc[i, 'r_heroes_players_mean_armor'] = r_stats[1]
            data.loc[i, 'd_heroes_players_mean_armor'] = d_stats[1]

            data.loc[i, 'r_heroes_players_mean_mana'] = r_stats[2]
            data.loc[i, 'd_heroes_players_mean_mana'] = d_stats[2]
        except:
            pass
    return data




def input_app_info(data):
    for func in [input_orgs_info, input_players_info, input_heroes_info, input_five_player_together_info, input_heroes_stat]:
        data = func(data)
    return data


def get_lvl(duration, xpm):
    duration /= 60
    xpm = xpm * duration
    lvl = 1
    while True:
        if xpm - lvl * 100 < 0:
            lvl += xpm / ((lvl+1) * 100)
            break
        else:
            xpm -= lvl * 100
        lvl += 1
    return round(lvl, 2)


def get_stats(heroes_id, players_id):
    stats = {}
    stats['health'] = 0
    stats['mana'] = 0
    stats['armor'] = 0
    for hero, player in zip(heroes_id, players_id):
        lvl = get_lvl(players_mean[str(player)]['heroes'][str(hero)]['duration'],
                      players_mean[str(player)]['heroes'][str(hero)]['xp_per_min'])

        stats['health'] += heroes[hero]['base_health']
        stats['armor'] += heroes[hero]['base_armor']
        stats['mana'] += heroes[hero]['base_mana']

        strange = lvl * heroes[hero]['str_gain'] + heroes[hero]['base_str']
        agility = lvl * heroes[hero]['agi_gain'] + heroes[hero]['base_agi']
        intellect = lvl * heroes[hero]['int_gain'] + heroes[hero]['base_int']

        stats['health'] += strange * 20
        stats['armor'] += agility * 0.16
        stats['mana'] += intellect * 12

    stats['health'] /= 5
    stats['armor'] /= 5
    stats['mana'] /= 5

    stats['health'] = round(stats['health'], 2)
    stats['armor'] = round(stats['armor'], 2)
    stats['mana'] = round(stats['mana'], 2)
    return stats['health'], stats['armor'], stats['mana']