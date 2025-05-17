import os
from google.cloud import secretmanager
from google.adk.tools.mcp_tool.mcp_toolset import SseServerParams

def secure_connection():
    return SseServerParams(
        url="https://grid-server:443/mcp",
        headers={"Authorization": f"Bearer {get_secret('mcp-token')}"},
        verify_ssl=True
    )

def get_secret(name):
    client = secretmanager.SecretManagerServiceClient()
    secret_name = f"projects/{os.getenv('PROJECT_ID')}/secrets/{name}/versions/latest"
    response = client.access_secret_version(request={"name": secret_name})
    return response.payload.data.decode('UTF-8')