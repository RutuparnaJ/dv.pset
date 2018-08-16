int fact=1, num=3;
void draw() {
  fact=fact*num;
  num=num-1;
  if(num==1)
  println("The factorial is "+ fact);
}
