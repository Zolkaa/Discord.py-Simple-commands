'''A 'jelek közötti szövegek helyére a saját szövegedet írd!'''

@client.command()
async def embed(ctx):
	
	if ctx.author.bot:
		return
		
	embed = discord.Embed(
    	title='title',
    	description='description',
    	color=discord.Color.green()
	)
	
	embed.set_author(name='author')
	embed.set_footer(text='footer')
	
	embed.add_field(name='name', value='value')
	
	await ctx.send(embed=embed)