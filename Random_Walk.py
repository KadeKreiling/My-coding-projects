import random
import matplotlib.pyplot as plt

# Function to plot the random walk for each animal
def plot_walk(animal):
    xs, ys = zip(*animal['positions'])

    plt.figure(figsize=(10, 10))
    plt.scatter(xs, ys, color=animal['color'], edgecolor='k', alpha=0.7, s=100, marker=animal['marker'])
    plt.plot(xs, ys, lw=1.5, ls='--', color=animal['color'])
    plt.grid(True)
    plt.title(f'Path of Random Walk for {animal["name"]}')
    plt.xlabel('East-West')
    plt.ylabel('North-South')

    # Save the plot to a file
    plt.savefig(f'{animal["name"]}_random_walk.png', dpi=300)
    plt.close()  # Close the figure


def random_walk(steps, chosen_animal):
    x, y = 0, 0
    positions = []

    for i in range(steps):
        random_choice = random.randint(0, 100)
        if random_choice <= chosen_animal["probabilities"][0]:
            y += 1
        elif random_choice <= chosen_animal["probabilities"][1]:
            y -= 1
        elif random_choice <= chosen_animal["probabilities"][2]:
            x += 1
        else:
            x -= 1
        positions.append((x, y))

    return positions


def main():
    chuck_the_chicken = {
        "name": "chuck_the_chicken",
        "probabilities": [25, 50, 75, 100],
        "marker": "o",
        "color": "blue"
    }

    daisy_the_dog = {
        "name": "daisy_the_dog",
        "probabilities": [50, 66, 82, 100],
        "marker": "s",
        "color": "red"
    }

    chester_the_cat = {
        "name": "chester_the_cat",
        "probabilities": [0, 0, 50, 100],
        "marker": "^",
        "color": "green"
    }

    animals = [chuck_the_chicken, daisy_the_dog, chester_the_cat]

    for animal in animals:
        animal["positions"] = random_walk(1000, animal)
        plot_walk(animal)


if __name__ == "__main__":
    main()