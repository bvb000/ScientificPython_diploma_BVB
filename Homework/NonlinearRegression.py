import numpy as np

def fxn(lam, beta1, beta2):
    return beta1/(lam**5*(np.exp(beta2/lam)-1))

def db1fxn(lam, beta2):
    return 1/(lam**5*(np.exp(beta2/lam)-1))

def db2fxn(lam, beta1, beta2):
    return -beta1*np.exp(beta2/lam)/(lam**6*(np.exp(beta2/lam)-1)**2)

wavelength=np.genfromtxt("sun_data.txt",usecols=(0))
density=np.genfromtxt("sun_data.txt",usecols=(1))
residuals=np.genfromtxt("sun_data.txt",usecols=(0)) #just to have same dimensions
jacobian=np.genfromtxt("sun_data.txt") #just to have right dimensions

beta1=1.0
beta2=1.0
alpha=0.1
e=10**(-6.0)
j=1
i=len(wavelength)

deltab=np.array([0,0])

while(True):
    for k in range(i):
        residuals[k]=density[k]-fxn(wavelength[k],beta1,beta2)
        jacobian[k][0]=db1fxn(wavelength[k],beta2)
        jacobian[k][1]=db2fxn(wavelength[k],beta1,beta2)
        
    D=np.dot(jacobian,np.transpose(jacobian))
    jtr=np.dot(residuals,jacobian)
    
    Dy=np.array([[D[0][0],jtr[0]],[D[1][0],jtr[1]]])
    print(jacobian)
    Dx=np.array([[jtr[0],D[0][1]],[jtr[1],D[1,1]]])
    
    detD=np.linalg.det(D)
    detDx=np.linalg.det(Dx)
    detDy=np.linalg.det(Dy)
    
    print(jacobian[1][1])
    print(detD)
    print(detDx)
    print(detDy)
    
    #deltab[0]=detDx/detD
    #deltab[1]=detDy/detD
    
    if ((deltab[0]**2+deltab[1]**2)<=e):
        break
    else:
        print(j,beta1,beta2)
        beta1=beta1+alpha*(deltab[0])
        beta2=beta2+alpha*(deltab[1])
        j=j+1
    
deltab[0]=beta1
deltab[1]=beta2

sigma=0

for k in range(i):
    sigma=sigma+(residuals[k]**2)/(i-2)
print("sigma^2=",sigma)

inversejtj=np.dot(jacobian,np.transpose(jacobian))
a1=inversejtj[0][0]
b1=inversejtj[1][0]
c1=inversejtj[0][1]
d1=inversejtj[1][1]

coeff=sigma/(a1*d1-b1*c1)
inversejtj[0][0]=coeff*d1
inversejtj[1][0]=coeff*(-b1)
inversejtj[0][1]=coeff*(-c1)
inversejtj[1][1]=coeff*a1
inversejtj[0][0]=np.sqrt(inversejtj[0][0])
inversejtj[1][0]=np.sqrt(inversejtj[0][0])
inversejtj[0][1]=np.sqrt(inversejtj[0][0])
inversejtj[1][1]=np.sqrt(inversejtj[0][0])

print("standard error=",inversejtj[0][0], inversejtj[1][1])
print("T [K]=",14387.77/beta2)
