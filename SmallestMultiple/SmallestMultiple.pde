/*2520 is the smallest number that can be divided by
each of the numbers from 1to 10 without any remainder.
What is the smallest positive number that is evenly 
divisible by all of the numbers from 1to 20? */

int i,j=0, num=1;
void draw()
{
  for(i=1;i<=20;i++)
  {
    if(num%i==0)    
     j++;
    else
    break;
  }
    if (j==20)
    {
      println("yes!The number is "+num); 
      exit();
    }
    else
    println("no for "+num);
    j=0;
    num++;
}

  
