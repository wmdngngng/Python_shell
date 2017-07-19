/*********************************************************************
*              SEGGER MICROCONTROLLER SYSTEME GmbH                   *
*        Solutions for real time microcontroller applications        *
**********************************************************************
*                                                                    *
*        (c) 1996-2004 SEGGER Microcontroller Systeme GmbH           *
*                                                                    *
* Internet: www.segger.com Support: support@segger.com               *
*                                                                    *
**********************************************************************
----------------------------------------------------------------------
File    : ARM.h
Purpose : Interface of the J-Link ARM module.
---------------------------END-OF-HEADER------------------------------


*/


#ifndef ARM_H           /* Guard against multiple inclusion */
#define ARM_H

#include "Global.h"     /* Required for data types: U8, U16, U32 */
#include "jtag.h"

#if defined(__cplusplus)
  extern "C" {          /* Make sure we have C-declarations in C++ programs */
#endif


/*********************************************************************
*
*       Enums required for API
*/
enum ARM_DEVICE {
  ARM_DEVICE_UNKNOWN,
  ARM_DEVICE_ARM7,
  ARM_DEVICE_ARM9
};

enum {
   ARM_NO_DELAY
  ,ARM_WRITE_DELAYED
};

enum ARM_ENDIAN {
  ARM_ENDIAN_LITTLE, ARM_ENDIAN_BIG
};

/*********************************************************************
*
*       ARM core registers
*/
typedef enum {
  ARM_REG_R0,
  ARM_REG_R1,
  ARM_REG_R2,
  ARM_REG_R3,
  ARM_REG_R4,
  ARM_REG_R5,
  ARM_REG_R6,
  ARM_REG_R7,
  ARM_REG_CPSR,
  ARM_REG_R15,
  ARM_REG_R8_USR,   ARM_REG_R9_USR,  ARM_REG_R10_USR, ARM_REG_R11_USR,
                    ARM_REG_R12_USR, ARM_REG_R13_USR, ARM_REG_R14_USR,
  ARM_REG_SPSR_FIQ, ARM_REG_R8_FIQ,  ARM_REG_R9_FIQ,  ARM_REG_R10_FIQ,
                    ARM_REG_R11_FIQ, ARM_REG_R12_FIQ, ARM_REG_R13_FIQ, ARM_REG_R14_FIQ,
  ARM_REG_SPSR_SVC, ARM_REG_R13_SVC, ARM_REG_R14_SVC,
  ARM_REG_SPSR_ABT, ARM_REG_R13_ABT, ARM_REG_R14_ABT,
  ARM_REG_SPSR_IRQ, ARM_REG_R13_IRQ, ARM_REG_R14_IRQ,
  ARM_REG_SPSR_UND, ARM_REG_R13_UND, ARM_REG_R14_UND,
  ARM_REG_SPSR_SYS, ARM_REG_R13_SYS, ARM_REG_R14_SYS,
  ARM_NUM_REGS
} ARM_REG;


/*********************************************************************
*
*       ICEBreaker Module registers
*/
#define ARM_ICE_DBG_CTRL		      0x00
#define ARM_ICE_DBG_STS			      0x01 
#define ARM_ICE_VECTOR_CATCH_CTRL	0x02     // ARM 9 only
#define ARM_ICE_DBG_COM_CTRL	    0x04
#define ARM_ICE_DBG_COM_DATA	    0x05

#define ARM_ICE_DCC_STAT 0x04       // Debug comms status / control
#define ARM_ICE_DCC_DATA 0x05       // Debug comms data
#define ARM_ICE_WP0_AV	 0x08
#define ARM_ICE_WP0_AM	 0x09
#define ARM_ICE_WP0_DV	 0x0A
#define ARM_ICE_WP0_DM	 0x0B
#define ARM_ICE_WP0_CV	 0x0C
#define ARM_ICE_WP0_CM	 0x0D
#define ARM_ICE_WP1_AV	 0x10
#define ARM_ICE_WP1_AM	 0x11
#define ARM_ICE_WP1_DV	 0x12
#define ARM_ICE_WP1_DM	 0x13
#define ARM_ICE_WP1_CV	 0x14
#define ARM_ICE_WP1_CM	 0x15


/*********************************************************************
*
*       API functions
*/
void         JLINKARM_Close(void);
void         JLINKARM_ClrBP(unsigned BPIndex);
void         JLINKARM_ClrError(void);
void         JLINKARM_EnableLog2File(void);
const char * JLINKARM_GetCompileDateTime(void);
U16          JLINKARM_GetEmbeddedFWVersion(void);
void         JLINKARM_GetHWStatus(JTAG_HW_STATUS * pStat);
U32          JLINKARM_GetId(void);
void         JLINKARM_GetIdData(JTAG_ID_DATA * pIdData);
U16          JLINKARM_GetSelDevice(void);
int          JLINKARM_GetVoltage(void);
U16          JLINKARM_GetSpeed(void);
void         JLINKARM_Go(void);
void         JLINKARM_GoIntDis(void);
char         JLINKARM_Halt(void);
char         JLINKARM_HaltNoSave(void);
char         JLINKARM_IsConnected(void);
char         JLINKARM_IsHalted(void);
const char * JLINKARM_Open(void);
int          JLINKARM_ReadDCC(U32 * pData, U32 NumItems, int TimeOut);
void         JLINKARM_ReadDCCFast(U32 * pData, U32 NumItems);
U32          JLINKARM_ReadICEReg(int RegIndex);
int          JLINKARM_ReadMem (U32 addr, U32 count, void * p);
void         JLINKARM_ReadMemU8 (U32 Addr, U32 NumItems, U8 * pData, U8* pStatus);
void         JLINKARM_ReadMemU16(U32 Addr, U32 NumItems, U16* pData, U8* pStatus);
void         JLINKARM_ReadMemU32(U32 Addr, U32 NumItems, U32* pData, U8* pStatus);
U32          JLINKARM_ReadReg (ARM_REG RegIndex);
void         JLINKARM_Reset(void);
void         JLINKARM_ResetPullsTRST (U8 OnOff);
void         JLINKARM_ResetPullsRESET(U8 OnOff);
void         JLINKARM_SelDevice(U16 DeviceIndex);
void         JLINKARM_SetBP(unsigned BPIndex, U32 Addr);
int          JLINKARM_SetEndian(int v);
int          JLINKARM_SetInitRegsOnReset(int v);
void         JLINKARM_SetMaxSpeed(void);
void         JLINKARM_SetResetDelay(int ms);
int          JLINKARM_SetResetPara(int Value);
void         JLINKARM_SetSpeed(int Speed);
char         JLINKARM_Step(void);
int          JLINKARM_Test(void);
U16          JLINKARM_UpdateFirmware(void);
U32          JLINKARM_UpdateFirmwareIfNewer(void);
int          JLINKARM_WaitDCCRead(int TimeOut);
int          JLINKARM_WriteDCC(const U32 * pData, U32 NumItems, int TimeOut);
void         JLINKARM_WriteDCCFast(const U32 * pData, U32 NumItems);
void         JLINKARM_WriteICEReg(int RegIndex, U32 Value, int AllowDelay);
char         JLINKARM_WriteReg(ARM_REG RegIndex, U32 Data);
void         JLINKARM_WriteMem(U32 addr, U32 count, const void * p);
void         JLINKARM_WriteMemDelayed(U32 Addr, U32 Count, const void * p);
void         JLINKARM_WriteU8 (U32 addr, U8 Data);
void         JLINKARM_WriteU16(U32 addr, U16 Data);
void         JLINKARM_WriteU32(U32 addr, U32 Data);

void          JLINKARM_EnableLogCom(void (*DebugFunc)(const char *));

/*********************************************************************
*
*       external functions
*
* These functions need to be provided by the application.
* Dummys will do for a start (or printf or MessageBox)
*/
void         ARM_X_ErrorOut(const char * s);
void         ARM_X_Log     (const char * s);
void         ARM_X_Log2File(const char * s);
void         ARM_X_Warn    (const char * s);
int          ARM_X_GetTickCount(void);


#if defined(__cplusplus)
}     /* Make sure we have C-declarations in C++ programs */
#endif

#endif    /* Guard against multiple inclusion */

/*************************** end of file ****************************/

