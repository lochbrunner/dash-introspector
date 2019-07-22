#!/usr/bin/env python3

import pickle
from trace import TraceStep

if __name__ == '__main__':
    trace = [TraceStep(f'step {i}', f'This is the {i}.th step')
             for i in range(20)]

    pickle.dump(trace, open('trace.pick', 'wb'))
