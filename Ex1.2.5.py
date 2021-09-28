import math

m_cass = 5600   
h_cass = 5     
d_cass = 2      
rpm_cass = 1   
dps_cass = 6    # degrees per second
m_ant = 50   
l_ant = 10 

r_cass = d_cass / 2        
r_ant = r_cass + l_ant  #

# moment of inertia 
I_a = (1/2 * m_cass * math.pow(r_cass,2)) + (2*m_ant * math.pow(r_cass,2)) # kg*m²

# angular momentum
L_a = I_a * dps_cass # kg*m²*deg/s

# moment of inertia
I_b = (1/2 * (m_cass) * math.pow(r_cass,2)) + (2*m_ant * math.pow(r_ant,2))

dps_deployed = L_a / I_b

print(dps_deployed)
