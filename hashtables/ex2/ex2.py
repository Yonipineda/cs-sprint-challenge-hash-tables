#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    lookup_table = {ticket.source: ticket.destination for ticket in tickets}
    curr_city = "NONE"

    layover = []
    while len(layover) == 0 or curr_city != "NONE":
        layover.append(lookup_table[curr_city])
        curr_city = lookup_table[curr_city]

    return layover
