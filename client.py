import asyncio
from datetime import datetime
from asyncua import Client
from database import initialize_database, insert_value

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
            try:
                value = await node.read_value()
                identifier = node.nodeid.Identifier
                timestamp = datetime.now().isoformat()
                insert_value(timestamp, identifier, value)
                print(f"{identifier}: {value}")
            except Exception as e:
                identifier = node.nodeid.Identifier
                message = str(e)
                print(f"Error reading {identifier}: {message}")
                if "Connection is closed" in message:
                    raise
        await asyncio.sleep(1)

async def main():
    initialize_database()
    while True:
        try:
            async with Client(url=URL) as client:
                print("Connected successfully!")

                nodes = await create_node_references(client)
                await read_and_display_values(nodes)
        except Exception as e:
            print(f"Connection lost or failed: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)

asyncio.run(main())