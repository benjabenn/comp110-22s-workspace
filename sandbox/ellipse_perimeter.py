#pyellipse by Tim Sheerman-Chase (C) 2021
#Calculate circumference of an ellipse in python (both exact and approximate approaches) 
#This source code may be used under the CC0 license https://creativecommons.org/publicdomain/zero/1.0/
#
#For the best exact circumference, use EllipseCircumAdlaj2012
#
#For good approximations that are faster to compute, see EllipseCircumRamanujan2ndApprox and EllipseCircumJacobsenWaadeland1985
#
#Incidentally, scipy has a function to exactly calculate it:
#	C = 4.0*a*special.ellipe(e*e)
#	https://stackoverflow.com/a/63676048/4288232

import math

def EllipseArea(a, b):

	return math.pi * a * b

def RisingFactorial(q, n):
	#https://en.wikipedia.org/wiki/Falling_and_rising_factorials

	out = 1.0
	for i in range(0, n):
		out *= (q + i)
	return out

def Hypergeometric(a,b,c,z,itNum=50):
	#https://en.wikipedia.org/wiki/Hypergeometric_function
	#More suitable for slow convergence

	total = 0.0
	a = float(a)
	b = float(b)
	c = float(c)
	z = float(z)
	for n in range(itNum-1, -1, -1): #Start with smaller terms

		term = (RisingFactorial(a, n) * RisingFactorial(b, n) / RisingFactorial(c, n)) * math.pow(z, n) / math.gamma(n+1.0)
		total += term
	return total

def HypergeometricFast(a,b,c,z):
	#https://en.wikipedia.org/wiki/Hypergeometric_function
	#Suitable for fast convergence but breaks as e -> 1.0

	total = 0.0
	a = float(a)
	b = float(b)
	c = float(c)
	z = float(z)
	n = 0
	while True:
		term = (RisingFactorial(a, n) * RisingFactorial(b, n) / RisingFactorial(c, n)) * math.pow(z, n) / math.gamma(n+1.0)
		oldTotal = total
		total += term
		if total == oldTotal: #Convergence check
			break
		n += 1		

	return total

def EllipseValidateParams(a, b):
	if math.isnan(a) or math.isinf(a): raise ValueError("Semi-major axis (a) should be a finite number")
	if math.isnan(b) or math.isinf(b): raise ValueError("Semi-minor axis (b) should be a finite number")
	if a < 0.0: raise ValueError("Semi-major axis (a) should be >= 0.0")
	if b < 0.0: raise ValueError("Semi-minor axis (b) should be >= 0.0")
	if b > a:
		a, b = b, a #By convention, a is the semi-major axis
	return a, b

def EllipseCircumMaclaurin1742Hypergeometric(a=1.0, b=0.5, iterNum=100):
	#http://www.numericana.com/answer/ellipse.htm#exact
	a, b = EllipseValidateParams(a, b)
	if a == 0.0: return 0.0
	try:
		e = pow(1.0 - b*b / (a*a), 0.5)
	except ZeroDivisionError:
		return 0.0

	return 2.0 * math.pi * a * Hypergeometric(-0.5, 0.5, 1.0, math.pow(e, 2.0), iterNum)

def EllipseCircumMaclaurin1742(a=1.0, b=0.5, iterNum=80):
	#http://www.numericana.com/answer/ellipse.htm#elliptic
	a, b = EllipseValidateParams(a, b)
	if a == 0.0: return 0.0
	try:
		e = pow(1.0 - b*b / (a*a), 0.5)
	except ZeroDivisionError:
		return 0.0

	total = 0.0
	for n in range(iterNum-1, -1, -1): #Start with smaller terms

		term = (-1.0 / (2.0 * n - 1.0))
		term2 = math.gamma(2.0 * n + 1.0)
		term2 /= pow(pow(2.0, n) * math.gamma(n + 1.0), 2.0)
		term *= pow(term2, 2.0)
		term *= math.pow(e, 2 * n)

		total += term

	return (total * 2.0 * math.pi * a)

def EllipseCalcBsq(e=0.9, a=1.0):
	bsq = (1.0 - e*e) * a*a
	return bsq

def EllipseCircumEuler1773Hypergeometric(a=1.0, b=0.5, iterNum=100):
	#http://www.numericana.com/answer/ellipse.htm#exact

	a, b = EllipseValidateParams(a, b)
	if a == 0.0: return 0.0
	try:
		e = pow(1.0 - b*b / (a*a), 0.5)
	except ZeroDivisionError:
		return 0.0
	esq = e*e
	delta = pow(esq / (2.0 - esq), 2.0)
	term = math.pi * pow(2.0*(a*a+b*b), 0.5)

	return term * Hypergeometric(-0.25, 0.25, 1.0, delta, iterNum)

def EllipseCircumIvory1796Hypergeometric(a=1.0, b=0.5, iterNum=100):
	#http://www.numericana.com/answer/ellipse.htm#exact

	a, b = EllipseValidateParams(a, b)
	if a == 0.0: return 0.0

	term = math.pi * (a + b)
	try:
		h = pow(a-b, 2.0) / pow(a+b, 2.0)
	except ZeroDivisionError:
		return 0.0

	return term * Hypergeometric(-0.5, -0.5, 1.0, h, iterNum)

