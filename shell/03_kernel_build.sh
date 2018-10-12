#!/bin/bash
echo "kernel build shell by labc"
cd ./kernel
pwd
rm -rf Build
cd ./Kernel-4.9.110
export ARCH=arm CROSS_COMPILE=arm-none-eabi-
make O=../Build/Kernel jiaxing_defconfig
make O=../Build/Kernel LOADADDR=0xA0008000 uImage dtbs -j4
