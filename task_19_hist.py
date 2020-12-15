
import random
import statistics
import concurrent.futures
import matplotlib.pyplot as plt



class Histogram:

    
    def hist_calc(self):
        amounts = []
        numbers = []
        for i in range(0, 1000):
            numbers.append(random.randint(0, 1000))
        for i in range(0, 1000, 25):
            amounts.append(int(statistics.mean(numbers[i:i + 24])))
        return amounts



    def run(self):

        with concurrent.futures.ThreadPoolExecutor(2) as thread:
            am = thread.submit(self.hist_calc)

        amount = am.result()

        plt.hist(amount, bins=40)
        plt.show()


def main():
    hist = Histogram()
    hist.run()

if __name__ == "__main__":
    main()

