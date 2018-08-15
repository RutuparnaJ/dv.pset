
int i=1, sum1=0, sum2=0, diff;
void draw() {
  while(i<=100)
  {
  sum1=sum1+(i*i);
  sum2=sum2+i;
  i++;
  }
  diff=sum2*sum2 - sum1;
  println(diff);
}
