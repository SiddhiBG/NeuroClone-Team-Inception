# NeuroClone-Team-Inception
This project aims to make a robot that works on commands received from brain. In other words, it can be controlled by mere thoughts. The following repo tells about the building of the software part of the bot.

## Introduction 

Our ITSP Project is based on tracking brain signals, manipulating them so that they could be used to simulate and control a robot. The basic motivation behind this project was to help the paralysed people so that they can perform their tasks with the help of the bot , thereby giving them a sense that they themselves are performing those actions. 
So what we concluded from our brain study is that all the functions which are performed by humans are the results of control and coordination of brain and other body systems. Brain controls the body movements by sending electrical signals. These electrical signals are specifically called EEG ( Electroencephalography ) signals.
 
Electroencephalography means writing of the electrical activity of the brain. Electroencephalography records the electrical activity of the brain using electrodes placed on the scalp. Measuring electrical activity from the brain is useful because it
reflects how the many different neurons in the brain network communicate with each
other via electrical impulses.


If we look more closely at paralysis, patients are not able to perform body movements because the contact between the brain and that specific body part has been disrupted due to some injury, accident or birth defects. If we want to perform an action, the 1st process involved is imagination.. This imagination is also done by the patients but it is not converted into action. The imagination is done in the form of electric signals.They can be detected using a set of electrodes placed on the scalp. The plan is to take these “imagination” signals, interpret them and send them to a robot that can do those actions for you. The EEG signals from the brain are extracted, filtered and digitized so that they can be used by the Bot. The bot would use the signals to perform desired action.

## Team division

We had a team of 5, we divided the work among 2 modules. The 1st module dealt with creation and extraction of EEG signals, and the 2nd module was involved in robot simulation. 

In this project we have only dealt with the hand movements due to time constraints and we don't have the proper resources for other body parts, also carrying out the activity in an online mode is a genuinely difficult task both in terms of implementation and assimilation. 

## We learnt the following softwares and studied the material to have a better knowledge about EEG datasets and robot simulation.
### Brain Study 
Acquired info about various parts of Brain like cerebrum, cerebellum , medulla, parietal lobe etc. and the parts which are responsible for hand movementsWe studied in detail how different lobes of the brain works. Mainly the frontal lobe and  parietal lobe contribute towards the movements.Frontal cortex contains motor areas which control voluntary movements of all of our limbs. Also brain study was required to have certain knowledge about which electrode to be placed on which part of the brain.  

 

### Study of electrodes source
In measurement of EEG signals the system adapted for placement of electrodes on the scalp is called the 10 - 20 electrode system. This system standardized physical placement and designations of electrodes on the scalp. The head is divided into proportional distances from prominent skull landmarks (nasion, preauricular points, inion) to provide adequate coverage of all regions of the brain. Label 10-20 designates proportional distance in percents between ears and nose where points for electrodes are chosen. Electrode placements are labelled according to adjacent brain areas: F (frontal), C (central), T (temporal), P (posterior), and O (occipital). The letters are accompanied by odd numbers at the left side of the head and with even numbers on the right side. Left and right side is considered by convention from the point of view of a subject.
We gathered this information by reading various research papers and reading through some pdf describing the experiments performed on EEG signals.This study of electrodes helped us to understand which electrodes signals represent signals corresponding to hand movement. 
### EEG datasets
Encephalographic measurements employ a recording system consisting of - electrodes with conductive media - amplifiers with filters - A/D converter - recording device. 
We used data set available on kaggle to train our ML programme 
https://www.kaggle.com/c/grasp-and-lift-eeg-detection/data 
The team targets to get more datasets in phase 2 by actual experiments 

### Machine learning and deep learning
We learnt the basics of machine learning. We learnt deep learning. We used convoluted neural networks to convert the EEG signals to commands tha. We found the code on kaggle. We edited that code accordingly to train a live data set. We also tried Matlab to process and filter data but in the end decided to stick to python. 

### Robotics
The Robotics part was done by Module2. It involved study of bots, how they interpret the data and perform required actions. 
It involved installing ubuntu softwares on virtualbox (as we worked on windows platform and had very little knowledge about the linux interface)
ROS beginner and intermediate level tutorials from ROS WIKI . Here we learnt about creating ros packages, nodes, turtlesim, publisher, subscriber(python) , graphs rqt_console , recording and playing back data. 

### Gazebo simulation
As we would be needing a simulation environment to show the bot moving, we learnt gazebo simulation, SLAM(Simulation Localization and Mapping) in order to create an environment for the bot. The SLAM (Simultaneous Localization and Mapping) is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of TurtleBot 

### Turtlebot
In order to start with implementing the EEG signals on the Bot, we used turtlebot3, we looked over the robotis tutorial and material. Turtlebot is a far simpler bot which was fit to serve as a starting point to us. We can have SLAM nodes, navigation, simulation and all other features we expect in our bot in a much simpler manner. 

### Open source manipulator
Open source manipulator is exactly the thing we needed, since as explained above we are only dealing with the hand movements, we needed a bot which could really perform those hand movements. Open Source manipulator is a hand robot which could be attached to the turtlebot and could be used to pick and hold objects and show movements. 

### Solidworks
We had a plan that once we complete the implementation of datasets turtlebot, we would create a bot of our own, which we would design on our own. Therefore we learnt Solidworks. We practiced through Solidworks Tutorials, CAD CAm tutorials and various workshops conducted. 

## Final Plan for the project 

A simulation that will be able to do a very specific job(mentioned in references) controlled by EEG signals, generated live

## Difficulties faced
Making us familiar with the topic and searching for usable research papers. Mentors helped us through this and extra efforts were put in.
It was difficult for our laptops to digest heavy software and for us to learn them in a short span.
Also problems occurred as the ROS GiTHUB server was down and it took a lot of time to find solutions through youtube and stackoverflow. 
One of the most important and unexpected difficulties was that we downloaded and started working on the ubuntu 20.04 platform, which supports ros noetic. We didn't know that open source manipulator is not compatible on ros noetic and is only compatible on ros kinetic and melodic. We realised this quite late and therefore we had to start all over again.  It led to a lot of chaos especially for Module2 

## References and Datasets
### MODULE 1

ML & DL courses: Coursera

EEG basics: various research papers: Resources 

EEGLAB Tutorial:
EEGLAB News 

datasets
List of datasets 

Kaggle:
https://www.kaggle.com/c/grasp-and-lift-eeg-detection/data 

Pre trained models codes
https://www.kaggle.com/banggiangle/cnn-eeg-pytorch/notebook 

PyTorch tutorials
Learn the Basics — PyTorch Tutorials 1.9.0+cu102 documentation 

Python Basics: https://github.com/wncc/learners-space
https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3
Book - AUTOMATE THE BORING STUFF WITH PYTHON.

EEG basics:  Fundamental_of_EEG_Measurement (1)
                     iMotions_EEG_Guide__2019 (2).pdf
                     
### MODULE 2
Turtlebot
https://emanual.robotis.com

Solidworks
ME119: Lecture 10 - Introduction to Solid Modelling.
ERC workshops: Solid works
CAD CAM tutorials : 
SolidWorks Tutorial 
Tried relaxing stuff like pliers , badminton cock , torsional spring etc. :P .

Ros beginner and intermediate level tutorials 

http://wiki.ros.org/ROS/Tutorials

 ROS Gazebo

Python through PYCK
Python through Coursera
Open Source Manipulator Simulations 












