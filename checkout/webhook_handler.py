from django.http import HttpResponse


class webhook_handler
    """ handle stripe webhooks """
    def __init__(self, request)
    self.request = request


    def handle_event(self,event)
        """ handle a generic/unknown/unexpected webhook event """
        
        return HttpResponse(
            content= f'webhook recieved: {event["type"]}',
            status=200)