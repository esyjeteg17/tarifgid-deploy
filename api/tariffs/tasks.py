import aiohttp
import asyncio
from bs4 import BeautifulSoup
from celery import shared_task
from django.db.models import Q
from asgiref.sync import sync_to_async
from .models import Tariff
import ssl
import async_timeout

@shared_task
def scrape_operator_data():
    urls = [
        ('https://moscow.megafon.ru/tariffs/all/', 'Мегафон', 'megafon'),
        ('https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile', 'МТС', 'mts'),
        ('https://msk.tele2.ru/tariffs', 'Теле2', 'tele2'),
    ]

    def extract_int(text):
        return int(''.join(filter(str.isdigit, text))) if text else 0

    async def fetch(session, url, retries=3):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": url
        }
        for attempt in range(retries):
            try:
                async with async_timeout.timeout(60):
                    async with session.get(url, headers=headers, ssl=False) as response:
                        return await response.text()
            except (aiohttp.ClientConnectorError, asyncio.TimeoutError) as e:
                if attempt < retries - 1:
                    continue  # Retry
                else:
                    raise e

    async def parse_page(url, head, operator):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
            html = await fetch(session, url)
            soup = BeautifulSoup(html, 'html.parser')

            if operator == 'megafon':
                tariffs = soup.find_all('div', {'class': 'tariffs-card-v4'})
            elif operator == 'mts':
                tariffs = soup.find_all('div', {'class': 'card'})
            elif operator == 'tele2':
                tariffs = soup.find_all('div', {'class': 'tariff-card'})
                
            print(f"Found {len(tariffs)} tariffs for {operator}")  # Logging number of tariffs found

            if not tariffs:
                print(f"No tariffs found for {operator}")
                # Логируем весь HTML контент страницы для анализа
                print(f"HTML content for {operator}:\n{soup.prettify()[:5000]}")  # Ограничиваем вывод до 5000 символов
                return

            for tariff in tariffs:
                if operator == 'megafon':
                    title_tag = tariff.find('div', {'class': 'tariffs-card-header-v4__title'})
                    price_tag = tariff.find('div', {'class': 'tariffs-card-buy-v4__price'})
                    additional_params = tariff.find_all('div', {'class': 'tariffs-card-additional-params-v4__value'})
                elif operator == 'mts':
                    title_tag = tariff.find('div', {'class': 'card-title'})
                    price_tag = tariff.find('span', {'class': 'price-text'})
                    additional_params = tariff.find_all('span', {'class': 'feature-description'})
                elif operator == 'tele2':
                    title_tag = tariff.find('a', {'class': 'tariff-card__title-link'})
                    price_tag = tariff.find('span', {'class': 'tariff-abonent-fee__current-price-value'})
                    additional_params = tariff.find_all('span', {'class': 'tariff-card-parameter__value'})

                title = title_tag.text.strip() if title_tag else 'N/A'
                price_text = price_tag.text.strip(' ₽') if price_tag else '0'
                price = extract_int(price_text)

                minutes = 0
                gigabytes = 0
                sms = 0

                for param in additional_params:
                    if 'минут' in param.text:
                        if param.find('svg'):
                            minutes = 99999
                        else:
                            minutes = extract_int(param.text)
                    elif 'ГБ' in param.text:
                        if param.find('svg'):
                            gigabytes = 99999
                        else:
                            gigabytes = extract_int(param.text)
                    elif 'SMS' in param.text:
                        if param.find('svg'):
                            sms = 99999
                        else:
                            sms = extract_int(param.text)

                # Logging data before adding
                print(f"Title: {title}, Price: {price}, Minutes: {minutes}, Gigabytes: {gigabytes}, SMS: {sms}, Operator: {operator}")

                # Check for the presence of the tariff in the database before adding
                existing_tariff = await sync_to_async(Tariff.objects.filter)(
                    Q(name=title) &
                    Q(operator=operator)
                )

                existing_tariff = await sync_to_async(existing_tariff.first)()

                if existing_tariff:
                    # Update the existing tariff if there are changes
                    updated = False
                    if existing_tariff.price != price:
                        existing_tariff.price = price
                        updated = True
                    if existing_tariff.minutes != minutes or existing_tariff.minutes != 99999:
                        existing_tariff.minutes = minutes
                        updated = True
                    if existing_tariff.gigabytes != gigabytes or existing_tariff.gigabytes != 99999:
                        existing_tariff.gigabytes = gigabytes
                        updated = True
                    if existing_tariff.sms != sms or existing_tariff.sms != 99999:
                        existing_tariff.sms = sms
                        updated = True

                    if updated:
                        await sync_to_async(existing_tariff.save)()
                        print(f"Tariff {title} from {operator} updated successfully.")
                    else:
                        print(f"Tariff {title} from {operator} has no changes.")
                else:
                    await sync_to_async(Tariff.objects.create)(
                        name=title,
                        price=price,
                        minutes=minutes,
                        gigabytes=gigabytes,
                        sms=sms,
                        operator=operator,
                        head=head
                    )
                    print(f"Tariff {title} from {operator} saved successfully.")

    async def main():
        tasks = [parse_page(url, head, operator) for url, head, operator in urls]
        await asyncio.gather(*tasks)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

    print("All data scraped and saved successfully.")