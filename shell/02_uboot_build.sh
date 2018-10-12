#!/bin/bash
echo "uboot shell by labc"
cd ./uboot-from-timesilicon/
pwd
rm -rf Build
cd ./U-Boot
export ARCH=arm CROSS_COMPILE=arm-none-eabi-
make mrproper
make O=../Build/U-Boot/ nextvpu_jiaxing_evb_defconfig
make O=../Build/U-Boot/ -j4 > ../Build/U-Boot/build.log
cd ../buildscripts
./buildall.sh ./uboot.img
#ls -al
cp ./uboot.img /usr/tftp/labc/
ls -al /usr/tftp/labc
