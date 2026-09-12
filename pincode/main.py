from fastapi import FastAPI
from fastapi.responses import JSONResponse

from exceptions import PincodeNotFoundError, pincode_not_found_handler, InvalidPincodeError, invalid_pincode_handler
from models import BulkRequest, BulkResponse, LocationResponse
from data import pincode_db
app = FastAPI(title = "Pincode API",
              description="This is an API for getting the Pincode of a state.")

#register custom exception handlers
app.add_exception_handler(PincodeNotFoundError, pincode_not_found_handler)  # pyright: ignore[reportArgumentType]
app.add_exception_handler(InvalidPincodeError, invalid_pincode_handler)# pyright: ignore[reportArgumentType]

@app.get('/pincode')
def get_pincode():
    return JSONResponse(content={
        "message": "Pincode is up and running"
    })

@app.get("/pincode/{code}",response_model=LocationResponse)
def lookup_pincode(code : str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPincodeError(code, "Must be exactly 6 digits")
    if code not in pincode_db:
        raise PincodeNotFoundError(code)
    return pincode_db[code]

@app.post("/pincode/bulk")
def bulk_lookup(request: BulkRequest):
    results = []
    missing = []

    for pincode in request.pincodes:
        if pincode not in pincode_db:
            missing.append(pincode)
        else:
            results.append(pincode_db[pincode])

    return BulkResponse(
        found = len(results),
        not_found = len(missing),
        location_response = results,
        missing_pincodes = missing
        )
