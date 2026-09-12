from fastapi import Request
from fastapi.responses import JSONResponse


class PincodeNotFoundError(Exception):
    def __init__(self,pincode: str):
            self.pincode = pincode

class InvalidPincodeError(Exception):
      def __init__(self, pincode: str, reason: str):
            self.pincode = pincode
            self.reason = reason

#Custom Handler
async def pincode_not_found_handler(req: Request, exception: PincodeNotFoundError):
      return JSONResponse(status_code=404,
                          content={
                                "error": "Pincode not found",
                                "message": f"No pincode found for pincode: {exception.pincode}"
                          })

async def invalid_pincode_handler(req: Request, exception: InvalidPincodeError):
      return JSONResponse(status_code=422,
                          content={
                                "error": "Pincode Invalid",
                                "message": f"Invalid pincode for pincode: {exception.pincode}"
                          })