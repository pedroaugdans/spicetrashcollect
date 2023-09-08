#walk imperative
import os

#parameters
#undesired file extention touple:
files_to_delete = ('.raw','.log','.plt')

path = "."
fname = []
for root,d_names,f_names in os.walk(path):
   for f in f_names:
      fname.append(os.path.join(root, f))

## trying comprehension filter
undesired_list = [filtered_name for filtered_name in fname if filtered_name.endswith(files_to_delete)]

#delete all files
deleted_list = [os.remove(dead_file) for dead_file in undesired_list]