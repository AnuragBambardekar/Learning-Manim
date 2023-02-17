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

## Outputs
https://user-images.githubusercontent.com/104393371/219791225-0bdb364f-8d1c-4032-b27b-fdd3c0d1b707.mp4


## Resources Used
- https://github.com/3b1b/manim - 3Blue1Brown GitHub Repository
- https://docs.manim.community/en/stable/installation/windows.html - Manim Community Version Installation Guide
- https://chocolatey.org/install#install-step2 - Chocolatey Installation Guide
- https://www.youtube.com/watch?v=hlKNyKVqT_k - Manim Installation Video Guide [Windows]
- Manim Sideview Extension in VSCode
- https://www.youtube.com/watch?v=KHGoFDB-raE - Tutorial on Manim by Brian Amedee
