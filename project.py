from typing import List, NamedTuple

from cmake_generator.version import Version

#----------------------------------------------------------------
class Project( NamedTuple ):
    project_name                        : str
    version                             : Version
    target_definitions_directory_paths  : List[ str ]
    destination_cmake_lists_file_path   : str
    build_directory_path                : str