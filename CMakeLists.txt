cmake_minimum_required(VERSION 2.8.3)

project(ros_qt_example)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy std_msgs
)

catkin_install_python(PROGRAMS scripts/ros_qt_app
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
