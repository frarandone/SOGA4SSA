parameters {
  real alpha;                       // intercept
  real beta;                        // slope
  real <lower=0, upper=1> lambda;   // lag
  real y1;
real y2;
real y3;
real y4;
real y5;
real<lower=0> y6;
}
model {
  alpha ~ normal(1,1);
  beta ~ normal(1,1); 
  y1 ~ normal(alpha +  0.5*beta + lambda, 0.5);
y2 ~ normal(alpha +  0.5*beta +  lambda*y1, 0.5);
y3 ~ normal(alpha +  0.5*beta +  lambda*y2, 0.5);
y4 ~ normal(alpha +  0.5*beta +  lambda*y3, 0.5);
y5 ~ normal(alpha +  0.5*beta +  lambda*y4, 0.5);
y6 ~ normal(alpha +  0.5*beta +  lambda*y5, 0.5);
}
