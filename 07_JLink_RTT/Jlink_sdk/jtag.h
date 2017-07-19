/*********************************************************************
*              SEGGER MICROCONTROLLER SYSTEME GmbH                   *
*        Solutions for real time microcontroller applications        *
**********************************************************************
*                                                                    *
*        (c) 1996-2003 SEGGER Microcontroller Systeme GmbH           *
*                                                                    *
* Internet: www.segger.com Support: support@segger.com               *
*                                                                    *
**********************************************************************
----------------------------------------------------------------------
File    : JTAG.h
Purpose : JTAG functions
---------------------------END-OF-HEADER------------------------------
*/


#ifndef JTAG_H
#define JTAG_H

#include "Global.h"

#define JTAG_MAX_DEVICE  3

#define JTAG_CMD_SCAN_N  0x02   // 0010b
#define JTAG_CMD_RESTART 0x04   // 0100b
#define JTAG_CMD_INTEST  0x0C   // 1100b
#define JTAG_CMD_IDCODE  0x0E   // 1110b
#define JTAG_CMD_BYPASS  0x0F   // 1111b


/*********************************************************************
*
*       Data structures
*
**********************************************************************
*/
/*********************************************************************
*
*       ARM_HW_STATUS
*/
typedef struct {
  U16 VTarget;           // Target supply voltage
  U8  tck;               // Measured state of TCK pin:  0 or 1
  U8  tdi;               // Measured state of TDI pin:  0 or 1
  U8  tdo;               // Measured state of TDO pin:  0 or 1
  U8  tms;               // Measured state of TMS pin:  0 or 1
  U8  tres;              // Measured state of TRES pin: 0 or 1
  U8  trst;              // Measured state of TRST pin: 0 or 1 or 255 (unknown)
} JTAG_HW_STATUS;

typedef struct {
  U16 Version;
  U16 JTAG_BufferSize;
} JTAG_FW_INFO;

typedef struct {
  int NumDevices;                 // Number of devices in this scan chain
  U16 ScanLen;                    // Total Number of bits in all scan chain select register
  U32 aId      [JTAG_MAX_DEVICE];
  U8  aScanLen [JTAG_MAX_DEVICE]; // Number of bits in individual scan chain select registers
  U8  aIrRead  [JTAG_MAX_DEVICE]; // Data read back from instruction register
  U8  aScanRead[JTAG_MAX_DEVICE]; // Data read back from scan chain select register
} JTAG_ID_DATA;

void         JTAG_ClearErrorState(void);
void         JTAG_CheckCmd(int BitPos);
void         JTAG_Close(void);
void         JTAG_GetFirmwareInfo(JTAG_FW_INFO * pFWInfo);
void         JTAG_GetFirmwareString(char * s, int BufferSize);
void         JTAG_GetHWStatus(JTAG_HW_STATUS * pStat);
U32          JTAG_GetId(void);
void         JTAG_GetIdData(JTAG_ID_DATA * pIdData);
int          JTAG_GetNumReturns(void);
int          JTAG_GetNumBitsInPipe(void);
int          JTAG_GetScanLen(void);
U32          JTAG_GetU32  (int BitOff);
int          JTAG_GetVoltage(void);
void         JTAG_GoToResetState(void);
const char * JTAG_Open(void);
void         JTAG_ResetTRST(void);
void         JTAG_ResetTarget(void);
void         JTAG_SetIdData(const JTAG_ID_DATA * pIdData);
void         JTAG_StoreCmd(U8 Cmd);
int          JTAG_StoreData(const U8 * pTDI, int NumBits);
void         JTAG_StoreBits(U32 TMS, U32 TDI, int NumBits);
int          JTAG_GetNumBitsInOutBuffer(void);
void         JTAG_WriteBytes(void);
void         JTAG_WriteBytesNoFlush(void);
char         JTAG_UpdateFirmware(U8* pFirmware, int NumBytes, U16 * pCRC);
char         JTAG_HasError(void);


U8    JTAG_HW_Clock (void);
void  JTAG_HW_ClrTMS(void);
void  JTAG_HW_SetTMS(void);
void  JTAG_HW_ClrTDI(void);
void  JTAG_HW_SetTDI(void);
void  JTAG_HW_ClrReset(void);
void  JTAG_HW_ReleaseResetStop  (int NumReps);
void  JTAG_HW_ReleaseResetStopEx(int NumReps, U16 CriteriaBytePos, U16 CriteriaMask, U16 CriteriaData);
void  JTAG_HW_SetReset(void);
void  JTAG_SetSpeed(U16 Speed);
U16   JTAG_GetSpeed(void);
void  JTAG_SelDevice(U16 DeviceIndex);

void         JTAG_X_ErrorOut(const char * s);
void         JTAG_X_Sleep(int ms);


#endif    /* Guard against multiple inclusion */

