# TestCase-Fastapi
FastAPI приложение ⦁	Сервис должен посчитать стоимость страхования для запроса используя актуальный тариф.

# Возможности
1.Добавлять тарифы на определенные материалы с помошью request JSON BODY или JSON файлом.
  Формат 
  
    {   "2023-06-12": [
          {
            "cargo_type": "Glass",
            "rate": "0.01"
          }
        ],
          "2023-07-1": [
          {
            "cargo_type": "Iron",
            "rate": "0.12"
          }
        ]
    }

2.Отправлять query(price, cargo_type, date) и получать  стоимость страхования (price * rate). Rate выбирается из бд с помошью фильтрации исходя из параметров date и cargo_type

# Роуты

      /add/                            Добавлять тарифы с помошью request query
      /add/by_file                     Добавлять тарифы с помошью JSON FILE
      /calculate_insurance            Посчитать стоимость страхования 

# Библиотеки 

  FastAPI
  TortoiseORM
  asyncpg
  


    
