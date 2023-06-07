var geojsonMarkerOptions = {
  radius: 8,
  fillColor: "#ff7800",
  color: "#000",
  weight: 1,
  opacity: 1,
  fillOpacity: 0.8
};

var map = L.map('map', {
  'center': [37.466513, -77.428683],
  'zoom': 12,
  'layers': [
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      'attribution': 'Map data &copy; OpenStreetMap contributors'
    })
  ]
});

$.getJSON('data.geojson', function (geojson) {
  L.geoJson(geojson, {
    onEachFeature: function (feature, layer) {
      layer.bindPopup(feature.properties.name);
    },
    pointToLayer: function (feature, latlng) {
      return L.circleMarker(latlng, geojsonMarkerOptions);
    }
  }).addTo(map);
});




