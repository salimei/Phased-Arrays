# Phased-Arrays

Scope : This repository stores all the "back-of-the-envelope" simulations I did during my time at MRT. 

| Name  | Summary |
| ------------- | ------------- |
| MRT_array_1.py | Calculating the array factor AF for equally spaced linear array (ESLA) |
| MRT_antenna_sim.py  | Caculating the link budget and Fresnel zone  |
| MRT_antenna_integration_results.py | Plotting the radiation patterns measured during integration testing |

Here is a more complete description. 

### MRT_array_1.py. 

This script allows us to calculate the AF (array factor) and radiation pattern of any equally spaced linear array (ESLA). Changing the phase of the complex excitation signal allows us to steer the beam. This simulation does rely on a few assumptions, however, most notably we ignore effects resulting from mutual coupling that arise when elements are too close to each other.

I implemented the array factor and radiation pattern functions based on the derivations from the following textbook:   
 > *Warren L. Stutzman, Gary A. Thiele - Antenna Theory and Design-Wiley (2012)*.

### MRT_antenna_sim.py

The first part of this script helps in choosing the most suitable COTS (comercial-off-the-shelf) antenna for a given long range application. I implemented Friis' transmission formula to calculate the link budget. To improve accuracy, I accounted for the VSWR of each antenna (mismatch). 

The second part of this script the radius of the first Fresnel zone. This is useful for determing the minimum clearance (zone of free obstacles) around an antenna. 

Finally, I added the experimental results collected during integration testing as means to compare our theoretical prediction with the much more complex real world. 

### MRT_antenna_integration_results.py

This script displays the radiation pattern measured during integration testing on a polar plot. 
