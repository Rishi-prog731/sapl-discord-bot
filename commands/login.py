@client.command(aliases=['loginPage','dashboard'])
async def login(ctx):
  await ctx.send("https://mysapl.bibliocommons.com/user/login?destination=%2Fdashboard%2Fuser_dashboard")
