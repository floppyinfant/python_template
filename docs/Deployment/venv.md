# Virtual Environments:

## venv
https://docs.python.org/3/library/venv.html  
```
# create venv
python -m venv .venv

# activate venv
source .venv/bin/activate  #Linux
.venv/Scripts/activate     #Windows

# deactivate venv

```

## conda
https://conda.io/docs/commands.html#conda-vs-pip-vs-virtualenv-commands  
```
# list all environments
conda info --envs

# create env
conda create --name $ENVIRONMENT_NAME python

# activate env
source activate $ENVIRONMENT_NAME

# deactivate env
source deactivate
```

## uv
```
uv init .
uv add <package_name>   # creates .venv
uv venv                 # creates .venv
.venv/Scripts/activate  # Windows
```
