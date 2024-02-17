import sys

intial_population = float(sys.argv[1])
growth_rate = float(sys.argv[2])
number_of_iterations = int(sys.argv[3])
output_file = sys.argv[4]

def logistics_equation(x, r, times, destination):
    x_list = []
    for i in range(times):
        x_list.append(x)
        new_pop = r * x * (1 - x)
        x = new_pop
    step = 1
    for pop in x_list:
        with open(destination, "a") as file:
            file.write(f"{step}. {pop:.3f}\n")
        step += 1


if 4 > growth_rate > 2 and 1 > intial_population > 0:
    logistics_equation(intial_population, growth_rate, number_of_iterations, output_file)
else:
    print("You're growth rate or intial population is either to big or small.")


