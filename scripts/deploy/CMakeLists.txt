# CMake is a generator of buildsystems
# @see docs/Tools/cmake.txt


# // Usage:
# mkdir build
# cd build
# cmake -G "Visual Studio 17 2022" ../
# // or:
# cmake ..
# cmake --build . --config Release
# // or:
# cmake -S .. -B .

# // Commands:
# cmake --version


# Documentation:
# https://cmake.org/cmake/help/book/mastering-cmake/chapter/Writing%20CMakeLists%20Files.html
# https://trove.assistants.epita.fr/docs/cmake/
# https://www.jetbrains.com/help/clion/cmakelists-txt-file.html#cmakelist-template
# https://learn.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170
# https://code.visualstudio.com/docs/cpp/cmake-quickstart


cmake_minimum_required(VERSION 3.18)
project(simple_example)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17) # Enable C++17 standard

# Add source files
set(SOURCE_FILES main.cpp)

# Create targets
add_executable(simple_example ${SOURCE_FILES})
#add_library(lib_simple ${SOURCE_FILES})

# ---

# Linker
add_library(MathFunctions mysqrt.cxx)
target_link_libraries(simple_example PUBLIC MathFunctions)

include(scripts/setup_output_dirs.cmake)
add_subdirectory(src)

find_package()

