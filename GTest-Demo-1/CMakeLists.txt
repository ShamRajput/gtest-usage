cmake_minimum_required(VERSION 3.15)
project(GTestDemo1)

enable_testing()


set(CMAKE_BUILD_TYPE Release)

find_package(GTest REQUIRED)

add_executable(GTestDemo1 main.cxx)

target_link_libraries(GTestDemo1 GTest::gtest GTest::gtest_main)

include(GoogleTest)
