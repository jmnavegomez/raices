# My own generated and maybe already existing square root algorithms
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

# Defining an initial value
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
# My own function
def funcion(N,S,k,k1):
    num = (N-k)
    den = (S+k1)
    frac1 = num/den
    frac2 = num/(den**2)
    resul = S+((frac1-S+k1)/(frac2+1))

    return resul

# General iteration for my own function
def propio(N):
    S0,i = valor_ini(N)
    k0 = 4*(10**i)
    k1 = 2*(10**(i/2))

    S = funcion(N,S0,k0,k1)

    for j in range(100):
        S0 = S
        S = funcion(N,S0,k0,k1)
        if(abs(S-S0)<0.000001):
            break

    return S,(j+1)

# My own symple function
def funcionS(N):
    s,bas = valor_ini(N)
    for i in range(100):
        sol = ((s/2)+(N/(2*s)))
        if abs(s-sol) < 0.000001:
            break
        else:
            s = sol
    return sol,i