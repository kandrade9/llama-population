def llama_population(start, end):
    """
    Calculates number of years until starting llama population reaches end llama population
    :param start: int initial llama population
    :param end: int desired llama population
    :return: int years
    """
    year = 0
    while start < end:
        born = start / 3
        passed = start / 4
        growth = born - passed
        start += growth
        year += 1
    return year

start_size = int(input("Start size: "))
while start_size < 1:
    start_size = int(input("Start size: "))

end_size = 0
while end_size < start_size:
    end_size = int(input("End size: "))

result = llama_population(start_size, end_size)
print(f"It will take {result} years for a llama population of {start_size} to reach {end_size}!")
