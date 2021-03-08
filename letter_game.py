import discord
client = discord.Client()

@client.event
async def letter_game(mssg1, mssg2):
    
    mssg1lastletter = mssg1[-1]
    mssg2firstletter = mssg2[0]
    if mssg1lastletter == mssg2firstletter:
        return "Correct"
    else:
        return "Wrong"


'''async def letter_game2(mssg1, mssg2):
    if mssg1[-2] == mssg2[1] and mssg1[-1] == mssg2[0]:
        return "Correct"
    else:
        return 'Wrong'''