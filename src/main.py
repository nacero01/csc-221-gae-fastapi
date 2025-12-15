from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse


app = FastAPI(title='CSC 221 - FastAPI on Google App Engine',
              description='The boilerplate for a FastAPI app on Google App Engine',
              redoc_url=None,
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=['*'],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS'], # allow_methods=['*'],
)

@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    return JSONResponse(status_code=500, content={
        'detail': [
            {'msg': str(err), 'type': type(err).__name__}
        ]
    })

router = APIRouter()

@router.get('/')
async def home_page():
    return "welcome"

@router.get('/id')
async def my_empl_id():
    return {'empl_id':'23759741'}

app.include_router(router)
