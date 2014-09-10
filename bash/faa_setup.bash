
# -----------------------------------------------------------------------------
# ROS settings
# -----------------------------------------------------------------------------
source ~/ros/faa_ws/setup.bash

# -----------------------------------------------------------------------------
# FAA setings
# -----------------------------------------------------------------------------
export FAA_RESOURCES=~/.faa
export FAA_NAME=$ROS_WORKSPACE/faa
export FAA_CONFIG=$ROS_WORKSPACE/faa_config
export FAA_INSTALL_SCRIPTS=$FAA_NAME/faa_install/scripts
export FAA_PYTHON_VIRTUALENV=$FAA_RESOURCES/pyenv/faa
export FAA_EXTERNAL_PACKAGE_DIR=$FAA_RESOURCES/external_packages
export FAA_DATA=~/faa_data
