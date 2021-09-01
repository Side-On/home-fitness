from django.http import HttpResponse

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhood has been received: {event["type"]}',
        status=200)