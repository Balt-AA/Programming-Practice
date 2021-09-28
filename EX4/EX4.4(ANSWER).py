from Constants import constants as const
import math


# Problem B

m_rosseta = 3000  # kg
isp = 220  # s

earth_g = const.earth_mu / (const.earth_r**2)

v = earth_g * isp * math.log(m_rosseta/(m_rosseta/2))

print("Problem B: " + str(v/1000))

v = 100  # m/s

m_100 = m_rosseta * math.pow(math.e, (-v/(earth_g*isp)))

print("Problem B_2: " + str(m_100))