# CS-499-ePortfolio

Benjamin Vallejo

Southern New Hampshire University



This repository contains selected projects demonstrating my skills in

software development, algorithms, graphics programming, and database systems.



Projects Included



CS300 – Algorithms and Data Structures  

Implementation of vector sorting and CSV parsing in C++.



CS330 – 3D Graphics Programming  

An OpenGL scene demonstrating object modeling, lighting, and textures.



CS340 – Database Development  

Animal shelter dashboard built with Python and MongoDB.

System Diagram

                    Enhanced Rendering and Scene Management Plan

+-------------------+
|   Main Program    |
|  (Application)    |
+---------+---------+
          |
          v
+-------------------+
|   Scene Manager   |
|-------------------|
| - Loads objects   |
| - Stores scene    |
| - Updates state   |
+---------+---------+
          |
          v
+-------------------+
| Rendering Manager |
|-------------------|
| - Draws objects   |
| - Applies shaders |
| - Handles camera  |
| - Controls light  |
+----+---------+----+
     |         |
     v         v
+---------+  +---------+
| Textures|  | Lighting|
+---------+  +---------+
     \         /
      \       /
       v     v
    +----------------+
    | Final 3D Scene |
    +----------------+

Pseudocode

Start Program
    Initialize application window
    Initialize Scene Manager
    Initialize Rendering Manager

    Scene Manager loads all scene objects
    Scene Manager organizes models, textures, and positions

    Rendering Manager initializes shaders, camera, and lighting

    While program is running
        Scene Manager updates scene data
        Rendering Manager reads scene data
        Rendering Manager applies textures and lighting
        Rendering Manager renders final scene to screen
    End While

Close Program

Explanation
This enhancement reorganizes the project by separating scene management from rendering tasks. The Scene Manager is responsible for loading and updating scene objects, while the Rendering Manager focuses on drawing objects, applying textures, managing lighting, and handling camera behavior. This modular design improves maintainability, readability, and scalability of the code. By separating responsibilities, the system becomes easier to extend and debug. This enhancement supports course outcomes related to software design improvement and innovation because it demonstrates better architectural organization and clearer responsibility separation.
