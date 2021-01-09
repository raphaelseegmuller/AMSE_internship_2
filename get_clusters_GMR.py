from libs.function import get_matrix2, find_clusters
from GMR_data import GMR_departments_list_2

Department_list = GMR_departments_list_2
GMR_var = "PAR"
Cluster_number = 2

### Period ###
start = 137
end = 138
period = [start, end]

M = get_matrix2(Department_list, GMR_var, period).transpose()

print("#####################################")

print(find_clusters(M, Cluster_number))
Cluster_list = find_clusters(M, Cluster_number)[0]
print("### Department | Cluster number ###")

for dep_nbr in range(len(Department_list)):
    print(Department_list[dep_nbr], " : ", Cluster_list[dep_nbr])

print("##################################")
