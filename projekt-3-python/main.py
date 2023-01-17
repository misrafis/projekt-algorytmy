from Node import Node

if __name__ == "__main__":
    Tree = Node()

    # numbers = [37, 28, 25, 37, 26, 17, 34, 36, 50, 47, 48, 46, 60, 58]
    # numbers = [78, 52, 31, 49, 89, 35, 32, 73, 58, 25, 11, 100, 38, 1, 76, 18, 51, 82, 21, 2, 4, 3, 5, 6, 8, 7]
    # numbers = []

    size = int(input("Write how many numbers you want to insert: "))

    for _ in range(size):
        number = int(input("Input number: "))
        Tree.insert_value(number)

    min_value = Tree.get_min_value()
    max_value = Tree.get_max_value()
    node_count = Tree.get_node_count()
    Tree.display()

    print(f'Minimum value in tree: {min_value}')
    print(f'Maximum value in tree: {max_value}')
    print(f'Number of nodes is: {node_count}')
    Tree.display_preorder()
    print()
    Tree.display_inorder()
    print()
    Tree.display_postorder()
    print()
    number_to_search = int(input("Write number to find in tree: "))
    searched_value = Tree.find_value(number_to_search)
    print(f'Number searched for: {number_to_search}. Does it belong to the tree? {searched_value}')
    print()
    number_to_delete = int(input("Write number to delete from tree: "))
    Tree.delete_value(number_to_delete)
    Tree.display()
