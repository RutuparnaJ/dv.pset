void setup()
{
  size(600,600);
  stroke(255);
}
float t=0,x,y, R=200, r=30;
void draw()
{
  translate(width/2, height/2);
  clear();
  x=R*cos(t);
  y=R*sin(t);
  ellipse(x,y,r,r);
  t=t+PI/60;  
}
