MAX_POSITION = 4095
MAX_DEGREE = 360
OFFSET = 0 #Enter here after calibrate

def degree_bit_convert(degree: float): # 0-360 => 0-4095
    degree = max(0, min(MAX_DEGREE, degree))
    bit = round(degree*(MAX_POSITION/MAX_DEGREE)) + OFFSET
    return bit

def bit_degree_convert(bit: int): # 0-4095 => 0-360
    bit = max(0, min(MAX_POSITION, bit))
    degree = round((bit - OFFSET) * (MAX_DEGREE/MAX_POSITION))
    return degree
from dynamixel_sdk import *

class MOTOR_DYNAMIXEL:
    ADDR_TORQUE_ENABLE          = 64    #Control table address for Torque Enable
    ADDR_GOAL_POSITION           = 116   #Control table address for Goal Position
    ADDR_PRESENT_POSITION        = 132
    
    def __init__(self, model, DEVICENAME, DXL_ID, BAUDRATE):
        self.model = model
        self.DEVICENAME = DEVICENAME 
        self.DXL_ID = DXL_ID
        self.BAUDRATE = BAUDRATE
        self.PROTOCOL_VERSION = 2.0
        self.home_position = 2048 # The middle value

        self.port_handler = PortHandler(self.DEVICENAME)
        self.packet_handler = PacketHandler(self.PROTOCOL_VERSION)
        self.port_handler.openPort()
        self.port_handler.setBaudRate(BAUDRATE)

        self.packet_handler.write1ByteTxRx(self.port_handler, self.DXL_ID, self.ADDR_TORQUE_ENABLE, 1)
        print("Torque Enabled.")
    
    #Control functions
    
    def send_joint_pos(self, degree):
        target_bit = degree_bit_convert(degree)
        self.packet_handler.write4ByteTxRx(self.port_handler, self.DXL_ID, self.ADDR_GOAL_POSITION, target_bit )
        print(f"Rotating the motor {degree}...")
    
    def get_joint_pos(self):
        current_bit, comm_result, error = self.packet_handler.read4ByteTxRx(self.port_handler, self.DXL_ID, self.ADDR_PRESENT_POSITION)
        return current_bit
    
    def go_home(self):
        self.packet_handler.write4ByteTxRx(self.port_handler, self.DXL_ID, self.ADDR_GOAL_POSITION, self.home_position)
        print("Rotating to the home position...")