---
name: genpark-personal-agent-cutaneous-mexameter-melanin-erythema-index-skill
description: Evaluates skin microvascular erythema (inflammation) and melanin pigmentation (phototype) via narrowband 568nm, 660nm, and 880nm reflectance spectrophotometry.
---

# Cutaneous Mexameter Melanin Index (MI) & Erythema Index (EI) Skill

This skill computes objective colorimetric indices for cutaneous erythema ($EI$) and pigmentation ($MI$) using narrowband optical reflectance to diagnose skin inflammatory disorders, quantify UV reactivity, and stage pigmentation according to dermatological standards.

## Core Capabilities
- Evaluates Erythema Index ($EI = 100 \cdot \log_{10}(R_{660} / R_{568})$, normal baseline $150 - 300\text{ AU}$).
- Evaluates Melanin Index ($MI = 100 \cdot \log_{10}(R_{880} / R_{660})$) correlating to Fitzpatrick phototypes I through VI.
- Computes baseline-adjusted $\Delta EI$ and $\Delta MI$ for patch testing, laser cooling recovery, and melasma tracking.
- Distinguishes active microvascular erythema from melanin dyschromia.

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
