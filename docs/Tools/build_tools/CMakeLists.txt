cmake_minimum_required(VERSION 3.18...3.21)           # required
cmake_policy(VERSION 3.18)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)
set(CMAKE_CXX_EXTENSIONS OFF)
set(BUILD_SHARED_LIBS ON)

project(LuisaRender LANGUAGES C CXX VERSION 0.1)      # required

option(LUISA_RENDER_BUILD_TESTS "Build tests for LuisaRender" ON)

include(src/compute/scripts/setup_output_dirs.cmake)  # cmake-script file *.cmake
add_subdirectory(src)                                 # which contains a CMakeLists.txt

# create an executable
add_executable(hello-world hello-world.cpp)

# create a STATIC or SHARED | MODULE library
add_library(message STATIC Message.hpp Message.cpp )

# link library to executable
target_link_libraries(hello-world message)

# ----------------------------------------------------------------------------
# more
# ----------------------------------------------------------------------------

target_include_directories()

find_package()

# set up install directories
include(GNUInstallDirs)
if (NOT WIN32)
    # DLLs are installed in the same directory as executables
    set(CMAKE_INSTALL_LIBDIR ${CMAKE_INSTALL_BINDIR})
elseif(APPLE)
    message()
elseif(UNIX)
    message()
endif ()

# ----------------------------------------------------------------------------
# Docs
# ----------------------------------------------------------------------------

# Usage:
# cmake --version

# mkdir build
# cd build

# // 1. Generate
# cmake -G "Visual Studio 17 2022" ../
# // 2. Build
# // manually build in VS

# // or:
# cmake ..
# cmake --build . --config Release

# // or with Build Options:
# cmake -S .. -B .
# cmake --build . -D CMAKE_BUILD_TYPE=Release

# ----------------------------------------------------------------------------

# Directories and Files:
# bin
# lib
# dist
# CMakeLists.txt
# *.cmake
# CMakeFiles
# *.vcxproj
# .sln

# ----------------------------------------------------------------------------

# Documentation:
# https://cmake.org/cmake/help/book/mastering-cmake/chapter/Writing%20CMakeLists%20Files.html
# https://trove.assistants.epita.fr/docs/cmake/
# https://www.jetbrains.com/help/clion/cmakelists-txt-file.html#cmakelist-template
# https://learn.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170
# https://code.visualstudio.com/docs/cpp/cmake-quickstart

# ----------------------------------------------------------------------------
# End
# ----------------------------------------------------------------------------
