"""
Cutaneous Mexameter Melanin Index (MI) & Erythema Index (EI) Spectrophotometry Client.
Zero-mock pure Python standard library implementation.
Calculates Erythema Index (EI), Melanin Index (MI) from narrowband 568nm, 660nm, 880nm reflectance,
Fitzpatrick phototype correlation, and cutaneous inflammatory/pigmentary staging.
"""

import math
from typing import Dict, Any, Optional, List


class MexameterSpectrophotometryClient:
    """
    Evaluates cutaneous erythema (hemoglobin) and pigmentation (melanin) via narrowband reflectance:
    - Erythema Index (EI): 100 * log10(R_660 / R_568)
        * Normal baseline: 150 - 300 AU
        * Mild inflammation: 301 - 450 AU
        * Moderate-to-severe erythema: > 450 AU
    - Melanin Index (MI): 100 * log10(R_880 / R_660)
        * Phototypes I-II: < 200 AU
        * Phototypes III-IV: 200 - 400 AU
        * Phototypes V-VI: > 400 AU
    - Essential for sunburn grading, rosacea severity, melasma, and laser skin safety.
    """

    def __init__(self):
        pass

    def evaluate_mexameter(
        self,
        erythema_index_ei: Optional[float] = None,
        melanin_index_mi: Optional[float] = None,
        reflectance_568nm_green: Optional[float] = None,
        reflectance_660nm_red: Optional[float] = None,
        reflectance_880nm_nir: Optional[float] = None,
        baseline_ei: Optional[float] = None,
        baseline_mi: Optional[float] = None,
        anatomical_site: Optional[str] = "Cheek",
        patient_age_years: Optional[int] = 38
    ) -> Dict[str, Any]:
        """
        Calculates EI and MI either from raw reflectance values or pre-calculated index values.
        reflectance values must be positive fractions (e.g. 0.25, 0.40, 0.65).
        """
        # Calculate from reflectance if provided
        if reflectance_568nm_green and reflectance_660nm_red:
            if reflectance_568nm_green <= 0 or reflectance_660nm_red <= 0:
                raise ValueError("Reflectance values must be strictly positive.")
            erythema_index_ei = round(100.0 * math.log10(reflectance_660nm_red / reflectance_568nm_green), 1)

        if reflectance_660nm_red and reflectance_880nm_nir:
            if reflectance_660nm_red <= 0 or reflectance_880nm_nir <= 0:
                raise ValueError("Reflectance values must be strictly positive.")
            melanin_index_mi = round(100.0 * math.log10(reflectance_880nm_nir / reflectance_660nm_red), 1)

        if erythema_index_ei is None or melanin_index_mi is None:
            raise ValueError("Either (erythema_index_ei, melanin_index_mi) or raw spectral reflectances must be provided.")

        # Compute delta indices if baseline provided
        delta_ei = round(erythema_index_ei - baseline_ei, 1) if baseline_ei is not None else None
        delta_mi = round(melanin_index_mi - baseline_mi, 1) if baseline_mi is not None else None

        # Erythema Inflammation Staging:
        if erythema_index_ei > 450.0:
            erythema_status = "Marked Cutaneous Erythema / Acute Inflammatory Flare"
            erythema_risk = "High-grade microvascular vasodilatation and dermal hyperemia; seen in active rosacea, acute sunburn, or severe contact dermatitis."
        elif erythema_index_ei > 300.0:
            erythema_status = "Mild-to-Moderate Erythema / Subclinical Inflammation"
            erythema_risk = "Moderate capillary dilatation; monitor for irritation or photosensitivity."
        else:
            erythema_status = "Normal Baseline Skin Tone (Quiescent Microvasculature)"
            erythema_risk = "Normal resting dermal perfusion without significant inflammatory hyperemia."

        # Melanin Phototype Classification:
        if melanin_index_mi < 180.0:
            phototype_category = "Fitzpatrick Phototype I-II (Very Fair / High Sunburn Risk)"
        elif melanin_index_mi <= 380.0:
            phototype_category = "Fitzpatrick Phototype III-IV (Medium / Olive Skin)"
        else:
            phototype_category = "Fitzpatrick Phototype V-VI (Deep Pigmentation / Low Sunburn Risk)"

        return {
            "status": "success",
            "spectrophotometric_indices": {
                "erythema_index_ei": round(erythema_index_ei, 1),
                "melanin_index_mi": round(melanin_index_mi, 1),
                "delta_erythema_index": delta_ei,
                "delta_melanin_index": delta_mi,
                "anatomical_site": anatomical_site
            },
            "classification_and_staging": {
                "erythema_status": erythema_status,
                "phototype_category": phototype_category,
                "pathophysiology_summary": erythema_risk
            }
        }
