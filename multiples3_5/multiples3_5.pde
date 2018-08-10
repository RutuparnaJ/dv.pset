
int sum=0, i=1;

void draw()
{
 
  if(i%3==0 || i%5==0)
  sum=sum+i;
  i++;
  println(sum);
  if(i==1000)
  exit();
}



  
