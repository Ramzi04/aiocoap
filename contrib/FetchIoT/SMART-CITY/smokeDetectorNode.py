#!/usr/bin/env python3


"""This represents a server of each office which host the sesnors/actuators resources"""

from random import randint

import aiocoap.resource as resource
import aiocoap
        
class CO2SensorResource(resource.Resource):
    """CO2 Sensor Resource"""
    
    async def render_get(self, request):
        concentration = str(1000*randint(1, 6)).encode('ascii')
        return aiocoap.Message(payload=concentration)
        
    @staticmethod
    def createNode():
        # Resource tree creation
        root = resource.Site()    
        root.add_resource(['6047', '0', '5700'], CO2SensorResource())
        
        node = resource.Site()
        node.add_resource(['.well-known', 'core'],
                resource.WKCResource(node.get_resources_as_linkheader, impl_info='https://github.com/Ramzi04/aiocoap/#version-1.0'))
        node.add_resource(["smokeDetecNode"], root)
        
        return node
