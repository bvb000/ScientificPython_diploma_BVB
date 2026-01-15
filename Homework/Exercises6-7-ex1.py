class Exercises:
    
    def quadratic(a,b,c):
        if (a==0):
            print("Undefined!")
        else:
            x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
            x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
            print('x1 = ',x1)
            print('x2 = ',x2)
            return x1,x2
    
    def ex1():        
        a=float(input("a="))
        b=float(input("b="))
        c=float(input("c="))
        s1,s2=Exercises.quadratic(a,b,c)
    
    def ex2():
        recaman = [0]
        
        N=int(input("please state N"))
        
        for i in range (1,N):
            if ((recaman[i-1]-i)>0) and (recaman.count(recaman[i-1]-i)==0):
                recaman.append(recaman[i-1]-i)
            else:
                recaman.append(recaman[i-1]+i)
        
        print(recaman)
        
    def ex3():
        mylist=[1,-99,89,0,234,77,-748,11]
        yourlist=mylist.copy()
        yourlist.sort()
        print(yourlist[::-1])
        print(mylist)       
        
    def ex4():
        list1=[3,1,4,1,5,9,2,6]
        list2=[5,3,5,8,9,7,9,3]
        
        set1=set(list1)
        set2=set(list2)
        
        combo=set1.union(set2)
        combolist=list(combo)
        
        print(combolist)
        
    def ex5():
        N=float(input("Input number:"))
        
        list=[]
        
        for i in range(1,int(N)):
            if (N%i==0) and list.count(float(i))==0:
                list.append((float(i),float(N/i)))
        
        print(list)
        
    def ex6():
        import time
        
        start_time=time.time()
        #1
        list1=[]
        for i in range(1000):
            if (i%3==0):
                list1.append(i)
        end_time=time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
                
        #2
        start_time=time.time()
        list22=[3*x for x in range(int(1000/3))]
        end_time=time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        
        #3
        start_time=time.time()
        list3=[]
        list3.extend(range(1000))
        list33=list3[::3]
        end_time=time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        
        #4
        start_time=time.time()
        list4=[]
        for i in range(3,1000,3):
            list4.append(i)
        end_time=time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
    
    def ex7():
        def stringeval(strin):
            list=[]
            list=strin
            
            exists= " " in strin
            if (exists==True):
                print("Spaces detected!")
                strin=strin.replace(" ","")
                
            if (strin!=strin.lower()):
                print("Uppercase detected!")
                strin=strin.lower()
                
            punclist=[".",",",":",";","!","?"]
            for x in punclist:
                exists2= x in list
                if(exists2==True):
                    print("Punctuation detected!")
                    strin=strin.replace(x,"")
                    
            revlist=list[::-1]
            if (list==revlist):
                print("Palindrome detected!")
        
            print(strin)
            return strin
        
        strin=input("Input string:")
        stringeval(strin)        
        
    def ex8():
        strin=input("Input string:")
        list=[]
        for x in strin:
            exists=x in list
            if (exists!=True):
                list.append(x)
        count=[]
        for i in list:
            count.append((i,strin.count(i)))
        print(max(count))
    
    def ex9():
        N=int(input("Input N:"))
        primelist=[]
        for i in range(2,N):
          primelist.append(i)
        
        for x in primelist:
            for y in primelist:
                if (x!=y):
                    if (y%x==0):
                        primelist.remove(y)
                else:
                    continue
        
        print(primelist)
        
print("Exercise 1: ---")
y=Exercises.ex1()
print("Exercise 2: ---")
y=Exercises.ex2()
print("Exercise 3: ---")
y=Exercises.ex3()
print("Exercise 4: ---")
y=Exercises.ex4()
print("Exercise 5: ---")
y=Exercises.ex5()
print("Exercise 6: ---")
y=Exercises.ex6()
print("Exercise 7: ---")
y=Exercises.ex7()
print("Exercise 8: ---")
y=Exercises.ex8()
print("Exercise 9: ---")
y=Exercises.ex9()