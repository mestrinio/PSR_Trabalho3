<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<div align="center">

[![Contributors][contributors-shield]][contributors-url]




<!-- PROJECT LOGO -->
<br />

  <a href="https://github.com/mestrinio/PSR_Trabalho3/graphs/">
    <img src="images/logo.png" alt="Logo" width="550" height="350">
  </a>

<h3 align="center">PSR - Trabalho Prático 3</h3>
<h3 align="center">THOR - Trully Hardworking Outstanding Robot</h3>

<h2><b> Repository Owner: Pedro Martins 103800
<br>Collaborators: Luís Fernandes 103085 & Afonso Pereira 89142 </b></h2>

  <p align="center">
    This repository was created for evaluation @ Robotic Systems Programming "PSR 23-24 Trabalho prático 3".
    <br />
    <!-- <a href="https://github.com/mestrinio/PSR_Trabalho3"><strong>Explore the Wiki »</strong></a> -->
    <br >
    <a href="https://github.com/mestrinio/PSR_Trabalho3/issues"> <u>Make Suggestion</u> </a>
  </p>
</div>
<br>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-assignment">About the assignment</a>
    </li>
     <li>
      <a href="#Objectives">Objectives</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<br>



<!-- ABOUT THE ASSIGNMENT -->
## About the Assignment
<div align="center">
<img  src="images/drawing1.png" alt="colorsegmenter" height="400">
</div>
<br>
This assignment was developed for Robotic Systems Programming. It uses a simulated environment to program a simulated robot, model TurtleBot3. The bot is meant to be accomplish a certain number of missions, including detection of objects or people, using image similarity or database comparison (with YOLOv8), and other navigation and localization missions. The model has been modified to have similarities with the "Thor" god character. The program uses ROS and its programmed with Python language and OpenCV library.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- Objectives -->
## Objectives/Missions
### Robot configuration (Objective)

The robot model is based on Turtlebot3 Waffle Pi but has been customized to fit the Thor theme. Colors and 3D features have been altered and included to match Thor's outfit style, and his hammer. An extra camera has been added to the top of the model.

<br>

### Scenery Mapping (Objective)

A previous mapping of the simulated house has been done using the procedure taught in class.................

<br>

### Robot navigation (Mission)

This robot features 4 different navigation modules:
- Teleop driving (incrementation of velocity values, linear and angular)
- Teleop videogame driving (WASD controls the instantaneous velocities)
- Autonomous point-to-point at specific location selected in RViz
- Autonomous point-to-point at specific room selected in mission manager.

<br>

### Object spawning in scenery (Objective)

It is possible to spawn different objects in different positions using a specific script.

<br>

### Object Detection (Missions)

THOR has it's own object detection features, which include usage of color and shape to detect objects using it's cameras.

#### Specific Missions

A more detailed view of the missions and features is explained later on this guide.


<!-- GETTING STARTED -->
## Getting Started

To use THOR, you need to have ROS properly installed on your system (<a href="http://wiki.ros.org/ROS/Installation"> <u>ROS Installation</u> </a>). Furthermore, you must have turtlebot3 original model associated (<a href="https://www.turtlebot.com/turtlebot3/"> <u>Turtlebot3 Models</u> </a>). Lastly, the house needs to be downloaded to the previously made catkin_ws/src directory (```git clone https://github.com/aws-robotics/aws-robomaker-small-house-world```) and some other packages must be installed on python for everything to work.
IMPORTANT NOTE: YOLOv8 from ultralytics occupies a lot of storage so be sure to have at least 20 GB free to use.

## Setup
<h3><b>Installs</b></h3>

```
sudo apt-get install ros-noetic-map-server
sudo apt-get install ros-noetic-amcl
sudo apt-get install ros-noetic-navigation
sudo apt-get install ros-<your-ros-distro>-cv-bridge
sudo apt-get install ros-<your-ros-distro>-image-transport
sudo apt install python3 python3-tk
pip install numpy
pip install ultralytics
pip install gTTS
pip install playsound
pip install opencv-python
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Launch simulation (Follow order)

```
roslaunch robutler_bringup_tp3 gazebo.launch
roslaunch robutler_bringup_tp3 bringup.launch
rosrun robutler_bringup_tp3 mission_manager_menu
```

Navigation (choose one):
```
rosrun robutler_bringup_tp3 teleop_key
rosrun robutler_bringup_tp3 teleop_keypressteste
```

##### Keybindings:
- 'W' to move forwards
- 'S' to move backwards
- 'D' to turn right
- 'A' to turn left 

<br>
Other navigations:

- Using RViz select option to move to 2d point.
- Right press the balloon over THOR to open missions menu, and select option to move to desired room.

***
OBJECT SPAWN, DETECTION AND SPECIFIC MISSIONS LEFT HERE.


## Specific Missions

The mission manager allows THOR to do various specific missions. He is able to:

- Take a picture of a specific division
- Search for specific objects and count how many of them there are
- Detect if there is someone at the house and where they are
- Race around the house

<br>

To start any given mission, the user needs to Right-click the gray circle above THOR in the RViz window. This will show the missions list and allow the user to select the mission type and objective (example, take a picture of the kitchen).



***
<br>

<!-- CONTACT -->
## Contact
Luís Fernandes - luis.c.fernandes8@ua.pt


Nuno Afonso Pereira - nafonsofp@ua.pt


Pedro Martins - pedro.mestre@ua.pt


Project Link: [Trabalho Prático 3](https://github.com/mestrinio/PSR_Trabalho3)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Professor Miguel Oliveira - mriem@ua.pt

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RobutlerAlberto/RobutlerAlberto.svg?style=for-the-badge
[contributors-url]: https://github.com/mestrinio/PSR_Trabalho3/graphs/contributors
[product-screenshot]: docs/logo.png
