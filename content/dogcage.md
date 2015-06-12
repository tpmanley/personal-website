Title: Open Sesame 
Date: 2015-6-11
Tags: IoT, XBee, Kicad, Sketchup, Arduino

I have been busy over the last few months working on a Wi-Fi controlled kennel door opener for
my dog. Her kennel is the basement where it is cool and quiet, and it would be convenient to open
the door without having to walk downstairs.

The brains is a [Teensy LC](https://www.pjrc.com/teensy/teensyLC.html) that gets signaled
to open the door over Wi-Fi and opens the door using a servo. After breadboarding up a prototype,
I designed the PCB in [Kicad](http://www.kicad-pcb.org/), used [OSH Park](https://oshpark.com/)
to fab it, and designed the servo mount and arm in [Sketchup](http://www.sketchup.com/) which
my coworker 3D printed for me.

I'm still assembling the boards and working out what I hope are the last few bugs. I'll post
more details when it is complete. In the meantime you can see the SW, HW and mechanical design
files on [Github](https://github.com/tpmanley/dogcage).