def EllipseCircumGaussKummer(a=1.0, b=0.5, maxIter=1000):
	#http://www.numericana.com/answer/ellipse.htm#gausskummer
	a, b = EllipseValidateParams(a, b)
	if a == 0.0: return 0.0

	term0 = math.pi * (a+b)
	try:
		h = pow(a-b, 2.0) / pow(a+b, 2.0)
	except ZeroDivisionError:
		return 0.0

	total = 0.0
	n = 0
	while True:
		term2 = math.comb(2*n, n) / ((1.0-2.0*n)*pow(-4.0, n))
		term = pow(term2, 2.0) * pow(h, n)
		oldTotal = total
		total += term
		if total == oldTotal: #Convergence check
			break
		if n > maxIter:
			break
		n += 1

	return term0 * total 

def EllipseCircumGaussKummerHypergeometric(a=1.0, b=0.5, iterNum=100):
	#http://web.tecnico.ulisboa.pt/~mcasquilho/compute/com/,ellips/PerimeterOfEllipse.pdf
	a, b = EllipseValidateParams(a, b)
	if a == 0.0: return 0.0

	term = math.pi * (a+b)
	try:
		h = pow(a-b, 2.0) / pow(a+b, 2.0)
	except ZeroDivisionError:
		return 0.0

	return term * Hypergeometric(-0.5, -0.5, 1.0, h, iterNum)

def EllipseCircumCayley1876(a=1.0, b=0.5, maxIter=1000):
	#http://web.tecnico.ulisboa.pt/~mcasquilho/compute/com/,ellips/PerimeterOfEllipse.pdf
	a, b = EllipseValidateParams(a, b)
	if a == 0.0: return 0.0

	#First term is trivial
	total = 1.0
	
	#Calculate second term
	try:
		k = b/a
	except ZeroDivisionError:
		return 0.0
	term1 = 0.5
	try:
		term2 = math.log(4.0/k) - 0.5
	except ZeroDivisionError:
		term2 = 1.0 #Arbitrary since it is multipled by zero
	if math.isinf(term2): term2 = 1.0

	n = 1
	f1 = n*2-3
	c2 = 1.0 / ((f1+2)*(f1+3))
	total += term1 * term2 * pow(k, 2)

	#Calculate third and later terms
	n = 2
	while True:
		f1 = n*2-3
		term1 *= f1*(f1+2)/((f1+1)*(f1+3))
		c1 = c2
		c2 = 1.0 / ((f1+2)*(f1+3))
		term2 -= c1 + c2
		oldTotal = total
		total += term1 * term2 * pow(k, n*2)
		if total == oldTotal: #Convergence check
			break
		if n > 1000:
			break
		n += 1	

	return 4.0 * a * total

def EllipseCircumHybrid(a=1.0, b=0.5):
	#Based on http://www.numericana.com/answer/ellipse.htm#exact
	a, b = EllipseValidateParams(a, b)
	if a == 0.0: return 0.0

	try:
		esq = 1.0 - b*b / (a*a)
	except ZeroDivisionError:
		return 0.0

	if esq == 0.0:
		return 2.0 * math.pi * a #Otherwise known as a circle
	elif esq == 1.0:
		return a * 4.0 #Degenerate case (a straight line)
	elif esq < 0.910: 
		#The 0.954 parameter is from Table 1 in http://web.tecnico.ulisboa.pt/~mcasquilho/compute/com/,ellips/PerimeterOfEllipse.pdf
		#but we are comparing to e^2 so use 0.910
		return EllipseCircumGaussKummer(a, b)
	else:
		return EllipseCircumCayley1876(a, b)

def EllipseCircumKeplerApprox(a=1.0, b=0.5):
	#http://www.ebyte.it/library/docs/math05a/EllipsePerimeterApprox05.html#K
	a, b = EllipseValidateParams(a, b)
	
	return 2.0 * math.pi * pow(a + b, 0.5)

def EllipseCircumNaiveApprox(a=1.0, b=0.5):
	#http://www.numericana.com/answer/ellipse.htm#euler
	a, b = EllipseValidateParams(a, b)

	return math.pi * (a + b)

def EllipseCircumEulerApprox(a=1.0, b=0.5):
	#http://www.numericana.com/answer/ellipse.htm#euler
	a, b = EllipseValidateParams(a, b)

	return math.pi * pow(2.0 * (a*a + b*b), 0.5)

def EllipseCircumRamanujan1stApprox(a=1.0, b=0.5):
	#http://www.numericana.com/answer/ellipse.htm#ramanju-1
	a, b = EllipseValidateParams(a, b)

	return math.pi * (3.0*(a+b) - pow((3.0*a+b)*(a+3.0*b), 0.5))

