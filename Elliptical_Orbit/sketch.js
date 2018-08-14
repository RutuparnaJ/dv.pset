function setup() {
createCanvas(500,500);
stroke(0);
}
var t=0, x, y, a=200, b=100, r=30;
function draw() {
  translate(500/2, 500/2);
  clear();
  x=a*cos(t);
  y=b*sin(t);
  ellipse(0,0, r,r);
  ellipse(x,y,r,r);
  t=t+PI/60;
}
