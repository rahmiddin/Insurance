# TestCase-Fastapi
FastAPI приложение ⦁	Сервис должен посчитать стоимость страхования для запроса используя актуальный тариф.

# Развертывание
1.git clone https://github.com/rahmiddin/Insurance.git
2.docker-compose up --build
3.Перейти по адресу http://127.0.0.1:8000/docs


# Возможности
1.Добавлять тарифы на определенные материалы с помошью request JSON BODY или JSON файлом.
  Формат 
  
  
      {
        "data": {
          "2022-12-12": [
            {
              "cargo_type": "Glass",
              "rate": 0.123
            }
          ]
        }
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
  


    

