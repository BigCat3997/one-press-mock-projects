import configparser
import logging
import os
from datetime import datetime

import uvicorn
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Specify the directory name
dir_name = "logs"

# Check if the directory exists
if not os.path.exists(dir_name):
    # If the directory doesn't exist, create it
    os.makedirs(dir_name)

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)
logging_file_name = "application-{:%Y%m%d}.log".format(datetime.now())
handler = logging.FileHandler(f"logs/{logging_file_name}")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Bootstrap the application...")

config = configparser.ConfigParser()

config.read("resources/config.ini")

app_name = config.get("CONFIGURATION", "APP_NAME", fallback="Simple API")
app_version = config.get("CONFIGURATION", "APP_VERSION", fallback="1.0.0")
app_port = config.getint("CONFIGURATION", "APP_PORT", fallback=8000)
sub_path = config.get("CONFIGURATION", "SUB_PATH", fallback="")
app_workers = config.getint("CONFIGURATION", "APP_WORKERS", fallback=1)

app = FastAPI(
    docs_url=f"{sub_path}/swagger-ui",
    openapi_url=f"{sub_path}/openapi.json",
    redoc_url=None,
    title=app_name,
    description=f"This is {app_name}.",
    version=app_version,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(f"{sub_path}/")
async def root():
    return {"message": f"Hello {app_name}!"}


@app.get(f"{sub_path}/version")
async def version():
    return {"name": f"{app_name}", "version": app_version}


@app.get(f"{sub_path}/vaults/secrets")
async def list_secrets():
    vault_url = os.getenv("VAULT_URL", "")
    vault_tenant_id = os.getenv("VAULT_TENANT_ID", "")
    vault_client_id = os.getenv("VAULT_CLIENT_ID", "")
    vault_client_secret = os.getenv("VAULT_CLIENT_SECRET", "")

    credential = ClientSecretCredential(
        tenant_id=vault_tenant_id,
        client_id=vault_client_id,
        client_secret=vault_client_secret,
    )

    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    secret_names = [
        secret.name for secret in secret_client.list_properties_of_secrets()
    ]
    print(secret_names)
    return secret_names


if __name__ == "__main__":
    print(f"The application are running with {app_workers} workers at {app_port} port.")

    uvicorn.run(
        "main:app", host="0.0.0.0", port=app_port, workers=app_workers, reload=False
    )
