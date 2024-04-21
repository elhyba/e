from mody import Mody
import telebot #مكتبة 
from PIL import Image #مكتبة

private = Mody.ELHYBA
bot = telebot.TeleBot(private)
is_bot_active = True #التشغيل 

bot.set_my_commands([telebot.types.BotCommand("/start", "بدء البوت 💛")]) #اوامر البوت

@bot.message_handler(commands=['start'])
def start(message):
        bot.reply_to(message, "• 👋 مرحبا بك عزيزي في بوت تحويل الصور وتعديلها الى لون الابيض والاسود ارسل الصورة الان للتعديل 〈 💛 〉 ") #رساله الترحيب

@bot.message_handler(content_types=["photo"])
def convert_to_black_and_white(message):

    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)
    with open("image.jpg", "wb") as image:
        image.write(downloaded_file)
    img = Image.open("image.jpg").convert('L')
    img.save("privatephoto.jpg")
    
    with open("privatephoto.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo)
  
admin = "Your ID"#ايديك

@bot.message_handler(func=lambda message: True)
def forward_message_to_admin(message):
    
    bot.forward_message(admin, message.chat.id, message.message_id)  
  
print("\033[2;32m running") #طباعة التشغيل         
bot.polling(none_stop=True)
