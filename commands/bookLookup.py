@client.command(aliases=['sapl', 'lookup'])
async def book(ctx, rawPath):
  rawPath = rawPath.replace('_','%20')
  await ctx.send(f'https://mysapl.bibliocommons.com/v2/search?query={rawPath}&searchType=smart')
