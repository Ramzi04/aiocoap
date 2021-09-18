#!/usr/bin/env python3


"""This represents a server of each office which host the sesnors/actuators resources"""

import aiocoap.resource as resource
import aiocoap

        
class PowerStripResource(resource.Resource):
    """Power Strip Resource"""
    def __init__(self):
        super().__init__()
        self.content = b"ON"
        
    async def render_get(self, request):
        return aiocoap.Message(payload=self.content)
        
    async def render_put(self, request):
        print('PUT payload: %s' % request.payload)
        self.content = request.payload
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.content)
    
    @staticmethod
    def createNode():
        # Resource tree creation
        root = resource.Site()
        
        root.add_resource(['3312', '0', '5850'], PowerStripResource())
        root.add_resource(['3312', '1', '5850'], PowerStripResource())
        root.add_resource(['3312', '2', '5850'], PowerStripResource())
        root.add_resource(['3312', '3', '5850'], PowerStripResource())
        
        node = resource.Site()
        node.add_resource(['.well-known', 'core'],
                resource.WKCResource(node.get_resources_as_linkheader, impl_info='https://github.com/Ramzi04/aiocoap/#version-1.0'))
        node.add_resource(["psNode"], root)
        
        return node
