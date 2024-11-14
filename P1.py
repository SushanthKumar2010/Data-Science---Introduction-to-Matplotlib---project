import matplotlib.pyplot as plt

january_sales = [200, 180, 190, 210, 220, 250, 240]
february_sales = [220, 210, 200, 230, 240, 260, 250]
days = [1, 2, 3, 4, 5, 6, 7]

# Line Chart
def line_chart():
    plt.plot(days, january_sales, marker='o', color='blue', label="January Sales")
    plt.title("January Month Sales (Line Chart)")
    plt.xlabel("Day")
    plt.ylabel("No. of Sales")
    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()

# Scatter Chart
def scatter_chart():
    plt.scatter(days, february_sales, color='g', label="January Sales", s=100)
    plt.title("January Month Sales (Scatter Chart)")
    plt.xlabel("Day")
    plt.ylabel("No. of Sales")
    plt.legend()
    plt.show()

line_chart()
scatter_chart()
