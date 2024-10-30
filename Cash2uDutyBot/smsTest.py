from datetime import datetime

duty_today = "Арсен\nДанияр"
today_date = datetime.today().strftime('%Y-%m-%d')
message = f"{today_date}\nНапоминание! \nСегодня дежурные: \n{duty_today} \n \nЗадача: Собрать мусор по всему офису, в том числе и на крыльце офиса. Навести порядок на кухне."
print(message)
