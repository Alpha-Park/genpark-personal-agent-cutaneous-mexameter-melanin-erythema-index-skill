"""
MCP Server implementation for Cutaneous Mexameter Melanin Index (MI) & Erythema Index (EI) Skill.
Exposes standard FastMCP-compatible tools for narrowband spectrophotometric skin analysis.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import MexameterSpectrophotometryClient


def evaluate_skin_erythema_and_melanin(
    erythema_index_ei: Optional[float] = None,
    melanin_index_mi: Optional[float] = None,
    reflectance_568nm_green: Optional[float] = None,
    reflectance_660nm_red: Optional[float] = None,
    reflectance_880nm_nir: Optional[float] = None,
    baseline_ei: Optional[float] = None,
    baseline_mi: Optional[float] = None,
    anatomical_site: Optional[str] = "Cheek",
    patient_age_years: Optional[int] = 38
) -> str:
    """
    Evaluates Erythema Index (EI) and Melanin Index (MI) from narrowband reflectance.
    Returns structured analysis of cutaneous erythema, inflammation, and Fitzpatrick phototyping.
    """
    client = MexameterSpectrophotometryClient()
    result = client.evaluate_mexameter(
        erythema_index_ei=erythema_index_ei,
        melanin_index_mi=melanin_index_mi,
        reflectance_568nm_green=reflectance_568nm_green,
        reflectance_660nm_red=reflectance_660nm_red,
        reflectance_880nm_nir=reflectance_880nm_nir,
        baseline_ei=baseline_ei,
        baseline_mi=baseline_mi,
        anatomical_site=anatomical_site,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_skin_erythema_and_melanin",
                "description": "Calculates Mexameter Erythema Index (EI) and Melanin Index (MI) from 568nm, 660nm, 880nm spectral reflectance to evaluate microvascular inflammation and Fitzpatrick phototype.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "erythema_index_ei": {"type": "number", "description": "Pre-calculated Erythema Index (AU, normal baseline 150 - 300 AU)"},
                        "melanin_index_mi": {"type": "number", "description": "Pre-calculated Melanin Index (AU, normal range 50 - 700 AU)"},
                        "reflectance_568nm_green": {"type": "number", "description": "Narrowband green reflectance at 568nm (hemoglobin absorption)"},
                        "reflectance_660nm_red": {"type": "number", "description": "Narrowband red reflectance at 660nm"},
                        "reflectance_880nm_nir": {"type": "number", "description": "Narrowband near-infrared reflectance at 880nm"},
                        "baseline_ei": {"type": "number", "description": "Optional baseline non-inflamed Erythema Index for delta calculation"},
                        "baseline_mi": {"type": "number", "description": "Optional baseline perilesional Melanin Index"},
                        "anatomical_site": {"type": "string", "description": "Skin anatomical site measured (default: 'Cheek')"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 38)"}
                    }
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = MexameterSpectrophotometryClient()
        test_res = client.evaluate_mexameter(
            erythema_index_ei=245.0,
            melanin_index_mi=280.0
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
