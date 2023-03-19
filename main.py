# python3
# Kristiāns Šneiders 11.grupa 221RDB042
def parallel_processing(n, m, data):
    output = []
    threads_time_list = []
    job_index = 0

    for i in range(n):
        if job_index < m:
            output.append([i, 0])
            threads_time_list.append(data[job_index])
            job_index += 1
        else:
            threads_time_list.append(0)

    current_time = 0
    while job_index < m or any(threads_time_list):
        min_time_left = min(time for time in threads_time_list if time > 0)
        current_time += min_time_left
        for i in range(n):
            if threads_time_list[i] > 0:
                threads_time_list[i] -= min_time_left
                if threads_time_list[i] == 0:
                    output.append([i, current_time])
                    if job_index < m:
                        threads_time_list[i] = data[job_index]
                        job_index += 1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split(" "))
    data = list(map(int, input().split()))
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i, j in result:
        print(i, j)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
