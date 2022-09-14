import math

#Square root algorithms previous existing algorithms
#     Copyright (C) <2022>  <José Manuel Naveiro Gómez>

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Defining an initial value for iterations
def valor_ini(N):
    j = N
    i=0
    while j>1:
        j = j/10
        i += 1
    
    if(i%2==0):
        num = 2*(10**i)
    else:
        num = 6*(10**i)
        i=i-1

    return num,i

# Babylonian method
def Babilonia(N):
    b,i = valor_ini(N)
    h = N/b
    cont = 0
    while (abs(b-h)>0.000001):
        b=(h+b)/2
        h=N/b
        cont += 1
    
    return b,cont

# Exponential identity
def lhopital(N):
    num = math.exp(0.5*(math.log(N)))
    return num

# Halley's method
def Halleys(N):
    x0,i = valor_ini(N)
    x = x0-(((2*(x0**3))-(2*N*x0))/((3*(x0**2))+N))
    for i in range(100):
        x0 = x
        x = x0-(((2*(x0**3))-(2*N*x0))/((3*(x0**2))+N))
        if(abs(x-x0)<0.000001):
            break
    
    return x,(i+1)