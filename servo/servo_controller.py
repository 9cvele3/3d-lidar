from scservo_sdk import PortHandler, PacketHandler, SCS_TOHOST, COMM_SUCCESS, SCS_LOWORD, SCS_HIWORD

# Control table address
ADDR_SCS_TORQUE_ENABLE = 40
ADDR_SCS_GOAL_ACC = 41
ADDR_SCS_GOAL_POSITION = 42
ADDR_SCS_GOAL_SPEED = 46
ADDR_SCS_PRESENT_POSITION = 56

# all methods must have `self` param, like in rust
# there is builtin `id` in python
class ServoController:
    def __init__(self, servo_id, device_name):
        self.id = servo_id
        self.device_name = device_name

        baudrate = 115200
        protocol_end = 1 # SCServo bit end(STS/SMS=0, SCS=1)
        self.port_handler = PortHandler(self.device_name)
        self.packet_handler = PacketHandler(protocol_end)
            
        if self.port_handler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")

        if self.port_handler.setBaudRate(baudrate):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")

    def __del__(self):
        print("ServoController destructor")
        self.port_handler.closePort()

    def get_id(self):
        return self.id

    def set_acc(self):
        SCS_MOVING_ACC = 0
        scs_comm_result, scs_error = self.packet_handler.write1ByteTxRx(self.port_handler, self.id, ADDR_SCS_GOAL_ACC, SCS_MOVING_ACC)
        self.log_errors(scs_comm_result, scs_error)

    def set_speed(self):
        SCS_MOVING_SPEED = 100
        scs_comm_result, scs_error = self.packet_handler.write2ByteTxRx(self.port_handler, self.id, ADDR_SCS_GOAL_SPEED, SCS_MOVING_SPEED)
        self.log_errors(scs_comm_result, scs_error)

    def set_goal_position(self, goal_position):
        scs_comm_result, scs_error = self.packet_handler.write2ByteTxRx(self.port_handler, self.id, ADDR_SCS_GOAL_POSITION, goal_position)
        self.log_errors(scs_comm_result, scs_error)

    def get_current_position_and_speed(self):
        scs_present_position_speed, scs_comm_result, scs_error = self.packet_handler.read4ByteTxRx(self.port_handler, self.id, ADDR_SCS_PRESENT_POSITION)
        self.log_errors(scs_comm_result, scs_error)
        present_position = SCS_LOWORD(scs_present_position_speed)
        present_speed = SCS_HIWORD(scs_present_position_speed)
        return (present_position, present_speed)

    def enable_torque(self):
        scs_comm_result, scs_error = self.packet_handler.write1ByteTxRx(self.port_handler, self.id, ADDR_SCS_TORQUE_ENABLE, 0)
        self.log_errors(scs_comm_result, scs_error)
    
    def log_errors(self, scs_comm_result, scs_error):
        if scs_comm_result != COMM_SUCCESS:
            print("%s" % self.packet_handler.getTxRxResult(scs_comm_result))
        elif scs_error != 0:
            print("%s" % self.packet_handler.getRxPacketError(scs_error))

