import os
import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)

    for i, item in enumerate(lst, 1):
        yield item

        try:
            cols = os.get_terminal_size().columns
        except OSError:
            cols = 80

        percent = i / total
        percent_str = f"{int(percent * 100)}%"
        # Adding a space before the count to match your requested format
        stats_str = f" {i}/{total}"

        # Calculate space for the bar: cols - percent - stats - brackets
        bar_len = cols - len(percent_str) - len(stats_str) - 4
        bar_len = max(bar_len, 5)

        filled_len = int(bar_len * percent)

        # Build the bar
        if i == total:
            # Full bar at 100%
            bar = '█' * filled_len
        else:
            # Bar
            bar = ('█' * (filled_len)) + (' ' * (bar_len - filled_len))

        sys.stdout.write(f"\r\033[K{percent_str}|{bar}|{stats_str}")
        sys.stdout.flush()

    print()
