from fastapi import Request

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from utils import process_desbaste_for_sitio

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.post("/api/desbaste")
async def calculate(request: Request):
    body = await request.json()
    
    # Extract data from request body
    percent = float(body.get('percent', 50))
    sitios_data = body.get('data', [])

    # Process each sitio
    sitios_results = []
    
    for sitio in sitios_data:
        sitio_num = sitio.get('numSitio')
        sitio_data = sitio.get('dataSitio', [])
        num_desbastes = body.get('numDesbastes')
        
        # Process this sitio's data
        sitio_result = await process_desbaste_for_sitio(sitio_data, percent)
        
        # Add sitio number to the result
        sitio_result['numSitio'] = sitio_num
        sitios_results.append(sitio_result)
    
    # Construct final response
    final_response = {
        'numDesbastes': body.get('numDesbastes'),
        'numSitios': body.get('numSitios'),
        'percent': percent,
        'sitios_results': sitios_results
    }
    
    print("Final response:", final_response)
    return final_response