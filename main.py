# pip install -r req.txt
from telebot.types import BotCommand
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytube import YouTube
from rembg import remove
from PIL import Image
from gtts import gTTS
from googletrans import Translator
from datetime import datetime
from googlesearch import search
from io import BytesIO
from telebot import types
import qrcode
import numpy as np
import cv2
import speedtest
import moviepy.editor
import threading
import time
import telebot
import os
import math
TOKEN = "7113724596:AAE4yYczuklB_raJ2pi4vObn7BzCUpO9YwE"
bot = telebot.TeleBot(TOKEN)
user_data = {}
print('-'*50)
print("SAZOM v1.9")
print('-'*19)
#-----------------------------------------------------------folders
bot.set_my_commands([BotCommand("start","لإعادة تشغيل البوت")])
DOWNLOADS = "./downloads/"
if os.path.exists(DOWNLOADS):
    print("alredy - [downloads]")
    pass
else:
    os.makedirs("downloads")
    print("creat folder - [downloads]")
TEMP = "./temp/"
if os.path.exists(TEMP):
    print("alredy - [temp]")
    pass
else:
    os.makedirs("temp")
    print("creat folder - [temp]")
PROCESSED = "./processed/"
if os.path.exists(PROCESSED):
    print("alredy - [processed]")
    pass
else:
    os.makedirs("processed")
    print("creat folder - [processed]")
SPEECH = "./speech/"
if os.path.exists(SPEECH):
    print("alredy - [processed]")
    pass
else:
    os.makedirs("speech")
    print("creat folder - [speech]")
CONVERT = "./convert/"
if os.path.exists(CONVERT):
    print("alredy - [convert]")
    pass
else:
    os.makedirs("convert")
    print("creat folder - [convert]")
LOCATION = "./location/"
if os.path.exists(LOCATION):
    print("alredy - [location]")
    pass
else:
    os.makedirs("location")
    print("creat folder - [location]")
STICKER = "./sticker/"
if os.path.exists(STICKER):
    print("alredy - [sticker]")
    pass
else:
    os.makedirs("sticker")
    print("creat folder - [sticker]")
TRANSLATE = "./translate/"
if os.path.exists(TRANSLATE):
    print("alredy - [translate]")
    pass
else:
    os.makedirs("translate")
    print("creat folder - [translate]")
SEARCH = "./search/"
if os.path.exists(SEARCH):
    print("alredy - [search]")
    pass
else:
    os.makedirs("search")
    print("creat folder - [search]")
QR = "./qr/"
if os.path.exists(QR):
    print("alredy - [qr]")
    pass
else:
    os.makedirs("qr")
    print("creat folder - [qr]")
