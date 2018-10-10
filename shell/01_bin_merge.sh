#!/bin/bash

bin_uboot=uboot_evb.img
bin_env=env.bin
bin_kernel=uImage
bin_dtb=nextvpu_jiaxing_evb.dtb
bin_DSP0=DSP_v11.bin
bin_DSP1=DSP_v11.bin
bin_DSP2=DSP_v11.bin
bin_DSP3=DSP_v11.bin
bin_fs_ext4=fs_ext4.img
bin_rootfs=rootfs.img
bin_img=jiaxing_evb.img

addr_uboot=0
addr_env=2816                       #0xB00@1.375M
addr_kernel=4096                    #0x1000@2M
addr_dtb=12288                      #0x3000@6M 
addr_DSP0=16384                     #0x4000@8M
addr_DSP1=20480                     #0x5000@10M  
addr_DSP2=24576                     #0x6000@12M  
addr_DSP3=28672                     #0x7000@14M  
addr_fs_ext4=40960                  #0xA000@20M 
addr_rootfs=43008                   #0xA800@21M  

#if [ "$(id -u)" != "0" ]; then
#    echo "Script must be run as root!"
#    exit 0
#fi

#./mkenvimage -s 32768 -o ${bin_env} env.txt
if [ ! -e ${bin_uboot} ]; then
    echo "${bin_uboot} is not exist!"
    exit 0
fi

if [ ! -e ${bin_env} ]; then
    echo "${bin_env} is not exist!"
    exit 0
fi

if [ ! -e ${bin_kernel} ]; then
    echo "${bin_kernel} is not exist!"
    exit 0
fi

if [ ! -e ${bin_dtb} ]; then
    echo "${bin_dtb} is not exist!"
    exit 0
fi

if [ ! -e ${bin_DSP0} ]; then
    echo "${bin_DSP0} is not exist!"
    exit 0
fi

if [ ! -e ${bin_DSP1} ]; then
    echo "${bin_DSP1} is not exist!"
    exit 0
fi

if [ ! -e ${bin_DSP2} ]; then
    echo "${bin_DSP2} is not exist!"
    exit 0
fi

if [ ! -e ${bin_DSP3} ]; then
    echo "${bin_DSP3} is not exist!"
    exit 0
fi

if [ ! -e ${bin_rootfs} ]; then
    echo "${bin_rootfs} is not exist!"
    exit 0
fi

if [ ! -e ${bin_fs_ext4} ]; then
    echo "${bin_fs_ext4} is not exist!"
    exit 0
fi

echo "Create ${bin_img}!"
dd if=/dev/zero bs=1M count=512 of=${bin_img}
echo "Add ${bin_uboot} to ${addr_uboot}!"
dd if=${bin_uboot} of=${bin_img} bs=512 seek=${addr_uboot}
echo "Add ${bin_env} to ${addr_env}!"
dd if=${bin_env} of=${bin_img} bs=512 seek=${addr_env}
echo "Add ${bin_kernel} to ${addr_kernel}!"
dd if=${bin_kernel} of=${bin_img} bs=512 seek=${addr_kernel}
echo "Add ${bin_dtb} to ${addr_dtb}!"
dd if=${bin_dtb} of=${bin_img} bs=512 seek=${addr_dtb}
echo "Add ${bin_DSP0} to ${addr_DSP0}!"
dd if=${bin_DSP0} of=${bin_img} bs=512 seek=${addr_DSP0}
echo "Add ${bin_DSP1} to ${addr_DSP1}!"
dd if=${bin_DSP1} of=${bin_img} bs=512 seek=${addr_DSP1}
echo "Add ${bin_DSP2} to ${addr_DSP2}!"
dd if=${bin_DSP2} of=${bin_img} bs=512 seek=${addr_DSP2}
echo "Add ${bin_DSP3} to ${addr_DSP3}!"
dd if=${bin_DSP3} of=${bin_img} bs=512 seek=${addr_DSP3}
echo "Add ${bin_fs_ext4} to ${addr_fs_ext4}!"
dd if=${bin_fs_ext4} of=${bin_img} bs=512 seek=${addr_fs_ext4}
echo "Add ${bin_rootfs} to ${addr_rootfs}!"
dd if=${bin_rootfs} of=${bin_img} bs=512 seek=${addr_rootfs}
sync
