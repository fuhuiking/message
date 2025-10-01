from fastapi.staticfiles import staticFiles
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi import FastAPI
app = FastAPI(docs_url=None, redoc_url=None)

# 挂载Swagger UI静态资源目录
app.mount("/static", staticFiles(directory="static"), name="static")

#自定义/docs路由
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="API docs",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url="/static/img.png"
    )

#自定义/redoc路由
@app.get("/redoc",include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title +"- ReDoc",
        redoc_js_url="/static/redoc.standalone.js"
    )