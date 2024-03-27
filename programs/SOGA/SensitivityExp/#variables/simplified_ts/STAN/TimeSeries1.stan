parameters {
  real alpha;                       // intercept
  real beta;                        // slope
  real <lower=0, upper=1> lambda;   // lag
  real<lower=0> y1;
}
model {
  alpha ~ normal(1,1);
  beta ~ normal(1,1); 
  y1 ~ normal(alpha +  0.5*beta + lambda, 0.5);
}
