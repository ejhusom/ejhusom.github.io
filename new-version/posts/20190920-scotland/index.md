---
title: "Skyline Scotland"
date: 2019-09-20T13:27:23+02:00
type: "posts"
draft: false
tags:
    - race
    - scotland
categories:
    - running
mastodonurl: ""
twitterurl: ""
instagramurl: ""
pixelfedurl: ""
image: "posts/20190920-scotland/scotland11.jpg"
---

<!--more--> 
<link rel="stylesheet" href="js/leaflet/leaflet.css" />
<script src="js/leaflet/leaflet.js"></script>
<script src="js/gpx.js"></script>

<div id="map" style="height: 400px; width: 100%;"></div>
<figcaption>Map of the Glen Coe Skyline route.</figcaption>

<script>
        var map = L.map('map');//.setView([60.14, 10.25], 11);
        L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
            maxZoom: 17,
            attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
        }).addTo(map);
        var gpx = 'posts/20190920-scotland/activity-20190922-glen-coe-skyline.gpx'; 
        new L.GPX(gpx, {
            async: true,
            marker_options: {
                startIconUrl: 'img/pin-icon-start.png',
                endIconUrl:   'img/pin-icon-end.png',
                shadowUrl:    'img/pin-shadow.png',
                //clickable: true,
                //showRouteInfo: true
            },
        }).on('loaded', function(e) {
            map.fitBounds(e.target.getBounds());
        }).addTo(map);
</script>

![](posts/20190920-scotland/scotland01.jpg)
View from Na Gruagaichean, the finish line of Mamores VK.

![](posts/20190920-scotland/scotland02.jpg)
The final ridge of Mamores VK.

![](posts/20190920-scotland/scotland03.jpg)
Scottish sunset 1.

![](posts/20190920-scotland/scotland04.jpg)
Scottish sunset 2.

![](posts/20190920-scotland/scotland05.jpg)
Scottish sunset 3.

![](posts/20190920-scotland/scotland06.jpg)
The gear I used during Glen Coe Skyline (I brought only some of the food
shown in the picture.)

![](posts/20190920-scotland/scotland07.jpg)
Nervous atmosphere before the start of Glen Coe Skyline.

![](posts/20190920-scotland/scotland08.jpg)
I was running at the tail of the lead pack during the first kilometers
of the race.

![](posts/20190920-scotland/scotland09.jpg)
This was the last picture I took during the race. At this point I
understood that things were going much better than expected, and I
needed to stop fumbling around with my GoPro camera.

![](posts/20190920-scotland/scotland10.jpg)
Finally done.

![](posts/20190920-scotland/scotland11.jpg)
Can\'t describe the feelings I had at this moment.

![](posts/20190920-scotland/scotland12.jpg)
A trophy and money. Best prize ever.

![](posts/20190920-scotland/scotland13.jpg)
Rather happy to be on that list of names. Photo credit: Skyline
Scotland.
