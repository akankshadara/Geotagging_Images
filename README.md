# Geotagging_Images
A python script to extract the exif data from an image file. The latitude and longitude information from this exif data is used to specify the street address of the image. 

**Required Dependecies:** 
1.) exifread
2.) requests
3.) json


**Usage:** 

Execute the following command on the command line:
```{r, engine='bash', count_lines}
python geotagging.py test.jpeg
```

**Sample Output:** 
```
Key: GPS GPSLatitudeRef, value S
Key: GPS GPSLatitude, value [37, 49, 256/25]
Key: GPS GPSLongitudeRef, value E
Key: GPS GPSLongitude, value [144, 56, 2247/100]
Key: GPS GPSAltitudeRef, value 0
Key: GPS GPSAltitude, value 4013/692
Key: GPS GPSTimeStamp, value [7, 11, 17]
Key: GPS GPSSpeedRef, value K
Key: GPS GPSSpeed, value 0
Key: GPS GPSImgDirectionRef, value T
Key: GPS GPSImgDirection, value 8086/73
Key: GPS GPSDestBearingRef, value T
Key: GPS GPSDestBearing, value 8086/73
Key: GPS GPSDate, value 2017:08:27
Key: GPS Tag 0x001F, value 5
--------------------------------------------------------------------
Latitude: -37.81666666666667, Longitude: 144.93333333333334
Geolocation of image is: 
Citylink, Docklands VIC 3008, Australia
--------------------------------------------------------------------

```
