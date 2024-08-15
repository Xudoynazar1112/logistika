from django.shortcuts import render
from django.conf import settings
import requests
from .forms import OrderForm, fields_name


def send_telegram_message(text):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text, 'parse_mode': 'HTML'}
    response = requests.post(url, data=data)
    print(response)
    return response


def order(request):
    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form_data = form.save()
            msg_to_bot = f"New order:\n "
            for field, label in fields_name.items():
                value = getattr(form_data, field, None)
                if value:
                    msg_to_bot += f"<b>{label}</b>: <em>{value}</em>\n"
            send_telegram_message(msg_to_bot)
            return render(request, 'success.html', )
        else:
            print(form.errors)
    else:
        form = OrderForm()
    return render(request, 'form.html', {'form': form})
