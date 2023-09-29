# DigiFG_RISC

## Description

DigiFG_RISC is a “digital” waveform generated that is to be implemented on RISCduino, a RISC-V based development board.

The firmware loaded in the microcontroller utilizes the USB port as a serial interface and I2C for communication with ****************MCP4725**************** 12-bit Digital-to-Analog Converter

The DigiFG_RISC receives serial input from a PC application (to be developed using python tKinter) through USB that provides it commands about the waveform type and frequency, which transfers all these control to the PC application, which makes the Function Generator compact and portable.

As of now, the Function Generator is able to generate **************************sine, triangular************************** and **************square************** waveforms

## Outputs

Partial outputs were simulated using Arduino UNO on Proteus.

### Sine wave

![image](https://github.com/pyCoder03/DigiFG_RISC/assets/93860462/30ed67ca-6af3-4fe3-88bd-268a041eeb32)


### Triangular wave

![image](https://github.com/pyCoder03/DigiFG_RISC/assets/93860462/3a0fe2da-5711-4792-b27f-31b8960dca12)


### Square wave

![image](https://github.com/pyCoder03/DigiFG_RISC/assets/93860462/0379ac7f-3d63-4fc4-866b-404454e69ba1)

