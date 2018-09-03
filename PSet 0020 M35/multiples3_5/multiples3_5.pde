
int sum=0, i=1;

void draw()
{
 
  if(i%3==0 || i%5==0)   //Using modulus to find the remainder. If rem is zero, the number is divisible by 3 or 5
  sum=sum+i;             // adding the divisible number to the sum
  i++;                   // incrementing i so that each number is checked
  println(sum);          // prints the sum
  if(i==1000)            // Checks if the value of i is 1000 and then exits so that sum is only calulated for multiples of 3 and 5 till 1000.
  exit();
}



  
