
#Python Project
#FEA AND EXPERIMENTAL ANALYSIS OF CANTILEVER BEAM USING PYTHON GUI


#PROGRAM FOR CALCULATION OF NODAL DISPLACEMENT OF 2 ELEMENT
import numpy as np
from matplotlib import pyplot as plt


'''TAKING DATA FROM USER'''

L = float(input("Enter the  dimension length of the beam 'L' in cm: "))
E = float(input("Enter the dimension of modulous of elasticity 'E' of material in N/cm^2 :"))
b=float(input("enter dimension of b in cm: "))
h=float(input("enter dimension of h in cm: "))

I=b*h**3/12  #Calculating Inertia

q=E*I/(L/2)**3
F=float(input("Enter the magnitude of force 2 'P' in N: "))



"GLOBAL STIFFNESS MATRIX"
m=np.array([[12,3*L,-12,3*L,0,0],[3*L,L*L,-3*L,L*L/2,0,0],[-12,-3*L,24,0,-12,3*L],[3*L,L*L/2,0,2*L*L,-3*L,L*L/2],[0,0,-12,-3*L,12,-3*L],[0,0,3*L,L*L/2,-3*L,L*L]])

" GLOBAL STIFNESS MATRIX PRINTING "
print("The Global Stiffness Matrix is: ")
print(m)
print( )
print( )

"FEA EQUATIONS"
k=np.array([[24,0,3*L],[0,2*L*L,L*L/2],[3*L,L*L/2,L*L]])
p=np.array([[F/q],[0],[0]])

"MATRIX SOLVING"
z=np.linalg.solve(k,p)

"NODAL DISPLACEMENT VALUE PRINTING"
print("The nodal displacement matrix is : ")
print(z)

"MATRIX FOR CALCULATING FORCE AND MOMENTS"
j=np.array([[-12,3*L,0],[-3*L,L*L/2,0],[-3*L,L*L/2,0]])
c=q*j
e=c.dot(z)
print()
print()
print("The matrix of Force and Moments is")
print(e) #PRINTING MATRIX FOR FORCE AND MOMENTS

'PLOTING OF GRAPH'
g=plt.plot(z,e)   #ploting graph for nodal displacement vs force
plt.show()
