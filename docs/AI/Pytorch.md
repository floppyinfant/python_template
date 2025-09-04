# Pytorch


## Installation

A. Install in .venv (managed by uv):
1. Download CUDA-Toolkit: 12.6 (for GTX 1060)  
https://developer.nvidia.com/cuda-downloads  
https://docs.nvidia.com/cuda/  
nvcc --version  

2. Install PyTorch for CUDA:  
https://pytorch.org/  
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126  

B. use Anaconda environment  

C. use Google CoLab (with free Tesla T4 GPU)  

---

### Error with CUDA-Toolkit 12.9
GPU (sm_61) not compatible with Torch (>= sm_70) --> CUDA-Toolkit 12.6 needed!  

Torch Arch List: ['sm_70', 'sm_75', 'sm_80', 'sm_86', 'sm_90', 'sm_100', 'sm_120']

L:\WORKSPACES\PYTHON_WS\python_template\.venv\Lib\site-packages\torch\cuda\__init__.py:283: UserWarning:
    Found GPU0 NVIDIA GeForce GTX 1060 6GB which is of cuda capability 6.1.
    Minimum and Maximum cuda capability supported by this version of PyTorch is (7.0) - (12.0)

  warnings.warn(
L:\WORKSPACES\PYTHON_WS\python_template\.venv\Lib\site-packages\torch\cuda\__init__.py:304: UserWarning:
    Please install PyTorch with a following CUDA configurations:  12.6
    following instructions at https://pytorch.org/get-started/locally/

  warnings.warn(matched_cuda_warn.format(matched_arches))
L:\WORKSPACES\PYTHON_WS\python_template\.venv\Lib\site-packages\torch\cuda\__init__.py:326: UserWarning:
NVIDIA GeForce GTX 1060 6GB with CUDA capability sm_61 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_70 sm_75 sm_80 sm_86 sm_90 sm_100 sm_120.
If you want to use the NVIDIA GeForce GTX 1060 6GB GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/
