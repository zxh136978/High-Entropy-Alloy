# Dictionary key order: 
# atomic number, atomic radius, electronegativity, valence electron number
# The sum of the components must be equal to 100%
import math

dict_atoms = {
    'H':  [1, 0.53,  2.20, 1],
    'He': [2, 1.22,  3.89, 2],
    'Li': [3, 1.52,  0.98, 1],
    'Be': [4, 1.11,  1.57, 2],
    'B':  [5, 0.83,  2.04, 3],
    'C':  [6, 0.77,  2.55, 4],
    'N':  [7, 0.70,  3.04, 5],
    'O':  [8, 0.66,  3.44, 6],
    'F':  [9, 0.72,  3.98, 7],
    'Ne': [10, 1.6,  3.67, 8],
    'Na': [11, 1.92, 0.93, 1],
    'Mg': [12, 1.60, 1.31, 2],
    'Al': [13, 1.43, 1.61, 3],
    'Si': [14, 1.17, 1.90, 4],
    'P':  [15, 1.15, 2.19, 5],
    'S':  [16, 1.04, 2.58, 6],
    'Cl': [17, 0.99, 3.16, 7],
    'Ar': [18, 1.91, 3.30, 8],
    'K':  [19, 2.27, 0.82, 1],
    'Ca': [20, 1.97, 1.00, 2],
    'Sc': [21, 1.61, 1.36, 3],
    'Ti': [22, 1.45, 1.54, 4],
    'V':  [23, 1.32, 1.63, 5],
    'Cr': [24, 1.25, 1.66, 6],
    'Mn': [25, 1.24, 1.55, 7],
    'Fe': [26, 1.24, 1.83, 8],
    'Co': [27, 1.25, 1.88, 9],
    'Ni': [28, 1.25, 1.91, 10],
    'Cu': [29, 1.28, 1.90, 11],
    'Zn': [30, 1.33, 1.65, 12],
    'Ga': [31, 1.22, 1.81, 3],
    'Ge': [32, 1.23, 2.01, 4],
    'As': [33, 1.25, 2.18, 5],
    'Se': [34, 1.14, 2.55, 6],
    'Br': [35, 1.11, 2.96, 7],
    'Kr': [36, 1.98, 3.00, 8],
    'Rb': [37, 2.48, 0.82, 1],
    'Sr': [38, 2.15, 0.95, 2],
    'Y':  [39, 1.81, 1.22, 3],
    'Zr': [40, 1.60, 1.33, 4],
    'Nb': [41, 1.43, 1.60, 5],
    'Mo': [42, 1.36, 2.16, 6],
    'Tc': [43, 1.36, 1.90, 7],
    'Ru': [44, 1.33, 2.20, 8],
    'Rh': [45, 1.35, 2.28, 9],
    'Pd': [46, 1.38, 2.20, 10],
    'Ag': [47, 1.44, 1.93, 11],
    'Cd': [48, 1.49, 1.69, 12],
    'In': [49, 1.63, 1.78, 3],
    'Sn': [50, 1.41, 1.96, 4],
    'Sb': [51, 1.36, 2.05, 5],
    'Te': [52, 1.43, 2.10, 6],
    'I':  [53, 1.28, 2.66, 7],
    'Xe': [54, 2.18, 2.67, 8],
    'Cs': [55, 2.65, 0.79, 1],
    'Ba': [56, 2.17, 0.89, 2],
    'La': [57, 1.73, 1.10, 3],
    'Ce': [58, 1.83, 1.12, 4],
    'Pr': [59, 1.83, 1.13, 5],
    'Nd': [60, 1.82, 1.14, 6], 
    'Pm': [61, 1.81, 1.13, 7],
    'Sm': [62, 1.80, 1.17, 8],
    'Eu': [63, 2.04, 1.20, 9],
    'Gd': [64, 1.80, 1.20, 10],
    'Tb': [65, 1.78, 1.10, 11],
    'Dy': [66, 1.77, 1.22, 12],
    'Ho': [67, 1.77, 1.23, 13],
    'Er': [68, 1.76, 1.24, 14],
    'Tm': [69, 1.75, 1.25, 15],
    'Yb': [70, 1.94, 1.10, 16],
    'Lu': [71, 1.73, 1.27, 17],
    'Hf': [72, 1.56, 1.30, 4],
    'Ta': [73, 1.43, 1.50, 5],
    'W':  [74, 1.37, 2.36, 6],
    'Re': [75, 1.37, 1.90, 7],
    'Os': [76, 1.34, 2.20, 8],
    'Ir': [77, 1.36, 2.20, 9],
    'Pt': [78, 1.38, 2.28, 10],
    'Au': [79, 1.44, 2.54, 11],
    'Hg': [80, 1.60, 2.00, 12],
    'Tl': [81, 1.70, 1.62, 3],
    'Pb': [82, 1.75, 2.33, 4],
    'Bi': [83, 1.55, 2.02, 5],
    'Po': [84, 1.67, 2.00, 6],
    'At': [85, 1.40, 2.22, 7],
    'Rn': [86, 2.20, 2.22, 8],
    'Fr': [87, 2.70, 0.70, 1],
    'Ra': [88, 2.20, 0.90, 2]
}

atoms_symbol = input("Please enter the type of element contained in HEA:\n")
atoms_symbol = atoms_symbol.split(" ")
atoms_component = input("Please enter the composition of atoms in HEA:\n")
atoms_component = atoms_component.split(" ")

atoms_radius_list = []
atoms_electronegativity_list = []
atoms_vec_list = []

#******************************************************************************************************#
for i in range(len(atoms_symbol)):
    for j in dict_atoms:
        if atoms_symbol[i] == j:
            atoms_radius_list.append(dict_atoms.get(j)[1])
            atoms_electronegativity_list.append(dict_atoms.get(j)[2])
            atoms_vec_list.append(dict_atoms.get(j)[3])

atoms_radius_average = 0
atoms_electronegativity_average = 0

for i in range(len(atoms_symbol)):
    atoms_radius_average += atoms_radius_list[i] * float(atoms_component[i])
    atoms_electronegativity_average += atoms_electronegativity_list[i]
    
atoms_radius_delte = 0
atoms_electronegativity_chi = 0
atoms_electronegativity_average /= len(atoms_symbol)
atoms_entropy_mixing = 0
atoms_vec = 0

for i in range(len(atoms_symbol)):
    atoms_radius_delte += float(atoms_component[i]) * ((1-float(atoms_radius_list[i])/atoms_radius_average) ** 2)
    atoms_electronegativity_chi += float(atoms_component[i]) * ((float(atoms_electronegativity_list[i]) - atoms_electronegativity_average) ** 2)
    atoms_entropy_mixing += float(atoms_component[i]) * math.log(float(atoms_component[i]))
    atoms_vec += float(atoms_component[i]) * float(atoms_vec_list[i])
    
print("The radius difference is: %.4f%% \nThe electronegativity difference is: %.4f%% \nMixing entropy is: %.4fR \nThe valence electron concentration is: %.2f" %((atoms_radius_delte**0.5)*100, (atoms_electronegativity_chi**0.5)*100, atoms_entropy_mixing*(-1), atoms_vec))
input("Press <enter>")
#******************************************************************************************************#