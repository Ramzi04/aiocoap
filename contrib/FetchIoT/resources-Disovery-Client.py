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
import time
import random
from cbor2 import dumps

from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    """
    protocol = await Context.create_client_context()
    x =  '{"t":"6","q":{"qt":"EXINC","trg":"a","l1":"if=core.a&lt=12000","l2":"sz=40&ct=40&qos=35","tr":"qos&sz&rt","ai":{}}}' 
    payload = bytes(x, encoding='utf-8')
    #json=50,CLF=40,cbor=60,xml=41
    #x = b'A2617461366171A6627174654558494E43637472676161626C317269663D636F72652E61266C743D3132303030626C3272737A3D34302663743D343026716F733D333562747269716F7326737A267274626169A0'
    #cbor_content = dumps(x)
    request = Message(content_format=60,code=FETCH, payload=payload, uri='coap://localhost/resource-lookup/')
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Average Request FETCH size in Bytes: %r'%(  len(request.encode())))  
        
    """
    
    nbr_requests = 30
    
    protocol = await Context.create_client_context()
 
    payload0 =  b'{"t":"6","q":{"qt":"EXINC","trg":"a","l1":"if=core.a&lt=12000","l2":"sz=40&ct=40&qos=35","tr":"qos&sz&rt"}}' 
    requestGET0 = Message(code=GET, uri='coap://localhost/resource-lookup/?if=core.a&lt=12000') 
    
    payload1 =  b'{"t":"6","q":{"qt":"EXINC","trg":"r","l1":["ipso.act","ipso.sen"],"l2":["ipso.act.lck","ipso.sen.temp"],"tr":"qos&sz&rt"}}' 
    requestGET1 = Message(code=GET, uri='coap://localhost/resource-lookup/?rt=ipso.act*&rt=ipso.sen*')
    
    payload2 =  b'{"t":"6","q":{"qt":"EXINC","trg":"d","l1":["bldg1.fl1","bldg1.fl2"],"l2":["bldg1.fl1.off1"],"tr":"qos&sz"}}'
    requestGET2 = Message(code=GET, uri='coap://localhost/resource-lookup/?d=bldg1.fl1*&d=bldg1.fl2*')

    payload3 =  b'{"t":"12","q1":"rt=ipso.lt.on","op":"OR","q2":"rt=ipso.sen.temp"}' 
    requestGET3 = Message(code=GET, uri='coap://localhost/resource-lookup/?rt=ipso.lt.on&rt=ipso.sen.temp')

    payload4 =  b'{"t":"6","q":{"qt":"INC","trg":"r","l1":["ipso.sen.pres","ipso.act.lck"],"tr":"qos&rt"}}'
    requestGET4 = Message(code=GET, uri='coap://localhost/resource-lookup/?rt=ipso.sen.pres&rt=ipso.act.lck')
    
    payload5 =  b'{"t":"6","q":{"qt":"EX","trg":"d","l1":["bldg1.fl1"],"tr":"qos"}}' 
    requestGET5 = Message(code=GET, uri='coap://localhost/resource-lookup/?d=bldg1*')
    
    payload6 =  b'{"t":"6","q":{"qt":"EX","trg":"a","l1":"if=core.a&ct=50","tr":"qos"}}' 
    requestGET6 = Message(code=GET, uri='coap://localhost/resource-lookup/?if=core.s&ct=4*')
    
     
    paylaods = [payload0, payload1, payload2, payload3, payload4, payload5, payload6]
    get_requests = [requestGET0, requestGET1,  requestGET2, requestGET3,  requestGET4,  requestGET5,  requestGET6]
    
    discovery_time_get = discovery_time_fetch = response_size_get = response_size_fetch = request_size_get = request_size_fetch =  0
    
    
    for index in range(nbr_requests):
        index_request = random.randint(0, 6)
        try:
            start_time = time.time()
            responseGET = await protocol.request(get_requests[index_request]).response
            discovery_time_get += 1000*(time.time() - start_time)
        except Exception as e:
            print('Failed to fetch resource:')
            print(e)
        else:
            request_size_get += len(get_requests[index_request].encode()) 
            response_size_get += len(responseGET.payload)
         
        #requestFetch = Message(content_format=50,code=FETCH, payload=dumps(paylaods[index_request]), uri='coap://localhost/resource-lookup/')
        requestFetch = Message(content_format=41,code=FETCH, payload=paylaods[index_request], uri='coap://localhost/resource-lookup/')
        try:
            start_time = time.time()
            responseFETCH = await protocol.request(requestFetch).response
            discovery_time_fetch += 1000*(time.time() - start_time)
        except Exception as e:
            print('Failed to fetch resource:')
            print(e)
        else:
            request_size_fetch += len(requestFetch.encode())
            response_size_fetch += len(responseFETCH.payload)

    print("\n")
    
    print("---  Average GET time in m-seconds: %.2f ---" % (discovery_time_get/nbr_requests)  )
    print("---  Average FETCH time in m-seconds: %.2f ---" % (discovery_time_fetch/nbr_requests)  )
    
    print("\n")
    
    print('Average Request GET size in Bytes: %.2f'%( request_size_get/nbr_requests ))      #<class 'aiocoap.message.Message'>
    print('Average Request FETCH size in Bytes: %r'%( request_size_fetch/nbr_requests ))      #<class 'aiocoap.message.Message'>
    
    print("\n")
    
    print('Average Response GET size in Bytes: %.2f'%( response_size_get/nbr_requests )) #<class 'bytes'>
    print('Average Response FETCH size in Bytes: %.2f'%(    response_size_fetch/nbr_requests   )) #<class 'bytes'>
    


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
