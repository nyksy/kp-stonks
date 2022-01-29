//leaflet
var map = L.map("map").setView([66, 26], 4);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

var marker = L.marker([62.601440207749064, 29.756984710693363]).addTo(map).openPopup();

/**
 * Händlätään kartan klikkaus eli siirretään markkeri ja haetaan uusi hinta
 * @param {event} e
 */
async function onMapClick(e) {
  const pricetag = document.getElementById("price-amount");
  pricetag.textContent = "Ladataan...";

  if (marker != undefined) {
    map.removeLayer(marker);
  }

  console.log(e.latlng);
  marker = L.marker(e.latlng).addTo(map);

  //passataan koordinaatit flaskille
  const coord = e.latlng; // no need for toString()
  const lat = coord.lat;
  const lng = coord.lng;

  const res = await fetch(
    "/loc?" +
    new URLSearchParams({
      lat: lat,
      lng: lng,
    })
  );

  const price = await res.text()
  console.log(price);

  pricetag.textContent = price;
}

async function load_geojson() {
  const response = await fetch("/static/data/suomi.geojson");
  const data = await response.json();
  console.log(data);
  L.geoJson(data).addTo(map);
}

//TODO geojson, jossa pelkästään kunnat, joista löytyy kotipizza?
//TODO tai sitten kaikki kotipizzat 
load_geojson();

map.on("click", onMapClick);
