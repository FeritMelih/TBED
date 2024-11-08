# LLM Emergency Detection Server

A simple HTTP server that processes text through Large Language Models (LLM) to detect emergency situations. Currently supports LM Studio and is prepared for Ollama integration.

## Features

- HTTP server implementation for emergency text analysis
- Support for LM Studio integration
- JSON-based API interface
- Configurable port and model settings
- Platform override capabilities

## Prerequisites

- Python 3.x
- LM Studio installed and running locally
- Required Python packages:
  - `http.server`
  - `json`
  - Custom `TBED_LMstudio` module

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Default settings in the code:
```python
server_port = 9111
platform = "LMstudio"
port = 1234
url = 'http://localhost:1234/v1/chat/completions'
model = "llama3"
```

## Usage

1. Start the server:
```bash
python server.py
```

2. Send POST requests to `http://localhost:9111` with JSON payload:

Basic request format:
```json
{
    "message": "your text here"
}
```

Advanced request with overrides:
```json
{
    "message": "your text here",
    "platform_override": "LMstudio",
    "port_override": 1234
}
```

## API Reference

### Endpoints

`POST /`

#### Request Body Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| message | string | Text to analyze for emergency situations |
| platform_override | string | (Optional) Override default platform |
| port_override | integer | (Optional) Override default port |

#### Response Format

Success Response:
```json
{
    "status": "success",
    "message": "Data received successfully",
    "emergency": "response data"
}
```

Error Response:
```json
{
    "status": "error",
    "message": "error description"
}
```

## Error Handling

The server handles various error scenarios:
- Invalid JSON format (400)
- Server processing errors (500)
- Platform connection issues

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

[Your License Here]

## Authors

[Your Name]

## Acknowledgments

- LM Studio team
- Contributors to the project
