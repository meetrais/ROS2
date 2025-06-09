#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('py_test')
        self.counter= 0
        self.get_logger().info('MyNode has been initialized!')
        self.create_timer(1.0, self.timer_callback)  # Timer that calls the callback every second
    
    def timer_callback(self):
        self.get_logger().info('Timer callback executed! ' + str(self.counter))
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    node.get_logger().info('Hello, ROS 2 from my first Python node!')
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()