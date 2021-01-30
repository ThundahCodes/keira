@client.command(aliases = ['chatbot'])
async def cb(ctx, *, phrase):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://bruhapi.xyz/cb/{phrase}") as response:
            resp = await response.json()
            await ctx.send(resp["res"])
    