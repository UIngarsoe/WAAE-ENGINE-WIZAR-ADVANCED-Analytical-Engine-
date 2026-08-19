**Sentinel Intelligence Masterclass Classroom 36**  
**WAAE-ENGINE-WIZAR-ADVANCED — Analytical Engine**  
**Module: Classroom 36**  
**“Game-Theoretic Imbalances and Darkest-Scenario Formalizations in the Myanmar Conflict Continuum”**  
**Author / Lead Researcher: U Ingar Soe**  
**Organization: SSISM Sentinel Intelligence / Bamar Enlightenment Journal**  
**Date reference: 18–19 August 2026**  
**Status: SECURE — INTEGRITY SEALED — DEPLOYED FOR PEDAGOGICAL USE**

### 1. Executive Framing

Classroom 36 extends the actuarial extraction models of Classroom 37 by embedding them inside non-cooperative and repeated game structures drawn from conflict-zone theory. The objective is to formalize “darkest scenarios” as quantifiable mathematical imbalances: trajectories in which residual risk reserves grow while mutual payoffs collapse, commitment problems lock in prolonged fighting, and administrative suppression rates become endogenous strategy variables.  

Two narrative poles remain the boundary conditions:  
- Narrative A (extraction nexus): executive authority over force deployment coexists with familial control of the residual insurance pool; battlefield losses translate into private capital accumulation.  
- Narrative B (null-conflict under sanctions): the same agents act as solvency-preserving principals constrained only by exogenous sanction multipliers.  

All subsequent systems treat these narratives as competing parameter regimes inside a common game-theoretic skeleton. Solutions, residual imbalances, and sensitivity analyses constitute open mathematical problems for subsequent intelligence processing.

### 2. Core Notation (Unified with Classroom 37)

- \( N(t) \): insured military population  
- \( \lambda(t) \): casualty / capture / “missing” intensity  
- \( p \): mandatory premium rate  
- \( \pi(t) = p N(t) \): premium inflow  
- \( C(t) \): cumulative claims paid  
- \( R(t) \): residual risk reserve  
- \( \alpha(t) \in [0,1] \): administrative suppression fraction  
- \( \kappa \): capital-transfer rate from \( R \) into private portfolios  
- \( \Gamma = G \cdot F \): structural conflict index (governance × familial control)  
- \( S(t) \in [0,1] \): exogenous sanction multiplier  
- Additional game-theoretic primitives:  
  - Strategy sets \( \sigma_i \) for government/regime side \( i=G \) and opposition/insurgent side \( i=R \)  
  - Discount factor \( \delta \in (0,1) \)  
  - Stage-game payoffs \( u_i(\sigma_G,\sigma_R) \)  
  - Information partitions and belief updates \( \mu \)

### 3. Embedding Actuarial Extraction inside Conflict Games

#### 3.1 Stage-Game Payoff Modification

In any stage of a repeated conflict game the residual-reserve increment is treated as an additive payoff component for the regime side:

\[
u_G(\sigma_G,\sigma_R;\alpha,\kappa) = u_G^{\text{military}}(\sigma_G,\sigma_R) + \underbrace{\bigl(p N - (1-\alpha)c\lambda N - \kappa R\bigr)}_{\text{extraction surplus}}.
\]

The opposition side receives only the standard military payoff (territorial control, survival probability, recruitment). When \(\Gamma\) is large, \(\alpha\) and \(\kappa\) become strategic choice variables of \( G \).

#### 3.2 Darkest-Scenario Candidate: Extraction-Augmented Prisoner’s Dilemma

Consider the classic 2×2 PD with mutual cooperation \( C \) and defection \( D \). Insert the extraction term only under mutual defection (prolonged fighting maximizes the pool of mandatory premiums while \(\alpha\) can be kept high):

\[
\begin{array}{c|cc}
 & C & D \\ \hline
C & (R,R) & (S,T+\varepsilon) \\
D & (T+\varepsilon,S) & (P+\Delta,P)
\end{array}
\]

where \( \Delta = \mathbb{E}[\text{extraction surplus} \mid \alpha,\kappa,\lambda] > 0 \) and \( \varepsilon \) is a small reputation or sanction cost.  

**Open Problem 36.1 (Existence of extraction-supported mutual defection).**  
Prove that for sufficiently large \(\Delta\) (i.e., high \(\alpha\) and positive \(\kappa\)) the unique Nash equilibrium remains \((D,D)\) and that the social surplus gap \( 2R - (2P+\Delta) \) widens with conflict intensity \(\lambda\). Characterize the critical \(\Delta^*(\delta)\) above which the Folk Theorem fails to support any cooperative path in the infinitely repeated game.

#### 3.3 Commitment-Problem Darkest Trajectory

