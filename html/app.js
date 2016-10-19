$(function(){

    var canvas=document.getElementById("canvas");
    var ctx=canvas.getContext("2d");
    canvas.width=window.innerWidth;
    canvas.height=window.innerHeight;
    ctx.lineWidth=3;

    var $canvas=$("#canvas");
    var canvasOffset=$canvas.offset();
    var offsetX=canvasOffset.left;
    var offsetY=canvasOffset.top;

    var $1=$(".L1");
    var $2=$(".L2");
    var $3=$(".L3");
    var $4=$(".L4");
    var $5=$(".L5");
    var $6=$(".L6");

    var $2r=$(".L2");
    var $3r=$(".L3");
    var $4r=$(".L4");
    var $5r=$(".L5");
    var $6r=$(".L6");

    var connectors=[];
    connectors.push({from:$1,to:$2r});
    connectors.push({from:$2,to:$3r});
    connectors.push({from:$3,to:$4r});
    connectors.push({from:$4,to:$5r});
    connectors.push({from:$5,to:$6r});

    connect();

    $(".draggable").draggable({
        // event handlers
        start: noop,
        drag:  connect,
        stop:  noop
    });

    function noop(){}

    function connect(){
        ctx.clearRect(0,0,canvas.width,canvas.height);
        for(var i=0;i<connectors.length;i++){
            var c=connectors[i];
            var eFrom=c.from;
            var eTo=c.to;
            var pos1=eFrom.offset();
            var pos2=eTo.offset();
            var size1=eFrom.size();
            var size2=eTo.size();
            ctx.beginPath();
            ctx.moveTo(pos1.left+eFrom.width()+3,pos1.top+eFrom.height()/2);
            ctx.lineTo(pos2.left+3,pos2.top+eTo.height()/2);
            ctx.stroke();

        }
    }

});
