def poisonedDuration(timeSeries, duration):
    timeDuration = duration
    for i in range(len(timeSeries)-1):
        if (timeSeries[i]+duration-1) >= timeSeries[i+1]:
            overlap = abs(timeSeries[i]+duration - timeSeries[i+1])
            timeDuration += duration - overlap
        else:
            timeDuration += duration
    
    return timeDuration

print(poisonedDuration(timeSeries = [1,2], duration = 2))