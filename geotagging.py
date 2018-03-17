import exifread
import json
import requests
from sys import argv


# Return Exif tags
def extractLatitudeLongitude(img):
    f = open(img, 'rb')
    tags = exifread.process_file(f)
    for tag in tags.keys():
        if tag.startswith("GPS"):
            print ("Key: %s, value %s" % (tag, tags[tag]))

    # d = map(str(tags['GPS GPSLatitude']).split(),int)
    d = str(tags['GPS GPSLatitude'])[1:-1].split(',')[:-1]
    north_south = -1 if (str(tags['GPS GPSLatitudeRef'])=="S") else 1

    d2 = str(tags['GPS GPSLongitude'])[1:-1].split(',')[:-1]
    east_west = -1 if (str(tags['GPS GPSLatitudeRef'])=="W") else 1

    for i,item in enumerate(d):
        d[i] = float(item)

    for i,item in enumerate(d2):
        d2[i] = float(item)

    lat = north_south*(d[0] + d[1]/60) 
    lon = east_west*(d2[0] + d2[1]/60)
    # print (d, degrees)
    return lat, lon

def getplace(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    
    for i in range(10):
        v = str(requests.get(url).text)
        j = json.loads(v)
        # print (j['results'])
        try: 
            z = j['results'][0]['formatted_address']
            break
        except:
            z = None
    # print (z)
    return z
 
if __name__ == '__main__':
    img = str(argv[1])
    lat,lon = extractLatitudeLongitude(img)
    print("--------------------------------------------------------------------")
    print ("Latitude: " + str(lat) + ", Longitude: " + str(lon))
    print("Geolocation of image is: ")
    print(getplace(lat, lon))
    print("--------------------------------------------------------------------")


