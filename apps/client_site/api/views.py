from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from twilio.rest import Client


@api_view(["POST"])
def booking(request: Request) -> Response:
    print(request.data)
    return Response({
        'success': True,
    })


@api_view(["POST"])
def contact(request: Request) -> Response:
    message = f'{request.data["your-name"]} with phone number {request.data["your-phone"]} wants {request.data["your-subject"]}. Please Call her!'

    account_sid = 'AC24974abf4514d372f564c0278bf99941'
    auth_token = 'fb1c45505879c51bec5962926276aff3'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+12518664540',
        body=message,
        to='+2348141524904'
    )

    print(message.sid)

    return Response({
        'success': True,
        'status': "sent",
        "message": "Thanks For reaching out to Us. We'll contact you shortly",

    })

