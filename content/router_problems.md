Title: Router Problems
Date: 2014-11-7
Tags: wi-fi

I've spent the last few evenings messing around with my Wi-Fi router. It's an Asus RT-N66U 
Dark Knight and it worked great for a few months but then it all went south on Monday 
night. Basically all of our devices couldn't load web pages, and rebooting the router and
the modem didn't help. The worst was the Roku didn't work so we had to watch basic cable!
There was a minor firmware update available for the router but that didn't change things. On recommendation
from a coworker I tried the [Merlin](http://www.lostrealm.ca/tower/node/79) firmware which
is based on the official Asus firmware with some bug fixes and minor feature updates. One of
the nice features is support for a ssh server. You just need to enable it in the web interface
and then you can login with the same username/password that you use for the web. I've been
poking around and it's pretty interesting. 

It's running Linux kernel 2.6.22:

    :::bash
    admin@RT-N66U-2DE0:/tmp/home/root# uname -a
    Linux RT-N66U-2DE0 2.6.22.19 #1 Sat Sep 20 14:47:02 EDT 2014 mips GNU/Linux
    
We're doing a router project at work with kernel 2.6.35 so it's kind of similar.

    :::bash
    admin@RT-N66U-2DE0:/# mount
    rootfs on / type rootfs (rw)
    /dev/root on / type squashfs (ro)
    proc on /proc type proc (rw)
    tmpfs on /tmp type tmpfs (rw)
    devfs on /dev type tmpfs (rw,noatime)
    sysfs on /sys type sysfs (rw)
    devpts on /dev/pts type devpts (rw)
    usbfs on /proc/bus/usb type usbfs (rw)
    admin@RT-N66U-2DE0:/# ls -l
    drwxrwxr-x    2 admin    root             3 Sep 20 14:11 asus_jffs
    drwxr-xr-x    2 admin    root           550 Sep 20 14:10 bin
    drwxr-xr-x    2 admin    root             3 Sep 20 14:11 cifs1
    drwxr-xr-x    2 admin    root             3 Sep 20 14:11 cifs2
    drwxrwxrwt    4 admin    root          1660 Nov  6 20:55 dev
    lrwxrwxrwx    1 admin    root             7 Sep 20 14:11 etc -> tmp/etc
    lrwxrwxrwx    1 admin    root             8 Sep 20 14:11 home -> tmp/home
    drwxr-xr-x    2 admin    root             3 Sep 20 14:11 jffs
    drwxr-xr-x    3 admin    root           354 Sep 20 14:11 lib
    drwxr-xr-x    2 admin    root             3 Sep 20 14:11 mmc
    lrwxrwxrwx    1 admin    root             7 Sep 20 14:11 mnt -> tmp/mnt
    lrwxrwxrwx    1 admin    root             7 Sep 20 14:11 opt -> tmp/opt
    dr-xr-xr-x   63 admin    root             0 Dec 31  1999 proc
    drwxr-xr-x    5 admin    root           651 Sep 20 14:11 rom
    lrwxrwxrwx    1 admin    root            13 Sep 20 14:11 root -> tmp/home/root
    drwxr-xr-x    2 admin    root          1640 Sep 20 14:11 sbin
    drwxr-xr-x   10 admin    root             0 Dec 31  1999 sys
    drwxr-xr-x    2 admin    root             3 Sep 20 14:11 sysroot
    drwxrwxrwx   10 admin    root           580 Nov  6 21:40 tmp
    drwxr-xr-x    7 admin    root           105 Sep 20 14:11 usr
    lrwxrwxrwx    1 admin    root             7 Sep 20 14:11 var -> tmp/var
    drwxr-xr-x   11 admin    root          5082 Sep 20 14:11 www

The rootfs is a readonly SquashFS, and directories like /etc are symlinked from a tmpfs.

It doesn't have the Wi-Fi tools I'm used to like iwconfig or iw, and I was surprised 
not to see any Wi-Fi interfaces in ifconfig:

    :::bash
    admin@RT-N66U-2DE0:/tmp# ifconfig
    br0        Link encap:Ethernet  HWaddr 40:16:7E:EA:2D:E0  
               inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
               UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
               RX packets:52230608 errors:0 dropped:0 overruns:0 frame:0
               TX packets:433740 errors:0 dropped:0 overruns:0 carrier:0
               collisions:0 txqueuelen:0 
               RX bytes:1594773459 (1.4 GiB)  TX bytes:89779676 (85.6 MiB)
    
    eth0       Link encap:Ethernet  HWaddr 40:16:7E:EA:2D:E0  
               inet addr:XXX.XXX.XXX.XXX  Bcast:XXX.XXX.XXX.XXX  Mask:255.255.240.0
               UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
               RX packets:5405694 errors:0 dropped:0 overruns:0 frame:0
               TX packets:53877525 errors:0 dropped:0 overruns:0 carrier:0
               collisions:0 txqueuelen:1000 
               RX bytes:693615441 (661.4 MiB)  TX bytes:3116562699 (2.9 GiB)
               Interrupt:4 Base address:0x2000 
    
    eth1       Link encap:Ethernet  HWaddr 40:16:7E:EA:2D:E0  
               UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
               RX packets:50065089 errors:0 dropped:0 overruns:0 frame:1378764
               TX packets:36198574 errors:11578317 dropped:0 overruns:0 carrier:0
               collisions:0 txqueuelen:1000 
               RX bytes:2058365479 (1.9 GiB)  TX bytes:604413991 (576.4 MiB)
               Interrupt:3 Base address:0x8000 
    
    eth2       Link encap:Ethernet  HWaddr 40:16:7E:EA:2D:E4  
               UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
               RX packets:1940719 errors:0 dropped:0 overruns:0 frame:82081
               TX packets:53933151 errors:5506 dropped:0 overruns:0 carrier:0
               collisions:0 txqueuelen:1000 
               RX bytes:570566131 (544.1 MiB)  TX bytes:2872841696 (2.6 GiB)
               Interrupt:5 Base address:0x8000 
    
    lo         Link encap:Local Loopback  
               inet addr:127.0.0.1  Mask:255.0.0.0
               UP LOOPBACK RUNNING MULTICAST  MTU:16436  Metric:1
               RX packets:80741 errors:0 dropped:0 overruns:0 frame:0
               TX packets:80741 errors:0 dropped:0 overruns:0 carrier:0
               collisions:0 txqueuelen:0 
               RX bytes:16345659 (15.5 MiB)  TX bytes:16345659 (15.5 MiB)
    
    vlan1      Link encap:Ethernet  HWaddr 40:16:7E:EA:2D:E0  
               UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
               RX packets:13441 errors:0 dropped:0 overruns:0 frame:0
               TX packets:51926724 errors:0 dropped:0 overruns:0 carrier:0
               collisions:0 txqueuelen:0 
               RX bytes:938656 (916.6 KiB)  TX bytes:2512739223 (2.3 GiB)

Turns out eth1 and eth2 are the wireless interfaces according to dmesg:

    :::bash
    eth1: Broadcom BCM4331 802.11 Wireless Controller 6.30.163.2002 (r382208)
    eth2: Broadcom BCM4331 802.11 Wireless Controller 6.30.163.2002 (r382208)

I assume only one of those is actually for the Wi-Fi interface and the other is
connected to a switch feeding the gigabit wired ports. Or it's all internal to the
Broadcom SOC. There must be some sort of control interface to the Wi-Fi interface 
to support functions like scans and AP configuration, but I haven't figured out
how that works yet. 

In between poking around the filesystem I did figure out that only the 2.4GHz 
operation is crap and 5Ghz is working fine. I've tried change channels and forcing
20MHz channels to no avail. It's definitely looking like it is a hardware problem. Google
indicates lot of people have had similar issues and none of the suggested fixes have
worked for me.