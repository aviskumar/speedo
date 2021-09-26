from session.pyrogram_main import *
async def op():
  await mongo_check()
  await run_bot()

if __name__ == "__main__":
  Speedo.loop.run_until_complete(run_bot())
