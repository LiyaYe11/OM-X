cmake_minimum_required(VERSION 3.22)
project(open_manipulator_x_moveit_config)


set(SKIP_BUILD OFF)

if(NOT SKIP_BUILD)
  find_package(ament_cmake REQUIRED)

  ament_package()

  install(DIRECTORY launch DESTINATION share/${PROJECT_NAME}
    PATTERN "setup_assistant.launch" EXCLUDE)
  install(DIRECTORY config DESTINATION share/${PROJECT_NAME})
  install(FILES .setup_assistant DESTINATION share/${PROJECT_NAME})

else()
  message(WARNING "Skipping compilation due to miss porting of code in Gazebo Harmonic.")
endif()