import numpy as np
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import scipy

import data
import GMR_data
from tourism_data import *


def get_histogram_values(scale):
    counter = 0
    histogram_values_list = []
    scale_0 = 0
    scale_1 = scale
    while counter != len(Department_tourism_2019_list):
        L = 0
        for val in Department_tourism_2019_list:
            if scale_0 <= val and val < scale_1:
                L += 1
                counter += 1
        histogram_values_list += [L]
        scale_0 = scale_1
        scale_1 += scale
    return histogram_values_list


def get_department_index(dep):
    """
    Get french department index
    :param dep: str
    :return: int
    """
    dep_num = None
    for d_num in range(len(data.departments_list)):
        if data.departments_list[d_num] == dep:
            dep_num = d_num
    assert (dep_num != None), "Department not in data.departments_list"
    return dep_num


def get_covid_case_list(dep):
    """
    Get the confirmed covid list of one french department.
    :param dep: str, french department from departments_list
    :return: numpy.ndarray
    """
    dep_num = get_department_index(dep)
    res_list = []
    for t_list in data.confirmed_covid_france_list:
        res_list += [t_list[dep_num]]
    return np.asarray(res_list)


def get_covid_case_list_2(dep):
    """
    Get the confirmed covid list of one french department. NORMALIZE
    :param dep: str, french department from departments_list
    :return: numpy.ndarray
    """
    dep_num = get_department_index(dep)
    dep_pop = data.french_department_population[dep_num]
    res_list = []
    for t_list in data.confirmed_covid_france_value_ma_list:
        if t_list[dep_num] == None:
            res_list += [None]
        else:
            res_list += [t_list[dep_num] / dep_pop]
    return np.asarray(res_list)


def None_replace(GMR_list):
    for i in range(len(GMR_list)):
        if GMR_list[i] == None:
            if i <= 6:
                print("No simplification")
                return GMR_list
            if i > 6:
                GMR_list[i] = (GMR_list[i - 7] + 2 * GMR_list[i - 6] + 3 * GMR_list[i - 5] + 4 * GMR_list[i - 4] + 5 *
                               GMR_list[i - 3] + 6 * GMR_list[i - 2] + 7 * GMR_list[i - 1]) / 28
    return GMR_list


def get_GMR_list(var):
    """
    Get the GMR data for one country, region or department.
    :param var: numpy.ndarray
    :return: numpy.ndarray
    """
    """ 
    RAR : retail_and_recreation_percent_change_from_baseline
    GAP : grocery_and_pharmacy_percent_change_from_baseline
    PAR : parks_percent_change_from_baseline
    TAS : transit_stations_percent_change_from_baseline
    WOR : workplaces_percent_change_from_baseline
    RES : residential_percent_change_from_baseline 
    """
    RAR, GAP, PAR, TAS, WOR, RES = [], [], [], [], [], []
    for t_list in var:
        # print(t_list)
        RAR += [t_list[0]]
        GAP += [t_list[1]]
        PAR += [t_list[2]]
        TAS += [t_list[3]]
        WOR += [t_list[4]]
        RES += [t_list[5]]
    return [np.asarray(None_replace(RAR)), np.asarray(None_replace(GAP)), np.asarray(None_replace(PAR)),
            np.asarray(None_replace(TAS)), np.asarray(None_replace(WOR)), np.asarray(None_replace(RES))]


