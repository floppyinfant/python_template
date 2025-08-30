# Blender Python API

https://docs.blender.org/api/current/index.html  

Extensions Tutorial  
https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html  

Addon Tutorial  
https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html  

---

YouTube Tutorial  
https://youtu.be/wWTAQP7-ZUQ (Blender)  

https://www.youtube.com/@CGPython  
https://youtu.be/YUytEtaVrrc (VScode Setup)  
https://youtu.be/0_QskeU8CPo (Panel Demo)  

https://youtube.com/playlist?list=PLRKZHg6r5mu42davqG2wUl_P-JDgJTaus (Curtis Holt)  

https://www.youtube.com/@DarkfallBlender  

---

## Blender Scripting Workspace

In Preferences > Interface > Python Tooltips enable  
In Preferences > Interface > Developer Extras enable  

## Development Tools  

https://developer.blender.org/docs/handbook/extensions/addon_dev_setup/  

### IDE VScode  

https://developer.blender.org/docs/handbook/development_environments/vscode/  

Blender Development Extension  
https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development  
Installs modules in Blender for Debugging;  
N-Panel > Dev:  
- Blender at Port 7993
- debugpy at Port 5428
- Editor at http://localhost:61762  

Setup  
Give write Permissions to Python Directory inside Blender Installation Path.  
https://youtu.be/YUytEtaVrrc?t=501  
Ctrl + Shift + P (Command Palette) > Blender: Start (Choose Blender.exe)  

Usage  
Ctrl + Shift + P (Command Palette) > Blender: Run Script  

Fake-bpy Module  
https://github.com/nutti/fake-bpy-module  
https://pypi.org/project/fake-bpy-module/  
```Bash
.venv/Scripts/activate
pip install fake-bpy-module
```
```Python
import bpy
"""automatically uses fake-bpy in VScode and works in Blender"""
```

