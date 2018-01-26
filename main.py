

X0 = 37.5
Y0 = 10.0
Z_MAX = 24.0
STEP_Z = -0.2
STEP_Y = 0.5
DEPTH_Z = -6
MILL_SIZE_X = 225
MILL_SIZE_Y = 160
FEED_RATE = "F1000"


SAFE_Z = "Z" + str(float(Z_MAX))
MIN_X = "X" + str(float(X0))
MIN_Y = "Y" + str(float(Y0))
MAX_X = "X" + str(float(X0 + MILL_SIZE_X))
MAX_Y = "Y" + str(float(Y0 + MILL_SIZE_Y))
HEADER = "G21\r\nG90\r\nS15000\r\nG0 " + SAFE_Z + " " + FEED_RATE + "\r\nG0 X0.0000 Y0.0000\r\nM03\r\n"
TALE = "G0 " + SAFE_Z + "\r\nM5\r\nG0 " + SAFE_Z + "\r\nG0 X0.0000 Y0.0000"

file = open('STOL_3018.tap', 'w')

def frange_negative(start, stop, step) :
    x = start
    while True:
        if round(x, 1) < stop: return
        yield round(x, 1)
        x += step

def frange(start, stop, step) :
    x = start
    while True:
        if round(x, 1) >= stop: return
        yield round(x, 1)
        x += step


file.write(HEADER)
file.write("G1 " + SAFE_Z + " " + FEED_RATE + "\r\n")
file.write("G0 " + MIN_X + "\r\n")
file.write("G0 " + MIN_Y + "\r\n")
for z in frange_negative(0, DEPTH_Z, STEP_Z) :
    file.write("\r\nG1 Z" + str(float(z)) + "\r\n")
    for y in frange(Y0, Y0 + MILL_SIZE_Y, STEP_Y*2) :
        file.write("G1 Y" + str(round(y, 1)) + "\r\n")
        file.write("G1 " + MIN_X + "\r\n")
        y += 0.5;
        file.write("G1 Y" + str(round(y, 1)) + "\r\n")
        file.write("G1 " + MAX_X + "\r\n")
file.write(TALE)
file.close()