def select_list(name):
    # Country
    if name == "France":
        return GMR_data.GMR_France
    # Regions
    elif name == "Auvergne-Rhône-Alpes":
        return GMR_data.GMR_France_AuvergneRhoneAlpes
    elif name == "Brittany":
        return GMR_data.GMR_France_Brittany
    elif name == "Bourgogne-Franche-Comté":
        return GMR_data.GMR_France_BourgogneFrancheComte
    elif name == "Corsica":
        return GMR_data.GMR_France_Corsica
    elif name == "Centre-Val de Loire":
        return GMR_data.GMR_France_CentreValDeLoire
    elif name == "Grand Est":
        return GMR_data.GMR_France_GrandEst
    elif name == "Hauts de France":
        return GMR_data.GMR_France_HautsDeFrance
    elif name == "Ile de France":
        return GMR_data.GMR_France_IleDeFrance
    elif name == "Nouvelle Aquitaine":
        return GMR_data.GMR_France_NouvelleAquitaine
    elif name == "Normandy":
        return GMR_data.GMR_France_Normandy
    elif name == "Occitanie":
        return GMR_data.GMR_France_Occitanie
    elif name == "Pays de la Loire":
        return GMR_data.GMR_France_PaysDeLaLoire
    elif name == "Provence-Alpes-Côte d\'Azur":
        return GMR_data.GMR_France_ProvenceAlpesCoteDAzur
    # Departments
    elif name == "Ain":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Ain
    elif name == "Aisne":
        return GMR_data.GMR_France_HautsDeFrance_Aisne
    elif name == "Allier":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Allier
    elif name == "Alpes-de-Haute-Provence":
        return GMR_data.GMR_France_ProvenceAlpesCoteDAzur_AlpesDeHauteProvence
    elif name == "Hautes-Alpes":
        return GMR_data.GMR_France_ProvenceAlpesCoteDAzur_HautesAlpes
    elif name == "Alpes-Maritimes":
        return GMR_data.GMR_France_ProvenceAlpesCoteDAzur_AlpesMaritimes
    elif name == "Ardèche":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Ardeche
    elif name == "Ardennes":
        return GMR_data.GMR_France_GrandEst_Ardennes
    elif name == "Ariège":
        return GMR_data.GMR_France_Occitanie_Ariege
    elif name == "Aube":
        return GMR_data.GMR_France_GrandEst_Aube
    elif name == "Aude":
        return GMR_data.GMR_France_Occitanie_Aude
    elif name == "Aveyron":
        return GMR_data.GMR_France_Occitanie_Aveyron
    elif name == "Bouches-du-Rhône":
        return GMR_data.GMR_France_ProvenceAlpesCoteDAzur_BouchesDuRhone
    elif name == "Calvados":
        return GMR_data.GMR_France_Normandy_Calvados
    elif name == "Cantal":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Cantal
    elif name == "Charente":
        return GMR_data.GMR_France_NouvelleAquitaine_Charente
    elif name == "Charente-Maritime":
        return GMR_data.GMR_France_NouvelleAquitaine_CharenteMaritime
    elif name == "Cher":
        return GMR_data.GMR_France_CentreValDeLoire_Cher
    elif name == "Corrèze":
        return GMR_data.GMR_France_NouvelleAquitaine_Correze
    elif name == "Corse-du-Sud":
        return GMR_data.GMR_France_Corsica_CorseDuSud
    elif name == "Haute-Corse":
        return GMR_data.GMR_France_Corsica_HauteCorse
    elif name == "Côte-d\'Or":
        return GMR_data.GMR_France_BourgogneFrancheComte_CoteDOr
    elif name == "Côtes-d\'Armor":
        return GMR_data.GMR_France_Brittany_CotesDArmor
    elif name == "Creuse":
        return GMR_data.GMR_France_NouvelleAquitaine_Creuse
    elif name == "Dordogne":
        return GMR_data.GMR_France_NouvelleAquitaine_Dordogne
    elif name == "Doubs":
        return GMR_data.GMR_France_BourgogneFrancheComte_Doubs
    elif name == "Drôme":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Drome
    elif name == "Eure":
        return GMR_data.GMR_France_Normandy_Eure
    elif name == "Eure-et-Loir":
        return GMR_data.GMR_France_CentreValDeLoire_EureEtLoir
    elif name == "Finistère":
        return GMR_data.GMR_France_Brittany_Finistere
    elif name == "Gard":
        return GMR_data.GMR_France_Occitanie_Gard
    elif name == "Haute-Garonne":
        return GMR_data.GMR_France_Occitanie_HauteGaronne
    elif name == "Gers":
        return GMR_data.GMR_France_Occitanie_Gers
    elif name == "Gironde":
        return GMR_data.GMR_France_NouvelleAquitaine_Gironde
    elif name == "Hérault":
        return GMR_data.GMR_France_Occitanie_Herault
    elif name == "Ille-et-Vilaine":
        return GMR_data.GMR_France_Brittany_IlleEtVilaine
    elif name == "Indre":
        return GMR_data.GMR_France_CentreValDeLoire_Indre
    elif name == "Indre-et-Loire":
        return GMR_data.GMR_France_CentreValDeLoire_IndreEtLoire
    elif name == "Isère":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Isere
    elif name == "Jura":
        return GMR_data.GMR_France_BourgogneFrancheComte_Jura
    elif name == "Landes":
        return GMR_data.GMR_France_NouvelleAquitaine_Landes
    elif name == "Loir-et-Cher":
        return GMR_data.GMR_France_CentreValDeLoire_LoirEtCher
    elif name == "Loire":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Loire
    elif name == "Haute-Loire":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_HauteLoire
    elif name == "Loire-Atlantique":
        return GMR_data.GMR_France_PaysDeLaLoire_LoireAtlantique
    elif name == "Loiret":
        return GMR_data.GMR_France_CentreValDeLoire_Loiret
    elif name == "Lot":
        return GMR_data.GMR_France_Occitanie_Lot
    elif name == "Lot-et-Garonne":
        return GMR_data.GMR_France_NouvelleAquitaine_LotEtGaronne
    elif name == "Lozère":
        return GMR_data.GMR_France_Occitanie_Lozere
    elif name == "Maine-et-Loire":
        return GMR_data.GMR_France_PaysDeLaLoire_MaineEtLoire
    elif name == "Manche":
        return GMR_data.GMR_France_Normandy_Manche
    elif name == "Marne":
        return GMR_data.GMR_France_GrandEst_Marne
    elif name == "Haute-Marne":
        return GMR_data.GMR_France_GrandEst_HauteMarne
    elif name == "Mayenne":
        return GMR_data.GMR_France_PaysDeLaLoire_Mayenne
    elif name == "Meurthe-et-Moselle":
        return GMR_data.GMR_France_GrandEst_MeurtheEtMoselle
    elif name == "Meuse":
        return GMR_data.GMR_France_GrandEst_Meuse
    elif name == "Morbihan":
        return GMR_data.GMR_France_Brittany_Morbihan
    elif name == "Moselle":
        return GMR_data.GMR_France_GrandEst_Moselle
    elif name == "Nièvre":
        return GMR_data.GMR_France_BourgogneFrancheComte_Nievre
    elif name == "Nord":
        return GMR_data.GMR_France_HautsDeFrance_Nord
    elif name == "Oise":
        return GMR_data.GMR_France_HautsDeFrance_Oise
    elif name == "Orne":
        return GMR_data.GMR_France_Normandy_Orne
    elif name == "Pas-de-Calais":
        return GMR_data.GMR_France_HautsDeFrance_PasDeCalais
    elif name == "Puy-de-Dôme":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_PuyDeDome
    elif name == "Pyrénées-Atlantique":
        return GMR_data.GMR_France_NouvelleAquitaine_PyreneesAtlantique
    elif name == "Hautes-Pyrénées":
        return GMR_data.GMR_France_Occitanie_HautesPyrenees
    elif name == "Pyrénées-Orientales":
        return GMR_data.GMR_France_Occitanie_PyreneesOrientales
    elif name == "Bas-Rhin":
        return GMR_data.GMR_France_GrandEst_BasRhin
    elif name == "Haut-Rhin":
        return GMR_data.GMR_France_GrandEst_HautRhin
    elif name == "Rhône":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Rhone
    elif name == "Haute-Saône":
        return GMR_data.GMR_France_BourgogneFrancheComte_HauteSaone
    elif name == "Saône-et-Loire":
        return GMR_data.GMR_France_BourgogneFrancheComte_SaoneEtLoire
    elif name == "Sarthe":
        return GMR_data.GMR_France_PaysDeLaLoire_Sarthe
    elif name == "Savoie":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_Savoie
    elif name == "Haute-Savoie":
        return GMR_data.GMR_France_AuvergneRhoneAlpes_HauteSavoie
    elif name == "Paris":
        return GMR_data.GMR_France_IleDeFrance_Paris
    elif name == "Seine-Maritime":
        return GMR_data.GMR_France_Normandy_SeineMaritime
    elif name == "Seine-et-Marne":
        return GMR_data.GMR_France_IleDeFrance_SeineEtMarne
    elif name == "Yvelines":
        return GMR_data.GMR_France_IleDeFrance_Yvelines
    elif name == "Deux-Sèvres":
        return GMR_data.GMR_France_NouvelleAquitaine_DeuxSevres
    elif name == "Somme":
        return GMR_data.GMR_France_HautsDeFrance_Somme
    elif name == "Tarn":
        return GMR_data.GMR_France_Occitanie_Tarn
    elif name == "Tarn-et-Garonne":
        return GMR_data.GMR_France_Occitanie_TarnEtGaronne
    elif name == "Var":
        return GMR_data.GMR_France_ProvenceAlpesCoteDAzur_Var
    elif name == "Vaucluse":
        return GMR_data.GMR_France_ProvenceAlpesCoteDAzur_Vaucluse
    elif name == "Vendée":
        return GMR_data.GMR_France_PaysDeLaLoire_Vendee
    elif name == "Vienne":
        return GMR_data.GMR_France_NouvelleAquitaine_Vienne
    elif name == "Haute-Vienne":
        return GMR_data.GMR_France_NouvelleAquitaine_HauteVienne
    elif name == "Vosges":
        return GMR_data.GMR_France_GrandEst_Vosges
    elif name == "Yonne":
        return GMR_data.GMR_France_BourgogneFrancheComte_Yonne
    elif name == "Territoire de Belfort":
        return GMR_data.GMR_France_BourgogneFrancheComte_TerritoireDeBelfort
    elif name == "Essonne":
        return GMR_data.GMR_France_IleDeFrance_Essonne
    elif name == "Hauts-de-Seine":
        return GMR_data.GMR_France_IleDeFrance_HautsDeSeine
    elif name == "Seine-Saint-Denis":
        return GMR_data.GMR_France_IleDeFrance_SeineSaintDenis
    elif name == "Val-de-Marne":
        return GMR_data.GMR_France_IleDeFrance_ValDeMarne
    elif name == "Val-d\'Oise":
        return GMR_data.GMR_France_IleDeFrance_ValDOise


