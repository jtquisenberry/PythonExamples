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

def do_conversion(in_node, out_node):

    rate = 1
    target_nodes = conversions_dict[in_node]
    for target_node in target_nodes:
        if target_node == out_node:
            bottom_rate = conversions_dict[in_node][target_node]
            ddd = 0
            return bottom_rate
        elif target_node not in conversions_dict:
            continue
        else:
            ccc = 0
            qqq = conversions_dict[in_node][target_node] * do_conversion(target_node, out_node)
            return qqq

    eee = 0


if __name__ == '__main__':
    build_tree(conversions=conversions)

    for request in requests:
        results = do_conversion(in_node=request[0], out_node=request[1])
        print(results)

    ttt = 0