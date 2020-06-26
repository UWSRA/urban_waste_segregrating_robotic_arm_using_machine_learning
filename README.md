# urban_waste_segregrating_robotic_arm_using_machine_learning
 A moving bot with a fixed robotic arm that picks up various wastes and places in respective bins using machine learning

Repository Contents:
Arduino: files used for Arduino to control the bot and the robotic arm
1.Arduino Uno - .ino file of the complete movement of the bot.
2.Arduino Nano - .ino file of the complete movement of the robotic arm.

MQTT: communication between the raspberry pi and the end system
1.End System - .py file of the server that acts as a subscriber
2.Raspberry Pi - .py file of the client that acts as a publisher
               - .py file of the server that acts as a subscriber
               
               
Object Detection: Prediction Algorithm
1.Prediction - .py file that runs the main algorithm
2.Textpublish - .py file that helps the end system to act as a client publisher.

Snapshots of results - Pictures and videos of the output

Tensorflow - To train the customized prediction model
1.CSV - .csv files of the train and the test labels
2.Frozen Inference Graph- .pb file of the trained model
3.Label Map - .pbtx file of the class labels
4.MyNotebook - .ipynb file of the notebook that contains the process of the trained model.
5.Used a dataset of 1500 images with 3 class labels namely fruit waste, leaf and paper.

Final command - .sh file that finally runs on pi
Captures the image fro pi cam and runs the pi as a client publisher.

Fine tuned Model - .zip of the entire customised trained model with its checkpoints.

Report - contains detailed explanation of the entire project.

System Requirement Specification - contains all the software and hardware requirements along with the design of the system.

Work Breakdown Structure - complete breakdown structure of the 4 members of the team.