def get_moving_av_list(GMR_list):
    new_list = np.zeros(len(GMR_list) - 4)
    for i in range(2, len(GMR_list) - 2):
        new_list[i - 2] = (GMR_list[i - 2] + 2 * GMR_list[i - 1] + 3 * GMR_list[i] + 2 * GMR_list[i + 1] + GMR_list[
            i + 2]) / 9
    return new_list


def get_moving_av_list_2(GMR_list):
    new_list = np.zeros(len(GMR_list) - 14)
    for i in range(7, len(GMR_list) - 7):
        new_list[i - 7] = (GMR_list[i - 7] + 2 * GMR_list[i - 6] + 3 * GMR_list[i - 5] + 4 * GMR_list[i - 4] + 5 *
                           GMR_list[i - 3] + 6 * GMR_list[i - 2] + 7 * GMR_list[i - 1] + 8 * GMR_list[i] + GMR_list[
                               i + 7] + 2 * GMR_list[i + 6] + 3 * GMR_list[i + 5] + 4 * GMR_list[i + 4] + 5 * GMR_list[
                               i + 3] + 6 * GMR_list[i + 2] + 7 * GMR_list[i + 1]) / 67
    return new_list


def get_PAR_max_list(name_list):
    new_list = []
    for name in name_list:
        print(name)
        new_list += [[int(np.max(get_moving_av_list_2(get_GMR_list(select_list(name))[2])))]]
    return new_list


