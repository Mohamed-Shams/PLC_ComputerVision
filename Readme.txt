# Demo Implementation Readme

This document outlines the steps required to successfully integrate the demo into the FIO Scene using PLC code, Prosys Integer objects, Python code, and Node-red. Please follow these instructions carefully to ensure a smooth setup and execution.

## Prerequisite Python Packages

Before you begin, ensure that you have the following Python packages installed:

- `opcua` library (imported as `Client`)
- `cv2` (OpenCV) library for computer vision
- `time` library for time-related operations
- `os` library for system-related functions
- `HandTrackingModule` as `ht` for hand tracking functionalities
- `sys` library for system-specific parameters and functions

Make sure these packages are installed in your Python environment to proceed with the integration.

## Node-red Packages

Also, ensure that you have the following Node-red packages installed:

- Install Node-red: [Node-RED Installation Guide](https://nodered.org/docs/getting-started/windows)
- `node-red-contrib-opcua`
- `node-red-contrib-s7`

## Instructions

1. **Write PLC Code for FIO Scene Compatibility:**
   Create PLC code that aligns with the requirements and compatibility of the FIO Scene environment (just line to activate the output).

2. **Create Prosys Integer Variable:**
   Within the Prosys environment, generate an Integer Variable that corresponds to the specific parameters or data points relevant to the demo. Configure its properties as needed.

3. **Modify Python Code Parameters:**
   In the provided Python code, locate the sections related to the demo's functionality. Modify the parameters, inputs, or settings according to the requirements of the project. Ensure that the Python code is aligned with the FIO Scene and Prosys setup.

4. **Adjust Parameters in Node-red:**
   Open the Node-red flow associated with the demo. Locate the nodes or modules that handle the communication or interaction with the Python code and Prosys Integer object. Adjust the parameters, mappings, or connections to match the changes made in previous steps.

5. **Connect and Execute:**
   Once all modifications are completed, ensure that all components are properly connected and integrated. Run the system to observe the desired outcome. Monitor for any errors or inconsistencies and make necessary adjustments.
