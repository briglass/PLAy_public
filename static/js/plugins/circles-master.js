var CirclesMaster = function () {

    return {

        //Circles Master v1
        initCirclesMaster1: function () {
        	//Circles 1
		    Circles.create({
		        id:         'circle-1',
		        percentage: 75,
		        radius:     60,
		        width:      10,
		        number:     75,
		        text:       '',
		        colors:     ['#471A3F', '#d76cbb']
		    })

        	//Circles 2
		    Circles.create({
		        id:         'circle-2',
		        percentage: 25,
		        radius:     25,
		        width:      4,
		        number:     20,
		        text:       '',
		        colors:     ['#471A3F', '#d76cbb'],
		        duration:   0
		    })

        	//Circles 3
		    Circles.create({
		        id:         'circle-3',
		        percentage: 50,
		        radius:     25,
		        width:      4,
		        number:     50,
		        text:       '',
		        colors:     ['#471A3F', '#d76cbb'],
		        duration:   0
		    })

		    //Circles 4
		    Circles.create({
		        id:         'circle-4',
		        percentage: 75,
		        radius:     25,
		        width:      4,
		        number:     75,
		        text:       '',
		        colors:     ['#471A3F', '#d76cbb'],
		        duration:   0
		    })

		    //Circles 5
		    Circles.create({
		        id:         'circle-5',
		        percentage: 82,
		        radius:     35,
		        width:      2,
		        number:     82,
		        text:       '%',
		        colors:     ['#eee', '#9B6BCC'],
		        duration:   2000
		    })

		    //Circles 6
		    Circles.create({
		        id:         'circle-6',
		        percentage: 87,
		        radius:     80,
		        width:      3,
		        number:     87,
		        text:       '%',
		        colors:     ['#eee', '#72c02c'],
		        duration:   2000
		    })

        	//Circles 7
		    Circles.create({
		        id:         'circle-7',
		        percentage: 74,
		        radius:     80,
		        width:      3,
		        number:     74,
		        text:       '%',
		        colors:     ['#eee', '#72c02c'],
		        duration:   2000
		    })

        	//Circles 8
		    Circles.create({
		        id:         'circle-8',
		        percentage: 65,
		        radius:     80,
		        width:      3,
		        number:     65,
		        text:       '%',
		        colors:     ['#eee', '#72c02c'],
		        duration:   2000
		    })

		    //Circles 9
		    Circles.create({
		        id:         'circle-9',
		        percentage: 91,
		        radius:     80,
		        width:      3,
		        number:     91,
		        text:       '%',
		        colors:     ['#eee', '#72c02c'],
		        duration:   2000
		    })
        },
        
        //Circles Master v2
        initCirclesMaster2: function () {
		    var colors = [
		        ['#D3B6C6', '#9B6BCC'], ['#C9FF97', '#72c02c'], ['#BEE3F7', '#3498DB'], ['#FFC2BB', '#E74C3C']
		    ];

		    for (var i = 1; i <= 4; i++) {
		        var child = document.getElementById('circles-' + i),
		            percentage = 45 + (i * 9);
		            
		        Circles.create({
		            id:         child.id,
		            percentage: percentage,
		            radius:     70,
		            width:      4,
		            number:     percentage / 1,
		            text:       '',
		            colors:     colors[i - 1],
		            duration:   1000,
		        });
		    }	    
        }

    };
    
}();