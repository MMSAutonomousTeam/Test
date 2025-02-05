from setuptools import find_packages, setup

package_name = 'turtle_control_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ahmedmwafy',
    maintainer_email='ahmedmwafy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          "drawing_A=turtle_control_1.drawing_A:main" ,
          "drawing_H=turtle_control_1.drawing_H:main" ,
          "drawing_M=turtle_control_1.drawing_M:main" ,
          "drawing_E=turtle_control_1.drawing_E:main" ,
          "drawing_D=turtle_control_1.drawing_D:main" 
        ],
    },
)
