from conan import ConanFile

from conan.tools.cmake import CMake
#from conan.tools.layout import cmake_layout



class GTestDemoConan(ConanFile):
    name = "GTestDemo1"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = "gtest/1.13.0"
    generators = "CMakeDeps", "CMakeToolchain"

    # code layout
    # def layout(self):
    #     cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    