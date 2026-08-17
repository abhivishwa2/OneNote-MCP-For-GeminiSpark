# OneNote-MCP-For-GeminiSpark

A small integration/utility to connect OneNote with GeminiSpark using the MCP (Message/Media/Content Provider) pattern. This repository contains code, configuration, and examples to synchronize OneNote content with GeminiSpark workflows, export OneNote notes into GeminiSpark-ready formats, and demonstrate common automation scenarios.

> Note: This README is intentionally generic — update the Usage and Configuration sections with repository-specific commands, environment variables, and examples after implementing the concrete integration details.

## Features

- Export OneNote pages and sections to structured JSON or Markdown
- Map OneNote metadata (titles, tags, created/modified dates) to GeminiSpark message fields
- Batch-sync and one-off export modes
- Hooks/examples for sending exported content to GeminiSpark endpoints or storing in MCP-compatible storage

## Requirements

- Python 3.10+
- uv package manager (recommended) or pip
- Microsoft Azure account (free)
- A Microsoft OneNote account / Microsoft Graph credentials with OneNote permissions
- (Optional) Credentials or API access for GeminiSpark endpoints

## Installation

. Install uv (if you don't have it)
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# or with Homebrew
brew install uv
2. Clone and Setup
git clone https://github.com/yourusername/onenote-mcp-server.git
cd onenote-mcp-server

# Create virtual environment and install dependencies
uv sync
3. Azure App Registration
You need to create an Azure app to access OneNote. Don't worry, it's free and takes 5 minutes:

# Go to Azure Portal (sign in with your Microsoft account)
Navigate to Azure Active Directory → App registrations → New registration
Fill out the form:
Name: "OneNote MCP Server" (or whatever you like)
Supported account types: "Accounts in any organizational directory and personal Microsoft accounts"
Redirect URI: Select "Web" and enter: <Redirect URI from Gemini Spark Custom Connected App Dialog Box>
Click Register
Copy the Application (client) ID - you'll need this!
4. Add Permissions
Still in your Azure app:

Go to API permissions → Add a permission
Select Microsoft Graph → Delegated permissions
Add these permissions:
Notes.Read - Read OneNote notebooks
Notes.ReadWrite - Create/modify OneNote content (optional but recommended)
User.Read - Read user profile
Offline.access - No need for Client Secret

Click Grant admin consent (the button at the top)

5 Go to Manifest -> Update signInAudience to AzureADandPersonalMicrosoftAccount and requestedAccessTokenVersion to 2 and Save.

# Generate Azure Refresh Token (One Time Activity)

- Update Azure Client ID in refresh_token.py file and run it on cmd.
- Browser window will open. Login with your Microsoft ID.
- Post successful login,  Token will be generated in cmd.
- 
# Deploy MCP Server on Cloud/Locally
 - e.g. for Google Cloud run following command. 

- gcloud run deploy onenote-mcp-server --source . --region us-central1 --set-env-vars="AZURE_REFRESH_TOKEN=YOUR_AZURE_REFRESH_TOKEN,AZURE_CLIENT_ID=YOUR_ACTUAL_CLIENT_ID" --allow-unauthenticated****
- Post Deployment MCP Server URL will be generated.

# Setup Custom Connected App in Gemini Spark

 - Click on Connected Apps
 - Fill MCP Server URL
 - In Advance Settings -> Fill Azure Client ID
 - Click on Copy Redirect URI and Go to Azure Portal --> Azure Client App --> Authentication --> Redirect URIs  --> Add URI --> Web --> Paste the Copied Link --> Remove any other Redirect URIs
 -  Click next and Follow screens.
 -  Onenote Mcp server will be created in Connected App Screen

## Usage

 - Open Gemini Spark -> Task --> List my OneNote notebook using onenote-mcp-server


## Contributing

Contributions are welcome. Please open an issue first to discuss larger changes. For small fixes, submit a pull request with descriptive commits and tests.

Guidelines:

- Follow existing code style and lint rules
- Add or update tests for new behavior
- Document new configuration or usage in this README

## License

Specify the repository license here (e.g., MIT, Apache-2.0). If you haven't chosen a license yet, consider adding one.

## Acknowledgements

- Microsoft Graph and OneNote API docs
- GeminiSpark integration and MCP design patterns

---


