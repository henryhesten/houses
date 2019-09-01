import json
import urllib.request
import pyperclip

EXPECTED_PROPERTY_STYLES = [{'label': 'Flat', 'value': 12},
                            {'label': 'Apartment', 'value': 27},
                            {'label': 'Maisonette', 'value': 15},
                            {'label': 'Studio flat', 'value': 13},
                            {'label': 'Terraced House', 'value': 6},
                            {'label': 'Ground floor flat', 'value': 11},
                            {'label': 'End of terrace house', 'value': 7},
                            {'label': 'Retirement property', 'value': 31},
                            {'label': 'Detached house', 'value': 9},
                            {'label': 'Ground floor maisonette', 'value': 14}]


def get_search_url(page=1, lat=51.50740835971825, long=-0.1276986901698333, max_price=300000, search_type="ForSale",
                   search_radius=10, sort_by=2):
    return f"https://www.purplebricks.co.uk/search/property-for-sale/greater-london/london" \
        f"#?q&location=london&page={page}&latitude={lat}&longitude={long}&priceTo={max_price}&searchType={search_type}&" \
        f"searchRadius={search_radius}&sortBy={sort_by}"


def get_api_url(page=1, lat="", long="", min_price="", max_price=300000, search_type="", search_radius=10, sort_by=2,
                min_bed="", max_bed="", page_size=10):
    return f"https://search.purplebricks.co.uk/api/search?" \
        f"location=london&locationCleared=false&latitude={lat}&longitude={long}&searchRadius={search_radius}&" \
        f"type={search_type}&priceFrom={min_price}&priceTo={max_price}&bedroomsFrom={min_bed}&bedroomsTo={max_bed}&" \
        f"pageNumber={page}&propertyId=&soldOrLet=false&pageSize=&pages=&sortBy={sort_by}&sortByChange=&" \
        f"sortByChangeNewVal=&searchPopulatedByUrl=&toLet=false"


def do_search(page=1, lat="", long="", min_price="", max_price=300000, search_type="", search_radius=10, sort_by=2,
              min_bed="", max_bed=""):
    url = get_api_url(page, lat, long, min_price, max_price, search_type, search_radius, sort_by, min_bed, max_bed)
    contents = urllib.request.urlopen(url).read()
    search_data = json.loads(contents.decode('utf-8'))
    assert search_data["distinctPropertyStyles"] == EXPECTED_PROPERTY_STYLES
    return process_search(search_data)


def process_search(search_data):
    return search_data


q = do_search()
