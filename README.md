<h1> Secure Multi-Party Computation Protocol</h1> 
<h2> About protocol </h2>
<h3> The protocol is based on the RSA cryptosystem. The protocol allows you to compare numbers secretlym. The protocol allows you to covertly compare numbers, avoiding a MITM attack.</h3>
<h3> How the protocol works </h3>
<p> Consider the situation between two subscribers A and B (Alice & Bob)</p>
<p> <h3>Step 1:</h3> Select rsa options. N - Product of two primes numbers p and q, m - Euler function of N, e - coprime with m (public key), d - e is raised to the power of -1 modulo m (secret key).</p>
<h3>Step 2:</h3>
<p> Selecting Protocol Options A0 - alice's number, B0 - Bob's number (A0 & B0 cannot be greater than N) </p>
<h3>Step 3: </h3>
<p> Subscriber Bob chooses a number x and calculates k - x to the power of e modulo N </p>
<h3>Step 4:</h3>
<p> Subscriber Bob send to Alice kB = k - B0 </p>
<h3>Step 5:</h3>
<p> Alice calculates numbers y = D(kB + u) for 1 ≤ u ≤ 20, D - kB+u raises to the power d modulo n </p>
<p> After that, A chooses a large random prime p. Next, A calculates the numbers
z = (y, modp) </p>
<h3>Step 6:</h3>
<p>A tells B a sequence of numbers z
B checks whether B0 is comparable or not a number from the sequence
with x (mod p). If so, he concludes that A0 ≥ B0. If not, he concludes,
that A0 < B0 </p>
<h2> Vulnerabilities: </h2>
<p>Vulnerabilities were implemented in the project: RSA secret key vulnerability, False conclusion, Vulnerability related to repetitions in the transmitted sequence</p>