def get_GMR_fig(name_list, GMR_selection, mov_av):
    fig = make_subplots(rows=1, cols=1)
    if len(GMR_selection) == 1 and len(name_list) == 1:
        title = "{} - {} - COVID 19".format(name_list[0], GMR_selection[0])
    elif len(GMR_selection) == 1:
        title = "{} - COVID 19".format(GMR_selection[0])
    else:
        title = "Google mobility report - COVID 19"
    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (day/month)'},
        yaxis={'title': 'Percentage'})
    if "RAR" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[0],
                    name="{} RAR".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[2:-2],
                    y=get_moving_av_list(get_GMR_list(select_list(name))[0]),
                    name="{} RAR".format(name))
    if "GAP" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[1],
                    name="{} GAP".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[2:-2],
                    y=get_moving_av_list(get_GMR_list(select_list(name))[1]),
                    name="{} GAP".format(name))
    if "PAR" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[2],
                    name="{} PAR".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[2:-2],
                    y=get_moving_av_list(get_GMR_list(select_list(name))[2]),
                    name="{} PAR".format(name))
    if "TAS" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[3],
                    name="{} TAS".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[2:-2],
                    y=get_moving_av_list(get_GMR_list(select_list(name))[3]),
                    name="{} TAS".format(name))
    if "WOR" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[4],
                    name="{} WOR".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[2:-2],
                    y=get_moving_av_list(get_GMR_list(select_list(name))[4]),
                    name="{} WOR".format(name))
    if "RES" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[5],
                    name="{} RES".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[2:-2],
                    y=get_moving_av_list(get_GMR_list(select_list(name))[5]),
                    name="{} RES".format(name))

    return fig


