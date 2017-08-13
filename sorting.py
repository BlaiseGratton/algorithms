def merge_sort(array):
    # bottomed out here so return sorted array
    if len(array) in (1, 0):
        return array

    # sort each half recursively
    split = len(array) / 2
    first_partition = merge_sort(array[0:split])
    second_partition = merge_sort(array[split:])

    # merge them in sorted order
    merged_list = []

    while first_partition and second_partition:
        if first_partition[0] <= second_partition[0]:
            merged_list.append(first_partition.pop(0))
        else:
            merged_list.append(second_partition.pop(0))

    # append any remaining items from the other list
    if first_partition:
        merged_list.extend(first_partition)
    if second_partition:
        merged_list.extend(second_partition)

    return merged_list


def quick_sort(array):
    pass


def heap_sort(array):
    pass


def shell_sort(array):
    pass
