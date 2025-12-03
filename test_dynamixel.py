#!/usr/bin/env python3
from dynamixel_sdk import *  # Uses Dynamixel SDK library

# -------------------------------
# Communication Settings
# -------------------------------
DEVICENAME = "/dev/ttyUSB0"    # Linux
# DEVICENAME = "COM3"          # Windows
BAUDRATE = 57600

# Control Table Address (Protocol 2.0 motors, e.g., XM430)
ADDR_TORQUE_ENABLE = 64
ADDR_GOAL_POSITION = 116
ADDR_PRESENT_POSITION = 132

TORQUE_ENABLE = 1

# -------------------------------
# Initialize Port & Packet
# -------------------------------
portHandler   = PortHandler(DEVICENAME)
packetHandler = PacketHandler(2.0)   # protocol version 2.0

if portHandler.openPort():
    print("Port opened successfully.")
else:
    raise Exception("Failed to open port")

if portHandler.setBaudRate(BAUDRATE):
    print("Baudrate set.")
else:
    raise Exception("Failed to set baudrate")

# -------------------------------
# Scan for Dynamixel IDs
# -------------------------------
print("\n>>> Scanning for Dynamixel IDs...")
found_ids = []

for dxl_id in range(0, 253):
    dxl_model, dxl_comm_result, dxl_error = packetHandler.ping(portHandler, dxl_id)

    if dxl_comm_result == COMM_SUCCESS and dxl_error == 0:
        print(f"Found ID {dxl_id} | Model: {dxl_model}")
        found_ids.append(dxl_id)

if not found_ids:
    print("No Dynamixel found.")
    exit()

target_id = found_ids[0]
print(f"\nUsing first detected Dynamixel ID = {target_id}")

# -------------------------------
# Enable Torque
# -------------------------------
packetHandler.write1ByteTxRx(portHandler, target_id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
print("Torque Enabled!")

# -------------------------------
# Move Motor to 512 (center pos)
# -------------------------------
goal_position = 512  # 0–1023 for AX-12A, 0–4095 for XM430
packetHandler.write4ByteTxRx(portHandler, target_id, ADDR_GOAL_POSITION, goal_position)
print("Moving motor to:", goal_position)

# -------------------------------
# Read Position Feedback
# -------------------------------
present_pos, result, error = packetHandler.read4ByteTxRx(
    portHandler, target_id, ADDR_PRESENT_POSITION
)
print("Present Position =", present_pos)

# -------------------------------
# Close Port
# -------------------------------
portHandler.closePort()
print("Port closed.")