#---------------------------------------------------------------
try:
    ADMIN_ID = 6020331913
    SEC_ADMIN_ID = 6880967426
    SEC_ADMIN_NAME = "واصل"
    ADMIN_NAME = "Alaa Safi"
    INTERVAL_MINUTES = 5
    homework_file = "home work.txt"
    keep_sending = True
    qr_types = {
        "WiFi": ["Enter SSID:", "Enter Password:", "Enter Security (WPA/WEP):"],
        "URL": ["Enter URL:"],
        "Text": ["Enter Text:"],
        "Email": ["Enter Email:"],
        "Phone": ["Enter Phone Number:"],
        "SMS": ["Enter Phone Number:", "Enter Message:"],
        "Geo": ["Enter Latitude:", "Enter Longitude:"],
        "YouTube": ["Enter YouTube URL:"],
        "Instagram": ["Enter Instagram Username:"],
        # يمكنك إضافة بقية الأنواع هنا بنفس الطريقة
}
    def send_periodic_message():
        while keep_sending:
            time.sleep(INTERVAL_MINUTES * 60)
            try:
                bot.send_message(ADMIN_ID, "البوت شغال بشكل جيد✅")
            except Exception as e:
                print(f"حدث خطأ عند إرسال الرسالة: {e}")
    @bot.message_handler(commands=['start_check'])
    def start(message):
        if message.from_user.id == ADMIN_ID:
            bot.send_message(ADMIN_ID, f"مرحبا سيدي, سيتم ارسال رسائل للتأكد من البوت يعمل كل {INTERVAL_MINUTES} ✅")
            threading.Thread(target=send_periodic_message).start()
        else:
            bot.send_message(message.chat.id, "هذه الوظيفة مخصصة للأدمن فقط.")
    @bot.message_handler(commands=['stop'])
    def stop(message):
        global keep_sending
        if message.from_user.id == ADMIN_ID:
            keep_sending = False
            bot.send_message(ADMIN_ID, "تم إيقاف رسائل التحقق الدورية ✔️.")
        else:
            bot.send_message(message.chat.id, "هذه الوظيفة مخصصة للأدمن فقط.")

    def check_user_id(user_id):
        with open("users.txt", "r") as file:
            users = file.readlines()
        if f"{user_id}\n" in users:
            return True
        return False

    def register_user(user_id):
        if not check_user_id(user_id):
            with open("users.txt", "a") as file:
                file.write(f"{user_id}\n")
                bot.send_message(ADMIN_ID,f"🏆 New User 🏆")
    @bot.message_handler(commands=["id"])
    def id(message):
        bot.send_message(message.chat.id,f"`{message.from_user.id}`",parse_mode="MarkdownV2")
        bot.send_message(message.chat.id,f"`{message.from_user.first_name}`",parse_mode="MarkdownV2")
        bot.send_message(message.chat.id,f"`{message.from_user.username}`",parse_mode="MarkdownV2")
    @bot.message_handler(commands=["start"])
    def start(message):
        user_id = message.from_user.id
        register_user(user_id)
        if user_id == ADMIN_ID:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("إرسال رسالة لجميع المستخدمين", callback_data="send_to_all"))
            markup.add(InlineKeyboardButton("إلغاء",callback_data="cancell"))
            bot.send_message(message.chat.id, "مرحبا بك، لقد تم التعرف عليك كمدير. يمكنك استخدام الأزرار أدناه.", reply_markup=markup)
        else:
            bot.send_message(message.chat.id,f"""SAZOM Company
        ____________________________
        مرحبا ({message.from_user.first_name})
        هذا هو بوت شركة SAZOM الرسمي هناك الكثير من الخدمات المجانية والتي ستجدها عن الآخرين بالدفع الإلكتروني.
    حسنا:
    1) ما هي شركة SAZOM ؟
    في الواقع SAZOM هي شركة برمجية ظهرت في الفترة الأخيرة لها الكثير من الخدمات البرمجية التي تتيح للمستخدم سهولة العمل بكافة الخدمات المجانية المتاحة لدى هذه الشركة.
    2) ما الخدمات التي تقدمها الشركة بشكل مختصر؟
    1️⃣ download وهي تعني تنزيل أي فيديو من اليوتيوب حصرا بأعلى دقة ممكنة
    2️⃣ remove وهي تعني حذف خلفية أي صورة بالذكاء الإصطناعي يعني: اذا كانت لديك صورة وورائك خلفية لا تريدها فقط ارسلها للبوت وهو سيقوم بحذف هذه الخلفية لك.
    3️⃣ speech وهي تعني تحويل أي نص تكتبه الى كلام باللغة العربية مع مراعاة التشكيل, مثلا: مازنٌ يمشي في الحديقةِ.
    4️⃣ convert وهي تعني تحويل الفيديو الى موسيقى, أي: أنا لدي فيديو وأريد تحويله الى موسيقى كل ما عليك فعله فقط إرسال هذا الفيديو الى بوت وهو سيقوم بتحويله
    5️⃣ location هي خدمة جديدة وقوية ولكن هي قيد التطوير فكرتها ببساطة أنها تستطيع من خلال الرقم الذي ترسله لها معرفة اسم الدولة مثلا: +963 ستعرف مباشرة أنها لدولة سوريا وتعرف أيضا اسم الشركة الصانعة مثلا: 51****** هذه لشركة MTN ومن خلال هذه المعلومات تأخذ إحداثيات هذا الرقم وعندها ترسل ملف بلاحقة HTML لتعرف مكان صاحب هذا الرقم. ولكن للأسف الشديد هذه الخدمة قيد التطوير وسيتم تشغيلها قريبا
    6️⃣ speed وهي تعني Speed Test Internet يعني قياس سرعة الانترنت لديك.
    7️⃣ sticker وهي تعني تحويل صورة ترسلها للبوت الى ملصق.
    8️⃣ trans وهي تعني ترجمة أي نص إلى اللغة العربية
    9️⃣ search وهي تعني بحث عن أي شيء في محرك البحث جوجل بمجرب ما إن تبحث عن أي شيء سيظهر لك رابط به الشيء الذي بحثت عنه

    ملاحظة:📝 كل هذه الخدمات تحافظ على خصوصية المستخدم بمجرد ما إن تنتهي ال function من العمل تحذف كل الوسائط والرسائل التي حفظت بالبوت من أجل الاستخدام والمعالجة.
    ملاحظة2: 📝 البوت في حالة تطوير دائمة لذلك يتوقف لمدة لا تتجاوز ال 8 ساعات للتطوير ولا تقلق سيتم إعلام المستخدمين بالوقت الذي سيتم إطفاء البوت فيه.
    عموما: أرجو الاستفادة من هذا البوت ونشره لأكبر قدر من المستخدمين على الأقل لأصدقائك ❤️‍🩹💯
    إذا أردت التواصل مع المبرمجين 📨📩:
    Alaa Safi علاء صافي 
    @AlaaSafiProgrammer218 
    +96395144936
    ___________________________________

    Zaid Makhzoom  زيد مخزوم
    @Zaidmakhzoom
    +963 992 883 477""")
        home(message)
    @bot.callback_query_handler(func=lambda call: call.data == "send_to_all")
    def prompt_for_message(call):
        if call.from_user.id == ADMIN_ID:
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = ReplyKeyboardMarkup()
            markup.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(call.message.chat.id, "يرجى كتابة الرسالة التي تريد إرسالها لجميع المستخدمين.",reply_markup=markup)
            bot.register_next_step_handler(call.message, broadcast_message)
        else:
            bot.send_message(call.message.chat.id, "عذرا، لا يمكنك استخدام هذا الزر.")
    @bot.callback_query_handler(func=lambda call: call.data == "cancell")
    def cancel_admin(call):
        if  call.from_user.id == ADMIN_ID:
            bot.delete_message(call.message.chat.id,call.message.message_id)
            bot.send_message(call.message.chat.id,"تمت إلغاء العملية بنجاح.")
            home(call.message)
        else:
            bot.send_message(call.message.chat.id, "عذرا، لا يمكنك استخدام هذا الزر.")
    def broadcast_message(message):
        if message.text == 'إلغاء ❌':
            bot.send_message(message.chat.id,"تمت إلغاء العملية بنجاح.")
            home(message)
        elif message.from_user.id == ADMIN_ID:
            with open("users.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    bot.send_message(user.strip(), message.text)
            bot.send_message(message.chat.id, "تم إرسال الرسالة لجميع المستخدمين.")
        else:
            bot.send_message(message.chat.id, "عذرا، لا يمكنك إرسال الرسالة.")
    #---------------------------------------------------buttons
        markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        markup.add(KeyboardButton("تنزيل فيديوهات 📥"))
        markup.add(KeyboardButton("حذف الخلفية 📷"))
        markup.add(KeyboardButton("رموز  QR 🈺"))
        markup.add(KeyboardButton("تحويل النص إلى كلام 🔀"))
        markup.add(KeyboardButton("تحويل أي فيدو إلى موسيقى 🔁"))
        markup.add(KeyboardButton("معرفة الموقع من الرقم 📲"))
        markup.add(KeyboardButton("معرفة سرعة الإنترنت 🌐"))
        markup.add(KeyboardButton("تحويل الصورة إلى ملصق 🖼"))
        markup.add(KeyboardButton("ترجمة النصوص من أي لغة إلى العربية 🔠"))
        markup.add(KeyboardButton("البحث عن اي يخطر في بالك في غوغل 🔍"))
        markup.add(KeyboardButton("استعلام الوظائف 📋"))
        b1 = KeyboardButton("التواصل مع الدعم 📞")
        b2 = KeyboardButton("كيفية الاستخدام 📝")
        markup.row(b1,b2)
        if message.from_user.id == ADMIN_ID:
            markup.add("إضافة بيانات الوظائف 🆕")
            bot.send_message(ADMIN_ID,"لقد تم التعرف عليك ك admin.")
        elif message.from_user.id == SEC_ADMIN_ID:
            markup.add("إضافة بيانات الوظائف")
            bot.send_message(SEC_ADMIN_ID,"لقد تم التعرف عليك ك admin.")
        bot.send_message(message.chat.id,"الرجاء إختيار طلبك من القائمة:",reply_markup=markup)
    def home(message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        markup.add(KeyboardButton("تنزيل فيديوهات 📥"))
        markup.add(KeyboardButton("حذف الخلفية 📷"))
        markup.add(KeyboardButton("رموز  QR 🈺"))
        markup.add(KeyboardButton("تحويل النص إلى كلام 🔀"))
        markup.add(KeyboardButton("تحويل أي فيدو إلى موسيقى 🔁"))
        markup.add(KeyboardButton("معرفة الموقع من الرقم 📲"))
        markup.add(KeyboardButton("معرفة سرعة الإنترنت 🌐"))
        markup.add(KeyboardButton("تحويل الصورة إلى ملصق 🖼"))
        markup.add(KeyboardButton("ترجمة النصوص من أي لغة إلى العربية 🔠"))
        markup.add(KeyboardButton("البحث عن اي يخطر في بالك في غوغل 🔍"))
        markup.add(KeyboardButton("استعلام الوظائف 📋"))
        b1 = KeyboardButton("التواصل مع الدعم 📞")
        b2 = KeyboardButton("كيفية الاستخدام 📝")
        markup.row(b1,b2)
        if message.from_user.id == ADMIN_ID:
            markup.add("إضافة بيانات الوظائف 🆕")
            bot.send_message(ADMIN_ID,"لقد تم التعرف عليك ك admin.")
        elif message.from_user.id == SEC_ADMIN_ID:
            markup.add("إضافة بيانات الوظائف")
            bot.send_message(SEC_ADMIN_ID,"لقد تم التعرف عليك ك admin.")
        bot.send_message(message.chat.id,"تمت العودة إلى القائمة الرئيسية, الرجاء الإختيار من القائمة:",reply_markup=markup)
    #---------------------------- show download
    def show_download(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تنزيل من اليوتيوب",callback_data="youtube"))
        bot.send_message(message.chat.id,"الجاء الإختيار من القائمة:",reply_markup=markup)
    #-------------------------------- show remove
    def show_remove(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("باستخدام AI", callback_data="remove"))
        bot.send_message(message.chat.id,"هل تريد حذف خلفية الصورة باستخدام:",reply_markup=markup)
    #--------------------------------------- show gtts
    def show_gtts(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("باستخدام غوغل.",callback_data="gtts"))
        bot.send_message(message.chat.id,"تحويل النص إلى كلام باستخدام:",reply_markup=markup)
    #-------------------------------------- show convert
    def show_convert(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تحويل عادي",callback_data="convert"))
        bot.send_message(message.chat.id,"نوع التحويل:",reply_markup=markup)
               
    #-------------------------------------- show convimg
    def show_convimg(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تحويل عادي",callback_data="convimg"))
        bot.send_message(message.chat.id,"نوع تحويل الصورة:",reply_markup=markup)
    #------------------------------------------- show translate
    def show_trans(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("العربية",callback_data="arabic"))
        markup.add(InlineKeyboardButton("الإنجليزية",callback_data="english"))
        markup.add(InlineKeyboardButton("الفرنسية",callback_data="french"))
        bot.send_message(message.chat.id,"ترجمة النص من أي لغة إلى:",reply_markup=markup)
    #--------------------------------------------- show google
    def show_google(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("غوغل",callback_data="google"))
        bot.send_message(message.chat.id,"البحث في:",reply_markup=markup)
    #----------------------------------------------- show QR
    def show_qr(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("إنشاء QR ✏️",callback_data="make"))
        markup.add(InlineKeyboardButton("قراءة QR 📖",callback_data="read_qr"))
        bot.send_message(message.chat.id,"اختر نوع ال QR:",reply_markup=markup)
    #---------------------- keyboard buttons
    def make_qr(message):
            try:
                markup = types.ReplyKeyboardMarkup(row_width=2)
                for qr_type in qr_types.keys():
                    markup.add(types.KeyboardButton(qr_type))
                    
                markup.add(types.KeyboardButton("إلغاء ❌"))
                bot.send_message(message.chat.id, "اختر نوع QR الذي تريد إنشاءه:", reply_markup=markup)
            except Exception as e:
                print(f"Error on [MAKE QR] ({e})") 
    @bot.message_handler(func=lambda message: message.text in qr_types)
    def handle_qr_type(message):
        qr_type = message.text
        user_data[message.chat.id] = {'type': qr_type, 'step': 0, 'inputs': []}
        bot.send_message(message.chat.id, qr_types[qr_type][0])
    @bot.message_handler(func=lambda message: message.chat.id in user_data)
    def handle_inputs(message):
        gen_qr(message)
    def gen_qr(message):
        chat_id = message.chat.id
        if chat_id not in user_data:
            bot.send_message(chat_id, "يرجى اختيار نوع QR أولاً باستخدام /start.")
            return
        user_state = user_data[chat_id]
        qr_type = user_state['type']
        step = user_state['step']
        user_state['inputs'].append(message.text)
        if step + 1 < len(qr_types[qr_type]):
            user_state['step'] += 1
            bot.send_message(chat_id, qr_types[qr_type][step + 1])
        else:
            create_qr(message, qr_type, user_state['inputs'])
            del user_data[chat_id]
    def create_qr(message, qr_type, inputs):
        try:    
            if qr_type == "WiFi":
                ssid, password, security = inputs
                qr_data = f"""
                WIFI:{ssid};
                T:{security};
                P:{password};"""
            elif qr_type == "URL":
                qr_data = inputs[0]
            elif qr_type == "Text":
                qr_data = inputs[0]
            elif qr_type == "Email":
                qr_data = f"mailto:{inputs[0]}"
            elif qr_type == "Phone":
                qr_data = f"tel:{inputs[0]}"
            elif qr_type == "SMS":
                phone, message = inputs
                qr_data = f"""
                smsto:{phone};
                Message:{message};"""
            elif qr_type == "Geo":
                latitude, longitude = inputs
                qr_data = f"""geo:{latitude};
                {longitude};"""
            elif qr_type == "YouTube":
                qr_data = inputs[0]
            elif qr_type == "Instagram":
                username = inputs[0]
                qr_data = f"https://www.instagram.com/{username}"
            img = qrcode.make(qr_data)
            img = img.convert("RGB")
            qr_pixels = img.load()
            background_color = (255, 255, 255)
            qr_color = (0, 0, 0)
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    if qr_pixels[x, y] == (0, 0, 0):
                        qr_pixels[x, y] = qr_color
                    else:
                        qr_pixels[x, y] = background_color
            img_path = f'./qr/{message.from_user.id}.png'
            img.save(img_path)
            with open(img_path, 'rb') as qr_file:
                bot.send_photo(message.chat.id, photo=qr_file, caption="رمز QR الخاص بك.")
            os.remove(img_path)
            bot.send_message(ADMIN_ID,f"""🏆 MAKE QR 🏆
        🚩 Name: {message.from_user.first_name}
        🚩 ID: {message.from_user.id}
        🚩 User Name: {message.from_user.username}
        🚩 Status: True ✅""")
            
            markread = InlineKeyboardMarkup()
            markread.add(InlineKeyboardButton("تجربة قراءة QR 📖",callback_data="read_qr"))
            markread.add(InlineKeyboardButton("إلغاء ❌",callback_data="cancel"))
            bot.send_message(message.chat.id,"هل تريد:",reply_markup=markread)
            home(message)
        except Exception as e:
            print(f"Error on [MAKE QR] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
            حدث خطأ ما ❌
            الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 MAKE QR 🏆
            🚩 Name: {message.from_user.first_name}
            🚩 ID: {message.from_user.id}
            🚩 User Name: {message.from_user.username}
            🚩 Status: Valid ❌""")
            pass
    @bot.message_handler(func=lambda message: True)
    def respond_buttons_keyboard(message):
        if message.text == 'إلغاء ❌':
            home(message)
        elif message.text == 'تنزيل فيديوهات 📥':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_download(message)
        elif message.text == 'حذف الخلفية 📷':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_remove(message)
        elif message.text == 'رموز  QR 🈺':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_qr(message)
        elif message.text == 'تحويل النص إلى كلام 🔀':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))    
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_gtts(message)
        elif message.text == 'تحويل أي فيدو إلى موسيقى 🔁':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_convert(message)
        elif message.text == "استعلام الوظائف 📋":
            usersend(message)
        elif message.text == "إضافة بيانات الوظائف 🆕":
            if message.from_user.id == ADMIN_ID:
                adminsend=bot.send_message(ADMIN_ID,"الرجاء إرسال الوظائف المطلوبة ✏️")
                bot.register_next_step_handler(adminsend,adminsendfunc)
            elif message.from_user.id == SEC_ADMIN_ID:
                secadminsend=bot.send_message(SEC_ADMIN_ID,"الرجاء إرسال الوظائف المطلوبة ✏️")
                bot.register_next_step_handler(secadminsend,adminsendfunc)
            else:
                bot.send_message(message.chat.id,"sorry you cant send message")
        elif message.text == 'معرفة الموقع من الرقم 📲':
            bot.send_message(message.chat.id,"""عذرا 🙁
هذه الخدمة متوقفة حاليا وقيد التطوير 💔
سيتم توفر هذه الخدمة قريبا 🔜""")
        elif message.text == 'معرفة سرعة الإنترنت 🌐':
            bot.send_message(message.chat.id,"""عذرا 🙁
هذه الخدمة متوقفة حاليا وقيد التطوير 💔
سيتم توفر هذه الخدمة قريبا 🔜""")
        elif message.text == 'تحويل الصورة إلى ملصق 🖼':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_convimg(message)
        elif message.text == 'ترجمة النصوص من أي لغة إلى العربية 🔠':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_trans(message)
        elif message.text == 'البحث عن اي يخطر في بالك في غوغل 🔍':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_google(message)
            
        elif message.text == 'التواصل مع الدعم 📞':
            bot.send_message(message.chat.id,"""للتواصل معنا 📞:
علاء صافي
Alaa Safi
00963951449364
alaasafi218k15@gmail.com
@AlaaSafiProgrammer218 
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
زيد مخزوم
Zaid Makhzoom
00963992883477
zaidmakzoom@gmail.com
@Zaidmakhzoom""")
        elif message.text == 'كيفية الاستخدام 📝':
            start(message)
        else:
            bot.send_message(message.chat.id,"عذرا, يرجى الإختيار من القائمة فقط.")
    @bot.callback_query_handler(func=lambda call: True)
    def callback_data(call):
        if call.data == 'cancel':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            home(call.message)
        elif call.data == 'youtube':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defdown = bot.send_message(call.message.chat.id,"تمام, يرجى إرسال رابط الفيديو.")
            bot.register_next_step_handler(defdown,download_sazom)
        elif call.data == 'remove':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defrembg = bot.send_message(call.message.chat.id,"يرجى ارسال الصورة.")
            bot.register_next_step_handler(defrembg,remove_sazom)
        elif call.data == 'make':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            make_qr(call.message) 
        elif call.data == 'read_qr':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defread = bot.send_message(call.message.chat.id,"يرجى إرسال الصورة لقراءة رمز QR.")
            bot.register_next_step_handler(defread,read_qr)
        elif call.data == 'gtts':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defgtts = bot.send_message(call.message.chat.id,"يرجى كتابة النص المراد تحويله إلى كلام.")
            bot.register_next_step_handler(defgtts,gtts_sazom)
        elif call.data == 'convert':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defconvert = bot.send_message(call.message.chat.id,"يرجى إرسال الفيديو.")
            
            bot.register_next_step_handler(defconvert,convert_sazom)
        elif call.data == 'convimg':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defconvimg = bot.send_message(call.message.chat.id,"يرجى إرسال الصورة.")
            bot.register_next_step_handler(defconvimg,convimg_sazom)
        #trans
        elif call.data == 'arabic':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defarabic = bot.send_message(call.message.chat.id,"يرجى ارسال النص")
            bot.register_next_step_handler(defarabic,arabic_sazom)
        elif call.data == 'english':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defeng = bot.send_message(call.message.chat.id,"يرجى ارسال النص")
            bot.register_next_step_handler(defeng,eng_sazom)
        elif call.data == 'french':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            deffr = bot.send_message(call.message.chat.id,"يرجى ارسال النص")
            bot.register_next_step_handler(deffr,fr_sazom)
        elif call.data == 'google':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defgoogle = bot.send_message(call.message.chat.id,"يرجى كتابة البحث الذي تريده.")
            bot.register_next_step_handler(defgoogle,google_sazom)
        else:
            bot.send_message(call.message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
        
        
    def read_qr(message):
            try:    
                file_info = bot.get_file(message.photo[-1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                result = read_qr_qr(downloaded_file)
                bot.reply_to(message, "تم العثور على البيانات.")
                bot.send_message(message.chat.id,result)
                markmake = InlineKeyboardMarkup()
                markmake.add(InlineKeyboardButton("تجربة إنشاء QR ✏️",callback_data="make"))
                markmake.add(InlineKeyboardButton("إلغاء ❌",callback_data="cancel"))
                bot.send_message(message.chat.id,"هل تريد:",reply_markup=markmake)
                home(message)
                bot.send_message(ADMIN_ID,f"""🏆 READ QR 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
            except Exception as e:
                print(f"Error on [READ QR] ({e})")
                bot.send_message(message.chat.id,"""للاسف ☹️
    حدث خطأ ما ❌
    الرجاء المحاولة لاحقا 🔄""")
                bot.send_message(ADMIN_ID,f"""🏆 READ QR 🏆
    🚩 Name: {message.from_user.first_name}
    🚩 ID: {message.from_user.id}
    🚩 User Name: {message.from_user.username}
    🚩 Status: Valid ❌""")
    def read_qr_qr(image_bytes):
        try:
            image = Image.open(BytesIO(image_bytes))
            image = np.array(image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            detector = cv2.QRCodeDetector()
            value, points, straight_qrcode = detector.detectAndDecode(gray)
            if value:
                return f"{value}"
            else:
                return "لم يتم العثور على QR code"
        except Exception as e:
            print(f"Error reading QR code: {e}")
        return None

    def google_sazom(message):
        user_id = message.from_user.id
        query = message.text
        try:
            with open(f"./search/{user_id}.txt", "a", encoding="utf-8") as file:
                file.write(f"{query}\n")
            results = []
            for result in search(query, num_results=10):
                results.append(result)
            bot.send_message(message.chat.id, "إليك أفضل 10 نتائج:")
            if results:
                for result in results:
                    bot.send_message(message.chat.id, result)
                    print("search results reached - done")
            else:
                bot.send_message(message.chat.id, "لم أتمكن من العثور على أي نتائج.")  
                print("search results reached - error")
            os.remove(f"./search/{user_id}.txt")
            print("search results file removed - done")
            home(message)
            bot.send_message(ADMIN_ID,f"""🏆 SEARCH GOOGLE 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
            
        except Exception as e:
            print(f"Error on [SEARCH] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 SEARCH GOOGLE 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
    def eng_sazom(message):
        try:
            chat_id=message.chat.id
            user_id = message.from_user.id
            translator = Translator()
            with open(f"./translate/{user_id}_eng.txt",'w',encoding="utf-8") as file:
                file.write(message.text)
            print("processing text...")
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة النص الذي ارسلته, الرجاء الإنتظار...")
            with open(f"./translate/{user_id}_eng.txt","r",encoding="utf-8") as file:
                SAZOM_file = file.read()
            SAZOM_en = translator.translate(text=SAZOM_file,src="auto",dest="en").text
            with open(f"./translate/{user_id}_SAZOM_eng.txt","w", encoding="utf-8") as file:
                file.write(SAZOM_en)
            print("processing text eng - done")
            text = open(f"./translate/{user_id}_SAZOM_eng.txt","rb")
            bot.send_message(chat_id=chat_id,text=text,parse_mode="Markdown")
            print(f"send text eng to ({message.from_user.first_name}) his id ({message.from_user.id})")
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            text.close()
            os.remove(f"./translate/{user_id}_SAZOM_eng.txt")
            print("the text SAZOM eng removed - done")
            os.remove(f"./translate/{user_id}_eng.txt")
            print("the text eng removed - done")
            home(message)
            bot.send_message(ADMIN_ID,f"""🏆 TRANSLATE ENGLISH 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
        except Exception as e:
            print(f"Error on [Trans ENGLISH] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 TRANSLATE ENGLISH 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
    def fr_sazom(message):
        try:
            chat_id=message.chat.id
            user_id = message.from_user.id
            translator = Translator()
            with open(f"./translate/{user_id}_fr.txt",'w',encoding="utf-8") as file:
                file.write(message.text)
            print("processing text...")
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة النص الذي ارسلته, الرجاء الإنتظار...")
            with open(f"./translate/{user_id}_fr.txt","r",encoding="utf-8") as file:
                SAZOM_file = file.read()
            SAZOM_fr = translator.translate(text=SAZOM_file,src="auto",dest="fr").text
            with open(f"./translate/{user_id}_SAZOM_fr.txt","w", encoding="utf-8") as file:
                file.write(SAZOM_fr)
            print("processing text to french - done")
            text = open(f"./translate/{user_id}_SAZOM_fr.txt","rb")
            bot.send_message(chat_id=chat_id,text=text,parse_mode="Markdown")
            print(f"send text french to ({message.from_user.first_name}) his id ({message.from_user.id})")
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            text.close()
            os.remove(f"./translate/{user_id}_SAZOM_fr.txt")
            print("the text SAZOM fr removed - done")
            os.remove(f"./translate/{user_id}_fr.txt")
            print("the text fr removed - done")
            home(message)
            bot.send_message(ADMIN_ID,f"""🏆 TRANSLATE FRENCH 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
        except Exception as e:
            print(f"Error on [Trans FRENCH] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 TRANSLATE FRENCH 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
    def arabic_sazom(message):
        try:
            chat_id=message.chat.id
            user_id = message.from_user.id
            translator = Translator()
            with open(f"./translate/{user_id}.txt",'w',encoding="utf-8") as file:
                file.write(message.text)
            print("processing text arabic to translate...")
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة النص الذي ارسلته, الرجاء الإنتظار...")
            with open(f"./translate/{user_id}.txt","r",encoding="utf-8") as file:
                SAZOM_file = file.read()
            SAZOM_ar = translator.translate(text=SAZOM_file,src="auto",dest="ar").text
            with open(f"./translate/{user_id}_SAZOM.txt","w", encoding="utf-8") as file:
                file.write(SAZOM_ar)
            print("processing text arabic to translate - done")
            text = open(f"./translate/{user_id}_SAZOM.txt","rb")
            bot.send_message(chat_id=chat_id,text=text,parse_mode="Markdown")
            print(f"send text to ({message.from_user.first_name}) his id ({message.from_user.id})")
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            text.close()
            os.remove(f"./translate/{user_id}_SAZOM.txt")
            print("the text arabic was removed - done")
            os.remove(f"./translate/{user_id}.txt")
            print("the text SAZOM was removed - done")
            home(message)
            bot.send_message(ADMIN_ID,f"""🏆 TRANSLATE ARABIC 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
        except Exception as e:
            print(f"Error on [Trans ARABIC] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 TRANSLATE ARABIC 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
    def convert_to_sticker(image_path,message):
        try:
            user_id = message.from_user.id
            input_image = Image.open(image_path)
            sticker_size = (512, 512)
            input_image.thumbnail(sticker_size)
            if input_image.size[0] != sticker_size[0] or input_image.size[1] != sticker_size[1]:
                background = Image.new('RGBA', sticker_size, (255, 255, 255, 0))
                background.paste(input_image, ((sticker_size[0] - input_image.size[0]) // 2, (sticker_size[1] - input_image.size[1]) // 2))
                input_image = background
            sticker_path = f'./sticker/{user_id}.webp'
            input_image.save(sticker_path)
            return sticker_path
        except Exception as e:
            print(f"Error on [STICKER] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            
    def convimg_sazom(message):
        try:
            user_id = message.from_user.id
            file_id = message.photo[-1].file_id
            chat_id=message.chat.id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الصورة التي ارسلتها , الرجاء الإنتظار...")
            with open(f'./sticker/{user_id}.jpg', 'wb') as new_file:
                new_file.write(downloaded_file)
            sticker_path = convert_to_sticker(f'./sticker/{user_id}.jpg')
            if sticker_path:
                sticker_file = open(sticker_path, 'rb')
                bot.send_sticker(message.chat.id, sticker_file)
                bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
                sticker_file.close()
                os.remove(f"./sticker/{user_id}.jpg")
                os.remove(f"./sticker/{user_id}.webp")
                home(message)
                bot.send_message(ADMIN_ID,f"""🏆 CONVERT IMAGE 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
            else:
            
                print(f"Error on [CONVIMG] ({e})")
                bot.send_message(chat_id,"""للاسف ☹️
    حدث خطأ ما ❌
    الرجاء المحاولة لاحقا 🔄""")
                bot.send_message(ADMIN_ID,f"""🏆 CONVERT IMAGE 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
        except Exception as e:
            print(f"Error on [CONVIMG] ({e})")
            bot.send_message(chat_id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
        
    def convert_sazom(message):
        try:
            if message.text == 'إلغاء ❌':
                home(message)
            user_id = message.from_user.id
            chat_id=message.chat.id
            video = message.video
            file_id = video.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            save_path = f"convert/{user_id}.mp4"
            downloaded_file = bot.download_file(file_path)
            with open(save_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الفيديوالذي ارسلته. الرجاء الإنتظار...")
            print("the video was downloaded successfully - done")
            input= f"./convert/{user_id}.mp4"
            mp4 = moviepy.editor.VideoFileClip(input)
            mp3 = mp4.audio
            mp3.write_audiofile(f"./convert/{user_id}.mp3")
            print("the video was converted to audio successfully - done")
            mediaconvert=open(f"./convert/{user_id}.mp3",'rb')
            bot.send_audio(chat_id=chat_id,audio=mediaconvert)
            print(f"the video send to ({message.from_user.first_name}) his id ({message.from_user.id})")
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            mediaconvert.close()
            mp4.close()
            os.remove(f"./convert/{user_id}.mp3")
            print("the audio was removed successfully - done")
            os.remove(f"./convert/{user_id}.mp4")
            print("the video was removed successfully - done")
            home(message)
            bot.send_message(ADMIN_ID,f"""🏆 CONVERT VIDEO 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
        except Exception as e:
            print(f"Error on [CONVERT] ({e})")
            bot.send_message(chat_id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 CONVERT VIDEO 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
    def gtts_sazom(message):
        try:
            chat_id = message.chat.id
            user_id = message.from_user.id
            text = message.text
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة النص الذي كتبته. الرجاء الإنتظار...")
            print("processing text to speech...")
            tts = gTTS(text=text, lang='ar', slow=False)
            tts.save(f"./speech/{user_id}.mp3")
            print("processing text to speech - done")
            mediaspeech = open(f"./speech/{user_id}.mp3","rb")
            bot.send_audio(chat_id=chat_id,audio=mediaspeech)
            print(f"send audio text to speech to ({message.from_user.first_name}) his id ({message.from_user.id})")
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            mediaspeech.close()
            os.remove(f"./speech/{user_id}.mp3")
            print("the audio was removed successfully - done")
            home(message)
            bot.send_message(ADMIN_ID,f"""🏆 CONVERT GTTS 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
        except Exception as e:
            print(f"Error on [GTTS] ({e})")
            bot.send_message(chat_id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 CONVERT GTTS 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
    def remove_sazom(message):
        try:
            chat_id = message.chat.id
            user_id = message.from_user.id
            photo = message.photo[-1]
            file_id = photo.file_id
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الصورة. الرجاء الإنتظار...")
            print("loading for download image...")
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            save_path = f"temp/{user_id}.jpg"
            downloaded_file = bot.download_file(file_path)
            with open(save_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            print("the image was downloaded successfully - done")
            input_path = f"./temp/{user_id}.jpg"
            output_path = f"./processed/{user_id}.png"
            input = Image.open(input_path)
            output = remove(input)
            output.save(output_path)
            print("the image was removed background - done")
            os.remove(f"./temp/{user_id}.jpg")
            print("the image was removed in temp - done")
            mediarembg = open(f"./processed/{user_id}.png",'rb')
            bot.send_photo(chat_id=chat_id,photo=mediarembg)
            print(f"the image was sended to ({message.from_user.first_name}), his id ({message.from_user.id})")
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            mediarembg.close()
            os.remove(f"./processed/{user_id}.png")
            print("the image was removed in processed - done")
            home(message)
            bot.send_message(ADMIN_ID,f"""🏆 REMOVE BG IMAGE 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
        except Exception as e:
            print(f"Error on [REMOVE] ({e})")
            bot.send_message(chat_id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 REMOVE BG IMAGE 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
    def download_sazom(message):
        try:
            url = message.text
            yt = YouTube(url)
            bot.send_message(message.chat.id,text=f"نحن نقوم بتنزيل الفيديو الخاص بك ('{yt.title}')(720p) الرجاء الإتظار...")
            video = yt.streams.get_highest_resolution()
            filename = f"./downloads/{message.from_user.id}.mp4"
            video.download(filename=filename)
            print(f"download video ({yt.title}) - done")
            mediadownload = open(f"./downloads/{message.from_user.id}.mp4",'rb')
            bot.send_video(message.chat.id,video=mediadownload)
            print(f"the video was sended successfully to ({message.from_user.frist_name}) his id ({message.from_user.id})")
            bot.send_message(message.chat.id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            mediadownload.close()
            os.remove(f"./downloads/{message.from_user.id}.mp4")
            print("the video was removed successfully.")
            home(message)
            bot.send_message(ADMIN_ID,f"""🏆 DOWNLOAD YOUTUBE 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: True ✅""")
        except:
            print("valid to download video - error")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
            bot.send_message(ADMIN_ID,f"""🏆 DOWNLOAD YOUTUBE 🏆
🚩 Name: {message.from_user.first_name}
🚩 ID: {message.from_user.id}
🚩 User Name: {message.from_user.username}
🚩 Status: Valid ❌""")
    def adminsendfunc(message):
        file_path = "home work.txt"
        text = message.text
        with open(file_path,"w",encoding="utf-8") as file:
            today = datetime.now().strftime("%Y/%m/%d")
            time = datetime.now().strftime("%H:%M:%S")
            if message.from_user.id == ADMIN_ID:
                file.write(f"التاريخ: {today}\n")
                file.write(f"الوظائف:\n")
                file.write(f"{text}\n")
                file.write("================================\n")
                file.write(f"تم التحديث بواسطة: {ADMIN_NAME}\n")
                file.write(f"تم آخر تحديث بتوقيت: {time}\n")
            elif message.from_user.id == SEC_ADMIN_ID:
                file.write(f"التاريخ: {today}\n")
                file.write(f"الوظائف:\n")
                file.write(f"{text}\n")
                file.write("================================\n")
                file.write(f"تم التحديث بواسطة: {SEC_ADMIN_NAME}\n")
                file.write(f"تم آخر تحديث بتوقيت: {time}\n")
        bot.send_message(ADMIN_ID,"تم تحديث الوظائف بنجاح ✅")
        bot.send_message(SEC_ADMIN_ID,"تم تحديث الوظائف بنجاح ✅")
    def usersend(message):
        file_path = "home work.txt"
        if os.path.exists(homework_file):
            with open(file_path,"r",encoding="utf-8") as file:
                readfhomework=file.read()
            bot.send_message(message.chat.id,readfhomework)
        else:
            bot.send_message(message.chat.id, "لا توجد وظائف حالياً ❌")
    def clear_homework_at_1_pm():
        while True:
            now = datetime.now()
            if now.hour == 12 and now.minute == 59:
                if os.path.exists(homework_file):
                    os.remove(homework_file)
                    bot.send_message(ADMIN_ID, "تم حذف جميع الوظائف لأنه حان الساعة 1:00 PM، لا توجد بيانات حاليًا.")
                    bot.send_message(SEC_ADMIN_ID, "تم حذف جميع الوظائف لأنه حان الساعة 1:00 PM، لا توجد بيانات حاليًا.")
            time.sleep(60)
    def start_time_checker():
        time_checker_thread = threading.Thread(target=clear_homework_at_1_pm)
        time_checker_thread.daemon = True
        time_checker_thread.start() 
except:
    print("ERROR*2")         
print("The bot is running!!!!")
start_time_checker()
while True:
    try:
        bot.polling(non_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"Error run bot ({e})")
        bot.send_message(ADMIN_ID,f"يوجد عطل في تشغيل البوت.")
        bot.send_message(ADMIN_ID,e)
#bot.infinity_polling()
