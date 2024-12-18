def hanoi(n,p1,p2,p3):
    if n == 1:
        print('Move disk from %s to %s'%(p1,p3))
    else:
        hanoi(n-1,p1,p3,p2)
        print('Move disk from %s to %s'%(p1,p3))
        hanoi(n-1,p2,p1,p3)
        
        
n = int(input('Please enter the number of disks: '))
hanoi(n,1,2,3)
