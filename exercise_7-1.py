images = [
    {
        "geoCountryCode": "DK",
        "format": "JPEG",
        "ip": "94.127.55.29",
        "geoLongitude": "12.5221",
        "url": "/v1/images/697c6837-c2e0-4535-a91d-3dbc146d551b",
        "geoCity": "Frederiksberg",
        "height": 4032,
        "geoTimezone": "Europe/London",
        "groupId": "05cf9123-c3d7-4ca3-be2b-3c2133fed220",
        "modified": "2018-08-24",
        "id": "697c6837-c2e0-4535-a91d-3dbc146d551b",
        "geoCountryName": "Denmark",
        "geoLatitude": "55.6785",
        "createdBy": "ff2a4775-468e-4f41-a16d-75d700b6dd6b",
        "takenAt": "2018-08-20",
        "bytesUsed": 2473733,
        "geoRegionName": "Europe/London",
        "width": 3024,
        "deleted": False,
        "created": "2018-08-22",
        "geoRegionCode": "84"
    },
    {
        "geoCountryCode": "DK",
        "format": "JPEG",
        "ip": "94.127.55.29",
        "geoLongitude": "12.5221",
        "url": "/v1/images/b8a49f4e-beba-4486-bb82-83136738b792",
        "geoCity": "Frederiksberg",
        "height": 4032,
        "geoTimezone": "Europe/Copenhagen",
        "groupId": "af024461-4b1b-49c8-85bf-821396626c8d",
        "modified": "2018-08-24",
        "id": "b8a49f4e-beba-4486-bb82-83136738b792",
        "geoCountryName": "Denmark",
        "geoLatitude": "55.6785",
        "createdBy": "ff2a4775-468e-4f41-a16d-75d700b6dd6b",
        "takenAt": "2018-08-28",
        "bytesUsed": 3487111,
        "geoRegionName": "Europe/Copenhagen",
        "width": 3024,
        "deleted": False,
        "created": "2018-08-28",
        "geoRegionCode": "84"
    },
    {
        "geoCountryCode": "GB",
        "format": "JPEG",
        "ip": "94.127.55.29",
        "geoLongitude": "12.5221",
        "url": "/v1/images/ca9e7e05-bdf9-4711-b506-ed3d85f2b2b5",
        "geoCity": "Frederiksberg",
        "height": 4032,
        "geoTimezone": "Europe/London",
        "groupId": "93d3b2a1-34a0-4cd4-b5d6-9e95d500be8b",
        "modified": "2018-08-24",
        "id": "ca9e7e05-bdf9-4711-b506-ed3d85f2b2b5",
        "geoCountryName": "England",
        "geoLatitude": "55.6785",
        "createdBy": "ff2a4775-468e-4f41-a16d-75d700b6dd6b",
        "takenAt": "2018-08-28",
        "bytesUsed": 2528287,
        "geoRegionName": "Europe/London",
        "width": 3024,
        "deleted": False,
        "created": "2018-08-28",
        "geoRegionCode": "84"
    },
    {
        "geoCountryCode": "DK",
        "format": "JPEG",
        "ip": "94.127.55.27",
        "geoLongitude": "12.5221",
        "url": "/v1/images/e8dd45e5-abe6-404a-be22-ed3c515ac417",
        "geoCity": "Frederiksberg",
        "height": 1280,
        "geoTimezone": "Europe/Copenhagen",
        "groupId": "44fe251f-1d3a-4198-9a98-209fdad52c13",
        "modified": "2018-08-22",
        "id": "e8dd45e5-abe6-404a-be22-ed3c515ac417",
        "geoCountryName": "Denmark",
        "geoLatitude": "55.6785",
        "createdBy": "ff2a4775-468e-4f41-a16d-75d700b6dd6b",
        "takenAt": "2018-08-22",
        "bytesUsed": 89017,
        "geoRegionName": "Europe/Copenhagen",
        "width": 960,
        "deleted": False,
        "created": "2018-08-22",
        "geoRegionCode": "84"
    },
    {
        "geoCountryCode": "GB",
        "format": "JPEG",
        "ip": "94.127.55.29",
        "geoLongitude": "12.5221",
        "url": "/v1/images/ebc98bd7-d6b1-4bab-8660-066a4206f595",
        "geoCity": "Frederiksberg",
        "height": 4032,
        "geoTimezone": "Europe/London",
        "groupId": "9cd2bde9-93ef-4afc-be48-5f65d4f18ce4",
        "modified": "2018-08-24",
        "id": "ebc98bd7-d6b1-4bab-8660-066a4206f595",
        "geoCountryName": "England",
        "geoLatitude": "55.6785",
        "createdBy": "ff2a4775-468e-4f41-a16d-75d700b6dd6b",
        "takenAt": "2018-08-19",
        "bytesUsed": 2898097,
        "geoRegionName": "Europe/London",
        "width": 3024,
        "deleted": False,
        "created": "2018-08-19",
        "geoRegionCode": "84"
    }
]


#TODO: Create a function that returns a list of URLs of all the images
def get_all_urls():
    urls = []
    for image in images:
        urls.append(image["url"])
    return urls


#print("all urls")
#print(get_all_urls())

#TODO: Create a function that returns a list of URLs of all the images taken in Copenhagen
def get_all_urls_for_copenhagen(region):
    urls = []
    for image in images:
        if region in image['geoRegionName']:
            urls.append(image['url'])

    return urls


#print("Images of Copenhagen")
#print(get_all_urls_for_copenhagen("Europe/Copenhagen"))

#TODO: Make this function more generic, so it can take in any location, not just Copenhagen

#TODO: Create a function that returns a list of URLs of all the images that were taken today

def get_all_urls_for_date(date):
    urls = []
    for image in images:
        if date in image['takenAt']:
            urls.append(image['url'])

    return urls


today = "2018-08-28"

#print("Pictures from today")
#print(get_all_urls_for_date(today))


choice = input("What filter would you like to use? All, Date, Location?").lower()

if choice == "all":
    print(get_all_urls())
elif choice == "date":
    date = input("Which date? format: 'yyyy-mm-dd'").lower()
    print(get_all_urls_for_date(date))
elif choice == "location":
    location = input("Which locations? London or Copenhagen?").lower()
    if location == "london":
        print(get_all_urls_for_copenhagen("Europe/London"))
    elif location == "copenhagen":
        print(get_all_urls_for_copenhagen("Europe/Copenhagen"))
    else:
        print("There are no results from the query")

