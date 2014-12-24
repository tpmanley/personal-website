Title: Freedom board and mbed
Date: 2014-12-23
Tags: FRDM-KL25Z, mbed, logic8

Freescale makes an inexpensive development platform for the Kinetis L series 
processors called the Freedom board. I borrowed the 
[FRDM-KL25Z](http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=FRDM-KL25Z)
from a coworker. It has a MKL25Z Cortex-M0+ processor with an RGB LED, a 
capacitive touch slider, serial, GPIOs, etc... 

There are a number of options for develping for the Freedom board, including
the Eclipse-based Kinetis Design Studio and CodeWarrior, but I decided to give
[mbed](https://mbed.org/) a try. Mbed is an operating system for ARM Cortex-M
processors. It has a web-based development environment and compiler which makes
it really easy to try out. 

The mbed environment has a number of sample apps for the KL25Z. The frdm_gpio
app basically just flashes the RGB LED and a toggles a digial output. I added
a SPI master device to the sample app that just wrote 0xA5 in a loop so I could
have something interesting to look at with the Saleae logic analyzer. Here is 
the code:

    #include "mbed.h"

    DigitalOut gpo(D0);
    DigitalOut led(LED_RED);
    SPI device(PTD2, PTD3, PTD1);

    int main()
    {
        device.format(8, 0);
        while (true) {
            gpo = !gpo; // toggle pin
            led = !led; // toggle led
            device.write(0xA5);
            wait(0.2f);
       }
    }  

I attached one of the probes on the Logic8 to pin PTD2 which was configured as
the Master-In Slave-Out (MOSI) PIN on the SPI device. Another probe was attached
to PTD1 which was configured as SCLK. Then I captured a trace while running the 
app and verified the alternating bit pattern of 0xA5 showed up in the capture.

This was all really simple but after spending so much time on management
and business stuff lately it was fun to get my hands dirty. I definitely would
like to learn more about mbed and also try out the Kinetis Design Studio.

