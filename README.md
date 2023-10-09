# Various Scripts and Files for FSAE Race Car Analysis

Note this repo is not heavily used yet, so not all analysis is here. Our team is just starting testing and thus do not have much data for the current iteration. We are also having difficulting with increasing realibility on the hardware side of this given limited time and unexpected EMI interference for example. 

The data we have for the current season is just linear potentiometer data to measure suspension displacement. These sensors read off a voltage that we then convert to distance in mm. This data is very noisy with our current sampling rate and resolution as well as the imense EMI influence on the driver's right. Luckily since we have such high sampling rate, even after increasing the resolution, we have near continous data with respect to our vehicle's relative speed on track, so we can refine the data using python scripts into a usable form that we can correlate back to our simulations. 

Currently have not implemented any filtering and this data is from 09/30/2023 and 10/1/2023, so behind the recent updates to resolution. Left side refers to drivers right, this will be changed in future version.  

## On Track Data  

![Alt text](sunday_linpot.png)

## Idling, Can see the Imact EMI has on the Side Left

The drop is from loss of power to the linear potentiometers.  
![Alt text](saturday_linpot.png)
