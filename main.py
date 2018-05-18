from sys import argv, exit
from directory_processing import DirectoryFlattener

if(len(argv) < 2):
    print('there should be exactly two arguments, source path being the first and destination being the second')
    exit(0)

source_path = argv[1]
destination_path = argv[2]

directory_flattener = DirectoryFlattener(source_path, destination_path)
directory_flattener.process_directory()

print('=============================')
print('Flattening went successfully')
print('=============================')


exit(0)