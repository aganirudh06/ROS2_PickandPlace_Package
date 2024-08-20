from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    gazebo_ros_pkg = get_package_share_directory('gazebo_ros')
    mtc_tutorial_pkg = get_package_share_directory('mtc_tutorial')
    
    #xacro_file = '$(find franka_description)/robots/common/franka_robot.xacro'
    #urdf_file = '/tmp/panda_arm_hand.urdf'
    urdf_file = os.path.expanduser('~/ws_moveit/src/mtc_tutorial/urdf/panda_arm_hand.urdf')
    
    #os.system(f'xacro {xacro_file} -o {urdf_file}')
    
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_pkg,'launch','gazebo.launch.py')
        )
    )

    return LaunchDescription([gazebo_launch,
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'panda', '-file', urdf_file, '-x','0','-y','0','-z','1'],
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        )
    ])

