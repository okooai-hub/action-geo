import agentflow as af

async def handle(context):
    return await af.arequest(
        "http://ip-api.com/json"
    )
