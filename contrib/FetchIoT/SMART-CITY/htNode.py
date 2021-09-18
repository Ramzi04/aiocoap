#!/usr/bin/env python3


"""This represents a server of each office which host the sesnors/actuators resources"""

from random import randint
import random
import asyncio

import aiocoap.resource as resource
import aiocoap
        
class HumiditySensorResource(resource.Resource):
    """Humidity Sensor Resource"""
    
    async def render_get(self, request):
        concentration = str(randint(1, 100)).encode('ascii')
        return aiocoap.Message(payload=concentration)

class TemperatureSensorResource(resource.ObservableResource):
    """Temperature Sensor Resource"""
    
    def __init__(self):
        super().__init__()
        self.handle = None
        self.temperature = 0

    def notify(self):
        self.updated_state()
        self.reschedule()

    def reschedule(self):
        self.handle = asyncio.get_event_loop().call_later(5, self.notify)
        
    def update_observation_count(self, count):
        if count and self.handle is None:
            print("Starting to get the temperature sensor")
            self.reschedule()
        if count == 0 and self.handle:
            print("Starting to get the temperature sensor")
            self.handle.cancel()
            self.handle = None
    
    async def render_get(self, request):
        print('**********************************')
        print(request.payload)
        query = request.payload.decode('utf8')
        query_attribs = dict(s.split('=') for s in query.split('&'))
        gt = query_attribs['gt']
        print(gt)
        
        
        
        self.temperature = str(random.randrange(-50, 50)).encode('ascii')
        return aiocoap.Message(payload=self.temperature)
        
    @staticmethod
    def createNode():
        # Resource tree creation
        root = resource.Site()
        
        root.add_resource(['3304', '0', '5700'], HumiditySensorResource())
        root.add_resource(['3303', '0', '5700'], TemperatureSensorResource())
        
        node = resource.Site()
        node.add_resource(['.well-known', 'core'],
                resource.WKCResource(node.get_resources_as_linkheader, impl_info='https://github.com/Ramzi04/aiocoap/#version-1.0'))
        node.add_resource(["htNode"], root)
        
        return node
