from src.insurance.models import Rate


class InsuranceDAO:
    """Class for work with Rate models in db"""

    model = Rate

    @classmethod
    async def add(cls, rate_dict):
        for date, info in rate_dict['data'].items():
            for item in info:
                await Rate.create(date=date,
                                  cargo_type=item['cargo_type'],
                                  rate=item['rate'])
        return rate_dict

    @classmethod
    async def find(cls, date, cargo_type):
        rate_query = await Rate.filter(date=date, cargo_type=cargo_type).values()
        if not rate_query:
            return None
        rate_list = list(rate_query)[-1]
        return rate_list
