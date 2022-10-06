from sympy.solvers import solve
from sympy import Symbol

class arit():
    
    def find_an():
        
        print('an = a1 + (n-1) * d')
        
        a1 = int(input('enter a1: '))
        n = int(input('enter n: '))
        d = int(input('enter d: '))
        
        ans = int(a1 + (n-1) * d)
        
        return ans
        
        print(f'an = {ans}')


    def find_a1():
        
        print('a1 = (n-1) * d - an')
        
        n = int(input('enter n: '))
        d = int(input('enter d: '))
        an = int(input('enter an: '))
        
        ans = int((n-1) * d - an)
        
        return ans
        

    def find_n():
        
        print('n = ((an - a1) / d) + 1')
        
        an = int(input('enter an: '))
        a1 = int(input('enter a1: '))
        d = int(input('enter d: '))
        
        ans = int(((an - a1) / d) + 1)
        
        return ans
    

    def find_d():
        
        print('finds d from formula')
        
        an = int(input('enter an: '))
        a1 = int(input('enter a1: '))
        n = int(input('enter n: '))
        
        x = Symbol('x')

        ans = solve((a1 + (n - 1) * x) - an, x)

        return int(ans[0])
    

    def find_Sn():
        
        print('Sn = ((2 * a1 + (n-1) * d) / 2) * n ')
        
        a1 = int(input('enter a1: '))
        n = int(input('enter n: '))
        d = int(input('enter d: '))
        
        ans = int(((2 * a1 + (n-1) * d) / 2) * n)
        
        return ans
    
    

class geom():
    
    def find_an():
        
        print('a1 - q**(n-1)')
        
        q = int(input('enter q: '))
        a1 = int(input('enter a1: '))
        n = int(input('enter n: '))
        
        ans = int(a1 - q**(n-1))
        
        return ans
    

    def find_q():
        
        print('q = a2 / a1')

        a2 = int(input('enter a2: '))
        a1 = int(input('enter a1: '))
        
        ans = int(a2 / a1)

        return ans


    def find_n():
            
        print('finds n from formula')
        
        an = int(input('enter an: '))
        q = int(input('enter q: '))
        a1 = int(input('enter a1: '))
        
        x = Symbol('x')

        ans = solve((a1 - q**(x-1)) - an, x)

        return str(ans[0])


    def find_a1():
            
        print('')
        
        ans = int()


    def find_Sn():
        print('Sn = (a1 * (q**n - 1)) / (q - 1)')
        
        q = int(input('enter q: '))
        a1 = int(input('enter a1: '))
        n = int(input('enter n: '))
        
        ans = int((a1 * (q**n - 1)) / (q - 1))
        print(ans)
