#!/bin/bash
echo "kernel build shell by labc"
cd ./kernel
pwd
rm -rf Build
cd ./Kernel-4.9.110
export ARCH=arm CROSS_COMPILE=arm-none-eabi-
make O=../Build/Kernel jiaxing_defconfig
make O=../Build/Kernel LOADADDR=0xB8000000 uImage dtbs -j4
cp ../Build/Kernel/arch/arm/boot/uImage /usr/tftp/labc/
cp ../Build/Kernel/arch/arm/boot/dts/nextvpu_jiaxing_evb.dtb /usr/tftp/labc/
ls -l /usr/tftp/labc/
