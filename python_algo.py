import math

#Core Math Concepts 

'''
	Prime Numbers 
		A number is prime if it is only divisible by 1 and itself.
		The Sieve of Eratosthenes will generate all the primes from 2 to a given number n. It begins by assuming that all numbers are prime. It then takes the first prime number and removes all of its multiples. It then applies the same method to the next prime number. This is continued until all numbers have been processed. 
'''
def isPrime(n):
	print n
	if n<=1: 
		return False
	if n==2:
		return True
	if n%2==0: 
		return False

	i=3
	m=math.sqrt(n)

	while(i<=m):
		if n%i==0:
			return False
		i+=2

	return True

def Sieve(n):
    limitn = n+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

'''
	GCD
		The greatest common divisor (GCD) of two numbers a and b is the greatest number that divides evenly into both a and b. 
		Lowest common multiple (LCM)
		Euclids algorithm can be used to solve linear Diophantine equations
			These equations have integer coefficients and are of the form
				ax + by = c
'''

def GCD(a,b):
	i = min(a,b)
	while i>=1:
		if a%i==0 and b%i==0:
			return i
		i-=1

def LCM(a,b):
	return b*a/GCD(a,b);

def Euclid(a,b):
	if b==0:
		return a
	return GDC(b,a%b)


'''
	Geometry
		Often we have to deal with polygons whose vertices have integer coordinates. 
			Such polygons are called lattice polygons.
	
	B = number of lattice points on the boundary of the polygon
	I = number of lattice points in the interior of the polygon
	Picks Theorem
		Picks theorem is useful when we need to find the number of lattice points inside a large polygon.
		Area = B/2 + I - 1

	Eulers Formula for polygonal nets
		 A polygonal net is a simple polygon divided into smaller polygons	
		 The smaller polygons are called faces
		 The sides of the faces are called edges 
		 The vertices of the faces are called vertices. 
		 Eulers Formula then states:
		 	V - E + F = 2 where
			V = number of vertices
			E = number of edges
			F = number of faces

'''



'''
	Bases

'''

def toDecimal(n,b):
	result=0
	multiplier=1

	while(n>0):
		result+=n%10*multiplier
		multiplier*=b
		n/=10;

	return result


def fromDecimal(n,b):
	result=0
	multiplier=1

	while(n>0):
		result+=n%b*multiplier
		multiplier*=10
		n/=b

	return result

def fromDecimal2(n,b):
	chars="0123456789ABCDEFGHIJ"
	result=""
   	while(n>0):
		result=chars[n%b] + result;
		n/=b;

	return result

      
'''
	Fractions and Complex Numbers
	In general, a complex number is a number of the form a + ib, where a and b are reals and i is the square root of -1. 
		m + n
			= (a + ib) + (c + id)
			= (a + c) + i(b + d)

		m * n
			= (a + ib) * (c + id)
			= ac + iad + ibc + (i^2)bd
			= (ac - bd) + i(ad + bc)

'''

def multiplyFractions(a,b):
	c = [(a[0]*b[0]),(a[1]*b[1])]
	return c

def addFractions(a,b):
	denom = LCM(a[1],b[1])
	c=[denom/a[1]*a[0] + denom/b[1]*b[0], denom]
	return c

def reduceFraction(a):
   b=GCD(a[0],a[1]);
   a[0]/=b;
   a[1]/=b;
   return a

def multiplyComplex(m,n):
	prod = [m[0]*n[0] - m[1]*n[1], m[0]*n[1] + m[1]*n[0]]
   	return prod;


#Geometry 

'''
	Vectors

'''



#http://community.topcoder.com/stat?c=problem_statement&pm=13782
#Dynamic Programming


def minimalAttacks(x):
	dp = dict()
	dp[(0, 0, 0)] = 0

	def minAttacks(h1, h2, h3):
	  h1 = max(h1, 0)
	  h2 = max(h2, 0)
	  h3 = max(h3, 0)
	  if (h1, h2, h3) in dp:
	    return dp[(h1, h2, h3)]
	  ans = 1 + min(
	  	  minAttacks(h1 - 9, h2 - 3, h3 - 1),
	      minAttacks(h1 - 9, h2 - 1, h3 - 3),
	      minAttacks(h1 - 3, h2 - 9, h3 - 1),
	      minAttacks(h1 - 3, h2 - 1, h3 - 9),
	      minAttacks(h1 - 1, h2 - 3, h3 - 9),
	      minAttacks(h1 - 1, h2 - 9, h3 - 3))
	  dp[(h1, h2, h3)] = ans
	  return ans

	x = list(x)
	while len(x) < 3:
	  x.append(0)
	return minAttacks(*x)



hp = [12,10,4]

print minimalAttacks(hp)











