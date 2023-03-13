import asyncio
import tornado.web
import settings
from handlers_loader import load_handlers

# key = input("key: ")
key = '&E)H@MbQeThWmZq4t7w!z%C*F-JaNdRf'
settings.KEY = key

pages = tornado.web.Application(**settings.app_settings)


def make_app():
    app = load_handlers(pages)
    return app


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())