def get_GMR_fig_2(name_list, GMR_selection, mov_av):
    fig = make_subplots(rows=1, cols=1)
    if len(GMR_selection) == 1 and len(name_list) == 1:
        title = "{} - {} - COVID 19".format(name_list[0], GMR_selection[0])
    elif len(GMR_selection) == 1:
        title = "{} - COVID 19".format(GMR_selection[0])
    else:
        title = "Google mobility report - COVID 19"
    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (day/month)'},
        yaxis={'title': 'Percentage'})
    if "RAR" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[0],
                    name="{} RAR".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[7:-7],
                    y=get_moving_av_list_2(get_GMR_list(select_list(name))[0]),
                    name="{} RAR".format(name))
    if "GAP" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[1],
                    name="{} GAP".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[7:-7],
                    y=get_moving_av_list_2(get_GMR_list(select_list(name))[1]),
                    name="{} GAP".format(name))
    if "PAR" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[2],
                    name="{} PAR".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[7:-7],
                    y=get_moving_av_list_2(get_GMR_list(select_list(name))[2]),
                    name="{} PAR".format(name))
    if "TAS" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[3],
                    name="{} TAS".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[7:-7],
                    y=get_moving_av_list_2(get_GMR_list(select_list(name))[3]),
                    name="{} TAS".format(name))
    if "WOR" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[4],
                    name="{} WOR".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[7:-7],
                    y=get_moving_av_list_2(get_GMR_list(select_list(name))[4]),
                    name="{} WOR".format(name))
    if "RES" in GMR_selection:
        for name in name_list:
            if mov_av == 'No':
                fig.add_scatter(
                    x=GMR_data.time_list_GMR,
                    y=get_GMR_list(select_list(name))[5],
                    name="{} RES".format(name))
            else:
                fig.add_scatter(
                    x=GMR_data.time_list_GMR[7:-7],
                    y=get_moving_av_list_2(get_GMR_list(select_list(name))[5]),
                    name="{} RES".format(name))

    return fig


