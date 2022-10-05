from typing import List

from cmake_format import cmake_format
from project import Language
from version import Version


def str_project(
    project_name    : str,
    version         : Version,
    languages       : List[ Language ]
) -> str:
    set_project_template = (
        "# ----------------------------------------------------------------\n"
        "# Project: {SHAKE_CMAKE_GENERATOR_project_name}\n"
        "\n"
        "project( {SHAKE_CMAKE_GENERATOR_project_name} VERSION {SHAKE_CMAKE_GENERATOR_version_major}.{SHAKE_CMAKE_GENERATOR_version_minor} LANGUAGES {SHAKE_CMAKE_GENERATOR_languages} )\n"
        "\n"
    )

    languages_str = languages[0].value
    for current_language in languages[1:]:
        languages_str += " " + current_language.value

    set_project_str = cmake_format(
        set_project_template,
        project_name    = project_name,
        version_major   = version.major,
        version_minor   = version.minor,
        languages       = languages_str
    )

    if Language.CUDA in languages:
        set_project_str += "find_package( CUDAToolkit )\n\n"

    return set_project_str