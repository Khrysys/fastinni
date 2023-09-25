from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from json import dumps
from fastapi import Depends
from fastapi_mail import MessageSchema, MessageType

from ...extensions import mail

contact = APIRouter(prefix="/contact", tags=['Contact'])

@contact.post('/')
async def post_contact(request: Request):
    try:
        data = await request.json()
        
        message = MessageSchema(
            recipients=[data['recipient']],
            subject="New Contact Request for Fastinni from " + data['name'],
            body="Additional Data: \n" + dumps(data, indent=4),
            subtype=MessageType.plain
        )
        await mail.send_message(message)
    except:
        return JSONResponse({"detail": "Bad Request"}, status_code=400)