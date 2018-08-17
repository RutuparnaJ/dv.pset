void setup()
{
  size(500,500);
  stroke(255,255);
  strokeWeight(2);
  background(120);
    
}
int l=500, b=500, i=0, r=30, j=40;
  
void draw()
{
  
   clear();
   ellipse(i,b/2,r,r);
   i=i+j;
   if(i>l-1)
   {
     j=j-5;
      j=-j;
   }
   if(i<0)
   {
     j=j+5;
     j=-j;
   }   
}
  
 
  
