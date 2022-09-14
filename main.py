#Square root algorithms main program
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

import time
import math
import previous as pre
import proper as pro

if __name__ == "__main__":
    N = float(input("Write the number: "))

    inicio = time.time()
    print(" Babylonian method:    ",pre.Babilonia(N))
    primero = time.time()
    print(" Exponential identity: ",pre.lhopital(N))
    segundo = time.time()
    print(" My try:               ",pro.propio(N))
    tercero = time.time()
    print(" Predefined sqrt:      ",math.sqrt(N))
    cuarto = time.time()
    print(" Halley's method:      ",pre.Halleys(N))
    quinto = time.time()
    print(" Simple try:           ",pro.funcionS(N))
    sexto = time.time()

    print("Tiempos:")
    print(" Babylonian method:    ",primero-inicio)
    print(" Exponential identity: ",segundo-primero)
    print(" My try:               ",tercero-segundo)
    print(" Predefined sqrt:      ",cuarto-tercero)
    print(" Halley's method:      ",quinto-cuarto)
    print(" Simple try:           ",sexto-quinto)
    print(" total time:           ",sexto-primero)