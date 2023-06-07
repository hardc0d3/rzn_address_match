import csv
import googlemaps
from collections import defaultdict


class GoogleGeocodeUtil:
    def __init__(self, api_key):
        self._api_key = api_key
        pass

    def from_csv(self, input_file_name, have_header=True) -> list:
        gmaps = googlemaps.Client(key=self._api_key)
        with open(input_file_name) as fp:
            reader = csv.reader(fp)
            # skip header row
            if have_header:
                next(reader)

            # grouping dict
            place_id__names = defaultdict(list)

            # query google maps api to retrieve place id
            for name, address in reader:
                retrieved_places = [place['place_id']
                                    for place in gmaps.geocode(address)]
                place_id = retrieved_places[0] if len(retrieved_places) == 1 else None
                if place_id is None:
                    continue
                # group by place id
                place_id__names[place_id].append(name)

            # process output
            names__list = sorted([", ".join(sorted(names))
                                  for _, names
                                  in place_id__names.items()])
            return names__list
