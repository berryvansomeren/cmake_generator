import logging
from typing import Dict, List

from cmake_generator.str_cmake_config   import str_cmake_config
from cmake_generator.str_import_target  import str_import_target
from cmake_generator.str_new_target     import str_new_target
from cmake_generator.str_project        import str_project
from cmake_generator.target             import ImportTarget, NewTarget, Target
from cmake_generator.version            import Version

#----------------------------------------------------------------
class CMakeGenerator:

    def __init__(
        self,
        project_name : str,
        project_version : Version,
        cmake_destination_path : str,
        build_dir : str
    ):
        self.cmake_destination_path = cmake_destination_path
        self.cmake_text = ""
        self._write( str_cmake_config( build_dir ) )
        self._write( str_project( project_name, project_version ) )

    # ----------------------------------------------------------------
    def _write( self, text : str ) -> None:
        self.cmake_text += text

    # ----------------------------------------------------------------
    def _add_target( self, target : Target, all_targets :  Dict[ str, Target ] ) -> None:
        dispatcher = {
            NewTarget       : str_new_target,
            ImportTarget    : str_import_target
        }
        # Note: we don't write a specific target for header only libraries
        # You'll see them back in the include directories of the targets that depend on them though
        if target.__class__ in dispatcher:
            self._write( dispatcher[ target.__class__ ]( target, all_targets ) + "\n" )

    # ----------------------------------------------------------------
    def generate( self, target_definitions : List[ Target ] ) -> None:

        logging.info( "----------------------------------------------------------------" )
        logging.info( "Generating CMake text" )

        target_dictionary = {}
        logging.info( "----------------------------------------------------------------" )
        logging.info( "Creating registry of targets" )
        for target in target_definitions:
            target_dictionary.update( { target.name : target} )
            logging.info( "Added target to registry: {}".format( target.name ) )

        logging.info( "----------------------------------------------------------------" )
        logging.info( "Generating CMake output" )
        for target in target_definitions:
            self._add_target( target, target_dictionary )
            logging.info( "Added target to CMake text: {}".format( target.name ) )

        logging.info( "----------------------------------------------------------------" )
        logging.info( "Writing CMake text to: {}".format( self.cmake_destination_path ) )
        with open( self.cmake_destination_path, 'w' ) as file_writer:
            file_writer.write( self.cmake_text )
        logging.info( "Done!" )
