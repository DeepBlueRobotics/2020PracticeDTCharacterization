{
    # Class names of motor controllers used.
    # Options:
    # 'Spark'
    # 'Victor'
    # 'VictorSP'
    # 'PWMTalonSRX'
    # 'PWMVictorSPX'
    # 'WPI_TalonSRX'
    # 'WPI_VictorSPX'
    "rightControllerTypes": ["WPI_TalonSRX", "WPI_VictorSPX", "WPI_TalonSRX"],
    "leftControllerTypes": ["WPI_TalonSRX", "WPI_VictorSPX", "WPI_VictorSPX"],
    # Ports for the left-side motors
    "leftMotorPorts": [1, 2, 3],
    # Ports for the right-side motors
    "rightMotorPorts": [4, 5, 6],
    # Inversions for the left-side motors
    "leftMotorsInverted": [False, False, False],
    # Inversions for the right side motors
    "rightMotorsInverted": [True, True, True],
    # Wheel diameter (in units of your choice - will dictate units of analysis)
    "wheelDiameter": 5,
    #(in inches)
    # If your robot has only one encoder, remove all of the right encoder fields
    # Encoder pulses-per-revolution (*NOT* cycles per revolution!)
    # This value should be the pulses per revolution *of the wheels*, and so
    # should take into account gearing between the encoder and the wheels
    "encoderPPR": 256,
    # Ports for the left-side encoder
    "leftEncoderPorts": [2, 3],
    # Ports for the right-side encoder
    "rightEncoderPorts": [0, 1],
    # Whether the left encoder is inverted
    "leftEncoderInverted": False,
    # Whether the right encoder is inverted:
    "rightEncoderInverted": True,
    # Your gyro type (one of "NavX", "Pigeon", "ADXRS450", "AnalogGyro", or "None")
    "gyroType": "NavX",
    # Whatever you put into the constructor of your gyro
    # Could be:
    # "SPI.Port.kMXP" (MXP SPI port for NavX or ADXRS450),
    # "I2C.Port.kOnboard" (Onboard I2C port for NavX)
    # "0" (Pigeon CAN ID or AnalogGyro channel),
    # "new WPI_TalonSRX(3)" (Pigeon on a Talon SRX),
    # "" (NavX using default SPI, ADXRS450 using onboard CS0, or no gyro)
    "gyroPort": "",
}

