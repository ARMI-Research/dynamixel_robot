#!/usr/bin/env python3
import mujoco
import mujoco.viewer
import sys
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: python viewer.py <model.xml>")
        sys.exit(1)
    model_path = sys.argv[1]

    #Load the model
    model = mujoco.MjModel.from_xml_path(model_path)
    data = mujoco.MjData(model)

    print(f"Loaded Model: {model_path}")
    print("Launching Mujoco viewer......")

    #Launch the viewer context
    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            mujoco.mj_step(model, data)
            viewer.sync()
            time.sleep(0.01)

    print("Viewer Closed.")

if __name__ == "__main__":
    main()
