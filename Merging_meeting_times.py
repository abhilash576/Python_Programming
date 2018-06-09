def merge_ranges(meetings):
    # Merge meeting ranges
    sorted_meetings = sorted(meetings)

    merged_meetings = [sorted_meetings[0]]
    for cur_start, cur_end in sorted_meetings[1:]:
        last_start, last_end = merged_meetings[-1]
        if cur_start <= last_end:
            merged_meetings[-1] = (last_start, max(last_end, cur_end))
        else:
            merged_meetings.append((cur_start, cur_end))

    return merged_meetings