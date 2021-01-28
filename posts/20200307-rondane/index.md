---
title: "Rondane"
date: 2020-03-07T13:27:23+02:00
type: "posts"
draft: false
tags:
    - rondane
categories:
    - outdoors
    - skimo
mastodonurl: ""
twitterurl: ""
instagramurl: ""
pixelfedurl: ""
image: "posts/20200307-rondane/20200307-rondane-1.jpg"
---

Tidlig i mars hadde det kommet unormalt mye snø i Rondane, og jeg
utnytta muligheten til å dra på topptur i området. Planen var egentlig å
få gått en runde over noen av toppene over 2000 moh, men mye dyp snø og
skredfare gjorde at jeg snudde ved Midtronden, og gikk samme vei
tilbake.

Nederst på sida ligger en video fra turen.

<!--more--> 

{{< rawhtml >}}
<link rel="stylesheet" href="js/leaflet/leaflet.css" />
<script src="js/leaflet/leaflet.js"></script>
<script src="js/gpx.js"></script>

<div id="map" style="height: 400px; width: 100%;"></div>

<script>
        var map = L.map('map');//.setView([60.14, 10.25], 11);
        L.tileLayer('https://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=topo4&zoom={z}&x={x}&y={y}', {
            attribution: '<a href="http://www.kartverket.no/">Kartverket</a>'
        }).addTo(map);
        var gpx = 'posts/20200307-rondane/activity-20200307.gpx'; 
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
{{< /rawhtml >}}


![](posts/20200307-rondane/20200307-rondane-1.jpg)
På vei oppover bjørkeskogen.

![](posts/20200307-rondane/20200307-rondane-3.jpg)
På toppen av Høgronden med utsikt mot Rondeslottet.

![](posts/20200307-rondane/20200307-rondane-4.jpg)
De to Midtrondene i sikte.

![](posts/20200307-rondane/20200307-rondane-5.jpg)
Flanken til høyre hadde jeg opprinnelig tenkt å stå ned, men der var det

![](posts/20200307-rondane/20200307-rondane-6.jpg)
På toppen av Midtronden Aust, med utsikt mot Midtronden Vest.

![](posts/20200307-rondane/20200307-rondane-9.jpg)
Sola nærmer seg horisonten, rett over Rondeslottet.

![](posts/20200307-rondane/20200307-rondane-10.jpg)
Nede igjen ved Gammelgarden.

{{< rawhtml >}}
<video id="video" width="640" height="480" controls>
    <source src="posts/20200307-rondane/20200307-rondane-video.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video> 
{{< /rawhtml >}}
