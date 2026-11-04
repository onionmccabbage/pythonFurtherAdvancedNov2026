import asyncio # from Python 3.7+  I/O is often a bottleneck
# NB the behaviour of asyncio has mutatted across Pythno versions
# it is stable since 3.11

async def countA():
    '''pretend this is a long running process'''
    print('some long-running preparatory stuff')
    await asyncio.sleep(4) # very similar to time.sleep(4)

async def countB():
    '''another long-running process'''
    print('carrying out important operations')
    await asyncio.sleep(4)

# make our functions aware of async operations (async and await always go together)
async def main():
    '''run our long-running operations (often I/O bound)'''
    # print('...Main process begins')
    # await countA() # the await lets this pause until the operation is completes
    # print('...Main process continues')
    # await countB()
    # we may need to work with many async operations
    await asyncio.gather( countA(), countB(), countA(), countA(), countB() )

if __name__ == '__main__':
    asyncio.run( main() )