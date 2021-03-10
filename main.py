"""Made possible by hackerss ZahidKK and ZadoKK """
""" ZZ """

import discord
import os
from keep_alive import keep_alive
from teams import make_group
from letter_game import letter_game
from random import shuffle
import time
import translators as ts

score = 0

client = discord.Client()
# onlar bakip ibret alsinlar diye bu kodu yaratti onlar bilirler ki spagetti kod
#yazanlar azabi deneyimleyecektir
# çalışıyor mu çalışıyor geeeç


@client.event
async def on_ready():
    print(f"{str(client.user)[:-5]} seni görmeye geldi:)")

    #chn = client.get_channel(817577645226197053)

    '''while True:
        try:
            # print(count)
            # print(chn)
            n = await chn.connect()
            # await message.channel.send('-p yenidena')
            # await chn.edit(name =  str(count))
            print('sa')
            time.sleep(10)

            await n.disconnect()
            time.sleep(2)
        except:
            pass'''


@client.event
async def on_message(message):  #x takım sayısı
    aut = message.author

    # print(aut.name)
    if aut == client.user:
        return
    
    # print(type(aut))

    msg = message.content
    #print(msg)
    if msg.startswith('!teams'):
        chn = aut.voice.channel
        kisiler = chn.members
        a = int(msg.split(' ')[1])  #a = takım sayısı
        await make_group(message, a, kisiler)

    elif msg.startswith("!shuffle") and message.channel.id == 804623145641181205:
        voicechannels = [
            803682253669531679, 817396638326063104, 804388415864963112,
            804388471397416980, 804703255128440875, 804703317284093982,
            804728191184666664
        ]
        tn = int(msg.split(' ')[1])  #team number
        kisiler = aut.voice.channel.members
        shuffle(kisiler)
        for o in range(len(kisiler)):
            await kisiler[o].move_to(
                client.get_channel(voicechannels[(o + 1) % tn]))

        await message.channel.send("Done!")

        
    elif msg.startswith('!t'):
      
      try: 
        example = msg.split()
        lang = example[1]
        trans = ' '.join(example[2:])
        
        ans = ts.google(trans, if_use_cn_host=True, to_language=lang)
        
        await message.channel.send(ans)
      except:
        await message.channel.send("Wrong input type!")
    

    elif message.channel.id == 817582872159977542:
        await letter_game(message)
        

    elif msg.startswith('!yenidena'):

        # x = client.get_user(816271806570692628)

        print('ok')
        count = 0
        chn = client.get_channel(817577645226197053)  #vitrin
        while True:
            count += 1

            print(count)
            print(chn)

            n = await chn.connect()

            # await mes0.5age.channel.send('-p yenidena')
            # await chn.edit(name =  str(count))

            print('sa')
            time.sleep(2)

            await n.disconnect()
            time.sleep(2)


    
        


keep_alive()
client.run(os.getenv('TOKEN'))
