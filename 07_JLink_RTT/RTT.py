import ctypes, struct
#import numpy as np

class RttBuf(object):
    def __init__(self, arr):
        self.sName,  self.pBuffer,  self.SizeOfBuffer,  self.WrOff,  self.RdOff,  self.Flags = arr

class RttCB(object):
    def __init__(self, buf):
        self.acID, self.MaxNumUpBuf,  self.MaxNumDownBuf  = struct.unpack("16sii", buf.raw[:24])
        print("len:", len(buf.raw[24:(48+0*24)]))
        for i in range(0, self.MaxNumUpBuf):
            print("i", i)
            self.aUp = RttBuf(struct.unpack("6L", buf.raw[(24+24*i):(48+24*i)]))
        
        aDown_start = 48+i*24
        for i in range(0, self.MaxNumDownBuf):
            self.aDown = RttBuf(struct.unpack("6L", buf.raw[(aDown_start + 24*i): (aDown_start+24+24*i)]))
            
        
class RTT(object):
    "RTT api"
    def __init__(self, parent=None):
        print("hello")
        
    def upBuff0Empty(self, rtt_addr, len):
        buf = ctypes.create_string_buffer(len)
        self.jlink.JLINKARM_ReadMem(rtt_addr, len, buf)
        rtt_cb = RttCB(buf)
        print(rtt_cb.aUp[0].sName)
        
        upBuffEnd = 24+24*1
        downBuffStart = 24+24*MaxNumUpBuf
        downBuffEnd = downBuffStart+24
        upBuffs0 = struct.unpack("PPiiii", buf.raw[24:upBuffEnd])
        downBuffs0 = struct.unpack("PPiiii", buf.raw[downBuffStart:downBuffEnd])
        self.upBuff0 = RttBuf(upBuffs0)
        self.downBuff0 = RttBuf(downBuffs0)
        print("sName:%x"%(self.upBuff0.sName))
        print("pBuffer:%x"%(self.upBuff0.pBuffer))
        print("SizeOfBuffer:%d"%(self.upBuff0.SizeOfBuffer))
        print("WrOff:%d"%(self.upBuff0.WrOff))
        print("RdOff:%d"%(self.upBuff0.RdOff))
        print("Flags:%d"%(self.upBuff0.Flags))
        return (self.upBuff0.RdOff == self.upBuff0.WrOff)
