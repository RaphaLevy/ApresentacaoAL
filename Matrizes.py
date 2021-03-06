import numpy as np

print("Matrizes da Simulação 1")
print("A:")
Sim_1_A = np.matrix('0.07, 0, 0; 0.93, 0.2, 0; 0, 0.8, 1') 
print(Sim_1_A)
print("U0:")
Sim_1_U0 = np.matrix('202206486; 5276942; 4721593 ')
print(Sim_1_U0)
print(" ")
print("U1:")
Sim_1_Uk = np.dot(Sim_1_A,Sim_1_U0)
print(Sim_1_Uk)
print("U10:")
power1 = np.dot(Sim_1_A**10,Sim_1_U0)
print(power1)
print("U25:")
power1 = np.dot(Sim_1_A**25,Sim_1_U0)
print(power1)
print("U50:")
power1 = np.dot(Sim_1_A**50,Sim_1_U0)
print(power1)
print("U100:")
power1 = np.dot(Sim_1_A**100,Sim_1_U0)
print(power1)

print('#####################################################')

print("Matrizes da Simulação 2")
print("A:")
Sim_2_A = np.matrix('0.27, 0, 0; 0.73, 0.36, 0; 0, 0.64, 1') 
print(Sim_2_A)
print("U0:")
Sim_2_U0 = np.matrix('7744985128; 46643798; 31156914 ')
print(Sim_2_U0)
print(" ")
print("U1:")
Sim_2_Uk = np.dot(Sim_2_A,Sim_2_U0)
print(Sim_2_Uk)
print("U10:")
power2 = np.dot(Sim_2_A**10,Sim_2_U0)
print(power2)
print("U25:")
power2 = np.dot(Sim_2_A**25,Sim_2_U0)
print(power2)
print("U50:")
power2 = np.dot(Sim_2_A**50,Sim_2_U0)
print(power2)
print("U100:")
power2 = np.dot(Sim_2_A**100,Sim_2_U0)
print(power2)

print('#####################################################')

print("Matrizes da Simulação 3")
print("A:")
Sim_3_A = np.matrix('0.8, 0, 0; 0.2, 0.36, 0; 0, 0.64, 1') 
print(Sim_3_A)
print("U0:")
Sim_3_U0 = np.matrix('7744985128; 46643798; 31156914 ')
print(Sim_3_U0)
print(" ")
print("U1:")
Sim_3_Uk = np.dot(Sim_3_A,Sim_3_U0)
print(Sim_3_Uk)
print("U10:")
power3 = np.dot(Sim_3_A**10,Sim_3_U0)
print(power3)
print("U25:")
power3 = np.dot(Sim_3_A**25,Sim_3_U0)
print(power3)
print("U50:")
power3 = np.dot(Sim_3_A**50,Sim_3_U0)
print(power3)
print("U100:")
power3 = np.dot(Sim_3_A**100,Sim_3_U0)
print(power3)

print('#####################################################')

print("Matrizes da Simulação 4")
print("A:")
Sim_4_A = np.matrix('0.38, 0, 0; 0.62, 0.19, 0; 0, 0.81, 1') 
print(Sim_4_A)
print("U0:")
Sim_4_U0 = np.matrix('234; 1396; 0 ')
print(Sim_4_U0)
print(" ")
print("U1:")
Sim_4_Uk = np.dot(Sim_4_A,Sim_4_U0)
print(Sim_4_Uk)
print("U10:")
power4 = np.dot(Sim_4_A**10,Sim_4_U0)
print(power4)
print("U25:")
power4 = np.dot(Sim_4_A**25,Sim_4_U0)
print(power4)
print("U50:")
power4 = np.dot(Sim_4_A**50,Sim_4_U0)
print(power4)
print("U100:")
power4 = np.dot(Sim_4_A**100,Sim_4_U0)
print(power4)

print('#####################################################')

print("Matrizes da Simulação 5")
print("A:")
Sim_5_A = np.matrix('0.25, 0, 0; 0.75, 0.8, 0; 0, 0.2, 1') 
print(Sim_5_A)
print("U0:")
Sim_5_U0 = np.matrix('59009; 166521; 0 ')
print(Sim_5_U0)
print(" ")
print("U1:")
Sim_5_Uk = np.dot(Sim_5_A,Sim_5_U0)
print(Sim_5_Uk)
print("U10:")
power5 = np.dot(Sim_5_A**10,Sim_5_U0)
print(power5)
print("U25:")
power5 = np.dot(Sim_5_A**25,Sim_5_U0)
print(power5)
print("U50:")
power5 = np.dot(Sim_5_A**50,Sim_5_U0)
print(power5)
print("U100:")
power5 = np.dot(Sim_5_A**100,Sim_5_U0)
print(power5)

print('#####################################################')

print("Matrizes da Simulação 7")
print("A:")
Sim_7_A = np.matrix('0.27, 0, 0; 0.73, 0.36, 0; 0, 0.64, 1')
print(Sim_7_A)
print("U0:")
Sim_7_U0 = np.matrix('7822785839; 1; 0 ')
print(Sim_7_U0)
print(" ")
print("U1:")
Sim_7_Uk = np.dot(Sim_7_A,Sim_7_U0)
print(Sim_7_Uk)
print("U10:")
power7 = np.dot(Sim_7_A**10,Sim_7_U0)
print(power7)
print("U25:")
power7 = np.dot(Sim_7_A**25,Sim_7_U0)
print(power7)
print("U50:")
power7 = np.dot(Sim_7_A**50,Sim_7_U0)
print(power7)
print("U100:")
power7 = np.dot(Sim_7_A**100,Sim_7_U0)
print(power7)

print('#####################################################')

print("Matrizes da Simulação 8")
print("A:")
Sim_8_A = np.matrix('0.8, 0, 0; 0.2, 0.36, 0; 0, 0.64, 1')
print(Sim_8_A)
print("U0:")
Sim_8_U0 = np.matrix('7822785839; 1; 0 ')
print(Sim_8_U0)
print(" ")
print("U1:")
Sim_8_Uk = np.dot(Sim_8_A,Sim_8_U0)
print(Sim_8_Uk)
print("U10:")
power8 = np.dot(Sim_8_A**10,Sim_8_U0)
print(power8)
print("U25:")
power8 = np.dot(Sim_8_A**25,Sim_8_U0)
print(power8)
print("U50:")
power8 = np.dot(Sim_8_A**50,Sim_8_U0)
print(power8)
print("U100:")
power8 = np.dot(Sim_8_A**100,Sim_8_U0)
print(power8)


            