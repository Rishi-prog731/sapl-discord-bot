@client.command()
async def latency(ctx):
  await ctx.send(f'{round(client.latency * 1000)}ms')
