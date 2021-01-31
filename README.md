# Geochem Data Format
a primitive design of Geochemeical Data file format.

# Example and Explaination
{
  "comment": "just some comment, whatever ",
	"date": "2021-1-31",
	"version": "0.02",
  "author": "fred yu",
  "title": "Title",
  "type": "xy", # or "xyz"
	"axis":["x","y"],
  "reference": "the source",

  "lines_coords": {
    "line1 or any other name": [
      [41, 0],
      [41, 3],
      [41, 79],
      [69, 8],
      [77.3, 0]
    ]
  },

  "labels": {
    "Name" : "Name One"
  },

  "labels_coords": {
    "Name":  [40, 12] 
  }

}

