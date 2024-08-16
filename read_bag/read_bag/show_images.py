import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class MinimalSubscriber(Node):

  def __init__(self):
    super().__init__('image_subscriber')

    self.declare_parameter('showImg', True)
    is_show = self.get_parameter('showImg').get_parameter_value().bool_value
    
    if (is_show):
      self.subscription = self.create_subscription(
          Image,
          '/kinect/image_raw',
          self.show_image,
          10)
      self.subscription_depth = self.create_subscription(
          Image,
          '/kinect/depth/image_raw',
          self.show_image_depth,
          10)
      self.subscription  # prevent unused variable warning


    self.bridge = CvBridge()


  def show_image(self, img):
    img_raw = self.bridge.imgmsg_to_cv2(img)
    cv2.imshow("img", img_raw)
    cv2.waitKey(1)

  def show_image_depth(self, img):
    img_raw = self.bridge.imgmsg_to_cv2(img)
    cv2.imshow("img_depth", img_raw)
    cv2.waitKey(1)



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()