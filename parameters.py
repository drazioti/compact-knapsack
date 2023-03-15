
a1=1/4;a2=1/2; #defines S
b1=1/8;b2=1/4; #defines S'
n = 48;m=4;R=192;t=80; #basic parameters
#1st part of the signature
# each element of the matrix is (R/8+a1*R) or (R/8+a2*R)
A=(m*t/2) * (R/8+a1*R) + (m*t)/2 * (R/8+a2*R)/2
#2nd part of the signature
B=(n*t)/2 * (R/8+b1*R) + (n*t)/2 * (R/8+b2*R)
print(A,B,A+B)