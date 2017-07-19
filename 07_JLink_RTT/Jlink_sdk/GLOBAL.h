/*********************************************************************
*                SEGGER MICROCONTROLLER SYSTEME GmbH                 *
*        Solutions for real time microcontroller applications        *
**********************************************************************
*                                                                    *
*           (C) 2003    SEGGER Microcontroller Systeme GmbH          *
*                                                                    *
*        Internet: www.segger.com    Support:  support@segger.com    *
*                                                                    *
**********************************************************************
----------------------------------------------------------------------
File    : GLOBAL.h
Purpose : Global types etc.
---------------------------END-OF-HEADER------------------------------
*/

#ifndef GLOBAL_H            // Guard against multiple inclusion
#define GLOBAL_H

#include <memory.h>

#if defined(__cplusplus)    // Allow usage of this module from C++ files (disable name mangling)
  extern "C" {
#endif

/*********************************************************************
*
*       Macros
*
**********************************************************************
*/

#define COUNTOF(a)    (sizeof(a)/sizeof(a[0]))
#define ZEROFILL(Obj) memset(Obj, 0, sizeof(Obj))

#define U8    unsigned char
#define U16   unsigned short
#define U32   unsigned int
#define U64   unsigned __int64
#define I8    signed char
#define I16   signed short
#define I32   signed int
#define I64   signed __int64

#define TRUE  1
#define FALSE 0

#if defined(__cplusplus)    // Allow usage of this module from C++ files (disable name mangling)
  }
#endif

#endif                      // Avoid multiple inclusion

/*************************** End of file ****************************/
