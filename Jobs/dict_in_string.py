


def return_substrings(string, subsequences):




    current_index = 0
    so_far = ''

    # Use a depth-first traversal to to find complete results.
    # Depth-first accomplished with stack.
    string_segments = list()
    string_segments.append([string, [so_far]])
    complete_results = []

    while len(string_segments) > 0:
        segment, so_far = string_segments.pop()
        print("segment",segment)
        print("so_far", so_far)
        for sequence in subsequences:
            if segment.find(sequence) == 0:
                print("found", sequence)
                so_far.append(sequence)
                remainder =  segment[len(sequence):]
                print("remainder", remainder)
                string_segments.append([segment[len(sequence):], 'xxx'])



return_substrings('into', ['in','to','into'])

