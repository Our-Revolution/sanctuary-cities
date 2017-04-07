var sanctuary = (function($) {
    
  var map, active = null, usedSearch = false, palceName = null, data = {}, match=false, mapboxToken = 'pk.eyJ1Ijoib3VycmV2b2x1dGlvbiIsImEiOiJjaXl4aWlrc3IwMDlzMzJycXJqejNmcTVnIn0.ufXFguXsHIg_J7z96ZTn7A';
    
  function init(mapDiv) {
    initMap(mapDiv);
  }
  
  function initMap(mapDiv) {  
    map = L.map(mapDiv);
    map.setView([37.8, -96.9], 4);
    
    var baseLayer = L.tileLayer('https://api.mapbox.com/styles/v1/ourrevolution/cj136j7f100042rrvmy6zw2u8/tiles/256/{z}/{x}/{y}?access_token=' + mapboxToken, {
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
      color = "#0167D2";
      // if(feature.properties.limited_ice_cooperation == "yes-by-law") {
      //   color = "#bf2";
      // } else if(feature.properties.limited_ice_cooperation == "yes-in-practice") {
      //   color = "#ff8";
      // } else if(feature.properties.limited_ice_cooperation == "unlimited") {
      //   color = "#f22";
      // } else {
      //   color = "#bf2";
      // }
    } else if (feature.properties.model == "map.city") {
      color = "#0A82FF";
      // if(feature.properties.limited_ice_cooperation == "yes-by-law") {
      //   color = "#9d0";
      // } else if(feature.properties.limited_ice_cooperation == "yes-in-practice") {
      //   color = "#dd6";
      // } else if(feature.properties.limited_ice_cooperation == "unlimited") {
      //   color = "#d00";
      // } else {
      //   color = "#999";
      // }
    } else if (feature.properties.model == "map.county") {
      color = "#218fff";
      // if(feature.properties.jails_honor_ice_detainers == "yes-by-law") {
      //   color = "#9d0";
      // } else if(feature.properties.jails_honor_ice_detainers == "yes-in-practice") {
      //   color = "#dd6";
      // } else if(feature.properties.jails_honor_ice_detainers == "unlimited") {
      //   color = "#d00";
      // } else {
      //   color = "#999";
      // }
    } else {
      color = "#000";
    }
    
    return color;
  }
  
  function updateInfo(layers) {
    resetInfo();
    
    for (var i=0; i<layers.length; i++) {
    
      var description = "", name = "", policy_summary = {'good': [], 'bad': []};
      
      name = layers[i].properties.name;
            
      if (layers[i].properties.model == "map.county") {
        if (layers[i].properties.jails_honor_ice_detainers == 'yes-by-law' || layers[i].properties.jails_honor_ice_detainers == 'yes-in-practice') {
          policy_summary.good.push('Jails do not honor ICE detainers');
        } else if (layers[i].properties.jails_honor_ice_detainers == 'unlimited') {
          policy_summary.bad.push('Jails honor ICE detainers');
        }
        
        if(layers[i].properties.jails_prohibit_inquiries == true) {
          policy_summary.good.push('Jails prohibit inquiries into immigration status and/or place of birth');
        } else if (layers[i].properties.jails_prohibit_inquiries == false) {
          policy_summary.bad.push('Jails do not prohibit inquiries into immigration status and/or place of birth');
        }
        
        if(layers[i].properties.ice_contracts == true) {
          policy_summary.bad.push('Participates in programs like 287(g)');
        } else if (layers[i].properties.ice_contracts == false) {
          policy_summary.good.push('Does not participate in programs like 287(g)');
        }
        
        if(layers[i].properties.isga == true) {
          policy_summary.bad.push('Jails have an IGSA');
        } else if (layers[i].properties.isga == false) {
          policy_summary.good.push('Jails don\'t have an IGSA');
        }
        
        if(layers[i].properties.preventing_policies == true) {
          policy_summary.good.push('Prevents local police from acting as immigration agents');
        } else if (layers[i].properties.preventing_policies == false) {
          policy_summary.bad.push('Does not prevent local police from acting as immigration agents');
        }
        
        if(layers[i].other_policies_and_services) {
          policy_summary.good.push('Has implemented other policies more welcoming to immigrants, people of color, the LGBTQ community or religious minorities');
        }
        
        if(layers[i].properties.permitting_policies == true) {
          policy_summary.bad.push('Permits local police from acting as immigration agents');
        } else if (layers[i].properties.permitting_policies == false) {
          policy_summary.good.push('Does not permit local police from acting as immigration agents');
        }
          
      } else if (layers[i].properties.model == "map.city") {        
        
        if (layers[i].properties.limited_ice_cooperation == 'yes-by-law' || layers[i].properties.limited_ice_cooperation == 'yes-in-practice') {
          policy_summary.good.push('Limited cooperation with ICE');
        } else if (layers[i].properties.limited_ice_cooperation == 'unlimited') {
          policy_summary.bad.push('Cooperates with ICE');
        }
        
        if (layers[i].properties.participate_287g_program == true) {
          policy_summary.bad.push('Participates in the 287(g) program');
        } else if (layers[i].properties.participate_287g_program == false) {
          policy_summary.good.push('Does not participate in the 287(g) program');
        }
        
        if(layers[i].properties.isga == true) {
          policy_summary.bad.push('City jails have an IGSA');
        } else if (layers[i].properties.isga == false) {
          policy_summary.good.push('City jails do not have an IGSA');
        }
        
        if(layers[i].properties.provide_legal_representation == true) {
          policy_summary.good.push('Provides undocumented immigrants with legal representation in court');
        } else if (layers[i].properties.provide_legal_representation == false) {
          policy_summary.bad.push('Does not provide undocumented immigrants with legal representation in court');
        }
        
        if(layers[i].properties.city_services == true) {
          policy_summary.bad.push('Asks about immigration status when applying or accessing city services');
        } else if (layers[i].properties.city_services == false) {
          policy_summary.good.push('Does not ask about immigration status when applying or accessing city services');
        }
        
        if(layers[i].properties.drivers_license == true) {
          policy_summary.good.push('Undocumented immigrants can get driver\'s licenses');
        } else if (layers[i].properties.drivers_license == false) {
          policy_summary.bad.push('Undocumented immigrants cannot get driver\'s licenses');
        }
        
        if(layers[i].properties.separate_form_of_id == true) {
          policy_summary.good.push('Provides form of ID if driver\'s licenses aren\'t available');
        } else if (layers[i].properties.separate_form_of_id == false) {
          policy_summary.bad.push('Does not provide form of ID if driver\'s licenses aren\'t available');
        }
        
        if(layers[i].properties.police_use_body_cameras == true) {
          policy_summary.good.push('City police use body cameras');
        } else if (layers[i].properties.police_use_body_cameras == false) {
          policy_summary.bad.push('City police don\'t use body cameras');
        }
        
        if(layers[i].properties.other_policies_and_services) {
          policy_summary.good.push('Has other policies more welcoming to immigrants, people of color, the LGBTQ community and religious minorities');
        }
        
      } else if (layers[i].properties.model == "map.state") {
        if (layers[i].properties.limited_ice_cooperation == 'yes-by-law' || layers[i].properties.limited_ice_cooperation == 'yes-in-practice') {
          policy_summary.good.push('Limited cooperation with ICE');
        } else if (layers[i].properties.limited_ice_cooperation == 'unlimited') {
          policy_summary.bad.push('Cooperates with ICE');
        }
        
        if(layers[i].properties.ice_contracts == true) {
          policy_summary.bad.push('Has 287(g) contracts or similar');
        } else if (layers[i].properties.ice_contracts == false) {
          policy_summary.good.push('Does not have 287(g) contracts or similar');
        }
        
        if(layers[i].properties.isga == true) {
          policy_summary.bad.push('State jails have an IGSA');
        } else if (layers[i].properties.isga == false) {
          policy_summary.good.push('State jails don\'t have an IGSA');
        }
        
        if(layers[i].properties.provide_legal_representation == true) {
          policy_summary.good.push('Provides undocumented immigrants with legal representation in court');
        } else if (layers[i].properties.provide_legal_representation == false) {
          policy_summary.bad.push('Does not provide undocumented immigrants with legal representation in court');
        }
        
        if(layers[i].properties.drivers_license == true) {
          policy_summary.good.push('Undocumented immigrants can get driver\'s licenses');
        } else if (layers[i].properties.drivers_license == false) {
          policy_summary.bad.push('Undocumented immigrants cannot get driver\'s licenses');
        }
        
        if(layers[i].properties.in_state_tuition == true) {
          policy_summary.good.push('Undocumented immigrants can get in-state tuition at public colleges');
        } else if (layers[i].properties.in_state_tuition == false) {
          policy_summary.bad.push('Undocumented immigrants cannot get in-state tuition at public colleges');
        }
        
        if(layers[i].properties.barrier == true) {
          policy_summary.bad.push('Immigration status acts as a barrier in accessing state services');
        } else if (layers[i].properties.barrier == false) {
          policy_summary.good.push('Immigration status does not act as a barrier in accessing state services');
        }
        
        if(layers[i].properties.policies_against_profiling == true) {
          policy_summary.good.push('Has policies against profiling');
        } else if (layers[i].properties.policies_against_profiling == false) {
          policy_summary.bad.push('Does not have policies against profiling');
        }
        
        if(layers[i].properties.other_policies_and_services) {
          policy_summary.good.push('Has other policies more welcoming to immigrants, people of color, the LGBTQ community and religious minorities');
        }
      }
      
      if (policy_summary.good.length > 0 || policy_summary.bad.length > 0) {
        description = '<h4 class="mt0 fw7">Policy Summary</h4>';
        for (var j = 0; j< policy_summary.good.length; j++) {
          description += '<li class="policy--good">' + policy_summary.good[j] + '</li>';
        }
        
        for (var j = 0; j< policy_summary.bad.length; j++) {
          description += '<li class="policy--bad">' + policy_summary.bad[j] + '</li>';
        }
      } else {
        description = "Click the button below to learn more about " + layers[i].properties.name + "'s policies and how you can get involved."
      }
                      
      layers[i].options.oldColor = layers[i].options.color;
      
      $('.app-info__status').append('\
        <div class="component">\
          <div class="component__heading">\
            <h4 class="component__name">' + name + '</h4>\
          </div>\
          <div class="component__info">\
            <div class="component__description">\
              <ul class="policy-list">\
              ' + description + '\
              </ul>\
            </div>\
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
            <strong>We haven\'t made it to this place yet.</strong> Want to help document this area\'s policies? <a href="https://go.ourrevolution.com/page/s/contribute-sanctuary-policy-info?source=sanctuary-no-data" target="_blank">Click here to let us know</a>.\
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
      oldLayer.setStyle({"fillColor": oldLayer.defaultOptions.fillColor,"fillOpacity":0.5})
    } 
    
    layer.setStyle({"fillColor":"#218fff", "fillOpacity":0.8});
    
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