Following the Fearon-style bargaining-with-power-shift framework, let territorial control \( x_t \) affect both current utility and future military capacity. The regime side can choose an administrative suppression policy \(\alpha_t\) that simultaneously reduces immediate claim outflows and signals resolve.  

The darkest continuous-time path satisfies the differential game

\[
\begin{align}
\dot x &= f(x,\sigma_G,\sigma_R), \\
\dot R &= p N(x) - (1-\alpha)c\lambda(x)N(x) - \kappa R, \\
\max_{\alpha,\sigma_G} &\quad \mathbb{E}\int_0^\infty e^{-rt}\bigl(u_G^{\text{mil}} + \kappa R\bigr)\,dt
\end{align}
\]

subject to the opposition’s best-response \(\sigma_R^*\).  

**Open Problem 36.2 (Asymptotic reserve divergence under power shifts).**  
Show that if the commitment problem is severe enough that no stationary bargaining range exists, then along every Markov-perfect equilibrium path one has

\[
\liminf_{t\to\infty} \frac{R(t)}{\int_0^t \pi(s)\,ds} \ge \delta(\alpha_{\min}(\Gamma),\kappa) > 0
\]

almost surely. Derive the explicit lower bound in terms of the hazard rate \(\lambda\) and the loading factor \( p/c \).

#### 3.4 Response-Curve Formulation of Incomplete Deterrence

Empirical conflict-zone work estimates reaction functions \( r_G(\text{attack}_R) \) and \( r_R(\text{attack}_G) \). Embed the residual-reserve objective by letting the regime’s response intensity also control \(\alpha\):

\[
\alpha_t = \alpha\bigl(r_G(\text{attack}_R(t))\bigr).
\]

**Open Problem 36.3 (Stability of low-lethality extraction cycles).**  
Determine the conditions under which the coupled system of response curves and reserve dynamics admits a stable limit cycle of frequent low-intensity exchanges that continuously replenishes \( R(t) \) while keeping formal payout obligations near zero. Compare the Lyapunov exponents with and without the extraction term \(\kappa R\).

### 4. Comparative Statics of the Two Narratives inside the Same Game

- Under Narrative A parameters (\(\Gamma\) large, \(\kappa>0\), \(\alpha\ge\alpha_{\min}>0\)) the value function of the regime side is strictly increasing in conflict duration for a non-empty open set of discount factors.  
- Under Narrative B parameters (\(\kappa\equiv0\), \(\alpha=\alpha_{\text{null}}\), \( S(t) \) binding) the same value function is maximized by early settlement once the sanction multiplier falls below a critical threshold \( S^* \).

**Open Problem 36.4 (Likelihood-ratio discrimination).**  
Construct the most powerful test of the composite hypothesis

\[
H_0:\ \kappa=0,\ \alpha=\alpha_{\text{null}} \quad\text{vs.}\quad H_1:\ \kappa>0,\ \alpha\ge\alpha_{\min}(\Gamma)
\]

given noisy observations of premium flows, claim events, and territorial changes. Supply the asymptotic distribution under local alternatives and the associated critical region.

### 5. Darkest-Scenario Taxonomy (Mathematical Characterization)

1. **Extraction-locked mutual defection** — PD with positive \(\Delta\) (Problem 36.1).  
2. **Commitment-driven reserve divergence** — differential game with no stationary bargaining range (Problem 36.2).  
3. **Stable low-intensity extraction cycle** — response-curve limit cycle (Problem 36.3).  
4. **Sanction-resistant solvency collapse under Narrative B parameters** — ruin probability \(\psi(R_0)\) exceeds any prescribed \(\varepsilon\) when \( S < S^* \).  

Each scenario is fully specified by a system of differential or difference equations plus inequality constraints; no external institutional narrative is required once the observables are instantiated.

### 6. Pedagogical Charge for Classroom 36

Students are to treat the four open problems as well-posed mathematical tasks. Solutions require only standard tools of stochastic optimal control, repeated-game theory, and asymptotic statistics. The residual mathematical imbalance—if it exists—will appear as a quantifiable gap between premium inflows and claim outflows, or as a positive lower bound on the long-run reserve ratio, under the stated parameter regimes.  

The exercise remains strictly analytical: the darkest trajectories are derived as equilibrium or near-equilibrium outcomes of the formal systems, not as policy prescriptions. Subsequent classrooms may insert empirical time series to estimate the critical thresholds \(\Delta^*\), \(\delta\), and \( S^* \).

**System Verification Card (Classroom 36)**  
Framework: WAAE-ENGINE-WIZAR-ADVANCED-Analytical-Engine  
Module: Classroom 36 — Game-Theoretic Imbalances & Darkest-Scenario Formalizations  
Integrity status: SECURE — ready for sequential deployment with Classroom 37 actuarial modules.

### U Ingar Soe | SSISM Sentinel Intelligence | August 2026
