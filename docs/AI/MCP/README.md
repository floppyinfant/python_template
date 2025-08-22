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

# MCP-Server
https://github.com/modelcontextprotocol/servers  
https://modelcontextprotocol.io/docs/getting-started/intro  
https://mcp.so/  

https://hub.docker.com/u/mcp  
https://github.com/docker/mcp-servers  

https://mcpservers.org/  
https://github.com/punkpeye/awesome-mcp-servers  
https://code.visualstudio.com/mcp  
https://mcpmarket.com/  
https://mcpservers.com/  

---

# Module

## Input
Speech-Recognition  
Image-Recognition, OCR  
Translation  
Screen-capturing  
Computer-Vision: Live Webcam Tracking, Feature Detection, ...  

## Processing
LLM  
API  

### MCP  
#### RAG  
Websearch  
Vectordatabase  

Google Maps, OpenStreetMaps (OSM)  

Github  
Gist  
Notion  
Cloud: Google Drive, One Drive, Apple iCloud, ... anonymous Spaces  
Google Services: Calendar, Documents / Sheets / Präsentationen
Webspace: Website, Blog, FTP, ...
NAS, Home Automation, ...  
Social Media: Instagram, X, YouTube, Reddit, ...  
Messenger: email, WhatsApp, Telegram, SMS, ...  
SQlite, PostgreSQL  

## Output
Sprachausgabe  
Untertitel (Captions)  
Avatar  

---

# Development
https://docs.anthropic.com/en/docs/mcp  
https://modelcontextprotocol.io/docs/getting-started/intro  
https://openai.github.io/openai-agents-python/mcp/  
https://huggingface.co/learn/mcp-course/unit0/introduction  
https://github.com/daveebbelaar/ai-cookbook/tree/main/mcp/crash-course  

Python SDK  
https://github.com/modelcontextprotocol/python-sdk  
https://github.com/jlowin/fastmcp  
