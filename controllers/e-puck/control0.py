from controller import Robot

robot = Robot()

timestep = 64
vel_max = 6.2
teclado = robot.getKeyboard()
teclado.enable(timestep)

# Obtener motores
izq_motor = robot.getDevice('r_motor1')
der_motor = robot.getDevice('r_motor2')
inicio_giro = 0
tiempo_giro = 2

# Configurar modo de velocidad continua
izq_motor.setPosition(float('inf'))
der_motor.setPosition(float('inf'))

# Inicializar velocidades
izq_motor.setVelocity(0.0)
der_motor.setVelocity(0.0)

# Bucle principal
while robot.step(timestep) != -1:
    
    der_velocidad = 0.5 * vel_max
    izq_velocidad = 0.5 * vel_max
    key = teclado.getKey()

    if key == teclado.UP:
        izq_motor.setVelocity(izq_velocidad)
        der_motor.setVelocity(der_velocidad)
        
    elif key == teclado.DOWN:
        izq_motor.setVelocity(-1*izq_velocidad)
        der_motor.setVelocity(-1*der_velocidad)
    
    elif key == teclado.LEFT:
        inicio_giro = robot.getTime()
        if robot.getTime() - inicio_giro < tiempo_giro:
            izq_motor.setVelocity(-1*izq_velocidad)
            der_motor.setVelocity(1*der_velocidad)
            
    elif key == teclado.RIGHT:
        inicio_giro = robot.getTime()
        if robot.getTime() - inicio_giro < tiempo_giro:
            izq_motor.setVelocity(1*izq_velocidad)
            der_motor.setVelocity(-1*der_velocidad)
    else:
        izq_motor.setVelocity(0.0)
        der_motor.setVelocity(0.0)

