class LightSwitch:
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on
        self.switchIsOn = True

    def turnOff(self):
        # turn the swith off
        self.switchIsOn = False

    def show(self):  # added for testing
        print(self.switchIsOn)


# Main code
oLightSwitch = LightSwitch()  # create a LightSwhitch object

# Calls to methods
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
