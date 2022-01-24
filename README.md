# Home Assistant
My home assistant configuration for a sunroom. The sunroom has many orchids and two automations for controlling humidity and light. Environmental variables are provided by a
z-wave multisensor.

## Growlights

### Purpose

The growlights are used to achieve a set amount of light for the plants. The growlights turn on and off based on the light level in the room and off at the end of 
an accumulated light period.

### User Inputs

Setpoint - Desired hours of light
Threshold - Light level at which the lights will turn on
Hysteresis - A buffer around the light level so the lights don't flicker


## Humidifer

### Purpose 

When the outside temperature drops too low, the windows in the sunroom start to accumulate condensation. To avoid this, I reduce the relative humidity
setpoint as a function of forecast low and current outdoor temperatures as reported by Environment Canada.

### User Inputs

Offset - A way to modify the calculated humidity. Positive offsets will cause a higher calculated setpoint.

### User Output

Setpoint - The setpoint is automatically calculated by the script as follows:
| Outdoor Temperature (C) | Humidity (RH) |
| -- | -- |
| -20 and Below | 30 |
| -19 to 0 | 0.5*Temp + 45 |
| Above 0 | 45 |
