#!/bin/sh
# A command whose running time jumps about: a random sleep between
# 40 ms and 290 ms on every run, like a service having good and bad
# moments.
exec python3 -c 'import random, time; time.sleep(random.uniform(0.04, 0.29))'
