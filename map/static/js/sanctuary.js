var sanctuary = (function() {
    
  var map, mapboxToken = 'pk.eyJ1Ijoib3VycmV2b2x1dGlvbiIsImEiOiJjaXl4aWlrc3IwMDlzMzJycXJqejNmcTVnIn0.ufXFguXsHIg_J7z96ZTn7A';
    
  function init(mapDiv) {
    initMap(mapDiv);
  }
  
  function initMap(mapDiv) {  
    map = L.map(mapDiv).setView([37.8, -96.9], 4);
    
    var baseLayer = L.tileLayer('https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=' + mapboxToken, {
        maxZoom: 18 
      }
    ).addTo(map);
  }
  
  function getAddress() {
    var geometry, place = autocomplete.getPlace();

    if (!place.geometry) {
      // TODO: Display this in .app__info
      console.log("We can't find that place - try again.");
      return;
    } else {
      geometry = [place.geometry.location.lat(),place.geometry.location.lng()]; 
      positionMap(geometry);
    }
  }
  
  function positionMap(geometry) {       
    console.log(map);   
    map.flyTo(geometry, 12, {duration:1});
  }
  
  function monitorAPI(input) {
    var defaultPlaceholder = input.placeholder;

    setTimeout(function(){
      
        input.value = '';
        setInterval(function(){
          
          if(input.placeholder.indexOf('Oops') != -1){

            // undo Google grossness
            input.placeholder = defaultPlaceholder;
            input.removeAttribute('disabled');
            input.removeAttribute('style');
            input.classList.remove('gm-err-autocomplete');

            // kill events
            var clone = input.cloneNode(true);
            input.parentNode.replaceChild(clone, input);
          }
        }, 200);
    }, 500);
  }
  
  function paintGeoJson(geometry, options) {
    var feature = L.geoJson(geometry, options);
            
    feature.addTo(map);
    // map.fitBounds(feature.getBounds());
  }
  
  return {
    init: init,
    paintGeoJson: paintGeoJson,
    map: this.map,
    getAddress: getAddress,
    mapboxToken: mapboxToken
  }
  
})();

var autocomplete;

function initAutocomplete() {		
  var input = document.getElementById('autocomplete');
  
  autocomplete = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */(input),
    {
      types: ['geocode'],
      componentRestrictions: {country: "us"}
    }
  );

  autocomplete.addListener('place_changed', sanctuary.getAddress);
}
