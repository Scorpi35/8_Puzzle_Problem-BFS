from copy import deepcopy
import sys
import numpy as np
from anytree import Node, RenderTree


class Update:

    queue_level = []

    # Specific level queue
    specific_queue = []

    instant_specific_queue = []

    # Previous state
    p_state = []

    # Parent node
    Parent_node = Node("Parent")

    # Declaring states
    u_state = [[], [], []]
    d_state = [[], [], []]
    l_state = [[], [], []]
    r_state = [[], [], []]

    def __init__(self):
        return


required_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
node_required_state = deepcopy(required_state)
node_required_state = Node(node_required_state)


def Condition(new_row, new_col, new_state):

    if new_row == 0:
        down(new_row, new_col, new_state)

    if new_row == 1:
        down(new_row, new_col, new_state)
        up(new_row, new_col, new_state)

    if new_row == 2:
        up(new_row, new_col, new_state)

    if new_col == 0:
        right(new_row, new_col, new_state)

    if new_col == 1:
        right(new_row, new_col, new_state)
        left(new_row, new_col, new_state)

    if new_col == 2:
        left(new_row, new_col, new_state)

    return


def down(old_row, old_col, old_state):
    d_matrix = deepcopy(old_state)
    # Swapping elements
    new_row = old_row + 1
    new_col = deepcopy(old_col)
    swapping_element = d_matrix[new_row, new_col]
    d_matrix[new_row, new_col] = 0
    d_matrix[old_row, old_col] = swapping_element

    d_mat = deepcopy(d_matrix)
    d_mat = d_mat.ravel()
    d_mat = d_mat.tolist()

    if d_mat in Update.p_state:
        return
    else:
        Update.specific_queue.append(d_mat)
        Update.instant_specific_queue.append(d_mat)
        Update.p_state.append(d_mat)

    return


def up(old_row, old_col, old_state):
    u_matrix = deepcopy(old_state)

    # Swapping elements
    new_row = old_row - 1
    new_col = deepcopy(old_col)
    swapping_element = u_matrix[new_row, new_col]
    u_matrix[new_row, new_col] = 0
    u_matrix[old_row, old_col] = swapping_element

    u_mat = deepcopy(u_matrix)
    u_mat = u_mat.ravel()
    u_mat = u_mat.tolist()

    if u_mat in Update.p_state:
        return
    else:
        Update.specific_queue.append(u_mat)

        Update.instant_specific_queue.append(u_mat)
        Update.p_state.append(u_mat)

    return


def left(old_row, old_col, old_state):
    l_matrix = deepcopy(old_state)

    # Swapping elements
    new_row = deepcopy(old_row)
    new_col = old_col - 1
    swapping_element = l_matrix[new_row, new_col]
    l_matrix[new_row, new_col] = 0
    l_matrix[old_row, old_col] = swapping_element

    l_mat = deepcopy(l_matrix)
    l_mat = l_mat.ravel()
    l_mat = l_mat.tolist()

    if l_mat in Update.p_state:
        return
    else:
        Update.specific_queue.append(l_mat)
        Update.instant_specific_queue.append(l_mat)
        Update.p_state.append(l_mat)

    return


def right(old_row, old_col, old_state):

    r_matrix = deepcopy(old_state)

    # Swapping elements
    new_row = deepcopy(old_row)
    new_col = old_col + 1
    swapping_element = r_matrix[new_row, new_col]
    r_matrix[new_row, new_col] = 0
    r_matrix[old_row, old_col] = swapping_element

    r_mat = deepcopy(r_matrix)
    r_mat = r_mat.ravel()
    r_mat = r_mat.tolist()

    if r_mat in Update.p_state:
        return
    else:
        Update.specific_queue.append(r_mat)
        Update.instant_specific_queue.append(r_mat)
        Update.p_state.append(r_mat)

    return


def find_0(passed_obtained_state):
    row_position, col_position = np.where(passed_obtained_state == 0)
    return row_position, col_position


def main():
    obtained_state = np.array(eval(sys.argv[1]))
    obtained_state.resize(3, 3)

    one_d_obtained = deepcopy(obtained_state)
    one_d_obtained = one_d_obtained.ravel()
    one_d_obtained = one_d_obtained.tolist()

    Update.specific_queue.append(one_d_obtained)
    Update.queue_level.append(Update.specific_queue)

    Update.p_state.append(one_d_obtained)
    print("-----------Initial State-------------")
    print(Update.specific_queue)
    print("-------------Goal State--------------")
    print(required_state)
    print("-------------------------------------")
    print("BFS Tree")

    i = 0

    while required_state not in Update.specific_queue:

        Update.specific_queue = []
        Update.movement_order = []
        Update.p_state_node = []

        new_queue = deepcopy(Update.queue_level[i])

        for selected_state in new_queue:

            Update.Parent_node = Node(selected_state)

            selected_state = np.array(selected_state)
            selected_state.resize(3, 3)

            selected_z_row, selected_z_col = find_0(selected_state)
            Condition(selected_z_row, selected_z_col, selected_state)

            for node_selection in Update.instant_specific_queue:
                Node(node_selection, parent=Update.Parent_node)

            Update.instant_specific_queue = []

            for pre, fill, node in RenderTree(Update.Parent_node):

                if node.name == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
                    print("%s%s Final State Found" % (pre, node.name))
                    continue
                print("%s%s" % (pre, node.name))

        print("------------------------------------")
        Update.queue_level.append(Update.specific_queue)
        i = i + 1


if __name__ == "__main__":
    main()

    print("State found")
