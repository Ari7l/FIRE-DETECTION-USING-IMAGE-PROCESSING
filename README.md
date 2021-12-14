# FIRE-DETECTION-USING-IMAGE-PROCESSING
With this project we overcame the limitations of traditional fire detection techniques by making use of already available resources
We used Python's Open CV library to detect the fire as well as humans. We used Harr Cascade Classifier to train our algorithm to successfully classify the
between fire and non-fire images. 
Follow link to see it in action!!
https://user-images.githubusercontent.com/65645372/145769911-286cc430-9d92-40a6-a706-56cb713b0eef.mp4

Working:
The First thing that the program will do is keep a check on the smoke detection. In
case smoke is detected it will raise an alarm so that fire may be extinguished by manual means
like fire extinguisher. If despite this a fire breaks out then the system will first determine the
exact location of the fire. In our model, we are showcasing two room monitoring so the
system will determine whether fire is in room 1 or room 2 or both. If fire is detected in room
1, the letter 'p' and for room 2 the letter 's' will be sent to arduino through serial
communication.
Once the arduino receives the signal, it will check the signal to determine which letter it has
received. For 'p' character, relay 1 will be operated and similarly for 's' character, relay 2 will
be operated. In case both letters are received, both relays will be operated.
