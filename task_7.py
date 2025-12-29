import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}
    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sum_counts[dice_sum] += 1

    # Обрахування ймовірності випаду кожної суми
    probabilities = {sum_val: count / num_rolls for sum_val, count in sum_counts.items()}

    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')

    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob * 100:.2f}%", ha='center')

    plt.show()

def print_comparison_table(monte_carlo_probs, theoretical_probs):
    print(f"{'Сума':>4} | {'Monte-Carlo (%)':>15} | {'Аналітична (%)':>17} | {'Різниця (%)':>12}")
    print("-----|-----------------|-------------------|---------------")

    for sum in range(2, 13):
        mc = monte_carlo_probs[sum] * 100
        theo = theoretical_probs[sum] * 100
        diff = abs(mc - theo)

        print(f"{sum:>4} | {mc:>15.2f} | {theo:>17.2f} | {diff:>12.2f}")


if __name__ == "__main__":

    theoretical_probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36
    }

    for accuracy in [100, 1000, 10000, 100000]:
        # Симуляція кидків і обчислення ймовірностей
        mc_probabilities = simulate_dice_rolls(accuracy)

        # Відображення ймовірностей на графіку
        plot_probabilities(mc_probabilities)

        print("\nПорівняльна таблиця (Monte-Carlo vs Аналітика):\n")
        print_comparison_table(mc_probabilities, theoretical_probabilities)