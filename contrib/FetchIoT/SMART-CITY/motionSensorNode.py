#!/usr/bin/env python3


"""This represents a server of each office which host the sesnors/actuators resources"""

import random

import aiocoap.resource as resource
import aiocoap
        
class PIRSensorResource(resource.Resource):
    """PIR Sensor Resource"""
    
    async def render_get(self, request):
        is_present = str(bool(random.getrandbits(1))).encode('ascii')
        return aiocoap.Message(payload=is_present)
        
    @staticmethod
    def createNode():
        # Resource tree creation
        root = resource.Site()
        root.add_resource(['3302', '0', '5500'], PIRSensorResource())
        
        node = resource.Site()
        node.add_resource(['.well-known', 'core'],
                resource.WKCResource(node.get_resources_as_linkheader, impl_info='https://github.com/Ramzi04/aiocoap/#version-1.0'))
        node.add_resource(["presenceNode"], root)
        
        return node
