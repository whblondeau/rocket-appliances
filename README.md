#rocket-appliances: a geospatial domain language

**rocket-appliances** is a design for a programming language. 

The name was adopted partly as an homage to the Canadian TV show [Trailer Park Boys](http://en.wikipedia.org/wiki/Trailer_Park_Boys) and partly as an act of desperation when all reasonable portmanteau forms of "gis", "geo", projection", "viewport", "wireframe", and "territory" were shown to be already colonized in googlespace - whether as the name of an existing company or product, or as a term of art in various communities of practice.

`rocket-appliances` is intended to be an analysis and investigation tool. It's probably not worth ever implementing; but that doesn't matter. The value of this language lies in designing it: by forcing the strict definition of the core data structures and operations of a generic geospatial language, `rocket-appliances` will hopefully create a general operational model that can underwrite attempts to teach, explain, learn, and analyze the assets and behavior of various resources and systems.

## rocket-appliances fundamentals
`rocket-appliances` is built around the logical model of how geographic projections provide structure to an interactive map. It involves five basic elements, or, as we might as well call them, _appliances_:

- The Wireframe Earth

- A Cartographic Projection

- The Flatland

- The Map

- The Territory

### Wireframe Earth
We start with the _Wireframe Earth_ (often simply _Wireframe_), which is a familiar concept. (Note that its right cartographic name is a [reference ellipsoid](http://en.wikipedia.org/wiki/Reference_ellipsoid); but "Wireframe Earth" seems more salient as an introductory term.) The Wireframe Earth is a representation of the Globe as an immaterial ellipsoidal surface traced with angular coordinates, normally latitude and longitude. Sometimes, for geodetic purposes, a radial scalar z-coordinate is added. The Wireframe Earth has no other properties. 

For a decent short discussion of the underlying reasoning and model of the Wireframe earth, see [http://www.georeference.org/doc/the_earth_as_an_ellipsoid.htm](http://www.georeference.org/doc/the_earth_as_an_ellipsoid.htm).


The purpose of the Wireframe Earth is to establish a notional space of geographic reference: a "Real Location" not subject to the mathematical distortions of projecting a spherical surface onto a flat plane.

### Cartographic Projection
Every ultimately two-dimensional map is based on three steps. 

This is the first of those steps. A _Cartographic Projection_ is a mathematical projection of the wireframe onto a [developable surface](http://en.wikipedia.org/wiki/Developable_surface). In Wikipedia's words, 
a developable surface "can be flattened onto a plane without distortion". Another way of describing a developable surface is one having only _simple_ curvature. 

A sphere has _compound curvature_, which is why projections are necessary. A projection is a way of compressing and stretching regions of the spherical Earth until they do, in fact, fit onto a developable surface without further modification.

The number of possible mathematical projections of the Earth's surface onto a developable surface is, in principle, infinite. In practice, the number of actual projections that cartographers choose to work with is quite a bit smaller than infinity. The International Association of Oil and Gas Producers, which has deep pockets and a vested interest in being able to precisely identify geographical locations, maintains one of the most complete registries of projections. This is accessible through its [Geomatics Committee web page](http://www.ogp.org.uk/committees/geomatics/). A more reasonably accessible [survey of a few of the most commonly used projections](http://egsc.usgs.gov/isb//pubs/MapProjections/projections.html), as well as some solid conceptual background, is available via the US Geological Survey's Publications Warehouse. (The Pubs warehouse itself is located at [http://egsc.usgs.gov/isb//pubs/MapProjections/projections.html](http://egsc.usgs.gov/isb//pubs/MapProjections/projections.html). Lots of good stuff there.)

### Flatland

One often neglected aspect of map projections is that the projection surface is not always a flat plane. Flat planes are an important concept, since maps are typically represented on a flat 2-dimensional surface (paper or computer screen display.)

Most projections include the flattening procedure as a natural part of the projection itself, which is a sensible way to think about it. However, for reasons of fussy clarity, it's worthwhile to call out the end product of the Projection as an explicitly two-dimensional surface. History and custom weigh in favor of calling this surface _Flatland_.

Flatland refers to the entire extent of the projected surface of Wireframe Earth. Most projections can't display the entire Earth in the first place (for example, Mercator projections increase vertically without bound as the projection approaches the Poles. There's nothing _mathematically_ wrong with that, but it's not useful for cartography. By custom, the Mercator flatland is terminated within 5 degrees of the Poles.

One important aspect of the flattening of the projected surface into Flatland is that cylindrical and conic projections must be _cut_ at some point. The traditional cut location when flattening a Mercator projection is the 180th meridian. Choice of a cut location for conic projections is a little more complicated, since it anticipates the subset of the projection to be viewed.

### The Map

A Map, in the accustomed sense of a paper roadmap or topo map or nautical chart, is a static viewport, almost always rectangular in shape (polar regions are often mapped to circles because the corners of rectangles become distorted to the point of uselessness in many polar projections that cover large amounts of territory) laid onto Flatland. The smaller the viewport in relation to the Flatland upon which it's drawn, the more detailed close-up view it affords of the corresponding surface. 

In traditional cartography, the relationship between the extent of Earth's surface shown on a map, and the physical size of the map, is called _scale_. When we get to electronic map displays, the map is subject to _zoom_ (change in scale), _translation_ (change in location), and sometimes _rotation_ (change in coordinate orientation with respect to the map's orientation.) The first two actions are completely natural and familiar to users of popular map systems - Google Maps, Yahoo Maps, and so on. They don't change much when you get to more precise mapping displays such as professional or military GIS systems.

The Map is, in principle, an interactive artifact. It provides all kinds of information about the portion of the Earth's surface it's displaying; in turn, you issue instructions about what else you want to see, or add observations of your own. Some of those are important records (surveying); some are of only transient importance (position plotting). It's very important to grasp this fact: maps and charts are, fundamentally, two-way information channels.

("Interactive" doesn't mean "computerized", by the way. I used to navigate at sea, and I can assure you that patiently and carefully erasing penciled position fixes, dead reckoning tracks, and so on from hydrographic charts is the moral equivalent of refreshing the computer display. Just more time-consuming, painstaking, and manual. But we _definitely_ interacted with those charts.) 



The interactive map is, in concept, a dimensioned _geographical representation surface_ ('g-surf'). The g-surf has three important properties: 

- the _coordinate system_, which is a system for specifying geospatial location.

- the _territory_, which is the portion of the Earth's surface being represented.

- the _viewfield_, which is an arbitrary location system, covering the entire g-surf, capable of resolving a location down to a single pixel in a raster-rendered view.

The territory is a dependent variable. It is determined by

	- a single location in the coordinate system, the _attachment point_;

	- a scaling factor, _zoom_ or _apparent altitude_, which expresses the amount of actual physical geography displayed in the viewfield;

	- the projection of the coordinate system, which will cause various points to be 

Note that the attachment point, being a single location, remains identical if the coordinate system of the territory

The reference is not inherently static: it's subject to pan, zoom, and rotation in the general case. The coordinate system can also be _reprojected_, i.e. converted to a different coordinate system. Reprojection does not alter the territory; only teleportation does that.