def EllipseCircumRamanujan2ndApprox(a=1.0, b=0.5):
	#http://www.numericana.com/answer/ellipse.htm#ramanju-2
	a, b = EllipseValidateParams(a, b)

	try:
		h = pow(a-b, 2.0) / pow(a+b, 2.0)
	except ZeroDivisionError:
		return 0.0

	return math.pi * (a+b) * (1.0 + 3.0 * h / (10.0 + pow(4.0 - 3.0 * h, 0.5)))

def EllipseCircumJacobsenWaadeland1985(a=1.0, b=0.5):
	#This is a type of Pade approximation
	#http://www.numericana.com/answer/ellipse.htm#pade
	a, b = EllipseValidateParams(a, b)

	try:
		h = pow(a-b, 2.0) / pow(a+b, 2.0)
	except ZeroDivisionError:
		return 0.0
	hsq = h*h

	return math.pi * (a+b) * ((256.0 - 48.0 * h - 21.0 * hsq)/(256.0 - 112.0 * h + 3.0 * hsq))

def Agm(x0=0.8, y0=1.0, its = 100, eps = 1e-15):
	#Arithmetic-geometric mean https://en.wikipedia.org/wiki/Arithmetic%E2%80%93geometric_mean

	xp = x0
	yp = y0

	for n in range(its):
		xn = 0.5 * (xp + yp)
		yn = pow(xp * yp, 0.5)

		#Convergence check
		if abs(xn-xp) < eps and abs(yn-yp) < eps : break

		xp = xn
		yp = yn

	return xn

def Magm(x0=0.8, y0=1.0, its = 100, eps = 1e-15):
	#Modified arithmetic-geometric mean from Adlay 2012

	xp = x0
	yp = y0
	zp = 0.0

	for n in range(its):
		xn = 0.5 * (xp + yp)
		t = pow((xp - zp) * (yp - zp), 0.5)
		yn = zp + t
		zn = zp - t
	
		#Convergence check
		if abs(xn-xp) < eps and abs(yn-yp) < eps : break

		xp = xn
		yp = yn
		zp = zn

	return xn

def EllipseCircumAdlaj2012(a=1.0, b=0.5):
	#Semjon Adlay, An Eloquent Formula for the Perimeter of an Ellipse, 2012
	#http://www.ams.org/notices/201208/rtx120801094p.pdf

	#Scale semi-major axis a to be 1.0
	a, b = EllipseValidateParams(a, b)
	try:
		bSc = b / a
	except ZeroDivisionError:
		return 0.0
	aSc = 1.0

	integSecKind = math.pi * Magm(bSc*bSc) / (2.0 * Agm(bSc))

	return 4.0 * integSecKind * a

def Examples():
	a = 1.0
	b = 0.5
	try:
		e = pow(1.0 - b*b / (a*a), 0.5)
	except ZeroDivisionError:
		e = None

	print ("Semi-major axis a\t", a)
	print ("Semi-minor axis b\t", b)
	print ("Eccentricity e\t\t", e)

	print ("Theoretically exact (less suitable for computers)")
	print ("Maclaurin1742\t\t\t", EllipseCircumMaclaurin1742(a, b))
	print ("Maclaurin1742Hypergeometric\t", EllipseCircumMaclaurin1742Hypergeometric(a, b))
	print ("Euler1773Hypergeometric\t\t", EllipseCircumEuler1773Hypergeometric(a, b))

	print ("\nTheoretically exact (somewhat suitable for computers)")
	print ("Ivory1796Hypergeometric\t\t", EllipseCircumIvory1796Hypergeometric(a, b))
	print ("GaussKummerHypergeometric\t", EllipseCircumGaussKummerHypergeometric(a, b))

	print ("\nTheoretically exact (more suitable for computers)")
	print ("GaussKummer (best when e<0.954)\t", EllipseCircumGaussKummer(a, b))
	print ("Cayley1876 (best when e>0.954)\t", EllipseCircumCayley1876(a, b))

	#The 0.954 parameter is from Table 1 in http://web.tecnico.ulisboa.pt/~mcasquilho/compute/com/,ellips/PerimeterOfEllipse.pdf
	print ("Hybrid (combines the 2 above)\t", EllipseCircumHybrid(a, b))

	print ("\nTheoretically exact (very suitable for computers, quadratic convergence)")
	print ("Adlaj2012\t\t\t", EllipseCircumAdlaj2012(a, b))

	print ("\nApproximations (faster to compute)")
	print ("Ordered from least to most accurate")
	print ("KeplerApprox\t\t\t", EllipseCircumKeplerApprox(a, b))
	print ("NaiveApprox\t\t\t", EllipseCircumNaiveApprox(a, b))
	print ("EulerApprox\t\t\t", EllipseCircumEulerApprox(a, b))
	print ("Ramanujan1stApprox\t\t", EllipseCircumRamanujan1stApprox(a, b))
	print ("JacobsenWaadeland1985\t\t", EllipseCircumJacobsenWaadeland1985(a, b))
	print ("Ramanujan2ndApprox\t\t", EllipseCircumRamanujan2ndApprox(a, b))

	print ("\nArea\t\t\t\t", EllipseArea(a, b))

if __name__=="__main__":
	Examples()