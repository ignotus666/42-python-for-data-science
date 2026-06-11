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
        stats_str = f" {i}/{total}"

        bar_len = cols - len(percent_str) - len(stats_str) - 4
        bar_len = max(bar_len, 5)

        filled_len = int(bar_len * percent)

        if i == total:
            bar = '█' * filled_len
        else:
            bar = ('█' * (filled_len)) + (' ' * (bar_len - filled_len))

        sys.stdout.write(f"\r\033[K{percent_str}|{bar}|{stats_str}")
        sys.stdout.flush()

    print()
