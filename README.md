# cmake_generator
Generate CMakeLists.txt automatically from minimal descriptions in Python.  
(This is an older BitBucket project of mine that I mainly worked on in 2019)

I like what CMake can do for me, but I don't particularly like how CMake wants me to do things. 
Defining targets should be quite simple, and CMake gets in the way with weird syntax and leaky abstractions.
While working on my (now abandoned) hobby game engine **[shake](https://github.com/berryvansomeren/shake/)**, 
I was using a monorepo where every submodule had very similar CMake settings. 
Instead of having many similar CMake files, I thought I would be able to generate those files, minimizing duplication, 
and use Python to make configuration even easier. 
Some examples of minimal target definition using cmake_generator could look like illustrated below. 
Note that in reality, shake has many more components and dependencies.

```python3
# Just a very basic shared library
shake_core_target_definition = SharedLibrary(
    name            = 'shake_core',
    src_dir_path    = absp( './src' ),
    dependencies    = [ 'glm' ]
)

# pyshake contains the python bindings for shake
# it contains c++ code that can be compiled to a library usable in Python
pyshake_target_definition = PythonModule(
    name = 'pyshake',
    src_dir_path = absp( './src' ),
    dependencies = [
        'glm',
        'pybind11',
        'shake_core',
    ]
)
```

The generator can gather many of such target specifications and generate the corrresponding CMakeLists.txt.