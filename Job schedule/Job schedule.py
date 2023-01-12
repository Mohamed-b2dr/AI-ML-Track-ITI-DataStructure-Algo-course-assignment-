def sortjobschedule(array):
    return sorted(array, key = lambda x : x[2], reverse = True)

def jobschedule(array, t):
    jobs = [-1 for i in range(t)]
    for j in range(len(array)):
        for i in range(min(t - 1, array[j][1] - 1), -1, -1):
            if jobs[i] == -1:
                jobs[i] = array[i][0]
    return jobs


if __name__ == '__main__':
    array = [['a', 7, 202],
             ['b', 5, 29],
             ['c', 6, 84],
             ['d', 1, 75],
             ['e', 2, 43]]

    arr = sortjobschedule(array)
    jobs = jobschedule(arr, 3)
    print('jobs = ', jobs)