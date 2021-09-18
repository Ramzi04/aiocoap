#!/usr/bin/env python3

import logging
import asyncio
from random import randint

from aiocoap import *

# </10359/0/50>;rt="ipso.act.lck";if="core.a";ct=40' 
# POST, payload=payload, uri="coap://localhost/resourcedirectory/?ep=sl1&d=bldg1.fl2.off3")

logging.basicConfig(level=logging.DEBUG)

async def main():
    ############ Smart city resources ##########################
    ###################################################
    index = 0 #used in IPSO objects instances
    for indexBuilding in range(1,2):    #1->11
        
            ############ Building resources ###########################
            ###################################################
            for indexFloor in range(1,2):   #1->4
                
                    ############ floor resources #############################
                    ###################################################
                    for indexOffice in range(1,3): #1->11
                        
                            domain = "bldg"+str(indexBuilding)+".fl"+str(indexFloor)+".off"+str(indexOffice)
                    ############ office resources #############################
                    ###################################################
                            # Luminary1 and Luminary1 nodes
                            for indexLum in range(1,3):
                                context = await Context.create_client_context()
                                payload = b'</3392/%s/404/>;rt="ipso.sen.lt";if="core.s";ct=40;qos=%s;lt=%s;sz=%s,</3311/%s/5851>;rt="ipso.lt.dim";if="core.a";ct=40;qos=%s;lt=%s;sz=%s' % (str(index).encode('ascii'),str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'),str(randint(1,100)).encode('ascii'),str(index).encode('ascii'), str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'),str(randint(1,100)).encode('ascii') )
                                request = Message(code=POST, payload=payload, uri="coap://localhost/resourcedirectory/?ep=lm00"+str(indexLum)+"&d="+domain)
                                request.opt.content_format = 40
                                try:
                                    await context.request(request).response
                                except Exception as e:
                                    print(e)
                            
                            # Power Strip
                            context = await Context.create_client_context()
                            payload = b'</3312/0/5850>;rt="ipso.pwr.rel";if="core.a";ct=50;qos=%s;lt=%s;sz=%s,</3312/1/5850>;rt="ipso.pwr.rel";if="core.a";ct=50;qos=%s;lt=%s;sz=%s,</3312/2/5850>;rt="ipso.pwr.rel";if="core.a";ct=50;qos=%s;lt=%s;sz=%s,</3312/3/5850>;rt="ipso.pwr.rel";if="core.a";ct=50;qos=%s;lt=%s;sz=%s' % (str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'),str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'))
                            request = Message(code=POST, payload=payload, uri="coap://localhost/resourcedirectory/?ep=ps001&d="+domain)
                            request.opt.content_format = 40
                            try:
                                await context.request(request).response
                            except Exception as e:
                                print(e)
                            
                            # PIR sensor
                            context = await Context.create_client_context()
                            payload = b'</3302/%s/5500>;rt="ipso.sen.pres";if="core.s";ct=40;qos=%s;lt=%s;sz=%s;obs' % (str(index).encode('ascii'), str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'))
                            request = Message(code=POST, payload=payload, uri="coap://localhost/resourcedirectory/?ep=pir1&d="+domain)
                            request.opt.content_format = 40
                            try:
                                await context.request(request).response
                            except Exception as e:
                                print(e)
                            
                            # HT sensor
                            context = await Context.create_client_context()
                            payload = b'</3303/%s/5700>;rt="ipso.sen.temp";if="core.s";ct=40;qos=%s;lt=%s;sz=%s;obs,</3304/%s/5700>;rt="ipso.sen.hum";if="core.s";ct=40;qos=%s;lt=%s;sz=%s;obs' % (str(index).encode('ascii'),str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'),str(randint(1,100)).encode('ascii') , str(index).encode('ascii'), str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'),str(randint(1,100)).encode('ascii'))
                            request = Message(code=POST, payload=payload, uri="coap://localhost/resourcedirectory/?ep=ht1&d="+domain)
                            request.opt.content_format = 40
                            try:
                                await context.request(request).response
                            except Exception as e:
                                print(e)    
                            
                            # CO2 sensor
                            context = await Context.create_client_context()
                            payload = b'</6047/%s/5700>;rt="ipso.sen.co2";if="core.s";ct=40;qos=%s;lt=%s;sz=%s;obs' % (str(index).encode('ascii'),str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'))
                            request = Message(code=POST, payload=payload, uri="coap://localhost/resourcedirectory/?ep=am1&d="+domain)
                            request.opt.content_format = 40
                            try:
                                await context.request(request).response
                            except Exception as e:
                                print(e)

							# office door smart lock (sl) actuator
                            context = await Context.create_client_context()
                            payload = b'</10359/%s/50>;rt="ipso.act.lck";if="core.a";ct=40;qos=%s;lt=%s;sz=%s,</10359/%s/100>;rt="ipso.act.lck";if="core.a";ct=40;qos=%s;lt=%s;sz=%s' % (str(index).encode('ascii'),str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'),str(randint(1,100)).encode('ascii') ,str(index).encode('ascii'), str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'),str(randint(1,100)).encode('ascii'))
                            request = Message(code=POST, payload=payload, uri="coap://localhost/resourcedirectory/?ep=sl1&d="+domain)
                            request.opt.content_format = 40
                            try:
                                await context.request(request).response
                            except Exception as e:
                                print(e)
								
							# office SMART Thermostat
                            context = await Context.create_client_context()
                            payload = b'</12300/%s/5209>;rt="ipso.act.thrms";if="core.a";ct=40;qos=%s;lt=%s;sz=%s' % (str(index).encode('ascii'),str(randint(1,100)).encode('ascii'), str(1000*randint(1,100)).encode('ascii'), str(randint(1,100)).encode('ascii'))
                            request = Message(code=POST, payload=payload, uri="coap://localhost/resourcedirectory/?ep=th1&d="+domain)
                            request.opt.content_format = 40
                            try:
                                await context.request(request).response
                            except Exception as e:
                                print(e)
                                    
                            index += 1
    
    
    '''
    index = 0
    indexGroup = 0
    payloadCO2 = payloadPIR = payloadHT = payloadLock = payloadTherms = b''
    for indexBuilding in range(1,2):    #1->11
        for indexFloor in range(1,2):   #1->4
            for indexOffice in range(1,3): #1->11
                payloadCO2 += b'</6047/%s/5700>;rt="ipso.sen.co2";if="core.s";ct=40;qos=30;lt=80000;sz=88;obs'  %(str(index).encode('ascii'))
                payloadPIR += b'</3302/%s/5500>;rt="ipso.sen.pres";if="core.s";ct=40;qos=55;lt=85000;sz=15;obs'  %(str(index).encode('ascii'))
                payloadHT += b'</3303/%s/5700>;rt="ipso.sen.temp";if="core.s";ct=40;qos=41;lt=25000;sz=22;obs,</3304/%s/5700>;rt="ipso.sen.hum";if="core.s";ct=40;qos=88;lt=55000;sz=15;obs'  %(str(index).encode('ascii'), str(index).encode('ascii'))
                payloadLock += b'</10359/%s/50>;rt="ipso.act.lck";if="core.a";ct=40;qos=41;lt=12000;sz=23,</10359/%s/100>;rt="ipso.act.lck";if="core.a";ct=40;qos=90;lt=47000;sz=22'  %(str(index).encode('ascii'), str(index).encode('ascii'))
                payloadTherms += b'</12300/%s/5209>;rt="ipso.act.thrms";if="core.a";ct=40;qos=75;lt=99000;sz=17'  %(str(index).encode('ascii'))
                index += 1
                
        # Group co2 sensor for Buidings %i
        context = await Context.create_client_context()
        request = Message(code=POST, payload=payloadCO2, uri="coap://localhost/resourcedirectory/?ep=group%s&gr=co2.bldg%s&d=bldg%s&if=core.gp" %(str(indexGroup),str(indexBuilding),str(indexBuilding))) 
        request.opt.content_format = 40
        try:
            await context.request(request).response
        except Exception as e:
            print(e)
        indexGroup += 1
        
        
        # Group PIR sensor for Buidings %i
        context = await Context.create_client_context()
        request = Message(code=POST, payload=payloadPIR, uri="coap://localhost/resourcedirectory/?ep=group%s&gr=pir.bldg%s&d=bldg%s&if=core.gp" %(str(indexGroup),str(indexBuilding),str(indexBuilding) ) )
        request.opt.content_format = 40
        try:
            await context.request(request).response
        except Exception as e:
            print(e)
        indexGroup += 1
        
        # Group HT sensor for Buidings %i
        context = await Context.create_client_context()
        request = Message(code=POST, payload=payloadHT, uri="coap://localhost/resourcedirectory/?ep=group%s&gr=ht.bldg%s&d=bldg%s&if=core.gp" %(str(indexGroup),str(indexBuilding), str(indexBuilding))) 
        request.opt.content_format = 40
        try:
            await context.request(request).response
        except Exception as e:
            print(e)
        indexGroup += 1
        
        # Group SMART Lock for Buidings %i
        context = await Context.create_client_context()
        request = Message(code=POST, payload=payloadLock, uri="coap://localhost/resourcedirectory/?ep=group%s&gr=sl.bldg%s&d=bldg%s&if=core.gp" %(str(indexGroup),str(indexBuilding),str(indexBuilding) ))
        request.opt.content_format = 40
        try:
            await context.request(request).response
        except Exception as e:
            print(e)
        indexGroup += 1
        
        # Group Thermostat for Buidings %i
        context = await Context.create_client_context()
        request = Message(code=POST, payload=payloadTherms, uri="coap://localhost/resourcedirectory/?ep=group%s&gr=th.bldg%s&d=bldg%s&if=core.gp" %(str(indexGroup),str(indexBuilding),str(indexBuilding) ))
        request.opt.content_format = 40
        try:
            await context.request(request).response
        except Exception as e:
            print(e)
        indexGroup += 1
        
    
    
    

    
    
    
    index = 0
    indexCollection = 0
    sensors_collection = actuators_collection = b''
    for indexBuilding in range(1,3):    #1->11
        for indexFloor in range(1,2):   #1->4
            for indexOffice in range(1,3): #1->11
                sensors_collection += b'</6047/%s/5700>;rt="ipso.sen.co2";if="core.s";ct=40;qos=30;lt=80000;sz=88;obs'  %(str(index).encode('ascii'))
                sensors_collection += b'</3392/%s/404>;rt="ipso.sen.lt";if="core.s";ct=40;qos=30;lt=80000;sz=88;obs'  %(str(index).encode('ascii'))
                sensors_collection += b'</3302/%s/5500>;rt="ipso.sen.pres";if="core.s";ct=40;qos=55;lt=85000;sz=15;obs'  %(str(index).encode('ascii'))
                sensors_collection += b'</3303/%s/5700>;rt="ipso.sen.temp";if="core.s";ct=40;qos=41;lt=25000;sz=22;obs,</3304/%s/5700>;rt="ipso.sen.hum";if="core.s";ct=40;qos=88;lt=55000;sz=15;obs'  %(str(index).encode('ascii'), str(index).encode('ascii'))
                
                actuators_collection += b'</10359/%s/50>;rt="ipso.act.lck";if="core.a";ct=40;qos=41;lt=12000;sz=23,</10359/%s/100>;rt="ipso.act.lck";if="core.a";ct=40;qos=90;lt=47000;sz=22'  %(str(index).encode('ascii'), str(index).encode('ascii'))
                actuators_collection += b'</12300/%s/5209>;rt="ipso.act.thrms";if="core.a";ct=40;qos=75;lt=99000;sz=17'  %(str(index).encode('ascii'))
                actuators_collection += b'</3311/%s/5851>;rt="ipso.lt.dim";if="core.a";ct=40;qos=55;lt=39000;sz=19'  %(str(index).encode('ascii'))
                actuators_collection += b'</3312/0/5850>;rt="ipso.pwr.rel";if="core.a";ct=50;qos=85;lt=31000;sz=11,</3312/1/5850>;rt="ipso.pwr.rel";if="core.a";ct=50;qos=15;lt=81000;sz=44,</3312/2/5850>;rt="ipso.pwr.rel";if="core.a";ct=50;qos=44;lt=74000;sz=15,</3312/3/5850>;rt="ipso.pwr.rel";if="core.a";ct=50;qos=47;lt=88000;sz=17'
                
                index += 1
        
        # Collection of sensors for Buidings %i
        context = await Context.create_client_context()
        request = Message(code=POST, payload=sensors_collection, uri="coap://localhost/resourcedirectory/?ep=col%s&if=core.ll&cn=col.sens.bldg%s" %(str(indexCollection), str(indexBuilding))) 
        request.opt.content_format = 40
        try:
            await context.request(request).response
        except Exception as e:
            print(e)
        indexCollection += 1
        
        # Collection of actuators for Buidings %i
        context = await Context.create_client_context()
        request = Message(code=POST, payload=actuators_collection, uri="coap://localhost/resourcedirectory/?ep=col%s&if=core.ll&cn=col.acts.bldg%s" %(str(indexCollection), str(indexBuilding))) 
        request.opt.content_format = 40
        try:
            await context.request(request).response
        except Exception as e:
            print(e)
        indexCollection += 1
    '''
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