def get_matrix(department_list, variable):
    """
    Give the matrix to make a clustering on GML data.
    :param department_list: numpy.ndarray
    :param variable: str, GML variable name
    :return: matrix to use find_clusters
    """
    matrix = [[] for i in range(len(GMR_data.time_list_GMR))]
    for dep in department_list:
        L = get_GMR_list(select_list(dep))
        period = len(L[0])
        if variable == "RAR":
            for t in range(period):
                matrix[t] += [L[0][t]]
        elif variable == "GAP":
            for t in range(period):
                matrix[t] += [L[1][t]]
        elif variable == "PAR":
            for t in range(period):
                matrix[t] += [L[2][t]]
        elif variable == "TAS":
            for t in range(period):
                matrix[t] += [L[3][t]]
        elif variable == "WOR":
            for t in range(period):
                matrix[t] += [L[4][t]]
        elif variable == "RES":
            for t in range(period):
                matrix[t] += [L[5][t]]
    return np.asarray(matrix)


def get_matrix2(department_list, variable, period):
    """
    Give the matrix to make a clustering on GML data.
    :param department_list: numpy.ndarray
    :param variable: str, GML variable name
    :param period: list, [start, end]
    :return: matrix to use find_clusters
    """
    matrix = [[] for i in range(period[1] - period[0])]
    for dep in department_list:
        L = get_GMR_list(select_list(dep))
        if variable == "RAR":
            for t in range(period[1] - period[0]):
                matrix[t] += [L[0][t + period[0]]]
        elif variable == "GAP":
            for t in range(period[1] - period[0]):
                matrix[t] += [L[1][t + period[0]]]
        elif variable == "PAR":
            for t in range(period[1] - period[0]):
                matrix[t] += [L[2][t + period[0]]]
        elif variable == "TAS":
            for t in range(period[1] - period[0]):
                matrix[t] += [L[3][t + period[0]]]
        elif variable == "WOR":
            for t in range(period[1] - period[0]):
                matrix[t] += [L[4][t + period[0]]]
        elif variable == "RES":
            for t in range(period[1] - period[0]):
                matrix[t] += [L[5][t + period[0]]]
    return np.asarray(matrix)


def reduction(matrix):
    """
    Reducing the matrix :
    - Subtraction of each column from its average
    - Division of each column by its standard deviation.
    :param matrix: numpy.ndarray
    :return: numpy.ndarray
    """
    new_matrix = np.copy(matrix.T)
    # Subtraction by the average.
    for i in range(new_matrix.shape[0]):
        new_matrix[i] = new_matrix[i] - np.mean(new_matrix[i])
    # Division by the standard deviation.
    for i in range(new_matrix.shape[0]):
        std = np.std(new_matrix[i])
        if std != 0:
            new_matrix[i] = new_matrix[i] / std
    return new_matrix.T


def process_matrix(DATA):
    """
    Calculation of eigenvalues and eigenvectors corresponding to the main components of DATA.
    :param DATA: numpy.ndarray
    :return: numpy.ndarray
    """
    data_reduced = reduction(DATA)
    corr_matrix = 1 / data_reduced.shape[0] * np.dot(data_reduced.T, data_reduced)
    print("corr_matrix is symetric :", np.all(corr_matrix == corr_matrix.T))
    print("corr_matrix is real :", np.all(corr_matrix == np.real(corr_matrix)))
    val_and_vec = scipy.linalg.eigh(corr_matrix)
    return val_and_vec


def sort_eigenvalues(eigen_values):
    """
    Obtaining eigenvalues sorted in descending order.
    :param eigen_values: numpy.ndarray
    :return: list
    """
    eigen_values = eigen_values.real
    for i in range(len(eigen_values)):
        if np.isclose(0, eigen_values[i]):
            eigen_values[i] = 0
        assert eigen_values[i] >= 0
    p = sum(eigen_values)
    supertuples = [(eigen_values[i], eigen_values[i] / p, i) for i in range(len(eigen_values))]
    supertuples.sort(reverse=True)
    return supertuples


