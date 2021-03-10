async def letter_game(message):

    if message.content == '!game!':
        await message.channel.send('Game Started!')

    elif message.content.startswith('1 '):
        global mssg1
        mssg1 = message.content.split(' ')[1]
        await message.channel.send("First word was token, type second one")
        global score
        score = 1
        print(mssg1)

    else:
        mssg2 = message.content

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


