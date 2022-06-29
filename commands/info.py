@client.command(aliases=['information','commands'])
async def info(ctx):
  await ctx.send("```.latency - Same as .ping but does not return Pong!\n.8ball - Ask a question and you will receive an answer\n
  .book - Book lookup through the SAPL website utilizing a smart search algorithm developed by SAPL\n.home - Provides link for the SAPL homepage\n
  .eventsNews - Provides link for SAPL website's upcoming events and news\n.eventCalender - Provides link for SAPL calendar showing upcoming events and news\n.about - Provides link for additional information on SAPL 
                \n.service - Provides link for the SAPL services
                \n.findLibrary - Provides link for geographic lookup of nearby SAPL libraries 
                \n.holiday - Provides link which provides days in which the SAPL library is in a state of enclosure
                \n.login - Provides link to the SAPL login dashboard\n.askQuestion - Provides link to the library's online reference site
                \n.info - The command which is a legend for all other commands; Provides information on all other commands
                \n.tictactoe - Allows you to play tictactoe with another person (2 player), and you evoke the command with the @ of yourself and the other person you want to play with
                \n.rps - Allows you to play rock, paper, scissors, with the bot (Singleplayer), and you evoke the command by .rps and pick rock, paper, or scissors```")
