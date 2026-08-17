# OneNote-MCP-For-GeminiSpark

A small integration/utility to connect OneNote with GeminiSpark using the MCP (Message/Media/Content Provider) pattern. This repository contains code, configuration, and examples to synchronize OneNote content with GeminiSpark workflows, export OneNote notes into GeminiSpark-ready formats, and demonstrate common automation scenarios.

> Note: This README is intentionally generic — update the Usage and Configuration sections with repository-specific commands, environment variables, and examples after implementing the concrete integration details.

## Features

- Export OneNote pages and sections to structured JSON or Markdown
- Map OneNote metadata (titles, tags, created/modified dates) to GeminiSpark message fields
- Batch-sync and one-off export modes
- Hooks/examples for sending exported content to GeminiSpark endpoints or storing in MCP-compatible storage

## Requirements

- Node.js >= 18 (or adjust depending on repo language)
- A Microsoft OneNote account / Microsoft Graph credentials with OneNote permissions
- (Optional) Credentials or API access for GeminiSpark endpoints

## Installation

1. Clone the repository

   git clone https://github.com/abhivishwa2/OneNote-MCP-For-GeminiSpark.git
   cd OneNote-MCP-For-GeminiSpark

2. Install dependencies (example for Node.js projects)

   npm install

Adjust the commands above if this project uses a different runtime or package manager (Python/pip, dotnet, etc.).

## Configuration

Create a `.env` file or update the configuration file with the following values (names are examples — match them to the actual implementation):

```
# Microsoft Graph / OneNote
GRAPH_CLIENT_ID=your-client-id
GRAPH_CLIENT_SECRET=your-client-secret
GRAPH_TENANT_ID=your-tenant-id
GRAPH_SCOPES=Notes.Read.All

# GeminiSpark / MCP endpoint
GEMINI_ENDPOINT=https://api.geminispark.example/v1/ingest
GEMINI_API_KEY=your-api-key

# Sync options
SYNC_MODE=batch     # or "one-off"
EXPORT_FORMAT=markdown # or json
```

If your project uses a different config mechanism, add instructions here for that mechanism (config.yaml, credentials file, secret manager, etc.).

## Usage

Examples below are illustrative. Replace `node ./bin/sync.js` with the actual entrypoint for this repository.

- Run a one-off export

  npm run export -- --notebook "My Notebook" --format markdown

- Run scheduled/batch sync

  npm run sync

- Send exported content to GeminiSpark

  npm run push -- --file ./exports/notes.json

## Project structure (suggested)

- src/           # Source code
- bin/           # CLI entrypoints or scripts
- examples/      # Example configs and request payloads
- tests/         # Unit and integration tests
- docs/          # Additional documentation

Update this section to reflect the actual layout of the repository.

## Development

- Run tests:

  npm test

- Lint and format:

  npm run lint
  npm run format

- Add a new connector or transformer by creating a new module under `src/connectors` and register it in the main sync flow.

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

If you'd like, I can tailor this README to the actual implementation details in the repo (language, commands, code examples). Tell me to inspect the repository and I'll update the Usage and Configuration sections with live commands and examples.
