function setup()
{
  createCanvas(600,600);
  stroke(255);
  background(0);
}
var x=0, A=50;
function draw()
{

  translate(0, height/2);
  point(50*x,A*sin(x));
  x=x+PI/100;
}
