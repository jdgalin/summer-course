import numpy as np
import matplotlib.pyplot as plt 
 
#CONSTANTS 
gamma_i= .0639 
lambda_i= 2.87 * 10 ** (-5) #second^-1 
gamma_x= .00237 
lambda_x= 2.09 * 10 ** (-5) #second^-1 
sigma_a_x= 2.65 * 10 ** 6 * 10 ** (-24) #cm^2 
#Sigma_f= sigma_f*N 
 
 
#PROBLEM CONSTANTS 
#phi=n/cm^2/s 
parts={ 
'a':10**11, 
'b':10**12, 
'c':10**13} 
subcases= { 
'i':100, 
'ii':10, 
'iii':.1, 
'iv':.01} 
 
#time variable 
t=np.arange(0,50*60*60+1,1) #0 to 50 hours 
 
 
#functions 
def I_t(phi_0,subcase): #returns N_X135/Sigma_f 
    phi_1=phi_0*subcase 
    I135= ((gamma_i*phi_1) / (lambda_i)) * (1 - (((phi_1 - phi_0) / (phi_1)) * np.exp(-lambda_i * t))) 
    return I135 
 
def X_t(phi_0,subcase): #returns N_X135/Sigma_f 
    phi_1=phi_0*subcase 
    X135 = ((((gamma_i + gamma_x) * phi_1) / 
    (lambda_x + (sigma_a_x * phi_1))) * 
    (1- 
    (((phi_1-phi_0)/(phi_1))* 
    (((lambda_x / (lambda_x + (sigma_a_x * phi_0))) * np.exp(-(lambda_x + (sigma_a_x * phi_1)) * t) 
    ) + 
    (((gamma_i) / (gamma_x + gamma_i)) * ((lambda_x + (sigma_a_x * phi_1)) / (lambda_x + (sigma_a_x * phi_1) - 
    lambda_i)) * 
    (np.exp(-(lambda_i * t)) - np.exp(-(lambda_x + (sigma_a_x * phi_1)) * t)))) 
    ) 
    ) 
    ) 
    return X135 
 
#graph
for part in parts.values(): 
    plt.figure(fignum) 
    plt.plot(t,X_t(part,subcases.get('i')),color='blue', linestyle='-', label=f'{subcases.get('i')*part:.0e}') 
    plt.plot(t,X_t(part,subcases.get('ii')),color='red', linestyle='--', label=f'{subcases.get('ii')*part:.0e}') 
    plt.plot(t,X_t(part,subcases.get('iii')),color='green', linestyle='-.', label=f'{subcases.get('iii')*part:.0e}') 
    plt.plot(t,X_t(part,subcases.get('iv')),color='orange', linestyle=':', label=f'{subcases.get('iv')*part:.0e}') 
    plt.xticks(np.arange(0,50*60*60+1,3600*5),np.arange(0,50+1,5)) 
    plt.legend(title=r"$\phi_1$ in $n/(cm^2s)$") 
    plt.xlabel(r'time in hours') 
    plt.ylabel(r'$Xe/\Sigma_f$ in $cm^(-2)$') 
    plt.title(rf'Xe Concentration for power changes with $\phi_0={part:.0e}$') 
    plt.savefig(f'homework 8 figure {fignum}.png') 
    fignum+=1 
    plt.show()