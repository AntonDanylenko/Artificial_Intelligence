var make_board = function(layout) {
  var ctx = document.getElementById("board").getContext("2d");
  for(var i=1; i<3; i++){
    // console.log("i: ", i);
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(i*ctx.canvas.width/3, 0);
    ctx.lineTo(i*ctx.canvas.width/3, ctx.canvas.height);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(0, i*ctx.canvas.height/3);
    ctx.lineTo(ctx.canvas.width, i*ctx.canvas.height/3);
    ctx.stroke();
  }
  ctx.font = "100px Courier New";
  ctx.fillStyle = "black";
  for(var i=0; i<3; i++){
    for(var ii=0; ii<3; ii++){
      if(layout[i*3+ii]!='_'){
        ctx.fillText(layout[i*3+ii],100*ii+18,100*i+80);
      }
    }
  }
}

var test = function() {
  console.log("TEST")
}
// var c = document.getElementById("board");
//
// c.addEventListener('click', function(e) {
//   if (e.offsetX<100){
//     if (e.offsetY<100){
//
//     }
//   }
//   e.preventDefault();
//   //red dots
//   ctx.fillStyle = "#FF0000";
//   //if there exists a previous dot
//   if (pX != null){
//     //draw a line from the preious dot to the new dot
//     ctx.beginPath();
//     ctx.moveTo(pX,pY);
//     ctx.lineTo(e.offsetX,e.offsetY);
//     ctx.stroke();
//     //draw a dot in the new place
//     ctx.beginPath()
//     ctx.ellipse(e.offsetX, e.offsetY, 3,3, 0, 0, 2 * Math.PI);
//     ctx.fill();
//     //cover up the line in the previous dot with a new dot
//     ctx.beginPath();
//     ctx.ellipse(pX, pY, 3,3, 0, 0, 2 * Math.PI);
//     ctx.fill();
//     //set it so that the next dot can connect to this one
//     pX = e.offsetX;
//     pY = e.offsetY;
//
//   }
//   else{
//     //no other dot exists so just draw a dot
//     ctx.beginPath();
//     ctx.ellipse(e.offsetX, e.offsetY, 3,3, 0, 0, 2 * Math.PI);
//     //fills ellipse with color.
//     ctx.fill();
//     pX = e.offsetX;
//     pY = e.offsetY;
//   }
// }
