@client.command()
async def ban(ctx, member: discord.Member, *, reason):
	await member.ban(reason=reason)
	await ctx.send(f'**{member.name}** has been banned. Reason: {reason}.')