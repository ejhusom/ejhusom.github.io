---
title: "Maridalen"
date: 2019-03-10T13:27:23+02:00
type: "posts"
draft: false
tags:
    - nordmarka
categories:
    - outdoors
mastodonurl: ""
twitterurl: ""
instagramurl: ""
pixelfedurl: ""
---

<!--more-->
{{< rawhtml >}}
<link rel="stylesheet" href="js/leaflet/leaflet.css" />
<script src="js/leaflet/leaflet.js"></script>
<script src="js/gpx.js"></script>

<div id="map" style="height: 400px; width: 100%;"></div>

<script>
        var map = L.map('map');//.setView([60.14, 10.25], 11);
        L.tileLayer('http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=topo4&zoom={z}&x={x}&y={y}', {
            attribution: '<a href="http://www.kartverket.no/">Kartverket</a>'
        }).addTo(map);
        var gpx = 'posts/20190310-maridalen/høgruta-i-maridalen.gpx'; 
        new L.GPX(gpx, {
            async: true,
            marker_options: {
                startIconUrl: '../images/pin-icon-start.png',
                endIconUrl:   '../images/pin-icon-end.png',
                shadowUrl:    '../images/pin-shadow.png',
                //clickable: true,
                //showRouteInfo: true
            },
        }).on('loaded', function(e) {
            map.fitBounds(e.target.getBounds());
        }).addTo(map);
</script>
{{< /rawhtml >}}

![](posts/20190310-maridalen/maridalen01.jpg)
![](posts/20190310-maridalen/maridalen02.jpg)
![](posts/20190310-maridalen/maridalen03.jpg)
