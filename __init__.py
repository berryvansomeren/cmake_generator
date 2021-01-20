from cmake_generator.cmake_generator import (
    CMakeGenerator,
    Version
)

from cmake_generator.target import (
    Executable,
    HeaderOnlyLibrary,
    ImportTarget,
    PythonModule,
    SharedLibrary,
    StaticLibrary,
    Target
)

from cmake_generator.target_type import (
    NewTargetType
)

from cmake_generator.project import (
    Project
)

from cmake_generator.path import abs_path_str_from_rel_to_this_file
absp = abs_path_str_from_rel_to_this_file # alias