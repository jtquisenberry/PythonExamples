# Input

conversions = [("USD", "EUR", 0.89), ("EUR", "GBP", 0.88), ("EUR", "MXP", 15.0)]
requests = [("USD", "GBP"), ("EUR", "MXP")]

conversions_dict = dict()
visited = set()


def build_tree(conversions=conversions):
    for conversion in conversions:

        in_node = conversion[0]
        out_node = conversion[1]
        rate = conversion[2]

        if in_node not in conversions_dict:
            conversions_dict[in_node] = {}
        conversions_dict[in_node][out_node] = rate

    print(conversions_dict)
    print()

def do_conversion(requests=requests):
    result = []

    for request in requests:
        in_node_request = request[0]
        out_node_request = request[1]
        rate_request = 1
        visited.add(in_node_request)
        node_stack = [(in_node_request, rate_request)]

        while len(node_stack) > 0:
            node = node_stack.pop()
            in_node = node[0]
            rate = node[1]

            out_nodes = conversions_dict[in_node]
            print(out_nodes)
            for out_node in out_nodes:
                if out_node == out_node_request:
                    result.append(rate * conversions_dict[in_node][out_node])
                    node_stack = []

                    # We must use `clear` rather than ` = set()` because creating
                    # a new set will create a new local variable, and we want to work
                    # with the global variable. The result would be different if the
                    # function had default argument visited=visited.
                    visited.clear()
                    #visited = set()
                    break
                else:
                    if out_node not in visited:
                        node_stack.append((out_node, rate * conversions_dict[in_node][out_node]))
                        visited.add(out_node)

        a_breakpoint = 0

    return result


if __name__ == '__main__':
    build_tree(conversions=conversions)
    results = do_conversion(requests=requests)
    print(results)
