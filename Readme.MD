# Learning Manim

## What is Manim?
Animation engine for explanatory math videos. Manim is an engine for precise programmatic animations, designed for creating explanatory math videos.

Note, there are two versions of manim. This repository began as a personal project by the author of 3Blue1Brown for the purpose of animating those videos, with video-specific code available here. In 2020 a group of developers forked it into what is now the community edition, with a goal of being more stable, better tested, quicker to respond to community contributions, and all around friendlier to get started with. [~From 3b1b GitHub Repository]


## Installation
- **Install chocolatey** [Chocolatey is a machine-level, command-line package manager and installer for software on Microsoft Windows. ] <br>
-- Run Powershell as Administrator <br>
-- Run ```Get-ExecutionPolicy```. If it returns Restricted, then run ```Set-ExecutionPolicy AllSigned``` or ```Set-ExecutionPolicy Bypass -Scope Process```.  <br>
--Now run the following command: <br>
 ```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

- **Install manim** <br>
-- In Powershell, run the following command: <br>
```choco install manimce```

- Reboot the System to see changes in effect.

## Executing code
- ```manim .\manim_tut1.py Test -pqm```
- or can use the VSCode ```Manim Sideview``` Extension, and just Click the play button in VSCode for executing the code.

## Programs
**Tutorial 1:** - Creating a circle <br>
**Tutorial 2:** - Creating a Square <br>
**Tutorial 3:** - Printing my Name & some shapes <br>
**Tutorial 4:** - Some Common Errors in Manim <br>
**Tutorial 5:** - Reading the Manim Library and Plotting Axes and Line Graph <br>
**Tutorial 6:** - Getters & Updaters <br>
**Tutorial 7:** - Harry Potter Deathly Hallows Symbol using Manim <br>
**Tutorial 8:** - Updaters, redraw function, MathTex [Moving Box] <br>
**Tutorial 9:** - Value Trackers <br>
**Tutorial 10:** - Graphing - NumberPlane and plotting a parabola and Riemann Rectangles <br>
**Tutorial 11:** - Graphing with Updaters [Axes, Parabola and Secant Slope] <br>
**Tutorial 12:** - Using SVGs with manim [OVO Logo (SVG)] <br>

## Outputs
My First Manim Video <br>

https://user-images.githubusercontent.com/104393371/219792268-2f4ed787-7ef4-417f-a3d8-8d9a56dd13fa.mp4

**Deathly Hallows Symbol from Harry Potter**

https://user-images.githubusercontent.com/104393371/219892419-27639e21-cfcd-45f8-bf0c-0213681e08fd.mp4



## Resources/References Used
- https://github.com/3b1b/manim - 3Blue1Brown GitHub Repository
- https://docs.manim.community/en/stable/installation/windows.html - Manim Community Version Installation Guide
- https://chocolatey.org/install#install-step2 - Chocolatey Installation Guide
- https://www.youtube.com/watch?v=hlKNyKVqT_k - Manim Installation Video Guide [Windows]
- Manim Sideview Extension in VSCode
- https://www.youtube.com/watch?v=KHGoFDB-raE - Tutorial on Manim by Brian Amedee
