@client.command()
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f'Succesfully deleted {amount} messages!')