def compute_new_data_matrix(DATA, eig_vectors, eig_values, n):
    """
    Calculation of the new data matrix evaluating each individual according to the new variables. If
    n < len(eig_values) the new matrix only contains the n most dispersive variables.
    :param DATA: numpy.ndarray -> Matrice de données initiale
    :param eig_vectors: numpy.ndarray
    :param eig_values: numpy.ndarray
    :param n: int
    :return: numpy.ndarray
    """
    assert n <= len(eig_values)

    eig_values = sort_eigenvalues(eig_values)
    eig_values = eig_values[:n]

    new_DATA = np.dot(reduction(DATA), eig_vectors)
    indexes = []
    for v in eig_values:
        indexes.append(v[2])
    new_DATA = new_DATA[:, indexes]
    return new_DATA


def find_clusters(new_DATA, nb_clusters):
    """
    Application of kmean clustering to find clusters.
    :param new_DATA: numpy.ndarray
    :param nb_clusters: int
    :return: tuple
    """
    kmeans = KMeans(n_clusters=nb_clusters, n_init=12).fit(new_DATA)
    labels = kmeans.labels_
    inertia = kmeans.inertia_
    return labels, inertia


def get_DATA_2D_in_clusters(DATA, nb_clusters):
    """
    Obtaining the projection of individuals in the space of the 3 variables of maximum inertia with clustering.
    :param DATA: numpy.ndarray
    :param nb_clusters: int
    :return: tuple
    """
    if nb_clusters > len(DATA):
        print("Not enough markers to distinguish all the clusters.")
    labels, inertia = find_clusters(DATA, nb_clusters)
    print("Inertia :", inertia)
    return labels, inertia


def plot_DATA_2D_in_clusters(DATA, labels):
    """
    Display of individuals in the space defined by the two eigenvectors representing the most important variables.
    dispersive.
    :param DATA: numpy.ndarray
    :param labels: numpy.ndarray
    :return: NoneType -> figure matplotlib.pyplot
    """
    K = np.max(labels)
    markerslist = [r"$\mathcal{A}$", r"$\mathcal{B}$", r"$\mathcal{C}$", r"$\mathcal{D}$",
                   r"$\mathcal{E}$", r"$\mathcal{F}$", r"$\mathcal{G}$", r"$\mathcal{H}$", r"$\mathcal{I}$",
                   r"$\mathcal{J}$", r"$\mathcal{K}$", r"$\mathcal{L}$", r"$\mathcal{M}$", r"$\mathcal{N}$",
                   r"$\mathcal{O}$", r"$\mathcal{P}$", r"$\mathcal{Q}$", r"$\mathcal{R}$", r"$\mathcal{S}$",
                   r"$\mathcal{T}$", r"$\mathcal{U}$", r"$\mathcal{V}$", r"$\mathcal{W}$", r"$\mathcal{X}$",
                   r"$\mathcal{Y}$", r"$\mathcal{Z}$"]
    cols = ["blue", "orange", "green", "red", "purple", "grey", "brown", "pink", "purple", "cyan", "beige", "deeppink"]

    for k in range(K + 1):
        l_x = []
        l_y = []
        for i, label in enumerate(labels):
            if label == k:
                indiv = DATA[i]
                x1 = indiv[0]
                y1 = indiv[1]
                l_x.append(x1)
                l_y.append(y1)

        plt.scatter(l_x, l_y, cmap="viridis", marker=markerslist[k], label="Group " + markerslist[k],
                    color=cols[k])  # ,edgecolor='black', linewidth='3')

    plt.gca().set_xlabel(r"Projection on $X'_1$ (in units of $\sigma'_1$)")
    plt.gca().set_ylabel(r"Projection on $X'_2$ (in units of $\sigma'_2$)")
    plt.legend()
