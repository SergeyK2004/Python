count = int(input("Введите количество секунд:"))
seconds = count % 60
count = count // 60
minutes = count % 60
hours = count // 60
print(f"Указанное время: {hours:02d}:{minutes:02d}:{seconds:02d}")