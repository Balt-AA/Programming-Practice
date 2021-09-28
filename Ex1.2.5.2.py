import math

sat_dist = 36000 * 1000     
solution_dist = 100 * 1000  
earth_radius = 6.378e6
grav_const = 6.673e-11
mu_earth = 3.986e14        

sat_dist = sat_dist + earth_radius


e_pot_1 = -mu_earth/sat_dist
e_kin_1 = math.pow(0,2)/2
e_pot_2 = -mu_earth/(earth_radius + solution_dist)

e_sum = e_pot_1 + e_kin_1 - e_pot_2

v_solution = math.sqrt(2*e_sum)
 
v_solution_km = v_solution / 1000

print(v_solution_km)