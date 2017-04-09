var map;
var src = 'http://www.nhc.noaa.gov/storm_graphics/api/AL142016_036adv_CONE.kmz';
var src2 = 'http://www.nhc.noaa.gov/storm_graphics/api/AL012016_002adv_TRACK.kmz';
function initMap() {
        // Create a map object and specify the DOM element for display.
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          scrollwheel: false,
          zoom: 8
        });

        var kmlLayer = new google.maps.KmlLayer(src, {
                  suppressInfoWindows: true,
                  preserveViewport: false,
                  map: map
                });
                kmlLayer.addListener('click', function(event) {
                  var content = event.featureData.infoWindowHtml;
                  var testimonial = document.getElementById('capture');
                  testimonial.innerHTML = content;
                });
      }
