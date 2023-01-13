from Node import Node

if __name__ == "__main__":
    Root = Node()
    Root.insert_value(4)
    Root.insert_value(5)
    Root.insert_value(2)
    Root.insert_value(1)
    Root.insert_value(3)
    max_value = Root.get_max_value()
    min_value = Root.get_min_value()
    parent = Root.value
    searched_value = Root.find_value(200)

    print(min_value, max_value, searched_value)