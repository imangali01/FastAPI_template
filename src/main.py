from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

import src.config as config
from src.routers import router as app_routers


app = FastAPI(title="FastAPI Project Title")


# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie",
                   "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)


@app.middleware("http")
async def catch_all(request: Request, call_next):
    response = await call_next(request)

    common_webbrowsers = ['Mozilla', 'Chrome']
    user_agent = request.headers.get('User-Agent')

    # if re.search(rf"({'|'.join(common_webbrowsers)})", user_agent):
    #     # if request send by webbrowser show error on ui
    #     if response.status_code == 401:
    #         return RedirectResponse("/login")
    #     elif response.status_code == 404:
    #         return templates.TemplateResponse('404/index.html', {'request': request, 'status_code': 404}, status_code=404)
    #     elif response.status_code == 403:
    #         return templates.TemplateResponse('404/index.html', {'request': request, 'status_code': 403}, status_code=403)

    # if request.__dict__['scope']['path'] == '/auth/login':
    #     data = response.headers.__dict__['_list'][2][1].decode("utf-8").replace('; HttpOnly', '').replace('; Secure', '').encode('utf-8')
    #     response.headers.__dict__['_list'][2] = (b'set-cookie', data)

    return response


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(app_routers)
