months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    # CASO 1: Formato M/D/YYYY (es. 9/8/1636)
    try:
        month, day, year = date.split('/')
        month = int(month)
        day = int(day)
        year = int(year)

        # Verifica che mese e giorno siano validi
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
    except ValueError:
        pass

    # CASO 2: Formato "Month Day, Year" (es. September 8, 1636)
    try:
        # Se c'è la virgola dopo il giorno (obbligatoria per questo formato)
        if "," in date:
            month_str, day_str, year_str = date.split()
            day = int(day_str.replace(",", ""))
            year = int(year_str)

            # Cerca il mese nella lista (gli indici vanno da 0 a 11, quindi aggiungiamo 1)
            month_str = month_str.capitalize()
            if month_str in months:
                month = months.index(month_str) + 1

                if 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
    except ValueError:
        pass