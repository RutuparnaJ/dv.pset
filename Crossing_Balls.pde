void setup()
{
  size(600,400);
  stroke(0);
}
int l=600,b=400,i=0,vel=5,r=30;
void draw()
{
  clear();
  ellipse(i,b/2,r,r);
  ellipse(l-i,b/2,r,r);
  i=i+vel;
  if(i==0 || i==l)
  vel=-vel;
}
