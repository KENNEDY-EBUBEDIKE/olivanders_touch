from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(["POST"])
def booking(request: Request) -> Response:
    print(request.data)
    return Response({
        'success': True,
    })


@api_view(["POST"])
def contact(request: Request) -> Response:

    print(request.data)

    return Response({
        'success': True,
        'status': "sent",
        "message": "Thanks For reaching out to Us. We'll contact you shortly",

    })

