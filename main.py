import os, discord, requests, json, random
from discord.ext import commands
from keep_alive import keep_alive

#dictionary of animal names to API endpoints
animals = {
  "fox":"fox",
  "hyena":"yeen",
  "bunny":"bun",
  "capybara":"capy",
  "painted-dog":"chi",
  "deer":"deer",
  "jaguar":"jaguar",
  "lion":"leo",
  "maned-wolf":"mane", 
  "otter":"otter",
  "pine-marten":"marten", 
  "oppossum":"poss",
  "puma":"puma",
  "raccoon":"racc",
  "skunk":"skunk",
  "snake":"snek",
  "snow-leopard":"snep", 
  "tiger":"tig",
  "red-panda":"wah", 
  "wolf":"woof",
  "coyote":"yote",
  "dog":"dog",
  "bear":"bear",
  "serval":"serval",
  "shiba-inu":"shiba" 
}

client = commands.Bot(command_prefix="!")

@client.command(name="random", brief="Displays an image of a random animal.", help="""Randomly selects an animal and displays a picture. Example:

!random""")
async def rand(ctx):
  # randomly selects a key from the list of animals and returns an image link
  await ctx.message.reply(request(random.choice(list(animals.values()))))
 

@client.command(name="picture", brief="Displays an image of a selected animal.", help="""Displays a picture of a selected animal.  Example:

!picture <animal>

List of animals (case insenitive, hyphens are mandatory):
- Bear
- Bunny
- Capybara
- Coyote
- Deer
- Dog
- Fox
- Hyena
- Jaguar
- Lion
- Maned-Wolf
- Oppossum
- Otter
- Painted-Dog
- Pine-Marten
- Puma
- Raccoon
- Red-Panda
- Skunk
- Serval
- Shiba-Inu
- Snake
- Snow-Leopard
- Tiger
- Wolf""")
async def picture(ctx, animal):
  if not animal:
    await ctx.message.reply("Please specify the name of an animal. A full list of animals can be found by running `!help picture`")
    return
  input = animal.lower() # make input lowercase to match keys
  if input not in animals.keys():
    await ctx.message.reply("Invalid animal name, did you mispell it? Remember that the animal names are case-insesitive.")
    return
  # returns an image link of the specified animal
  await ctx.message.reply(request(animals[input]))
  

def request(animal):
  # request image location from API
  resp = requests.get("https://api.tinyfox.dev/img?animal=" + animal + "&json")
  # interperet JSON data
  data = json.loads(resp.content)
  # return image link
  return "https://tinyfox.dev" + data["loc"]


keep_alive() # small website to keep bot alive
bot_secret = os.environ['DISCORD_TOKEN'] # setup bot with auth token
client.run(bot_secret) # run bot
