# Architecture

## 1. System orientation

This repository models a transition-oriented system rather than a protocol-first system.

The system consists of four layers:

1. **State layer**: states and transitions
2. **Difference layer**: structure of changes
3. **Boundary layer**: constraints and event horizon
4. **Witness layer**: independent validation

---

## 2. Layer model

```text
State Layer
    ↓
Difference Layer
    ↓
Boundary Template Layer
    ↓
Witness Validation Layer
    ↓
Structural Proof Layer
```

The core insight is that the system should be described by how transitions interact with boundaries and validation, not by how a canonical protocol defines every object in advance.

---

## 3. Core modules

### 3.1 difference_calculus.py
Responsible for:
- extracting positional differences,
- computing structural deltas,
- comparing sequences under a common index frame.

### 3.2 state_topology.py
Responsible for:
- representing state objects,
- linking transitions,
- establishing a state graph over time.

### 3.3 template_boundaries.py
Responsible for:
- N/S/E/W boundary semantics,
- padding domains,
- allowable transformation windows.

### 3.4 standing_waves.py
Responsible for:
- recurrence detection,
- pattern concentration,
- phase-like state alignment.

### 3.5 witness_validation.py
Responsible for:
- independent validation of the same transition,
- multi-observer agreement logic,
- proof-of-coherence functions.

### 3.6 structural_inversion.py
Responsible for:
- explaining structural reversibility,
- reconstructing transitions through defined operations,
- avoiding false claims about hash inversion.

---

## 4. Encoding layer

The encoding layer deliberately borrows the idea of self-description without enforcing any single standard.

It supports:
- compact representation of deltas,
- directional masks,
- structured carrying of boundary data,
- and minimality of representation.

---

## 5. Proof layer

The proof layer is intentionally modest but principled:
- it checks information preservation,
- it verifies boundary consistency,
- it offers witness-based confidence,
- and it distinguishes structural reversibility from cryptographic inversion.

This separation is critical. The project does not overclaim.

---

## 6. Example runtime flow

```text
input state A
input state B
extract Δ(A, B)
classify boundary zones
compute recurrence / standing wave signal
run witness validations
aggregate evidence
report structural confidence
```

---

## 7. Why this architecture is useful

It allows the system to be interpreted as:
- a topology of transformations,
- a boundary-aware state machine,
- a witness-based evidence model,
- and a reversible structural semantics rather than a single protocol.

This is useful precisely because it does not assume the world is already organized into a single stable schema.
