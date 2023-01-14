from Node import Node

if __name__ == "__main__":
    Root = Node()

    numbers = [78, 52, 31, 49, 89, 35, 32, 73, 58, 25, 11, 1, 38, 20, 76, 18, 51, 82, 21]
    # numbers = []

    for i in numbers:
        Root.insert_value(i)

    number_to_search = int(input("Write number to find in tree: "))

    min_value = Root.get_min_value()
    max_value = Root.get_max_value()
    searched_value = Root.find_value(number_to_search)
    node_count = Root.get_node_count()

    print(f'Number searched for: {number_to_search}. Does it belong to the tree? {searched_value}')
    print(f'Minimum value in tree: {min_value}')
    print(f'Maximum value in tree: {max_value}')
    print(f'The number of nodes is: {node_count}')
