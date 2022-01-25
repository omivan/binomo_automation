from economical_calendar_parser import get_quotes
import time


if __name__ == '__main__':
    time_before = time.time()
    while True:
        previous_quote, current_quote = get_quotes("Индикатор уверенности потребителей", "Consumer confidence")
        print(previous_quote, current_quote)
        if current_quote != False:
            time_after = time.time()
            print(f"Time: {round(time_after - time_before, 2)} ")
            break
