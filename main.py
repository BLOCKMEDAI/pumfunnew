
import requests
import time
import telegram

# Configurações do bot
TELEGRAM_TOKEN = "7886005192:AAExBYx3YaXsXH4I71rePSdGThS7asmO93s"
CHAT_ID = "855971772"
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Armazenar os tokens já enviados
enviados = set()

def buscar_tokens():
    url = "https://pump.fun/api/tokens"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            tokens = resposta.json()
            for token in tokens:
                token_id = token.get("id")
                name = token.get("name")
                contract_address = token.get("address")
                twitter = token.get("twitter")
                telegram_link = token.get("telegram")

                if token_id not in enviados and twitter and telegram_link:
                    mensagem = f"🚀 Novo token no Pump.fun

"
                    mensagem += f"📛 Nome: {name}
"
                    mensagem += f"📜 Endereço: {contract_address}
"
                    mensagem += f"🐦 Twitter: {twitter}
"
                    mensagem += f"📢 Telegram: {telegram_link}"

                    bot.send_message(chat_id=CHAT_ID, text=mensagem)
                    enviados.add(token_id)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    while True:
        buscar_tokens()
        time.sleep(30)
