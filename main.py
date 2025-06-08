from navigate import create_booking
import threading

def main():
    num_iterations = 3
    day_of_month='17'
    num_of_guests=2

    threads = []
    for x in range(num_iterations):
        thread = threading.Thread(target=create_booking, args=(day_of_month, num_of_guests))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()