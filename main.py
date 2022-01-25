from economical_calendar_parser import get_quotes



if __name__ == '__main__':
    while True:
        previous_quote, current_quote = get_quotes("Индекс настроений в деловых кругах", "Business Climate")
        print(previous_quote, current_quote)
        if current_quote != False:
            break
