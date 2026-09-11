#!/usr/bin/env python3
"""Module defining VerboseList, a list that notifies on modifications."""


class VerboseList(list):
    """A list that prints a message when items are added or removed."""

    def append(self, item):
        """Add an item to the end of the list, then print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with items from an iterable, then notify."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Print a notification, then remove the first occurrence of item."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification, then remove and return the item at index."""
        try:
            item = self[index]
        except IndexError:
            return super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)


vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)

print(vl)
