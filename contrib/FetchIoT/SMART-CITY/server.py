#!/usr/bin/env python3


"""This represents a server of each office which host the sesnors/actuators resources"""

import logging
import asyncio

import aiocoap

from lightManagerNode import LightSensorResource
from motionSensorNode import PIRSensorResource
from smokeDetectorNode import CO2SensorResource
from htNode import TemperatureSensorResource
from psNode import PowerStripResource
from doorLockNode import SMARTLockResource
from thermostatNode import ThermostatResource


# logging setup
logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

def main():
    
    #Port is defined as : 1*DeviceType*indexBuilding*indexFloor*indexOffice
    for indexBuilding in range(0,1):
        ############ Building resources ###########################
        for indexFloor in range(1,4):
                ############ floor resources #############################
                for indexOffice in range(0, 1):
                    """
                    #LightManagerNode
                    lightManagerNode = LightSensorResource.createNode()
                    NodePort1 = int("11"+str(indexBuilding)+str(indexFloor)+str(indexOffice))   
                    asyncio.Task(aiocoap.Context.create_server_context(lightManagerNode, ("localhost", NodePort1)))  
                    
                    #PIRSensorNode
                    pIRSensorNode = PIRSensorResource.createNode()
                    NodePort2 = int("12"+str(indexBuilding)+str(indexFloor)+str(indexOffice))   
                    asyncio.Task(aiocoap.Context.create_server_context(pIRSensorNode, ("localhost", NodePort2)))
                    
                    #CO2SensorNode
                    cO2SensorNode = CO2SensorResource.createNode()
                    NodePort3 = int("13"+str(indexBuilding)+str(indexFloor)+str(indexOffice))   
                    asyncio.Task(aiocoap.Context.create_server_context(cO2SensorNode, ("localhost", NodePort3)))  
                    """
                    #HTSensorNode
                    hTSensorNode = TemperatureSensorResource.createNode()
                    NodePort4 = int("14"+str(indexBuilding)+str(indexFloor)+str(indexOffice))   
                    asyncio.Task(aiocoap.Context.create_server_context(hTSensorNode, ("localhost", NodePort4)))  
                    """
                    #PowerStripNode
                    powerStripNode = PowerStripResource.createNode()
                    NodePort5 = int("15"+str(indexBuilding)+str(indexFloor)+str(indexOffice))   
                    asyncio.Task(aiocoap.Context.create_server_context(powerStripNode, ("localhost", NodePort5)))  
                    
                    #SMARTLockNode
                    sMARTLockNode = SMARTLockResource.createNode()
                    NodePort6 = int("16"+str(indexBuilding)+str(indexFloor)+str(indexOffice))   
                    asyncio.Task(aiocoap.Context.create_server_context(sMARTLockNode, ("localhost", NodePort6)))  
                    
                    
                    #ThermostatNode
                    thermostatNode = ThermostatResource.createNode()
                    NodePort7 = int("17"+str(indexBuilding)+str(indexFloor)+str(indexOffice))   
                    asyncio.Task(aiocoap.Context.create_server_context(thermostatNode, ("localhost", NodePort7)))  
                    """
                    
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
