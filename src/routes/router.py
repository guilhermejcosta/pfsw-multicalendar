from sys import path
from os.path import join
from os import  getenv
from fastapi import FastAPI

path.append(join(getenv('APP_PATH')))

from src.routes.rest_router import Router as RestRouter
# from src.routes.graphql_router import GraphRouter

class Router:
    def __init__(self):
        self.rest_routes = RestRouter