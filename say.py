@client.command()
async def say(ctx, *, message):
	if ctx.author.bot:
		return
		
	await ctx.send(message)