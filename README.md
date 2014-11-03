#rocket-appliances: a geospatial domain language

**rocket-appliances** is a design for a programming language. 

The name was adopted partly as an homage to the Canadian TV show [Trailer Park Boys](http://en.wikipedia.org/wiki/Trailer_Park_Boys) and partly as an act of desperation when all reasonable portmanteau forms of "gis", "geo", projection", "viewport", "wireframe", and "territory" were shown to be already colonized in googlespace - whether as the name of an existing company or product, or as a term of art in various communities of practice.

`rocket-appliances` is intended to be an analysis and investigation tool. It's probably not worth ever implementing; but that doesn't matter. The value of this language lies in designing it: by forcing the strict definition of the core data structures and operations of a generic geospatial language, `rocket-appliances` will hopefully create a general operational model that can underwrite attempts to teach, explain, learn, and analyze the assets and behavior of various resources and systems.

## rocket-appliances fundamentals
`rocket-appliances` is built around the logical model of how geographic projections provide structure to an interactive map. It involves five basic elements, or, as we might as well call them, _appliances_:

- The Wireframe Earth

- A Geographic Projection

- The Flatland

- The Map

- The Territory

### Wireframe Earth
We start with the _Wireframe Earth_ (often simply _Wireframe_), which is a familiar concept. The Wireframe Earth is a representation of the Globe as an immaterial spherical surface traced with angular coordinates, normally latitude and longitude. Sometimes, for geodetic purposes, a radial scalar z-coordinate is added. The Wireframe Earth has no other properties. 

The purpose of the Wireframe Earth is to esnablish a notional space of geographic reference: a "Real Location" not subject to the mathematical distortions of map projection.

### Projection
Every ultimately two-dimensional map is based on two steps. 

The first step is a mathematical projection of the wireframe onto a developable surface. In [Wikipedia's words](http://en.wikipedia.org/wiki/Developable_surface), a developable surface "can be flattened onto a plane without distortion". Another way of describing a developable surface is one having only _simple_ curvature. 

A sphere has _compound curvature_, which is why projections are necessary. A projection is a way of compressing and stretching regions of the spherical Earth until they do, in fact, fit onto a developable surface without further modification.

The number of possible mathematical projections of the Earth's surface onto a developable surface is, in principle, infinite. In practice, the number of actual projections that people choose to work with is quite a bit smaller than infinity. The International Association of Oil and Gas Producers, which has deep pockets and a vested interest in being able to precisely identify geographical locations, maintains one of the most complete registries of projections. This is accessible through its [Geomatics Committee web page](http://www.ogp.org.uk/committees/geomatics/). A more academic resource is an admirable paper (warning: PDF) at the USGS Publications Warehouse.

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


