cmake_minimum_required(VERSION 3.10.9)
project(c++_version)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11  -lbcm2835")

set(SOURCE_FILES
        ${CMAKE_SOURCE_DIR}/read.cpp
        ${CMAKE_SOURCE_DIR}/write.cpp
        )
add_executable(RFID  ${SOURCE_FILES})