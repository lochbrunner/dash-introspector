#!/usr/bin/env python3

import pickle
from trace import TraceStep
from random import choices

if __name__ == '__main__':

    names = ['vision_sensor', 'radar_sensor', 'fusion',
             'planing', 'validator', 'wheel_actuator', 'steering_actuator']

    trace = [TraceStep(name, f'This is {name} in seq {seq}', seq) for
             name in choices(names, k=5) for seq in range(30)]

    pickle.dump(trace, open('trace.pick', 'wb'))
