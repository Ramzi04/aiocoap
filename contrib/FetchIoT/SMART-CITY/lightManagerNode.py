#!/usr/bin/env python3


"""This represents a server of each office which host the sesnors/actuators resources"""

from random import randint

import aiocoap.resource as resource
import aiocoap


class DimmableLightResource(resource.Resource):
    """Dimmable Light Resource"""
    
    def __init__(self):
        super().__init__()
        self.content = b"Dimmer Settings: 40%"
        
    async def render_get(self, request):
        return aiocoap.Message(payload=self.content)
        
    async def render_put(self, request):
        print('PUT payload: %s' % request.payload)
        self.content = request.payload
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.content)
        

class LightSensorResource(resource.Resource):
    """Light Sensor Resource"""
    
    async def render_get(self, request):
        percentage = str(randint(1, 100)).encode('ascii')
        return aiocoap.Message(payload=percentage)
        
    @staticmethod
    def createNode():
        # Resource tree creation
        root = resource.Site()
        
        root.add_resource(['3311', '0','5851'], DimmableLightResource())
        root.add_resource(['3311', '1','5851'], DimmableLightResource())
        root.add_resource(['3301', '0', '5700'], LightSensorResource())
        root.add_resource(['3301', '1', '5700'], LightSensorResource())
        
        node = resource.Site()
        node.add_resource(['.well-known', 'core'],
                resource.WKCResource(node.get_resources_as_linkheader, impl_info='https://github.com/Ramzi04/aiocoap/#version-1.0'))
        node.add_resource(["lightManager"], root)
        
        return node
