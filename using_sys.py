import sys # sys is a library giving acces to the system
import os

# consider - how frequently will someone actually be sat at the terminal to enter data....
# not common at all

print( os.getcwd() )
print( sys.version_info )
print( sys.platform )
# we may add paths where Python will look for import
sys.path.append('c:/inhere/keepgoing/hereitis')
print( sys.path )

# we can access run-time argument variables (they are ALWAYS strings)
for a in sys.argv: # sys.argv[0] is ALWAYS the name of the current module
    print(a, type(a))