import matplotlib.pyplot as plt

def f(x: list[int], func) -> list[float]:
    result : list[float] = []
    for i in x:
        result.append(func(i))
    return result




def crossProduct(aVector: list[float], bVector : list[float]) -> list[float]:
    return [
        (aVector[1] * bVector[2]) - (aVector[2]*bVector[1]),
        -1 * (aVector[0]*bVector[2] - aVector[2]*bVector[0]),
        (aVector[0]*bVector[1] - aVector[1]*bVector[0])
        ]



def linspace(start: float, end: float, step: float) -> list[float]:
    stepSize : float = end/step
    tempCount: float = start
    result: list[float] = []
    result.append(start)
    for i in range(step):
        tempCount += stepSize
        result.append(tempCount)

    return result

def bisector(p: list[int], q: list[int]):
    x0 : float = (p[0] + q[0]) / 2
    y0 : float = (p[1] + q[1]) / 2

    a : float = q[0] - p[0]
    b : float = q[1] - p[1]
    c = -a*x0 - (b*y0)
    return lambda x: (-c - a*x)/b



xpoints = [1, 6]
ypoints = [5, 4]

minX, maxX = min(xpoints) - 1, max(xpoints)
minY, maxY = min(ypoints) - 1, max(ypoints)


graphX : list[float] = linspace(minX, maxX,10)
graphY : list[float] = linspace(minY, maxY,10)


graphBisector = bisector(
    [xpoints[0], ypoints[0]], 
    [xpoints[1], ypoints[1]])

allPoints : list[list[float]] = []
for idx, i in enumerate(xpoints):
    allPoints.append([i, ypoints[idx]])



while (len(allPoints) > 1):
    for i in range(1, len(allPoints)):
        graphBisector = bisector(allPoints[0], allPoints[i])
        yAxis = []
        for idx, i in enumerate(graphX):
            yAxis.append(graphBisector(i))
        plt.plot(graphX, yAxis)
    allPoints.pop(0)



plt.plot(xpoints, ypoints, 'o')
plt.show()