import asyncio
from asyncua import Client

URL = "opc.tcp://localhost:4840/freeopcua/server/"

async def create_node_references(client):
    """Generate references to 50 OPC-UA variable nodes."""
    nodes = []
    for i in range(1, 51):
        node = client.get_node(f"ns=2;i={i+1}")
        nodes.append(node)
    return nodes

async def read_and_display_values(nodes):
    """Read and print current values for all provided OPC-UA nodes."""
    while True:
        for node in nodes:
            value = await node.read_value()
            identifier = node.nodeid.Identifier
            print(f"{identifier}: {value}")
        await asyncio.sleep(1)

async def main():
    async with Client(url=URL) as client:
        print("Connected successfully!")

        nodes = await create_node_references(client)
        await read_and_display_values(nodes)

asyncio.run(main())