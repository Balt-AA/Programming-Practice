import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import math
from Constants import constants as const

I_sp = 220;
g = const.earth_mu / (const.earth_r**2);


V_delta= g*I_sp* math.log(3000/1500);

m_f= 3000 / (math.exp(-100/(g*I_sp)));





print(V_delta/1000);
print(m_f);
