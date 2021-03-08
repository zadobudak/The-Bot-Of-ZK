import discord
client = discord.Client()

@client.event
async def letter_game(message, score):
	
    if message.content == '!game!':
        await message.channel.send('took')
        
    elif message.content.startswith('!g '):
        takentext = message.content.split(' ')[1]

        if not mssg1:
            mssg2 = takentext.split(' ')[1]
            mssg1lastletter = mssg1[-1]
            mssg2firstletter = mssg2[0]
            if mssg1lastletter == mssg2firstletter:
                answerr = "Correct"
            else:
                answerr = "Wrong"
            
            if answerr == "Correct":
                score += 1
                await message.channel.send(f"Correct, score:{score}")
                print(mssg2)
                mssg1 = mssg2
            elif answerr == "Wrong":
                score *= 0
                await message.channel.send("GAME OVER! If you want to play again, send '!game!'")

        else:
            score += 1
            mssg1 = takentext.split(' ')[1]
            await message.channel.send("First word was token, type second one")
            print(mssg1)


