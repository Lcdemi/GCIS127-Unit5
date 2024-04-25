def make_student(id, name):
    student_list = [id, name, 0, 0.0]
    return student_list

def add_student(population, id, name):
    # for element in range(len(population)):
    #     student = population[element]
    #     if student[0] == id:
    #         population.pop(element)
    #         break

    # new_student = make_student(id, name)
    # population.append(new_student)

    student = make_student(id, name)
    population[id] = student

def get_student(population, id):
    # for student in population:
    #     if student[0] == id:
    #         return student
    # return None

    if id in population:
        return population[id]
    else:
        return None

def add_credits(population, id, credits):
    student = get_student(population, id)
    if student is not None:
        student[2] += credits

def get_credits(population, id):
    student = get_student(population, id)
    if student is not None:
        return student[2]
    else:
        return None

def main():
    #population = []
    population = {}
    add_student(population, "GJB1234", "Greg James Boyd")
    add_student(population, "FB1234", "Fiona James Boyd")
    add_student(population, "JJB1234", "John James Boyd")
    add_student(population, "GJB1234", "Greg Jr. James Boyd")
    print(population)
    print(get_student(population, "GJB1234"))
    print(get_student(population, "XXX1234"))
    add_credits(population, "FB1234", 3)
    add_credits(population, "FB1234", 10)
    add_credits(population, "FB1234", 3)
    print(get_credits(population, "FB1234"))
    #Greg = make_student("GJB1234", "Greg")
    #print(Greg)
    #Fred = make_student("FDJ1234", "Fred")
    #print(Fred)


if __name__ == "__main__":
    main()