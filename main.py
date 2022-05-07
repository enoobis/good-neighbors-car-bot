import logging 
import re
import asyncio
import os


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image


from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


#automatic maintenance launcher 
from keep_alive import keep_alive

# web settings
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')

#link to website
driver = webdriver.Chrome(options=chrome_options)    
driver.get("http://www.gps110.org")
#interaction with the website
ru_button = driver.find_element_by_class_name('v_en')
ru_button.click()
user_input = driver.find_element_by_id('txtUserName')
user_input.send_keys(os.environ['USERNAME'])
password_input = driver.find_element_by_id('txtPwd')
password_input.send_keys(os.environ['PASSWORD'])
login_button = driver.find_element_by_id('login')
login_button.click()


iframe = driver.find_element_by_id('mUrl')
driver.switch_to.frame(iframe)

car1 = driver.find_element_by_id('2898cf40a941446d96c8ba34386c7cc7').text
car2 = driver.find_element_by_id('83f10decc35842119e8f1c549c638e25').text
car3 = driver.find_element_by_id('cbd3f3a458214ce6915924348d352b97').text
car4 = driver.find_element_by_id('18e990bc96b24d1996bffe5f53fd9140').text
car5 = driver.find_element_by_id('51423640f2274485a8af17b477896ac2').text
car6 = driver.find_element_by_id('de2778922798475ba37efaeb5822648f').text
car7 = driver.find_element_by_id('021a6fc2bbc14f8eacad899c1b7d6f04').text
car8 = driver.find_element_by_id('540dc4c6031840828bf28872db5ef86c').text
#Logging level
logging.basicConfig(level=logging.INFO)

#Initalization of bot 
bot = Bot('5368245711:AAHg0sbF_iYmcTWNSrpkRJYhA-ha66LV9-Q')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["text", "image" , "list"]
    keyboard.add(*buttons)
    await message.answer("𝙒𝙝𝙖𝙩 𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙬𝙤𝙪𝙡𝙙 𝙔𝙤𝙪 𝙡𝙞𝙠𝙚 𝙩𝙤 𝙧𝙚𝙘𝙚𝙞𝙫𝙚 ?", reply_markup=keyboard)


@dp.message_handler(Text(equals="text"))
async def text_com(message: types.Message):
    await message.reply('-------'+'\n'+car1+'\n'+'-------'+'\n'+car2 +'\n'+'-------'+'\n'+car3+ '\n'+ '-------' +'\n'+car4+ '\n'+'-------'+'\n' +car5+ '\n'+'-------'+'\n' +car6 +'\n'+ '-------'+'\n'+ car7+'\n'+'-------' +'\n' +car8 )
  
@dp.message_handler(Text(equals="image"))
async def image_com(message: types.Message):
    driver.get_screenshot_as_file('images/full.png')
    image = Image.open('images/full.png')
    image = image.crop((0, 265, 400, 580))
    image.save('images/crop.png')
    opened_image = open("images/crop.png", "rb")
    await bot.send_photo(message.from_user.id, opened_image)

@dp.callback_query_handler(text="car1_value")
async def send_car1_value(call: types.CallbackQuery):
    await call.message.answer(car1)

@dp.callback_query_handler(text="car2_value")
async def send_car2_value(call: types.CallbackQuery):
    await call.message.answer(car1)

@dp.callback_query_handler(text="car3_value")
async def send_car3_value(call: types.CallbackQuery):
    await call.message.answer(car1)

@dp.callback_query_handler(text="car4_value")
async def send_car4_value(call: types.CallbackQuery):
    await call.message.answer(car1)

@dp.callback_query_handler(text="car5_value")
async def send_car5_value(call: types.CallbackQuery):
    await call.message.answer(car1)

@dp.callback_query_handler(text="car6_value")
async def send_car6_value(call: types.CallbackQuery):
    await call.message.answer(car1)

@dp.callback_query_handler(text="car7_value")
async def send_car7_value(call: types.CallbackQuery):
    await call.message.answer(car1)

@dp.callback_query_handler(text="car8_value")
async def send_car8_value(call: types.CallbackQuery):
    await call.message.answer(car1)

@dp.message_handler(Text(equals="list"))
async def list_com(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.InlineKeyboardButton(text="01KG 1504 M", callback_data= "car1_value"))
    keyboard.add(types.InlineKeyboardButton(text="01KG 1458 M", callback_data= "car2_value"))
    keyboard.add(types.InlineKeyboardButton(text="01KG 1318 M", callback_data= "car3_value"))
    keyboard.add(types.InlineKeyboardButton(text="01KG 1317 M", callback_data= "car4_value"))
    keyboard.add(types.InlineKeyboardButton(text="01KG 1319 M", callback_data= "car5_value"))
    keyboard.add(types.InlineKeyboardButton(text="01KG 1902", callback_data= "car6_value"))
    keyboard.add(types.InlineKeyboardButton(text="01KG 1903", callback_data= "car7_value"))
    keyboard.add(types.InlineKeyboardButton(text="01KG 1773", callback_data= "car8_value"))
    await message.answer("list", reply_markup=keyboard)



@dp.message_handler(commands=["timeline"])
async def nowing_timeline(message: types.Message):

    await bot.send_message(message.from_user.id, ("start %d, end %d, interval %d" % (start_time, end_time, interval/60)))



  
#setting's for screenshot making time
start_time = 15
end_time = 17
interval = 3600

class Mydialog(StatesGroup):
    otvet = State()  # Will be represented in storage as 'Mydialog:otvet'

#Здесь мы начинаем общение с клиентом и включаем состояния
@dp.message_handler(commands=["make_custom_timline"])
async def cmd_dialog(message: types.Message):
    await Mydialog.otvet.set()  # вот мы указали начало работы состояний (states)

    await message.reply("Ok send me your settings in this format \n Satrt at 21 hour end at 7 hour with interval 60 minuets (pleace write interval use a minuets)")

# А здесь получаем ответ, указывая состояние и передавая сообщение пользователя
@dp.message_handler(state=Mydialog.otvet)
async def process_message(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        
        try:
            parser = r"(?P<start>\d+)\s\w+"
            result = re.findall(parser, user_message)
            global start_time
            global end_time
            global interval
            start_time = int(result[0])
            end_time = int(result[1])
            interval = int(result[2]) * 60
        
        except Exception as e:
            await bot.send_message(message.from_user.id, "time line dosen't change: " + e, parse_mode='HTML')
                                   
        answer_for_user = ("Ok I'll start at %d hour end at %d hour with interval %d minuets" % (start_time, end_time, interval/60))
        
        await bot.send_message(message.from_user.id, answer_for_user , parse_mode='HTML')
    # Finish conversation
    await state.finish()  # закончили работать с сотояниями
async def makeing_screenshot_for_night():
    
    while True:
        date = datetime.now()
        try:
            await asyncio.sleep(1)
            if int(date.hour) >= start_time or int(date.hour) <= end_time: 
                driver.get_screenshot_as_file('images/full.png')
                image = Image.open('images/full.png')
                image = image.crop((0, 265, 400, 600))
                image.save('images/crop.png')
                opened_image = open("images/crop.png", "rb")

                await bot.send_photo('849046064', opened_image)
                await bot.send_message('849046064', "photo sended")
                await bot.send_photo('849046064', opened_image)

                await asyncio.sleep(interval)
        except asyncio.TimeoutError:
            await bot.send_message('849046064', "error happends")

async def on_startup(_):
    asyncio.create_task(makeing_screenshot_for_night())

keep_alive()
#Runing code
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = on_startup)

