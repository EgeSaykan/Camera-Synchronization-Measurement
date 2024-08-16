import rclpy
from rclpy.node import Node

import message_filters
from std_msgs.msg import String
from sensor_msgs.msg import Image, Imu

from cv_bridge import CvBridge

import numpy as np
import cv2
import io, os, yaml

class MinimalSubscriber(Node):

    def __init__(self):
      super().__init__('bag_subscriber')

      self.declare_parameter('my_parameter', 'world')

      self.subscription = self.create_subscription(
                                                  String,
                                                  'topic',
                                                  self.listener_callback,
                                                  10)
      self.subscription  # prevent unused variable warning