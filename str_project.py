from cmake_generator.cmake_format import cmake_format
from cmake_generator.version import Version

#----------------------------------------------------------------
def str_project(
    project_name : str,
    version : Version
) -> str:
    set_project_template = """
# ----------------------------------------------------------------
# Project: {SHAKE_CMAKE_GENERATOR_project_name}

project( {SHAKE_CMAKE_GENERATOR_project_name} VERSION {SHAKE_CMAKE_GENERATOR_version_major}.{SHAKE_CMAKE_GENERATOR_version_minor} LANGUAGES CXX C )
"""
    set_project_str = cmake_format(
        set_project_template,
        project_name    = project_name,
        version_major   = version.major,
        version_minor   = version.minor
    )
    return set_project_str