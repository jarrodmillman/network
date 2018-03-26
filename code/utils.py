import numpy as np


node_options = {
    'node_color': 'royalblue',
    'node_size': 50,
    'edgecolors': 'white',
}

edge_options = {
    'line_color': 'grey',
    'alpha': 0.7,
}


def load():
    """Load respondent adjacency graphs from disk.

    Returns
    -------
    adjacencies : (N, N, M) array
        For each of the `M` fields, this array contains the adjacency
        matrix.  Columns correspond with participants in the workshop,
        rows with respondents to the survey.
    fields : array of strings
        The question type for each entry in the adjacency matrix
        above, e.g. 'Personally communicate'.
    people : array of strings
        Graph nodes (participants).

    Examples
    --------
    >>> adjacencies, fields, people = load()
    >>> print(fields[0], ':')
    Collaborate :
    >>> print(adjacencies[:5, :5, 0])
    [[0. 0. 0. 0. 0.]
     [1. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0.]
     [1. 1. 0. 0. 0.]
     [0. 0. 0. 0. 0.]]
    """
    data = np.load('../data/graph.npz')
    fields = ('adjacencies', 'fields', 'people')

    return [data[field] for field in fields]


if __name__ == "__main__":
    adjacencies, fields, people = load()

    print(fields[0], ':')
    print(adjacencies[:, :, 0])
