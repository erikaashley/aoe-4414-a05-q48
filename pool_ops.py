# pool_ops.py lect 15 slide 72
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
#  
#
# Parameters:
#  r_x_km: ECEF x-component in km
#  r_y_km: ECEF y-component in km
#  r_z_km: ECEF z-component in km
# Output:
#
# Written by: Erika Ashley
# Other contributors: None
#
# import Python modules
import math # math module
import sys  # argv

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions


# initialize script arguments
c_in = float('nan') 
h_in = float('nan') 
w_in = float('nan') 
h_pool = float('nan') 
w_pool = float('nan') 
s = float('nan') 
p = float('nan') 

# parse script arguments
if len(sys.argv)==8:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  h_pool = float(sys.argv[4])
  w_pool = float(sys.argv[5])
  s = float(sys.argv[6])
  p = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

# write script below this line
c_out=c_in
h_out=math.floor(((h_in+2*p-h_pool)/s)+1)
w_out=math.floor(((w_in+2*p-w_pool)/s)+1)
adds=c_in*h_out*w_out*(h_pool*w_pool-1)
muls=0
divs=c_in*h_out*w_out


print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed