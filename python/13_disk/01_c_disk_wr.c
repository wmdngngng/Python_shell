// disk_wr.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <windows.h>
#include <conio.h>
#include <stdio.h>
#include <tchar.h>
#include <winioctl.h>
#include <ntddscsi.h>


int _tmain (int Argc, _TCHAR *argv[])
{
	int i = 0;

	HANDLE hDev;
	hDev=CreateFile("\\\\.\\G:",GENERIC_READ,FILE_SHARE_WRITE,0,OPEN_EXISTING,0,0);
	if (hDev == INVALID_HANDLE_VALUE){
		printf("CreatFile Error\n");
	}

	unsigned char Buffer[512] = {0};
	DWORD dwRet = 0;
	ReadFile(hDev,Buffer,512,&dwRet,0);
	if (dwRet < 0){
		printf("ReadFile Error\n");
	}

	for(int i=0; i< 512; i++){
		printf("%x " ,Buffer[i]);
	}

	CloseHandle(hDev);
	scanf("%d",&i);
	return 1;
}