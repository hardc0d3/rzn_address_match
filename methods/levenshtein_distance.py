
import csv
from collections import defaultdict
from Levenshtein import ratio


class LevenshteinDistUtil:
    def __init__(self, acceptance_ratio_limit: float, have_header: bool = False):
        self.acceptance_ratio_limit = acceptance_ratio_limit
        self.have_header = have_header

    def from_csv(self, input_csv: str) -> list:
        with open(input_csv) as fp:
            reader = csv.reader(fp)
            output = []
            grouping = defaultdict(set)
            if self.have_header:
                next(reader)
            for name, address in reader:
                tokens = address.replace(',', ' ').split(' ')
                token_set = {t.strip().lower() for t in tokens if t != ''}
                token_sorted = sorted(list(token_set))
                output.append((name, ' '.join(token_sorted)))

            # calculate Levenshtein distance between items

            names = set()
            for idx_a, (name_a, address_a) in enumerate(output):
                for idx_b, (name_b, address_b) in enumerate(output):
                    names.add(name_a)
                    names.add(name_b)
                    if idx_a == idx_b:
                        continue
                    r = ratio(address_a, address_b)
                    if r > self.acceptance_ratio_limit:
                        grouping[name_a].add(name_b)
                        grouping[name_a].add(name_a)

            # grouping set

            groups = {", ".join(sorted(list(group)))
                      for name, group in grouping.items()}

            # add lonely ones

            for name in names:
                if name not in grouping:
                    groups.add(name)

            return sorted(list(groups))


