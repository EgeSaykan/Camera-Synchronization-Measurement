import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImageSubscriber(Node):

  def __init__(self):
    super().__init__('image_subscriber')

    self.declare_parameter('showImg', True)
    self.declare_parameter('showImgDepth', True)

    self.declare_parameter('showImg2', True)
    self.declare_parameter('showImgDepth2', True)
    self.declare_parameter('showIR2', True)

    is_show = self.get_parameter('showImg').get_parameter_value().bool_value
    is_show_depth = self.get_parameter('showImgDepth').get_parameter_value().bool_value
    if is_show:
      self.subscription = self.create_subscription(
          Image,
          '/kinect/image_raw',
          self.show_image,
          10)
      self.subscription  # prevent unused variable warning
    
    if is_show_depth:
      self.subscription_depth = self.create_subscription(
          Image,
          '/kinect/depth/image_raw',
          self.show_image_depth,
          10)
      self.subscription_depth  # prevent unused variable warning

    if True:
      self.subscription_img2 = self.create_subscription(
          Image,
          '/kinect2/hd/image_color_rect',
          self.show_image2,
          10)
      self.subscription_img2  # prevent unused variable warning
      
    if True:
      self.subscription_depth2 = self.create_subscription(
          Image,
          '/kinect2/hd/image_depth_rect',
          self.show_image_depth2,
          10)
      self.subscription_depth2  # prevent unused variable warning

    if True:
      self.subscription_IR2 = self.create_subscription(
          Image,
          '/kinect2/sd/image_ir_rect',
          self.show_image_IR2,
          10)
      self.subscription_IR2  # prevent unused variable warning


    self.bridge = CvBridge()


  def show_image(self, img):
    img_raw = self.bridge.imgmsg_to_cv2(img)
    cv2.imshow("img", img_raw)
    cv2.waitKey(1)

  def show_image_depth(self, img):
    img_raw = self.bridge.imgmsg_to_cv2(img)
    cv2.imshow("img_depth", img_raw)
    cv2.waitKey(1)

  def show_image2(self, img):
    img_raw = self.bridge.imgmsg_to_cv2(img)
    cv2.imshow("img_2", img_raw)
    cv2.waitKey(1)

  def show_image_depth2(self, img):
    img_raw = self.bridge.imgmsg_to_cv2(img)
    cv2.imshow("img_depth_2", img_raw)
    cv2.waitKey(1)

  def show_image_IR2(self, img):
    img_raw = self.bridge.imgmsg_to_cv2(img)
    cv2.imshow("img_IR", img_raw)
    cv2.waitKey(1)



def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    rclpy.spin(image_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()