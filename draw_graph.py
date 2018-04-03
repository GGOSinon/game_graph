import numpy as np
import matplotlib.pyplot as plt

print("Please type the value of N.")
print("If you type -1, N will be set in default value 10000.")
N = int(input("N : "))
if N==-1: N=10000
print("Please type the value of K.")
print("If you type -1, this program will simulate about various K.")
K = int(input("K : "))

if K==-1:
   print("This program will simulate about various K.")
   Mode = True
   print("Type the min value of K.")
   min_k=int(input("Min_K : "))
   print("Type the max value of K.")
   max_k=int(input("Max_K : "))   
else: Mode = False

if Mode == True:
    plot_f_x = []
    plot_f_a = []
    plot_f_b = []

    for k in range(min_k, max_k+1):
        print("Step k="+str(k)+" started")
        plot_f_x.append(k)
	c = np.zeros(32000)
	plot_x = []
	plot_a = []
	plot_b = []
	a = []
	b = []
	S = []

	X = 0
	m = 0

	for i in range(N):
	    plot_x.append(i)
	    while c[X]==1: X+=1
	    a.append(X)
	    plot_a.append(float(X)/(i+1))
	    c[X]=1
	    chk = False
	    for x in S:
		if (X-x)%k==0:
		    m+=1
		    S = []
		    break
	    S.append(X)
	    b.append(X+m+1)
	    plot_b.append(float(X+m+1)/(i+1))
	    c[X+m+1]=1
        
        plot_f_a.append(float(X)/(i+1))
        plot_f_b.append(float(X+m+1)/(i+1))

    plt.plot(plot_f_x, plot_f_a, plot_f_x, plot_f_b)
    plt.xlabel('K')
    plt.show()
else:
    print("Step k="+str(K)+" started")
    c = np.zeros(32000)
    plot_x = []
    plot_a = []
    plot_b = []
    a = []
    b = []
    S = []

    X = 0
    m = 0

    for i in range(N):
        plot_x.append(i)
        while c[X]==1: X+=1
        a.append(X)
        plot_a.append(float(X)/(i+1))
        c[X]=1
        chk = False
        for x in S:
            if (X-x)%K==0:
                m+=1
                S = []
                break
        S.append(X)
        b.append(X+m+1)
        plot_b.append(float(X+m+1)/(i+1))
        c[X+m+1]=1
        
	#for i in range(N):
	    #print("["+str(a[i])+","+str(b[i])+"]")
	#print(a)
	#print(b)
    plt.xlabel('N')	
    plt.plot(plot_x, plot_a, plot_x, plot_b)
    plt.show()
