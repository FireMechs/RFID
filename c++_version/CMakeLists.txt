cmake_minimum_required(VERSION 3.10.2)
project(c++_version)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11  -lbcm2835")

set(RFID_INCLUDE_DIR  ${CMAKE_SOURCE_DIR}/RPi-RFID/)
include_directories(${RFID_INCLUDE_DIR})
set(BCM_LIB  ${CMAKE_SOURCE_DIR}/bcm2835-1.50/src/bcm2835.o)

set(SOURCE_FILES
        ${CMAKE_SOURCE_DIR}/RPi-RFID/MFRC522.cpp
        ${CMAKE_SOURCE_DIR}/read.cpp
        ${CMAKE_SOURCE_DIR}/write.cpp
        )
add_executable(RFID  ${SOURCE_FILES})
target_link_libraries(RFID  ${BCM_LIB})