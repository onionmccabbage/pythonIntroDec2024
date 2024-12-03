import sys # sys is a library giving acces to the system
import os

print( os.getcwd() )
print( sys.version_info )
print( sys.platform )
# we may add paths where Python will look for import
sys.path.append('c:/inhere/keepgoing/hereitis')
print( sys.path )

# we can access run-time argument variables
for a in sys.argv:
    print(a)