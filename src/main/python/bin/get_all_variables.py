import os
import pprint as pp

#pp.pprint(dict(os.environ)['JAVA_HOME'])

### Set Enviroment Variables
os.environ['envn'] = 'TEST'
os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'

### Set Enviroment Variables
envn = os.environ['envn']
header = os.environ['header']
inferSchema = os.environ['inferSchema']

### Set other Variables
appName = "MSF Memory Report"
current_path = os.getcwd()
staging_dim_memory = current_path + '\staging\statsfile'
print(staging_dim_memory)