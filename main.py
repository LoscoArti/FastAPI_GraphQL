from fastapi import FastAPI
import strawberry
import uvicorn
from strawberry.fastapi import GraphQLRouter

from Graphql.query import Query
from Graphql.mutation import Mutation

from config import db


def init_app():
    apps = FastAPI(
        title="GraphQL FastAPI Application", description="Fast API", version="1.0.0"
    )

    @apps.on_event("startup")
    async def startup():
        await db.create_all()

    @apps.on_event("startup")
    async def shutdown():
        await db.close()

    @apps.get("/")
    def home():
        return "welcome to the home page!"

    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema=schema)

    apps.include_router(graphql_app, prefix="/graphql")

    return apps


app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)
