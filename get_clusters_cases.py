import numpy as np

from libs.function import find_clusters, get_covid_case_list_2

GMR_departments_list_test = np.array(["Ain", "Aisne", "Allier"
                                         , "Alpes-de-Haute-Provence", "Hautes-Alpes", "Alpes-Maritimes"
                                         , "Ardèche", "Ardennes", "Ariège"
                                         , "Aube", "Aude", "Aveyron"
                                         , "Bouches-du-Rhône", "Calvados", "Cantal"
                                         , "Charente", "Charente-Maritime", "Cher"
                                         , "Corrèze", "Côte-d\'Or", "Côtes-d\'Armor"
                                         , "Creuse", "Dordogne", "Doubs"
                                         , "Drôme", "Eure", "Eure-et-Loir"
                                         , "Finistère", "Corse-du-Sud", "Haute-Corse"
                                         , "Gard", "Haute-Garonne", "Gers"
                                         , "Gironde", "Hérault", "Ille-et-Vilaine"
                                         , "Indre", "Indre-et-Loire", "Isère"
                                         , "Jura", "Landes", "Loir-et-Cher"
                                         , "Loire", "Haute-Loire", "Loire-Atlantique"
                                         , "Loiret", "Lot", "Lot-et-Garonne"
                                         , "Lozère", "Maine-et-Loire", "Manche"
                                         , "Marne", "Haute-Marne", "Mayenne"
                                         , "Meurthe-et-Moselle", "Meuse", "Morbihan"
                                         , "Moselle", "Nièvre", "Nord"
                                         , "Oise", "Orne", "Pas-de-Calais"
                                         , "Puy-de-Dôme", "Hautes-Pyrénées"
                                         , "Pyrénées-Orientales", "Bas-Rhin", "Haut-Rhin"
                                         , "Rhône", "Haute-Saône", "Saône-et-Loire"
                                         , "Sarthe", "Savoie", "Haute-Savoie"
                                         , "Paris", "Seine-Maritime", "Seine-et-Marne"
                                         , "Yvelines", "Deux-Sèvres", "Somme"
                                         , "Tarn", "Tarn-et-Garonne", "Var"
                                         , "Vaucluse", "Vendée", "Vienne"
                                         , "Haute-Vienne", "Vosges", "Yonne"
                                         , "Territoire de Belfort", "Essonne", "Hauts-de-Seine"
                                         , "Seine-Saint-Denis", "Val-de-Marne", "Val-d\'Oise"])

Department_list = GMR_departments_list_test
Cluster_number = 2

M = []
for i in range(len(Department_list)):
    M += [[get_covid_case_list_2(Department_list[i])[104]]]
M = np.asarray(M)

print("#####################################")

print(find_clusters(M, Cluster_number))
Cluster_list = find_clusters(M, Cluster_number)[0]
print("### Department | Cluster number ###")
#
for dep_nbr in range(len(Department_list)):
    print(Department_list[dep_nbr], " : ", Cluster_list[dep_nbr])

print("##################################")
