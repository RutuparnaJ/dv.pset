function setup() {
createCanvas(500,500);
stroke(0);
strokeWeight(5);
translate(0,250);
}
var PI=3.14;
var x, y, p=PI/4, u=30, t=0;
var g=-9.8;


function draw() {
  clear();
  x=u*cos(p)*t;
  y=500-(u*sin(p)*t+(0.5*g*t*t));
  ellipse(x,y,30,30);
  t=t+0.1;
}
