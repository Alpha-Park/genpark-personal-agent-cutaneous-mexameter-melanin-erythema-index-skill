"""
Example usage for Cutaneous Mexameter Melanin Index (MI) & Erythema Index (EI) Skill.
"""

from client import MexameterSpectrophotometryClient


def main():
    client = MexameterSpectrophotometryClient()

    print("--- Case 1: Normal Baseline Cheeks in Medium Phototype ---")
    normal_case = client.evaluate_mexameter(
        erythema_index_ei=240.0,
        melanin_index_mi=265.0,
        anatomical_site="Cheek",
        patient_age_years=34
    )
    print("Erythema Index (EI):", normal_case["spectrophotometric_indices"]["erythema_index_ei"], "AU")
    print("Melanin Index (MI):", normal_case["spectrophotometric_indices"]["melanin_index_mi"], "AU")
    print("Erythema Status:", normal_case["classification_and_staging"]["erythema_status"])
    print("Phototype Category:", normal_case["classification_and_staging"]["phototype_category"])
    print()

    print("--- Case 2: Acute Rosacea Erythematous Flare ---")
    rosacea_case = client.evaluate_mexameter(
        erythema_index_ei=510.0,
        melanin_index_mi=275.0,
        baseline_ei=240.0,
        anatomical_site="Malar Cheek",
        patient_age_years=46
    )
    print("Erythema Index (EI):", rosacea_case["spectrophotometric_indices"]["erythema_index_ei"], "AU")
    print("Delta EI:", rosacea_case["spectrophotometric_indices"]["delta_erythema_index"], "AU")
    print("Erythema Status:", rosacea_case["classification_and_staging"]["erythema_status"])
    print("Pathophysiology:", rosacea_case["classification_and_staging"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Derivation from Raw Optical Reflectances ---")
    spectral_case = client.evaluate_mexameter(
        reflectance_568nm_green=0.18,
        reflectance_660nm_red=0.36,
        reflectance_880nm_nir=0.55,
        anatomical_site="Dorsal Forearm"
    )
    print("Calculated EI:", spectral_case["spectrophotometric_indices"]["erythema_index_ei"], "AU")
    print("Calculated MI:", spectral_case["spectrophotometric_indices"]["melanin_index_mi"], "AU")
    print("Phototype Category:", spectral_case["classification_and_staging"]["phototype_category"])


if __name__ == "__main__":
    main()
