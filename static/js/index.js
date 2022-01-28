var map = L.map("map").setView([66, 26], 4);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

/* NOSONAR
L.marker([51.5, -0.09])
  .addTo(map)
  .bindPopup("A pretty CSS3 popup.<br> Easily customizable.")
  .openPopup();*/

var marker;

function onMapClick(e) {
  if (marker != undefined) {
    map.removeLayer(marker);
  }

  console.log(e.latlng);
  marker = L.marker(e.latlng).addTo(map);
}

async function load_geojson() {
  const response = await fetch("/static/data/suomi.geojson");
  const data = await response.json();
  console.log(data);
  L.geoJson(data).addTo(map);
}

load_geojson();

map.on("click", onMapClick);
