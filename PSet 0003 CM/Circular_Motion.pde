void setup()
{
  size(600,600); //setting the size of display window
  stroke(255);   // defining the stroke colour
}
float t=0,x,y, R=200, r=30;
void draw()
{
  translate(width/2, height/2);  //moving the origin to the specified x and y coordinates
  clear();      // clears the screen
  x=R*cos(t);   // setting the x any y coordinates with respect to polar coordinates (R and angle theta)
  y=R*sin(t);
  ellipse(x,y,r,r); //draws an ellipse
  t=t+PI/60;    // incrementing theta by PI/60
}
