# RocketLab
Laboratory for model rocket simulations and control.  

## Goals
Currently, the goals of the model rocket (to be designed) will be to launch and land in a predefined landing zone. Thrust vector control will be implemented to aid in the flight trajectory and the landing. The landing will be a rocket powered landing. 

### Software
**C/C++**  
The software used will be created for a flight computer (tba) that will run the trajectory analysis, when to fire the motor, and actuator control for the thrust vector control.

----

**Python**  
There will be a light weight simulator that will be able to provide basic information about the rocke to aide in design. This part of the project should be designed with the ease of use for any model rocket enthusiast and thus, a GUI is being created to run the simulations. The program will be packaged in a convientent way to allow for easy download and use.

### Flight
The goal of the rocket flight will be to go to apogee and return to a specific location with a rocket powered descent/landing. The landing zone will be predetermined before launch

## How to Use
The code in this project is available, open-source, under the [GNU General Public License v3.0](https://github.com/A-Hopkins/RocketLab/blob/master/LICENSE)

### Simulator
The simulator can be [downloaded](https://www.github.com/a-hopkins/RocketLab) in a package that will be click to run. This software will provide you with graphs to analyze your rockets, velocity, height, and acceleration. It has support for inputting your own data of your rocket (weight, engine values, etc.) or loading a configuration file with that information. It supports multiple engine firings (multistage) and a time adjustment for when the stages start. 

### Flight Code
The flight code will be available for use, but not packaged in the same way as the simulator. You will have to modify it for whatever flight computer you choose and for whatever design choices you make on your own rocket.
