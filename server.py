import asyncio
from asyncua import Server, ua

# Async helper function to create OPC-UA variables
async def create_variable(parent_object, namespace_idx, var_name, initial_value):
    """
    Create an OPC-UA variable node.
    
    Args:
        parent_object: The parent object to add the variable to
        namespace_idx: The namespace index
        var_name: The variable name
        initial_value: The initial value for the variable
    
    Returns:
        The created variable object
    """
    variable = await parent_object.add_variable(namespace_idx, var_name, initial_value)
    await variable.set_writable()
    return variable

async def create_variables(parent_object, namespace_idx):
    """
    Create 50 OPC-UA variable nodes with dynamic names.
    
    Args:
        parent_object: The parent object to add variables to
        namespace_idx: The namespace index
    
    Returns:
        A list of 50 created variable objects
    """
    variables = []
    for i in range(1, 51):
        var_name = f"Variable_{i}"
        initial_value = i
        variable = await create_variable(parent_object, namespace_idx, var_name, initial_value)
        print(variable.nodeid)
        variables.append(variable)
    return variables

async def main():

    server = Server()

    await server.init()

    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    idx = await server.register_namespace("OPCUA_TEST")

    objects = server.nodes.objects

    myobj = await objects.add_object(idx, "MyObject")

    variables = await create_variables(myobj, idx)
    print(f"Created {len(variables)} OPC-UA variables")

    print("OPC-UA Server Started!")

    async with server:
        while True:
            for variable in variables:
                value = await variable.read_value()
                value += 1
                await variable.write_value(value)
                print(f"{variable.nodeid.Identifier}: {value}")

            await asyncio.sleep(1)

asyncio.run(main())