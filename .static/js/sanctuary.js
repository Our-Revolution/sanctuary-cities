var sanctuary = (function($) {
    
  var map, active = null, usedSearch = false, palceName = null, data = {}, match=false, mapboxToken = 'pk.eyJ1Ijoib3VycmV2b2x1dGlvbiIsImEiOiJjaXl4aWlrc3IwMDlzMzJycXJqejNmcTVnIn0.ufXFguXsHIg_J7z96ZTn7A';
    
  function init(mapDiv) {
    initMap(mapDiv);
  }
  
  function initMap(mapDiv) {  
    map = L.map(mapDiv).setView([37.8, -96.9], 4);
    
    var baseLayer = L.tileLayer('https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=' + mapboxToken, {
        maxZoom: 18 
      }
    ).addTo(map);
    
    $(map).on('zoomend', function() {
      
      // only do this after user has used search box
      if (usedSearch) {
        getLocationsWithinBounds(map.getBounds());
      }  
    })
    
    // populate(map);
  }
  
  function getAddress() {
    var geometry, place = autocomplete.getPlace();
    usedSearch = true;

    if (!place.geometry) {
      // TODO: Display this in .app__info
      console.log("We can't find that place - try again.");
      return;
    } else {
      if (place.name) {
        placeName = place.name;
      }
      geometry = [place.geometry.location.lat(),place.geometry.location.lng()]; 
      positionMap(geometry);
    }
  }
  
  function positionMap(geometry) {   
    map.flyTo(geometry, 8, {duration:1});
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
  
  function addFeature(feature) {
    feature.addTo(map);
  }
  
  function paintGeoJson(geometry, options) {
    var feature = L.geoJson(geometry, options);
    
    feature.addTo(map);
  }

  function populate() {
    $.ajax({
      url: "/api/1/territories",
      data: {
        'lat':47.606209,
        'lng':-122.332071
      }
    }).done( function(data) {
      $.each(data, function(key) {
        paintGeoJson(JSON.parse(data[key]))
        updateInfo(JSON.parse(data[key])['features'])
      })
    })
  }
  
  function resetInfo() {
    $('.app-info__status').html('');
    console.log('reset')
  }
  
  function getColor(feature) {
    if(feature.properties.model == "map.state") {      
      if(feature.properties.limited_ice_cooperation == "yes-by-law") {
        color = "#bf2";
      } else if(feature.properties.limited_ice_cooperation == "yes-in-practice") {
        color = "#ff8";
      } else if(feature.properties.limited_ice_cooperation == "unlimited") {
        color = "#f22";
      } else {
        color = "#bf2";
      }
    } else if (feature.properties.model == "map.city") {
      if(feature.properties.limited_ice_cooperation == "yes-by-law") {
        color = "#9d0";
      } else if(feature.properties.limited_ice_cooperation == "yes-in-practice") {
        color = "#dd6";
      } else if(feature.properties.limited_ice_cooperation == "unlimited") {
        color = "#d00";
      } else {
        color = "#999";
      }
    } else if (feature.properties.model == "map.county") {
      if(feature.properties.jails_honor_ice_detainers == "yes-by-law") {
        color = "#9d0";
      } else if(feature.properties.jails_honor_ice_detainers == "yes-in-practice") {
        color = "#dd6";
      } else if(feature.properties.jails_honor_ice_detainers == "unlimited") {
        color = "#d00";
      } else {
        color = "#999";
      }
    } else {
      color = "#000";
    }
    
    return color;
  }
  
  function updateInfo(layers) {
    resetInfo();
    
    for (var i=0; i<layers.length; i++) {
    
      var description, name = "";
      
      if(layers[i].properties.model == "map.county") {
        name = layers[i].properties.name;
        
        if (!layers[i].properties.jails_honor_ice_detainers_short_answer.includes('N/A')) {
          description = layers[i].properties.jails_honor_ice_detainers_short_answer;
        }
      } else {
        name = layers[i].properties.name;
        
        if (!layers[i].properties.limited_ice_cooperation_short_answer.includes('N/A')) {
          description = layers[i].properties.limited_ice_cooperation_short_answer;
        }
      }
      
      if (!description) {
        description = "Click the button below to learn more about " + layers[i].properties.name + "'s policies and how you can get involved."
      }
                
      layers[i].options.oldColor = layers[i].options.color;
      
      $('.app-info__status').append('\
        <div class="component">\
          <div class="component__heading">\
            <h4 class="component__name">' + name + '</h4>\
          </div>\
          <div class="component__info">\
            <p class="component__description">\
              ' + description + '\
            </p>\
            <a href="/'+ layers[i].properties.slug +'" class="component__cta btn btn-block btn-success btn-uppercase">Get Involved</a>\
          </div> \
        </div>\
      ');
      
      if(i==0 && layers.length>1 && match) {
        $('.app-info__status').append('\
        <div class="component">\
          <div class="component__heading component__heading--dark">\
            <h4 class="component__name">Nearby Communities</h4>\
          </div>\
        </div>\
        ');
      }
      
    }
    
  }
  
  function getLocationsWithinBounds(bounds) {
    var layers = [], t0 = performance.now();
    
    match = false;
    
    map.eachLayer(function (layer) {
      if(layer.properties) {
        layer.eachLayer(function (sublayer) {              
          if(bounds.intersects(sublayer.getBounds())) {
            if (layer.properties.name.indexOf(placeName) >= 0) {
              // add to front of array if we have a match on what they typed
              console.log('match');
              console.log(layer);
              match = true;
              $.each(layer._layers, function() {
                setActive(this);
                var bounds = this.getBounds();
      			    map.flyToBounds(bounds, 12, {duration:1});
              })
              
              // setActive(layer);
              layers.unshift(layer);
            } else {
              layers.push(layer);
            }
          }
        })
      }
      
    });
    
    if (layers.length == 0) {
      resetInfo();
      $('.app-info__status').append('\
          <p class="pa4">\
            <strong>We haven\'t made it to this place yet.</strong> Want to help document this area\'s policies? Let us know at <a href="mailto:sanctuary@ourrevolution.com">sanctuary@ourrevolution.com</a>.\
          </p>');
    } else {
      updateInfo(layers);
    }
    
    var t1 = performance.now();
    console.log("Call took " + (t1 - t0) + " milliseconds.")
    usedSearch = false;
    map.invalidateSize();
  }
  
  function setActive(layer) {
    // layer.options.oldColor = layer.options.color;
    
    if(active) {
      var oldLayer = map._layers[active];
      console.log(oldLayer)
      oldLayer.setStyle({"color": oldLayer.defaultOptions.color})
    } 
    
    layer.setStyle({"color":"#78a515"});
    
    active = layer._leaflet_id;
  }
  
  function getActive() {
    return active;
  }
  
  function getMap() {
    return map;
  }
  
  return {
    init: init,
    paintGeoJson: paintGeoJson,
    getMap: getMap,
    getAddress: getAddress,
    data: data,
    addFeature: addFeature,
    updateInfo: updateInfo,
    getLocationsWithinBounds: getLocationsWithinBounds,
    getColor: getColor,
    setActive: setActive,
    getActive: getActive
  }
  
})(jQuery);

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