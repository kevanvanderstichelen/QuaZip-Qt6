from conans import ConanFile, CMake, tools


class QuazipQt6Conan(ConanFile):
    name = "quazip"
    version = "1.4.0"
    license = "LGPL-2.1, zlib/png"
    description = "Qt/C++ wrapper over minizip"
    topics = ("conan", "quazip", "qt6")
    url = "https://github.com/kevanvanderstichelen/QuaZip-Qt6"
    homepage = "https://github.com/stachenov/quazip"
    exports_sources = "*"
    generators = ("cmake","cmake_find_package")
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    build_policy = "missing"

    requires = ("bzip2/1.0.8@",
                "zlib/1.2.13@")

    def config_options(self):
        pass

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.definitions["QUAZIP_QT_MAJOR_VERSION"] = 6
        cmake.configure(source_folder=".")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["quazip"]

