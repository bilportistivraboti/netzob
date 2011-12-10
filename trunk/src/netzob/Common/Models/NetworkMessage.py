# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|         01001110 01100101 01110100 01111010 01101111 01100010             | 
#+---------------------------------------------------------------------------+
#| NETwork protocol modeliZatiOn By reverse engineering                      |
#| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#| @license      : GNU GPL v3                                                |
#| @copyright    : Georges Bossert and Frederic Guihery                      |
#| @url          : http://code.google.com/p/netzob/                          |
#| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#| @author       : {gbt,fgy}@amossys.fr                                      |
#| @organization : Amossys, http://www.amossys.fr                            |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+ 
#| Standard library imports
#+---------------------------------------------------------------------------+
import logging

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+
from netzob.Common.Models.AbstractMessage import AbstractMessage
from netzob.Common.Models.Factories.NetworkMessageFactory import NetworkMessageFactory

#+---------------------------------------------------------------------------+
#| NetworkMessage :
#|     Definition of a network message
#| @author     : {gbt,fgy}@amossys.fr
#| @version    : 0.2
#+---------------------------------------------------------------------------+
class NetworkMessage(AbstractMessage):
    def __init__(self, id, timestamp, data, ip_source, ip_destination, protocol, l4_source_port, l4_destination_port):
        AbstractMessage.__init__(self, id, timestamp, data, "Network")
        self.ip_source = ip_source
        self.ip_destination = ip_destination
        self.protocol = protocol
        self.l4_source_port = l4_source_port
        self.l4_destination_port = l4_destination_port
        # create logger with the given configuration
        self.log = logging.getLogger('netzob.Common.Models.NetworkMessage.py')
    
    #+-----------------------------------------------------------------------+
    #| getFactory
    #| @return the associated factory
    #+-----------------------------------------------------------------------+
    def getFactory(self):
        return NetworkMessageFactory
    
    #+-----------------------------------------------------------------------+
    #| getProperties
    #|     Computes and returns the properties of the current message
    #| @return an array with all the properties [[key,val],...]
    #+-----------------------------------------------------------------------+
    def getProperties(self):
        properties = []        
        properties.append(['ID', str(self.getID())])
        properties.append(['Type', self.getType()])
        properties.append(['Timestamp', self.getTimestamp()])
        properties.append(['Protocol', self.getProtocol()])
        properties.append(['IP source', self.getIPSource()])
        properties.append(['IP target', self.getIPDestination()])
        properties.append(['Source port', self.getL4SourcePort()])
        properties.append(['Target port', self.getL4DestinationPort()])
        properties.append(['Data', self.getStringData()])
        
        return properties    
        
    #+---------------------------------------------- 
    #| GETTERS : 
    #+----------------------------------------------
    def getProtocol(self):
        return self.protocol
    def getIPSource(self):
        return self.ip_source
    def getIPDestination(self):
        return self.ip_destination
    def getL4SourcePort(self):
        return self.l4_source_port
    def getL4DestinationPort(self):
        return self.l4_destination_port
    def getTimestamp(self):
        return self.timestamp
       
    #+---------------------------------------------- 
    #| SETTERS : 
    #+----------------------------------------------
    def setProtocol(self, protocol):
        self.protocol = protocol
    def setIPSource(self, ipSource):
        self.ip_source = ipSource
    def setIPDestination(self, ipDestination):
        self.ip_destination = ipDestination
    def setL4SourcePort(self, l4sourcePort):
        try :
            self.l4_source_port = int(l4sourcePort)
        except :
            self.log.warning("Impossible to set the given L4 source port since its not an int ! " + l4sourcePort)
            self.l4_source_port = -1
            
    def setL4DestinationPort(self, l4targetPort):
        try :
            self.l4_destination_port = int(l4targetPort)
        except :
            self.log.warning("Impossible to set the given L4 target port since its not an int !")
            self.l4_destination_port = -1
        
    def setTimestamp(self, timestamp):
        self.timestamp = timestamp
  
