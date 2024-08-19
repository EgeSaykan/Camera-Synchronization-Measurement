import launch

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  ld = LaunchDescription()
  config_path = os.path.join(get_package_share_directory('read_bag'), 'config', 'params.yaml')  
  print(config_path)

  base_node =       Node(
                        package = 'mynteye_ros2_wrapper',
                        executable = 'mynteye_raw_data',
                        output = 'screen',
                        emulate_tty=True,
                        parameters = [config_path]
  )
  rect_node =       Node(
                        package = 'mynteye_ros2_wrapper',
                        executable = 'mynteye_rectification.py',
                        output = 'screen',
                        emulate_tty=True,
                        parameters = [config_path]
  )
  disp_node =       Node(
                        package = 'stereo_image_proc',
                        executable = 'disparity_node',
                        output = 'screen',
                        emulate_tty=True,
                        parameters = [config_path]
  )
  view_node =       Node(
                        package = 'image_view',
                        executable = 'disparity_view',
                        output = 'screen',
                        emulate_tty=True,
                        remappings=[('/image', '/disparity')],
                        parameters= [config_path]
  )
  kinect_v1_image = Node(
                        package="kinect_ros2",
                        executable="kinect_ros2_node",
                        name="kinect_ros2",
                        namespace="kinect"
  )
  kinect2 = Node(
                        package='kinect2_bridge',
                        executable='kinect2_bridge',
                        emulate_tty=True,
                        name='kinect2_bridge',
                        parameters=[config_path],
                        output='screen')
  kinect_v1_show =  Node(
                        package="read_bag",
                        executable="kinect_show_image",
                        name="kinect_show_image",
                        namespace="kinect",
                        parameters=[config_path]
  )
  
  ld.add_action(base_node)
  ld.add_action(rect_node)
  ld.add_action(disp_node)
  ld.add_action(view_node)
  ld.add_action(kinect_v1_image)
  ld.add_action(kinect_v1_show)
  ld.add_action(kinect2)

  return ld
