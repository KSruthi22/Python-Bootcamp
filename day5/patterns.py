#square pattern
n=int(input("enter number of rows"))
for i in range(1,n+1):
     for j in range(1,n+1):
        print("*",end=" ")
     print()
#inotqualsj square pattern
n=int(input("enter number of rows"))
for i in range(1,n+1):
     for j in range(1,n+1):
         if i==j:
             print(" ",end=" ")
         else:  
             print("*",end=" ")
     print()  
#print uppertriangular matrix
'''    * * * * *
         * * * *
           * * *
             * *
               *
'''
n=int(input())
for i in range(1,n+1):
    spaces=i-1
    for k in range(1,spaces+1):
        print(" ",end=" ")
    for j in range(1,n-i+1+1):
        print("*",end=" ")
    print()        
#print lower triangular matrix
'''     *
        * *
        * * *
        * * * *
        * * * * *    '''
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()        
#print rhombus
'''     *
       * *
      * * *
            '''
#print parallellogram
'''        * * * * * 
         * * * * *
       * * * * * 
     * * * * * 
   * * * * *                    '''
n=int(input())
for i in range(1,n+1):
    spaces=n-i
    for k in range(1,spaces+1):
        print(" ",end=" ")
    for j in range(1,n+1):
        print("*",end=" ")
    print()        
#print number pyramid