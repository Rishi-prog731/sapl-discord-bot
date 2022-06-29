@client.command(aliases=['question','askmysapl'])
async def askQuestion(ctx):
  await ctx.send("https://ask.mysapl.org/")
