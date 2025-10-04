r"""
Genesis for Embodies AI, Physical AI, Robotics
Physics Engine, Robotics Simulation Platform, Generative Agentic AI Framework, Rendering System

https://github.com/Genesis-Embodied-AI/Genesis/

https://github.com/Genesis-Embodied-AI/Genesis/tree/main/examples


https://genesis-world.readthedocs.io/en/latest/user_guide/index.html

https://genesis-world.readthedocs.io/en/latest/api_reference/index.html

---

https://docs.taichi-lang.org/

---

Installation:
https://genesis-world.readthedocs.io/en/latest/user_guide/overview/installation.html

# first install PyTorch & CUDA Toolkit
# https://developer.nvidia.com/cuda-12-6-3-download-archive
# uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

uv pip install genesis-world

# or
pip install git+https://github.com/Genesis-Embodied-AI/Genesis.git

---

# or with Ray Tracer:
# https://genesis-world.readthedocs.io/en/latest/user_guide/getting_started/visualization.html#photo-realistic-ray-tracing-rendering
git clone https://github.com/Genesis-Embodied-AI/Genesis.git
cd Genesis
git submodule update --init --recursive
uv pip install -e ".[render]"
# alternative: pip install "pybind11[global]"
# install gcc, gxx, cmake, vulkan, x11, libuuid, zlib
cd genesis/ext/LuisaRender
# Remember to use the correct cmake. By default, we use OptiX denoiser (For CUDA backend only). If you need OIDN denoiser, append -D LUISA_COMPUTE_DOWNLOAD_OIDN=ON.
#cmake -S . -B build -D CMAKE_BUILD_TYPE=Release -D PYTHON_VERSIONS=3.13 -D LUISA_COMPUTE_DOWNLOAD_NVCOMP=ON -D LUISA_COMPUTE_ENABLE_GUI=OFF -D LUISA_RENDER_BUILD_TESTS=OFF # remember to check python version
cmake -S . -B build -D CMAKE_BUILD_TYPE=Release -D PYTHON_VERSIONS=3.13 -D LUISA_COMPUTE_DOWNLOAD_NVCOMP=ON -D LUISA_COMPUTE_ENABLE_GUI=OFF -D LUISA_RENDER_BUILD_TESTS=OFF -D CMAKE_CUDA_COMPILER="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\bin\nvcc.exe" -D LUISA_COMPUTE_ENABLE_CUDA=ON -D LUISA_COMPUTE_ENABLE_DX=OFF -D NVTT_DIR="C:\Program Files\NVIDIA Corporation\NVIDIA Texture Tools" -D pybind11_DIR="L:\WORKSPACES\PYTHON_WS\python_template\.venv\Lib\site-packages\pybind11\share\cmake\pybind11"
cmake --build build -j $(nproc)

---

# build Open3D from Source for Python 3.13 (no wheels on Pypy or releases):
# https://www.open3d.org/docs/latest/compilation.html#compilation
git clone https://github.com/isl-org/Open3D
cd Open3D
mkdir build
cd build
cmake -G "Visual Studio 17 2022" -A x64 -DCMAKE_INSTALL_PREFIX="dist_bin" ..
cmake --build . --config Release --target ALL_BUILD
# :: install Open3D C++ library
#cmake --build . --config Release --target INSTALL
# :: install Open3D Python library
cmake --build . --config Release --target install-pip-package
# :: Create pip package in build/lib
# :: This creates a .whl file that you can install manually.
cmake --build . --config Release --target pip-package
# verify Python installation
python -c "import open3d; print(open3d)"

---

# get infos on your system:
# Check the maximum CUDA version supported by the installed NVIDIA driver
nvidia-smi          # NVIDIA-SMI 576.57, Driver Version: 576.57, CUDA Version: 12.9
# check your "active" cuda version
nvcc --version      # Cuda compilation tools, release 12.6, V12.6.85, Build cuda_12.6.r12.6/compiler.35059454_0
cmake --version     # cmake version 3.27.4


"""

import numpy as np
import genesis as gs

########################## init ##########################

gs.init(backend=gs.gpu)

scene = gs.Scene(
    show_viewer = True,
    viewer_options = gs.options.ViewerOptions(
        res             = (1920, 1080),
        camera_pos      = (3.5, 0, 2.5),
        camera_lookat   = (0, 0, 0.5),
        camera_fov      = 40,
        max_FPS         = 60,
    ),
    vis_options = gs.options.VisOptions(
        show_world_frame = True, # visualize the coordinate frame of `world` at its origin
        world_frame_size = 1.0, # length of the world frame in meter
        show_link_frame  = False, # do not visualize coordinate frames of entity links
        show_cameras     = False, # do not visualize mesh and frustum of the cameras added
        plane_reflection = True, # turn on plane reflection
        ambient_light    = (0.1, 0.1, 0.1), # ambient light setting
    ),
    renderer = gs.renderers.Rasterizer(), # using rasterizer for camera rendering,
    #renderer=gs.renderers.RayTracer(),  # need to compile LuisaRender:
    # https://genesis-world.readthedocs.io/en/latest/user_guide/getting_started/visualization.html#photo-realistic-ray-tracing-rendering

    # Physics Simulation: Smooth Particle Hydrodynamics (SPH) Solver, Material Point Method (MPM) Solver, Position Based Dynamics (PBD) Solver
    # https://genesis-world.readthedocs.io/en/latest/user_guide/getting_started/beyond_rigid_bodies.html
    # sim_options = gs.options.SimOptions(
    #     dt = 0.01,
    # ),
)

########################## entities ######################

plane = scene.add_entity(
    gs.morphs.Plane()
)

# gs.morphs.Box, Cylinder, Sphere (Shape Primitives)
# gs.morphs.Terrain for custom height maps
# gs.morphs.MJCF for MuJoCo XML robot configurations
# gs.morphs.URDF for Unified Robot Description Format files
# gs.morphs.Mesh for 3D assets like .obj, .ply, .stl, .glb, and .gltf

########################## cameras #######################

cam_0 = scene.add_camera(
    res = (1920, 1080),
    pos = (3.5, 0.0, 2.5),
    lookat = (0.0, 0.0, 0.5),
    fov = 30,
    GUI = True,  # if 'True': each camera will create an opencv window to dynamically display the rendered image.
                 # Note that this is different from the viewer GUI.
    # spp = 512,
)

scene.build()
# scene.reset()

# start camera recording.
cam_0.start_recording()
for i in range(120):
    scene.step()

    cam_0.render()
    # Alternative: opens 4 windows, if 'GUI = True'
    # rgb, depth, segmentation, normal = cam.render(depth=True, segmentation=True, normal=True)

    # change camera position
    cam_0.set_pose(
        pos=(3.0 * np.sin(i / 60), 3.0 * np.cos(i / 60), 2.5),
        lookat=(0, 0, 0.5),
    )

# stop recording and save video.
cam_0.stop_recording(save_to_filename='video.mp4', fps=60)
