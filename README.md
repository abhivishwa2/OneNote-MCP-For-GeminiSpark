# OneNote-MCP-For-GeminiSpark

A robust Model Context Protocol (MCP) server for Microsoft OneNote integration with Gemini Spark. This repository contains code, configuration, and examples to synchronize OneNote content with GeminiSpark workflows, export OneNote notes into GeminiSpark-ready formats, and demonstrate common automation scenarios.


## 🎯 What This Does

Transform your OneNote notebooks into an AI-accessible knowledge base:
- **List all your notebooks, sections, and pages**
- **Read page content** for analysis and search
- **Natural language queries** like "Show me my DevOps notes" or "Find pages about project planning"
- **Secure OAuth authentication** with Microsoft Graph API
- **Bulletproof error handling** with detailed debugging

## ✨ Why This Implementation

Unlike other OneNote MCP servers, this one:
- ✅ **Actually works** - tested extensively with real OneNote data
- ✅ **Complete functionality** - all core OneNote operations implemented
- ✅ **Robust authentication** - two-step device flow that handles edge cases
- ✅ **Production ready** - proper error handling and logging
- ✅ **Easy setup** - detailed instructions for non-technical users

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ 
- [uv package manager](https://docs.astral.sh/uv/getting-started/installation/) (recommended) or pip
- Google Gemini Account
- Microsoft Azure account (free)
### 1. Install uv (if you don't have it)
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# or with Homebrew
brew install uv
```

### 2. Clone and Setup
```bash
git clone https://github.com/yourusername/onenote-mcp-server.git
cd onenote-mcp-server

# Create virtual environment and install dependencies
uv sync
```

### 3. Azure App Registration
You need to create an Azure app to access OneNote. **Don't worry, it's free and takes 5 minutes:**

1. Go to [Azure Portal](https://portal.azure.com) (sign in with your Microsoft account)
2. Navigate to **Azure Active Directory** → **App registrations** → **New registration**
3. Fill out the form:
   - **Name**: "OneNote MCP Server" (or whatever you like)
   - **Supported account types**: "Accounts in any organizational directory and personal Microsoft accounts"
4. Click **Register**
5. Copy the **Application (client) ID** - you'll need this!

### 4. Add Permissions
Still in your Azure app:
1. Go to **API permissions** → **Add a permission**
2. Select **Microsoft Graph** → **Delegated permissions**
3. Add these permissions:
   - `Notes.Read` - Read OneNote notebooks
   - `Notes.ReadWrite` - Create/modify OneNote content (optional but recommended)
   - `User.Read` - Read user profile
   - `Offline.access` - Permit Refresh Token Access
4. Click Grant admin consent (the button at the top)
5. Go to Manifest -> Update signInAudience to AzureADandPersonalMicrosoftAccount and requestedAccessTokenVersion to 2 and Save.

### 5. Generate Azure Refresh Token (One Time Activity)

- Update Azure Client ID in refresh_token.py file and run it on cmd.
- Browser window will open. Login with your Microsoft ID.
- Post successful login,  Token will be generated in cmd.
  
### 6. Deploy MCP Server on Cloud/Locally
- e.g. for Google Cloud Deployment run following command. 
  ```
  gcloud run deploy onenote-mcp-server --source . --region us-central1
  --set-env-vars="AZURE_REFRESH_TOKEN=YOUR_AZURE_REFRESH_TOKEN,AZURE_CLIENT_ID=YOUR_ACTUAL_CLIENT_ID"
  --allow-unauthenticated

  ```
- Post Deployment MCP Server URL will be generated.

### 7.  Setup Custom Connected App in Gemini Spark

 - Click on Connected Apps
 - Fill MCP Server URL/sse  (Do not forget to add /sse at the of the URL)
 - In Advance Settings -> Fill Azure Client ID
 - Click on Copy Redirect URI and Go to Azure Portal --> Azure Client App --> Authentication --> Redirect URIs  --> Add URI --> Web --> Paste the Copied Link --> Remove any other Redirect URIs
 - On the Connected App Dialog box -> Click next and Follow screens.
 - Onenote Mcp server will be created in Connected App Screen

## Usage

Once Connected App is setup, try these tasks in Gemini Spark :

```
List my OneNote notebooks
Show me sections in my Work notebook  
What pages are in my Ideas section?
Read the content of my "Project Plan" page
```



## 🛠 Troubleshooting

### "No tools available" in Gemini Spark Connected Apps Screen
- Make sure you copied redirect URI from Screen and updated on Microsoft Azure App correctly.
- Check if your cloud deployment of MCP server is enabled for unauthenticated access.
- Verify uv is installed: `uv --version`

### Authentication issues
- **Safari OAuth problems**: Safari may not handle Microsoft's OAuth redirect properly - use Firefox or Chrome instead
- **"nativeclient" prompts**: Normal Microsoft OAuth behavior, but if it blocks authentication, try a different browser
- **Recommended browsers**: Firefox (confirmed working), Chrome, or Edge for best compatibility

### "Command not found" errors
- Make sure uv is in your PATH
- Alternative: replace `"uv"` with `"python"` in the config and use the full path to your Python interpreter

### Permission denied errors
- Check the file permissions in your project directory
  

## 🏗 Development

### Project Structure
```
onenote-mcp-server/
├── onenote_mcp_server.py      # Main server implementation
├── pyproject.toml             # Dependencies and metadata
├── refresh_token.py           # Generate Refresh Token
├── README.md                  # This file
├── LICENSE                    # MIT License
└── .gitignore                 # Git ignore rules
```

### Key Features

- **Complete Graph API integration**: All OneNote operations supported
- **Robust error handling**: Detailed logging and graceful failures
- **FastMCP framework**: Clean, maintainable code structure
- **Environment variable configuration**: Secure credential handling

### Adding New Features
The server is built with FastMCP, making it easy to add new tools:

```python
if method == "tools/list":
                    await custom_send({"type": "http.response.start", "status": 200, "headers": [(b"content-type", b"application/json")]})
                    tools = [
  
    # Your implementation here
    return 
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch
3. Add tests for new functionality  
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp) framework
- Uses Microsoft Graph API for OneNote access
- Inspired by the amazing work of [purpleslurple](https://github.com/purpleslurple/onenote-mcp-server)

## ⚠️ Important Notes

- This server only reads/writes data you already have access to
- Your Azure app credentials stay on your machine
- All authentication happens directly between you and Microsoft
- No data is sent to third parties

---

**Built with ❤️ for the Gemini Spark + OneNote community**

*Turn your OneNote into an AI-accessible knowledge base!*
