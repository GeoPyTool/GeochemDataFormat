# Geochem Data Format
A simple Geochemical Data file format design.

# Example
```
{
    "date": "2021-02-01",
    "version": "0.02",
    "author": "Fred Yu, Pieter Vermeesch",
    "title": "AnAbOr",
    "type": "xyz",
    "reference": "Barker1979",
    "lines": {
	"1":[
	    [30,70,0],
	    [20,60,20],
	    [17.5,57.5,25],
	    [15,50,35],
	    [39,26,35]
	],
	"2":[
	    [48,32,20],
	    [20,60,20]
	],
	"3":[
	    [17.5,57.5,25],
	    [0,70,30]
	]
    },
    "type": {
	"1": "solid",
	"2": "solid",
	"3": "solid"
    },
    "polygons": {
	"A":[
	    [30,70,0],
	    [17.5,57.5,25],
	    [0,70,30],
	    [0,100,0]
	],
	"B":[
	    [30,70,0],
	    [20,60,20],
	    [80,0,20],
	    [100,0,0]
	],
	"C":[
	    [80,0,20],
	    [20,60,20],
	    [17.5,57.5,25],
	    [15,50,35],
	    [65,0,35]
	],
	"D":[
	    [65,0,35],
	    [0,0,100],
	    [0,70,30],
	    [17.5,57.5,25],
	    [15,50,35]
	]
    },
    "classes": {
    	"A": "Trondhjemite",
	"B": "Tonalite",
	"C": "Granodiorite",
	"D": "Granite"
    },
    "labels": {
	"Trondhjemite": [10,75,15,0],
	"Tonalite": [40,50,10,60],
	"Granodiorite": [30,42.5,27.5,60],
	"Granite": [15,25,60,0]
    }
}
```
# Explanation

`"classes"` gives the full name of the different polygons.
`"labels"` uses names that are shown on the plot. If a diagram contains a lot of polygons (e.g., the TAS diagram), then it is advisable to use short labels instead of the full class names.
`"labels"` specifies the coordinates of the labels (first three elements if `type=xyz`, or the first two elements if `type=xy`) as well as their angle of rotation (in degrees, last element in the location vectors).
