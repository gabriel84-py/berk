from machine import Pin, PWM
import time

# =========================
# MOTEUR GAUCHE
# =========================
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
ENA = PWM(Pin(4))
ENA.freq(1000)

# =========================
# MOTEUR DROIT
# =========================
IN3 = Pin(6, Pin.OUT)
IN4 = Pin(7, Pin.OUT)
ENB = PWM(Pin(5))
ENB.freq(1000)

# =========================
# ENCODEURS
# =========================

# gauche
ENC_L_A = Pin(14, Pin.IN)
ENC_L_B = Pin(15, Pin.IN)

# droite
ENC_R_A = Pin(16, Pin.IN)
ENC_R_B = Pin(17, Pin.IN)

ticks_L = 0
ticks_R = 0

# =========================
# INTERRUPTIONS
# =========================

def callback_L(pin):
    global ticks_L
    if ENC_L_B.value():
        ticks_L += 1
    else:
        ticks_L -= 1

def callback_R(pin):
    global ticks_R
    if ENC_R_B.value():
        ticks_R += 1
    else:
        ticks_R -= 1

ENC_L_A.irq(trigger=Pin.IRQ_RISING, handler=callback_L)
ENC_R_A.irq(trigger=Pin.IRQ_RISING, handler=callback_R)

# =========================
# FONCTIONS MOTEURS
# =========================

def moteur_gauche(speed):
    if speed > 0:
        IN1.value(1)
        IN2.value(0)
    else:
        IN1.value(0)
        IN2.value(1)
    ENA.duty_u16(abs(speed))

def moteur_droit(speed):
    if speed > 0:
        IN3.value(1)
        IN4.value(0)
    else:
        IN3.value(0)
        IN4.value(1)
    ENB.duty_u16(abs(speed))

# =========================
# MOUVEMENTS
# =========================

def avancer(speed=30000):
    moteur_gauche(speed)
    moteur_droit(speed)

def reculer(speed=30000):
    moteur_gauche(-speed)
    moteur_droit(-speed)

def tourner_gauche(speed=30000):
    moteur_gauche(-speed)
    moteur_droit(speed)

def tourner_droite(speed=30000):
    moteur_gauche(speed)
    moteur_droit(-speed)

def stop():
    moteur_gauche(0)
    moteur_droit(0)

# =========================
# TEST
# =========================

print("Test robot 2 moteurs")

ticks_L = 0
ticks_R = 0

avancer(30000)
time.sleep(3)

stop()

print("Ticks gauche:", ticks_L)
print("Ticks droite:", ticks_R)