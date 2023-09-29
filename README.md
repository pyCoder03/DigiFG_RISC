## Description

DigiFG_RISC is a “digital” waveform generated that is to be implemented on RISCduino, a RISC-V based development board.

The firmware loaded in the microcontroller utilizes the USB port as a serial interface and I2C for communication with ****************MCP4725**************** 12-bit Digital-to-Analog Converter

The DigiFG_RISC receives serial input from a PC application (to be developed using python tKinter) through USB that provides it commands about the waveform type and frequency, which transfers all these control to the PC application, which makes the Function Generator compact and portable.

As of now, the Function Generator is able to generate **************************sine, triangular************************** and **************square************** waveforms

## Outputs

Partial outputs were simulated using Arduino UNO on Proteus

### Sine wave

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5b454901-597f-4fc7-ad88-5cdaccba61fa/f15a9326-1c77-4ca2-8786-762ccc209c0f/Untitled.png)

### Triangular wave

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5b454901-597f-4fc7-ad88-5cdaccba61fa/6d078fc1-74d4-4754-9998-573c9d58fbf5/Untitled.png)

### Square wave

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5b454901-597f-4fc7-ad88-5cdaccba61fa/fc6dd495-267c-4d47-8e80-1ecbe588ad9e/Untitled.png)
