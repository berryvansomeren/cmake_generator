from generate_cmake_file import generate_cmake_file

from path import abs_path_str_from_rel_to_this_file
absp = abs_path_str_from_rel_to_this_file # alias

from project import Language, Project

from target import (
    Executable,
    HeaderOnlyLibrary,
    ImportTarget,
    PythonModule,
    SharedLibrary,
    StaticLibrary,
    Target
)

from version import Version