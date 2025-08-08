# uv
https://docs.astral.sh/uv/  
https://docs.astral.sh/uv/getting-started/features/  
```
# Python Versions
uv python list

# Scripts
uv run <script_name>
```

## Projects
https://docs.astral.sh/uv/guides/projects/  
https://docs.astral.sh/uv/guides/migration/pip-to-project/#requirements-files  
```
uv init .

uv init <project_name>  # pyproject.toml
cd <project_name>
uv add <package_name>   # creates .venv

uv sync                 # install packages in .venv
uv tree                 # show package tree
uv build                # build package
uv publish              # publish package to a package index
```

## Tools
https://docs.astral.sh/uv/guides/tools/  
```
uvx <package_name>      # run in a temporary environment
uv tool run <package>   # run in a temporary environment (=uvx)
uv tool install <package_name>
uv tool list
uv tool update-shell
```

## Pip Interface
https://docs.astral.sh/uv/pip/environments/  
```
# create virtual environment .venv
uv venv

# make packages of .venv available (Windows)
.venv/Scripts/activate

# exit virtual environment
deactivate
```

### Package Management
https://docs.astral.sh/uv/pip/packages/  
```
# install package in .venv
uv pip install <package_name>

# install current project as an editable package
uv pip install -e .

uv pip install -r requirements.txt
uv pip install -r pyproject.toml

uv pip list
uv pip tree
uv pip freeze
uv pip check
```

### compile
https://docs.astral.sh/uv/pip/compile/  
```
uv pip compile pyproject.toml -o requirements.txt
uv pip sync requirements.txt
```

## Utility
```
uv cache dir
uv cache clear
uv tool dir
uv python dir
uv self update
```
