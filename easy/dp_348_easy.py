def rabbit_infestations(males_given, females_given, target_pop,
                        rabbit_lifespan=96, male_offspring=5,
                        female_offspring=9, fertile_age=5):
    "Calculates the time in months before we all doomed."
    # pop_by_age list of month in form
    # [..., [males_of_that_age, females_of_that_age], ...]
    pop_by_age = []
    for i in range(rabbit_lifespan):
        pop_by_age.append([0, 0])
    # given rabbits start at 2 months old
    pop_by_age[2][0] = males_given
    pop_by_age[2][1] = females_given

    current_pop = sum(pop_by_age[2])
    fertile_pop = pop_by_age[fertile_age][1]
    current_month = 0

    while current_pop < target_pop:
        # raddits died
        died_this_month = pop_by_age[-1]
        del pop_by_age[-1]
        # rabbits born
        fertile_pop += pop_by_age[fertile_age-1][1]- died_this_month[1]
        males_born = fertile_pop*male_offspring
        females_born = fertile_pop*female_offspring
        born_this_month = [males_born, females_born]
        pop_by_age.insert(0, born_this_month)

        current_pop += sum(born_this_month) - sum(died_this_month)
        current_month += 1

    return current_month

if __name__ == '__main__':
    print("should be 32: ", rabbit_infestations(2, 4, 1000000000))
    print("should be 36: ", rabbit_infestations(2, 4, 15000000000))
