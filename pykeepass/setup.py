from setuptools import setup

setup(name="pykeepass",
       version="3.2.1",
       license="GPL3",
       description="Python library to interact with keepass databases ",
       long_description =open('README.rst', 'rb').read().decode('utf-8'),
       author="Philipp Schmitt",
       author_email="philipp@schmitt.co",
       url="https://github.com/libkeepass/pykeepass",
       download_url="https://github.com/libkeepass/pykeepass/archive/3.2.1.tar.gz",
       data_files=['CHANGELOG.rst',  'LICENSE',  'README.rst'],
       packages = ['src.pykeepass' , 'src.pykeepass.kdbx_parsing'],
       install_requires = ["python-dateutil", "construct==2.10.54", 
                                    "argon2_cffi", "pycryptodome>=3.6.2", "lxml", "future"],
       include_package_data=True
)
