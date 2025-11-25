# dynamixel_robot

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Platform](https://img.shields.io/badge/Platform-OpenCR-green)
![Dynamixel](https://img.shields.io/badge/Dynamixel-Protocol%202.0-orange)
![Status](https://img.shields.io/badge/Status-Under%20Development-yellow)
![ROS](https://img.shields.io/badge/ROS-Optional-blue)
![ROS2](https://img.shields.io/badge/ROS2-Optional-purple)

A development project for building a **Dynamixel-based robot arm** using the **OpenCR** board.  
This project is inspired by and references the **ROBOTIS OpenManipulator** architecture, aiming to offer an open, modular, and extensible robotic arm platform for research, education, and rapid prototyping.

---

## 📌 Project Overview

This repository develops a robotic arm powered by **Dynamixel motors**, controlled via **OpenCR** using **Dynamixel Protocol 2.0**.  
The system is designed to be:

- Modular  
- Open-source  
- Easy to extend  
- Compatible with ROS / ROS2 (planned)

---

## ✨ Features

- Modular robot arm (OpenManipulator-inspired)
- Full Dynamixel Protocol 2.0 support  
- OpenCR firmware support  
- Forward/Inverse kinematics (WIP)  
- Trajectory & joint motion control  
- Expandable hardware (extra joints, gripper)  
- ROS / ROS2 interface (planned)  
- Example demos and calibration tools  

---

## 🧱 Hardware Requirements

- **OpenCR 1.0 / 1.1 board**  
- **Dynamixel Servos:**  
  - X Series / etc.  
- Power supply (12V or 24V depending on servo model)  
- Optional:  
  - 3D-printed links  
  - Gripper module  
  - USB cable  

---

## 🧰 Software Requirements

- Arduino IDE **or** PlatformIO  
- OpenCR Arduino libraries  
- Dynamixel SDK  
- (Optional) ROS/ROS2 packages:  
  - `dynamixel_workbench`  
  - `open_manipulator`  

---

## 📁 Project Structure
```
dynamixel_robot/
├── firmware/ # OpenCR firmware, Arduino sketches
├── kinematics/ # FK/IK implementations
├── config/ # IDs, baudrate, profiles, params
├── launch/ # ROS/ROS2 launch files (future)
├── docs/ # Documentation, diagrams, wiring
└── examples/ # Basic motion demos
```

---

## 🚀 Getting Started

### 1. Flash OpenCR Firmware  
Upload your firmware from `firmware/` using:
- Arduino IDE  
- PlatformIO  
- or OpenCR Manager

### 2. Configure Dynamixel Motors  
Set motor IDs & baudrate using:
- Dynamixel Wizard  
- or Dynamixel SDK

### 3. Connect the Hardware  
Follow connection & wiring diagrams in the `docs/` folder.

### 4. Run Example  
```bash
cd examples
opencr_upload basic_motion.ino
