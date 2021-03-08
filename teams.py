from random import shuffle

async def make_group(message,x,kisiler):
 
  shuffle(kisiler)
  #print('ok')
  count = len(kisiler)
  #print(count)
  try :
    if count == 1: 
      errorMessage = "You are all alone dumbass!"
    
    elif x < 1:
      errorMessage = "Wrong number please input bigger number."
      
    elif  x > count:
      errorMessage = "Wrong number please input lower number"
    
    else:
      teams = [[]]*x
      # print(teams)
      print(f'Who called: {message.author.name}')
      for i in range(count):
        
        print(i,kisiler[i].name)
        temp =i%x
        teams[temp] = teams[temp] + [kisiler[i].name]
        ans = ''
      for ad in range(x):
        ans += f"{ad+1}. Team: {'--'.join(teams[ad])} \n"
      #print('a')
      await message.channel.send(ans)
      return
  except:
    errorMessage = 'Wrong input please type a number.'
  await message.channel.send(errorMessage)
  return