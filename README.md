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

### This One Weird Rule of Rocket Appliances

Before looking at each of the appliances in detail, it's important to understand the one geometric rule that relates them:

<blockquote>Any point on any appliance will map to, at most, one point on each of the other appliancess. This mapping establishes a set of up to five "corresponding points", one per appliance. Less than five corresponding points means you'e off the edge someplace.</blockquote>

"Off the edge" cannot apply to the Wireframe Earth, because it by definition includes all points. However, many projections are truncated, so they omit points on the Wireframe Earth's surface. Flatland includes all of the points included in the corresponding projection; but a Map is typically only a subset of Flatland.
 
### Wireframe Earth
We start with the _Wireframe Earth_ (often simply _Wireframe_), which is a familiar concept. (Note that its right cartographic name is a [reference ellipsoid](http://en.wikipedia.org/wiki/Reference_ellipsoid); but "Wireframe Earth" seems more salient as an introductory term.) The Wireframe Earth is a representation of the Globe as an immaterial ellipsoidal surface traced with a _graticule_ of angular coordinates, normally latitude and longitude. Sometimes, for geodetic purposes, a radial scalar z-coordinate is added. The Wireframe Earth has no other properties. 

For a decent short discussion of the underlying reasoning and model of the Wireframe Earth, see [http://www.georeference.org/doc/the_earth_as_an_ellipsoid.htm](http://www.georeference.org/doc/the_earth_as_an_ellipsoid.htm).


The purpose of the Wireframe Earth is to establish a notional space of geographic reference: a "Real Location" not subject to the mathematical distortions of projecting a spherical surface onto a flat plane.

### Cartographic Projection
Every ultimately two-dimensional map is based on three steps. 

This is the first of those steps. A _Cartographic Projection_ is a mathematical projection of the wireframe onto a [developable surface](http://en.wikipedia.org/wiki/Developable_surface). In Wikipedia's words, a developable surface "can be flattened onto a plane without distortion". Another way of describing a developable surface is one having only _simple_ curvature. 

A sphere has _compound curvature_, which is why projections are necessary. A projection is a way of compressing and stretching regions of the spherical Earth until they do, in fact, fit onto a developable surface without further modification.

The number of possible mathematical projections of the Earth's surface onto a developable surface is, in principle, infinite. In practice, the number of actual projections that cartographers choose to work with is quite a bit smaller than infinity. The International Association of Oil and Gas Producers, which has deep pockets and a vested interest in being able to precisely identify geographical locations, maintains one of the most complete registries of projections. This is accessible through its [Geomatics Committee web page](http://www.ogp.org.uk/committees/geomatics/). A more reasonably accessible [survey of a few of the most commonly used projections](http://egsc.usgs.gov/isb//pubs/MapProjections/projections.html), as well as some solid conceptual background, is available via the US Geological Survey's Publications Warehouse. (The Pubs warehouse itself is located at [http://egsc.usgs.gov/isb//pubs/MapProjections/projections.html](http://egsc.usgs.gov/isb//pubs/MapProjections/projections.html). Lots of good stuff there.)

### Flatland

One often neglected aspect of map projections is that the projection surface is not always a flat plane. Flat planes are an important concept, since maps are typically represented on a flat 2-dimensional surface (paper or computer screen display.)

Most projections include the flattening procedure as a natural part of the projection itself, which is a sensible way to think about it. However, for reasons of fussy clarity, it's worthwhile to call out the end product of the Projection as an explicitly two-dimensional surface. History and custom weigh in favor of calling this surface _Flatland_.

Flatland refers to the entire extent of the projected surface of Wireframe Earth. Most projections can't display the entire Earth in the first place (for example, Mercator projections increase vertically without bound as the projection approaches the Poles. There's nothing _mathematically_ wrong with that, but it's not useful for cartography. By custom, the Mercator flatland is terminated within 5 degrees of the Poles.

One important aspect of the flattening of the projected surface into Flatland is that cylindrical and conic projections must be _cut_ at some point. The traditional cut location when flattening a Mercator projection is the 180th meridian. Choice of a cut location for conic projections is a little more complicated, since it anticipates the subset of the projection to be viewed.

### The Map

A Map, in the accustomed sense of a paper roadmap or topo map or nautical chart, is a static viewport, almost always rectangular in shape (polar regions are often mapped to circles because the corners of rectangles become distorted to the point of uselessness in many polar projections that cover large amounts of territory) laid onto Flatland. The smaller the viewport in relation to the Flatland upon which it's drawn, the more detailed close-up view it affords of the corresponding surface. 

In traditional cartography, the relationship between the extent of Earth's surface shown on a map, and the physical size of the map, is called _scale_. When we get to electronic map displays, the map is subject to _zoom_ (change in scale), _pan_ or  _translation_ (change in location), and sometimes _rotation_ (change in coordinate orientation with respect to the map's orientation.) The first two actions are completely natural and familiar to users of popular map systems - Google Maps, Yahoo Maps, and so on. They don't change much when you get to more precise mapping displays such as professional or military GIS systems.

The Map is, in principle, an interactive artifact. It provides all kinds of information about the portion of the Earth's surface it's displaying; in turn, you issue instructions about what else you want to see, or add observations of your own. Some of those are important records (surveying); some are of only transient importance (position plotting). It's very important to grasp this fact: maps and charts are, fundamentally, two-way information channels.

("Interactive" doesn't mean "computerized", by the way. I used to navigate at sea, and I can assure you that patiently and carefully erasing penciled position fixes, dead reckoning tracks, and so on from hydrographic charts after using them to plot a passage is the moral equivalent of refreshing the computer display. Just more time-consuming, painstaking, and manual. But we _definitely_ interacted with those charts.) 

### Territory
So, now we have defined the first four appliances: Wireframe Earth, Projection, Flatland, and Map. In order to discuss the fifth, Territory, we need to consider the One Weird Rule. This tells us that, for any point on the Map, there is exactly one corresponding point on the Wireframe Earth. This allows us to define the Territory Appliance: _Territory is the projection of the Map onto the Wireframe Earth_. Territory is therefore a dependent structure, representing the portion of the Earth's surface shown on the Map. When the Map is zoomed or panned, the Territory changes accordingly.







