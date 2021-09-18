#!/usr/bin/env python3

# This file is part of the Python aiocoap library project.
#
# Copyright (c) 2012-2014 Maciej Wasilak <http://sixpinetrees.blogspot.com/>,
#               2013-2014 Christian Amsüss <c.amsuess@energyharvesting.at>
#
# aiocoap is free software, this file is published under the MIT license as
# described in the accompanying LICENSE file.

"""This is a usage example of aiocoap that demonstrates how to implement a
simple client. See the "Usage Examples" section in the aiocoap documentation
for some more information."""

import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()

    #request = Message(code=GET, uri='coap://localhost/.well-known/core')
    #request = Message(code=GET, uri='coap://localhost/endpoint-lookup/?d=bldg1*')

    #x =  '{ "name":"John", "age":30, "city":"New York"}'
    #x =  '{ "hd":{"L1":"d=bldg1.fl1.off1", "L2":"rt=temp OR rt=humd", "L3":""} , "gd":{}}'
    #x =  '{"t":"11","q":"d=bldg1.fl1.off1"}'
    #x =  '{"t":"12","q1":"rt=temp","op":"OR","q2":"rt=humd"}'
    #string_in_string = "rt=ipso.act.lck&if=core.a&d={}".format(x)
    #string_in_string = "rt=ipso.act.lck&if=core.a"
    #x =  '{"t":"11","q":"d=bldg1.fl1.off2"}'
    #payload = bytes(x, encoding='utf-8')
    #request = Message(code=FETCH, payload=payload, uri='coap://localhost/resource-lookup/')
    #request = Message(code=FETCH, uri='coap://localhost/resource-lookup/')
    #request = Message(code=GET, uri='coap://localhost/.well-known/core?rt=core.rd-lookup-res')
    #request = Message(code=GET, uri='coap://localhost/.well-known/core?rt=core.rd')
    #request = Message(code=GET, uri='coap://localhost/.well-known/core')
    
    #Observation Client
    #request = Message(code=GET, uri='coap://127.0.0.1:14010/htNode/3303/0/5700?gt=23&pmin=7&qos=40')
    #request = Message(code=GET, uri='coap://127.0.0.1:14010/htNode/3303/0/5700')
    request = Message(code=GET, uri='coap://localhost:13928/whoami?gt=32', observe=1)
    request.opt.observe = 0


    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
