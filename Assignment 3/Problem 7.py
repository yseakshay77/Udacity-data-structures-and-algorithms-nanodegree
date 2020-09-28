class RouteTrie:

    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, path):
        route_list = split_path(path)

        current_node = self.root

        for route in route_list:
            if route not in current_node.children:
                current_node.insert(route)

            current_node = current_node.children[route]

    def find(self, path):
        route_list = split_path(path)
        current_node = self.root

        for route in route_list:
            if route not in current_node.children:
                return None

            current_node = current_node.children[route]

        return current_node.handler


class RouteTrieNode:

    def __init__(self):
        self.handler = None
        self.children = {}

    def insert(self, route):
        self.children[route] = RouteTrieNode()


class Router:

    def __init__(self, root_handler, not_found_handler):
        self.root = RouteTrieNode()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler_data):
        route_list = self.split_path(path)
        current_node = self.root

        for route in route_list:

            if route not in current_node.children:
                current_node.insert(route)

            current_node = current_node.children[route]

        current_node.handler = handler_data
        # print(current_node)

    def lookup(self, path):
        if path == "/":
            return "root_handler"

        route_list = self.split_path(path)

        current_node = self.root

        for route in route_list:
            try:
                if current_node.children[route]:
                    current_node = current_node.children[route]
            except:
                return "handler not found "
        if not current_node.handler:
            return "handler not found"

        return current_node.handler

    def split_path(self, path):
        if path[0] == "/":
            path = path[1:]
        # print(path)
        if path[-1] == "/":
            path = path[:-1]

        route_list = path.split("/")
        # print(route_list)
        return route_list


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/"))
print(router.lookup("/home"))
print(router.lookup("/home/about"))
print(router.lookup("/home/about/"))
print(router.lookup("/home/about/me"))