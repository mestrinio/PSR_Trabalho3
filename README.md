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

  <a href="https://github.com/mestrinio/Avaliacao2-PSR/graphs/">
    <img src="images/logo.png" alt="Logo" width="550" height="350">
  </a>

<h3 align="center">PSR - Trabalho Prático 2</h3>

<h2><b> Repository Owner: Pedro Martins 103800
<br>Collaborators: Gustavo Reggio 118485 & Tomás Taxa 121863 </b></h2>

  <p align="center">
    This repository was created for evaluation @ Robotic Systems Programming "PSR 23-24 Trabalho prático 2".
    <br />
    <!-- <a href="https://github.com/mestrinio/Avaliacao2-PSR"><strong>Explore the Wiki »</strong></a> -->
    <br >
    <a href="https://github.com/mestrinio/Avaliacao2-PSR/issues"> <u>Make Suggestion</u> </a>
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
This assignment was developed for Robotic Systems Programming. It is an Augmented Reality Painting program, which uses the computer webcam to detect a specific chosen color, and with that, draw on the exact position in a white canvas. This uses Python's OpenCV and includes some advanced features requested by the teacher.

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
## Objectives
### Color Segmenter
The color segmenter program asks the user what parameters for color detection he wants. This part captures the webcam and shows 6 trackbars on the image so that the user can define the right color detection for whatever object he wants to use for painting. Then saves these values on a JSON file.




### AR Paint

The actual painting part of the program should accomplish the following requirements:

#### SETUP
- Read the arguments on the command line to path the json file;
- Read the json file specified in the path, that has the color limits;
- Setup the webcam's capture;
- Create a white canvas to draw on, which has the same size as the incoming capture video of the webcam;

#### CONTINUOUS
- Record and show each webcam's frame;
- Process the incoming video feed with a mask containing the desired pixel color values (and show the mask on another window);
- Process the mask to obtain only the biggest object, and show it;
- Calculate that object's centroid (and mark it as a red cross 'X' on the webcam's feed);
- Use that centroid to paint a circle or a line in the white canvas, with the chosen characteristics for the painting;
***

#### Advanced features
##### Feature 1 - Use Shake Protection
The program is designed to draw lines between centroids instead of circles in each centroid. But sometimes errors in the color detection can happen, and detections on random points of the camera happen, resulting in enormous lines across the canvas. Shake protection detects if the distance between lines is too big to be right, and prevents the drawing. The program should also function using the mouse clicks to draw when either the detections are failing, or the user chooses to do it.

##### Feature 2 - Use webcam feed as canvas
The program should allow the switch in the canvas choice, between the white canvas and the actual webcam frames.

##### Feature 3 - Draw shapes
The program should allow the drawing of shapes on the canvas, rectangles, circles and ellipses. To do so, the user shall press & hold the corresponding key of the shape, to start drawing it, and release it when finishing the size of the shape.


<!-- GETTING STARTED -->
## Getting Started

This is a Python file, so it should be ran in a dedicated terminal running color_segmenter.py, which is the file that runs the first part of the program, to select the desired values for detections. The second and main part of the program, ar_paint.py, runs the painting part and all it's features, but it has some arguments which will be explained later but can be seen using -h argument.

```
./color_segmenter.py
./ar_paint.py -h
```



## Setup
<h3><b>Libraries</b></h3>

To run the program, the following libraries should be installed:

```
sudo apt install python3 python3-tk
pip install opencv-python
pip install numpy
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### How it works

Run color_segmenter.py:
- Select desired values for color detection using the trackbars;
- Use the masked image to understand if the values are as desired;
- Hit 'W' to save the values to the JSON file.

<br>
<br>
<div align="center">
<img  src="images/colorsegmenter.png" alt="colorsegmenter" height="">
</div>
<div align="center">Choose your detection values then hit 'W' to save them</div>
<br>
<br>

***

Arguments when running ar_paint.py:
- -h (Calls for help argument, that explains the other arguments used);
- -usp (Activates the usage of shake protection).
- -j (Insert the full path to the JSON file created in color_segmenter.py)

<br>
<div align="center">
<img  src="images/runarpaint.png" alt="runarpaint" height="">
</div>
<div align="center">Specify the full JSON file's path after -j and write -usp if you want to activate shake protection</div>
<br>
<br>
<br>

Run ar_paint.py:
- A rememberal for the hotkeys to use during the program should pop-up;

<br>
<div align="center">
<img  src="images/tkinter.png" alt="tkinter" height="300">
</div>
<div align="center">Keybindings window pop-up</div>
<br>
<br>

- Drawing in the blank canvas should start happening when detecting the color on the camera;
- Use the hotkeys to change the brush characteristics, switch to drawing on the webcam capture, draw using the mouse and clean or save the current canvas;

<br>
<div align="center">
<img  src="images/drawings.png" alt="drawings" height="300">
</div>
<div align="center">Start drawing!</div>

##### Keybindings:
- 'R' to change brush color to <p style="color: rgb(255,0,0)">RED</p>
- 'G' to change brush color to <p style="color: rgb(0,255,0)">GREEN</p>
- 'B' to change brush color to <p style="color: rgb(0,0,255)">BLUE</p>
- 'P' to change brush color to <p style="color: rgb(0,0,0)">BLACK</p>
- '+' to increase brush size
- '-' to decrease brush size
- 'X' to use rubber
- 'C' to clear the canvas
- 'W' to save the current canvas to an image file
- 'J' to switch between the white canvas and the webcam
- 'M' start using the mouse to draw
- 'I' stop using the mouse to draw
- 'Q' shutdown the program

***
<br>

<!-- CONTACT -->
## Contact
Gustavo Reggio - gustavo.reggio@ua.pt


Pedro Martins - pedro.mestre@ua.pt


Tomás Taxa - tomas.taxa@ua.pt


Project Link: [Trabalho Prático 2](https://github.com/mestrinio/Avaliacao2-PSR)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Professor Miguel Oliveira - mriem@ua.pt

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RobutlerAlberto/RobutlerAlberto.svg?style=for-the-badge
[contributors-url]: https://github.com/mestrinio/Avaliacao2-PSR/graphs/contributors
[product-screenshot]: docs/logo.png
