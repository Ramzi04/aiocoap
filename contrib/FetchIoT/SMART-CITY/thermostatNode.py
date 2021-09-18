#!/usr/bin/env python3


"""This represents a server of each office which host the sesnors/actuators resources"""

import aiocoap.resource as resource
import aiocoap

class ThermostatResource(resource.Resource):
    """SMART Lock Resource"""
    def __init__(self):
        super().__init__()
        self.currentTemp = b"25 Deg Cel"
        
    async def render_get(self, request):
        return aiocoap.Message(payload=self.currentTemp)
        
    async def render_put(self, request):
        print('PUT payload: %s' % request.payload)
        self.currentTemp = request.payload
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.currentTemp)
        
    @staticmethod
    def createNode():
        # Resource tree creation
        root = resource.Site()
        
        root.add_resource(['12300', '0', '5209'], ThermostatResource())
        
        node = resource.Site()
        node.add_resource(['.well-known', 'core'],
                resource.WKCResource(node.get_resources_as_linkheader, impl_info='https://github.com/Ramzi04/aiocoap/#version-1.0'))
        node.add_resource(["thermostat"], root)
        
        return node
