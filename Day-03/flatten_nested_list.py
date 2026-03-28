# Write a function that takes a nested list and flattens it into a single list.

def flatten(nested_list):
    """Recursively flattens a nested list into a single flat list."""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


# Test with a nested list
nested = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]

print("Original list:", nested)
print("Flattened list:", flatten(nested))
