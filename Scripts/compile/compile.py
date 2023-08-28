import os
from Utilities.unpyc3_compiler import Unpyc3PythonCompiler


release_dir = os.path.join('..', '..', 'Release', 'FirstWorldProblems')

# This function invocation will compile the files found within Scripts/firstWorldProblems, put them inside of a file named firstWorldProblems.ts4script, and it will finally place that ts4script file within <Project>/Release/FirstWorldProblems.
Unpyc3PythonCompiler.compile_mod(
    folder_path_to_output_ts4script_to=release_dir,
    names_of_modules_include=('firstWorldProblems',),
    output_ts4script_name='firstWorldProblems'
)
