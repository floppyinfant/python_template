# conda
https://conda.io/docs/user-guide/overview.html  
https://conda.io/docs/_downloads/conda-cheatsheet.pdf  

## Virtual Environments
https://conda.io/docs/commands.html#conda-vs-pip-vs-virtualenv-commands  
```
# list all environments
conda info --envs
conda create --name $ENVIRONMENT_NAME python
source activate $ENVIRONMENT_NAME
source deactivate


conda search $SEARCH_TERM
conda list --name $ENVIRONMENT_NAME
# create requirements file
conda list --export

conda update <package>
conda update --all
conda update python

conda install <package>
conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME
```
