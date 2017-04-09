var map;

function initMap() {
    // Create a map object and specify the DOM element for display.
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        scrollwheel: false,
        zoom: 8
    });

    // var src = []
    // for (var i = 40; i < 47; i++) {
    //     src[i] = 'http://www.nhc.noaa.gov/storm_graphics/api/AL142016_0' + i + 'adv_TRACK.kmz';
    //     var kmlLayer = new google.maps.KmlLayer(src[i], {
    //         suppressInfoWindows: true,
    //         preserveViewport: false,
    //         map: map
    //     });
    //     kmlLayer.addListener('click', function(event) {
    //         var content = event.featureData.infoWindowHtml;
    //         var testimonial = document.getElementById('capture');
    //         testimonial.innerHTML = content;
    //     });
    // }

    var src = 'http://localhost:8000/AL142016_015adv_TRACK.kmz';
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
