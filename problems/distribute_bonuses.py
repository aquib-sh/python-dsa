
def get_bonuses(performance):
    count = len(performance)
    bonuses = [1] * count

    for i in range(1, count-1):
        if performance[i-1] < performance[i]:
            bonuses[i] += 1

        if performance[i+1] < performance[i]:
            bonuses[i] += 1

    return bonuses


if __name__ == "__main__":
    employees = [1, 2, 3, 2, 3, 5, 1]
    print(get_bonuses(employees))

