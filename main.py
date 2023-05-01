from sys import path
from os.path import join
from os import  getenv
from fastapi import FastAPI

path.append(join(getenv('APP_PATH')))

from src.routes.router import Router
from src.metadata.tags import tags_metadata

description = """
Multi Calendar API Service ajuda você a gerenciar múltiplas agendas em um mesmo espaço.

Não será mais necessário ter diversas contas em uma ou mais plataformas.<br>
Além disso, diga adeus ao papel. Ajude o meio ambiente.
"""

app = FastAPI(
    title="Multi Calendar API Service",
    description=description,
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Guilherme José Costa",
        #"url": "http://x-force.example.com/contact/",
        "email": "guiijc96@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
    openapi_url="/api/openapi.json",
    docs_url=None, # Documentação OpenAPI 3.0 Swagger
    redoc_url="/documentation" # Documentação OpenAPI 3.0 ReDoc
)

app.include_router(Router().rest_routes)
# app.include_router(RouterGraphQL, prefix="/graphql")