"""Main file for the FastAPI Template."""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from fastapi.openapi.docs import get_swagger_ui_html

# from fastapi.staticfiles import StaticFiles

from app.config.helpers import get_api_version
from app.config.settings import get_settings
from app.database.db import database, get_database, database_client
from app.queries import tables_queries
from app.resources import config_error
from app.resources.routes import api_router

# from rich import print  # pylint: disable=W0622


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan function Replaces the previous startup/shutdown functions.

    Correctly we only ensure that the database is available and configured
    properly. We disconnect from the database immediately after.
    """
    try:
        await database.connect()
        print("Database configuration Tested.")
        await create_tables()
    except Exception as exc:
        print(f"Have you set up your .env file?? ({exc})")
        print("Clearing routes and enabling " "error message.")
        app.routes.clear()
        app.include_router(config_error.router)
    finally:
        await database.disconnect()

    yield
    # we would normally put any cleanup code here, but we don't have any at the
    # moment so we just yield.


async def create_tables():
    """Create the database tables."""
    async with await database_client() as db:
        try:
            for table in tables_queries.list_tables_queries:
                await db.execute(table)
        except Exception as exc:
            print(f"Error creating tables: {exc}")
            raise exc
    return True


app = FastAPI(
    title=get_settings().api_title,
    description=get_settings().api_description,
    redoc_url=None,
    # docs_url=None,  # we customize this ourselves
    license_info=get_settings().license_info,
    contact=get_settings().contact,
    version=get_api_version(),
    lifespan=lifespan,
)

app.include_router(api_router)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# set up CORS
cors_list = (get_settings().cors_origins).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# # --------------------- override the default Swagger docs -------------------- #
# @app.get("/docs", include_in_schema=False)
# async def custom_swagger_ui_html():
#     """Customize the default Swagger docs.

#     In this case we merely override the default page title.
#     """
#     return get_swagger_ui_html(
#         openapi_url=app.openapi_url,  # type: ignore
#         title=f"{app.title} | Documentation",
#         oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#         swagger_ui_parameters={"defaultModelsExpandDepth": 0},
#         swagger_js_url=(
#             "https://cdn.jsdelivr.net/npm/" "swagger-ui-dist@4/swagger-ui-bundle.js"
#         ),
#         swagger_css_url=(
#             "https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui.css"
#         ),
#     )
