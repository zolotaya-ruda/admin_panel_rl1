import apps
import ws_apps


def load_handlers(pages):
    '''
    PathsHandler -> класс, отвечающий за рендеринг html-файла
    RequestHandler -> класс, отвечающий за запросы ajax и СВЯЗАННЫЙ СО СВОИМ "PathsHandler"
    функция load_handlers необходима для заполнения путей, на вход которой подается pages: tornado.web.Application
    цикл for проходит по всем элементам из apps
    пример cls и name в этом цикле:
    -> cls: <module 'apps.login' from 'D:\\projects\\stream_project\\je\\apps\\login\\__init__.py'> -- это модуль приложения
    -> name: register -- это название приложения т.е apps.register
    далее в "if name[0] != '_':" отсееваются все специальные методы класса
    далее мы пытаемся получить обработчик запросов ajax: "request_handler = cls.handler.RequestHandler"
    если это удается, то мы устанавливаем "is_request_handler" как True
    если обработчиков ajax запросов существует, то мы добавляем обработчик запросов ajax("RequestHandler")
    и класс, связанный с этим обработчиком(PathsHandler), в pages
    в условии: "if is_request_handler:" и после чего повествуем об усешной конфигурации приложения
    в противном случае мы добавляем в pages только "PathsHandler"
    '''

    is_request_handler = False

    for name, cls in apps.__dict__.items():
        if name[0] != '_':
            try:
                try:
                    request_handler = cls.handler.RequestHandler
                    is_request_handler = True
                except:
                    pass

                if is_request_handler:
                    paths_handler = cls.handler.PathsHandler

                    pages.add_handlers(r'.*', [(paths_handler.PATH, paths_handler)])
                    pages.add_handlers(r'.*', [(request_handler.PATH, request_handler)])

                    is_request_handler = False

                    print(f'[+] Success configured {name} path handler & {name} request handler')
                    continue

                paths_handler = cls.handler.PathsHandler
                pages.add_handlers(r'.*', [(paths_handler.PATH, paths_handler)])
                print(f'[+] Success configured {name} path handler')

            except:
                pass

    for name, cls in ws_apps.__dict__.items():
        if name[0] != '_':
            try:
                ws_handler = cls.handler.WSHandler
                pages.add_handlers(r'.*', [(ws_handler.PATH, ws_handler)])
                print(f'[+] Success configured {name} web socket')

            except Exception as e:
                pass

    return pages
