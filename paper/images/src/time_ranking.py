import numpy as np
import matplotlib.pyplot as plt

time_passed = range(72)

def score(v, t, g=1.8):
    return (v - 1) / (t + 2)**g

v = 10
g = 1.8
scores = [score(v, ti, g) for ti in time_passed]
plt.plot(time_passed, scores, label="$v_i$={}, $G$={},".format(v, g))

v = 100
g = 1.8
scores = [score(v, ti, g) for ti in time_passed]
plt.plot(time_passed, scores, label="$v_i$={}, $G$={},".format(v, g))

v = 1000
g = 1.8
scores = [score(v, ti, g) for ti in time_passed]
plt.plot(time_passed, scores, label="$v_i$={}, $G$={},".format(v, g))

plt.ylim(0, 3)
plt.xlim(0, 71)

plt.xlabel("hours since creation")
plt.ylabel("score")

plt.legend(loc="upper right")
plt.savefig("../time_ranking_1.png")
# plt.show()


plt.clf()


v = 100
g = 1.5
scores = [score(v, ti, g) for ti in time_passed]
plt.plot(time_passed, scores, label="$v_i$={}, $G$={},".format(v, g))

v = 100
g = 1.8
scores = [score(v, ti, g) for ti in time_passed]
plt.plot(time_passed, scores, label="$v_i$={}, $G$={},".format(v, g))

v = 100
g = 2.1
scores = [score(v, ti, g) for ti in time_passed]
plt.plot(time_passed, scores, label="$v_i$={}, $G$={},".format(v, g))

plt.ylim(0, 3)
plt.xlim(0, 71)

plt.xlabel("hours since creation")
plt.ylabel("score")

plt.legend(loc="upper right")
plt.savefig("../time_ranking_2.png")
# plt.show()
