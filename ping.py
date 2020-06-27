@client.command()
async def ping(ctx):
	await ctx.send('Latency: {}.'.format(round(client.latency * 1000)))