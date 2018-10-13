cmake_minimum_required(VERSION 2.8.3)

project(ros_qt_example)

find_package(catkin REQUIRED COMPONENTS rospy)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy
)

catkin_install_python(PROGRAMS scripts/ros_qt_app
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
