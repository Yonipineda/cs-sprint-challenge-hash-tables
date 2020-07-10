# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for file in files:
        i = file.split('/')[-1]
        if i in cache:
            cache[i].append(file)
        else:
            cache[i] = [file]

    for j in queries:
        if j in cache:
            for r in cache[j]:
                result.append(r)


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
