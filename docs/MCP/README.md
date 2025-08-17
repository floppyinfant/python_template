# Model Context Protocol (MCP)

## Server  

Blender  
https://github.com/ahujasid/blender-mcp  
https://blender-mcp.com/  

Ableton Live  
https://github.com/ahujasid/ableton-mcp  

Reaper  
https://github.com/dschuler36/reaper-mcp-server  
https://playbooks.com/mcp/itsuzef-reaper  


### VScode
.vscode/mcp.json  
```
{
	"servers": {
		"blenderMCP": {
			"type": "stdio",
			"command": "uvx",
			"args": [
				"blender-mcp"
			]
		},
        "AbletonMCP": {
            "command": "uvx",
            "args": [
                "ableton-mcp"
            ]
        }
	},
	"inputs": []
}
```
---

### Gemini
~/.gemini/settings.json  
```
{
	"mcpServers": {
		"blenderMCP": {
			"command": "uvx",
			"args": [
				"blender-mcp"
			]
		},
        "AbletonMCP": {
            "command": "uvx",
            "args": [
                "ableton-mcp"
            ]
        }
	}
}
```
---

