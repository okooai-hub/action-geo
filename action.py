import agentflow as af

async def handle():
    return await af.arequest(
        "http://ip-api.com/json"
    )
