from RobotArm import RobotArm


robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for i in range(1):
    robotArm.moveRight()
for i in range(3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if i < 3:
        robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()