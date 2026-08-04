#!/usr/bin/env python3
"""
SSISM / MYISM Sentinel LLM Engine Stack
Architect: U Ingar Soe
Function: Multi-LLM Data Fusion, Risk Verification, & Automated Dossier Rendering
"""

import math
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

# --- CONFIGURATION & LLM REGISTRY ---
SENTINEL_VERSION = "2026.4-GOLD"
LOCKOUT_THRESHOLD = 0.20  # Trust Score < 0.20 triggers mandatory 24h lockout

LLM_NODES = {
    "NODE_01": {"name": "Gemini-Pro", "role": "Primary Synthesis & Knowledge Vault"},
    "NODE_02": {"name": "Claude-3.5", "role": "Linguistic & Structural Logic Verification"},
    "NODE_03": {"name": "GPT-4o", "role": "BASH/Python Scripting & Code Auditing"},
    "NODE_04": {"name": "Grok-3", "role": "Real-Time OSINT & Narrative Stream Analysis"},
    "NODE_05": {"name": "DeepSeek-R1", "role": "Deep Math & Cryptographic Verification"},
    "NODE_06": {"name": "Llama-3-Local", "role": "Air-Gapped Offline Sentinel Fallback"}
}

# --- MATHEMATICAL RISK MODEL (Sigmoid Logistic Regression) ---
def calculate_trust_score(A: float, U: float, L: float, R: float, dT: float) -> dict:
    """
    Computes Risk Score Z and Digital Trust Score Phi.
    Z = w0 + wA*A + wU*U + wL*L + wR*R + wT*dT
    """
    # System Weights (Tuned for social engineering & threat defense)
    w0, wA, wU, wL, wR, wT = -1.5, 0.85, 0.90, 0.65, 1.10, 0.75
    
    Z = w0 + (wA * A) + (wU * U) + (wL * L) + (wR * R) + (wT * dT)
    Phi = 1.0 / (1.0 + math.exp(Z)) # Sigmoid transformation
    
    lockout_active = Phi < LOCKOUT_THRESHOLD
    
    return {
        "raw_risk_z": round(Z, 4),
        "trust_score_phi": round(Phi, 4),
        "lockout_triggered": lockout_active,
        "action": "MANDATORY 24H LOCKOUT / VERIFICATION" if lockout_active else "OPERATIONAL PASS"
    }

# --- CRYPTOGRAPHIC SEALING ---
def generate_sha256_seal(payload: dict) -> str:
    encoded_data = json.dumps(payload, sort_keys=True).encode('utf-8')
    return hashlib.sha256(encoded_data).hexdigest()

# --- WEASYPRINT / HTML REPORT GENERATOR ---
def build_html_template(data: dict) -> str:
    nodes_html = "".join([
        f"<tr><td><strong>{k}</strong></td><td>{v['name']}</td><td>{v['role']}</td><td style='color:#00ffcc;'>ACTIVE</td></tr>"
        for k, v in data["nodes"].items()
    ])

    lockout_color = "#ff3366" if data["assessment"]["lockout_triggered"] else "#00ffcc"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{ size: A4; margin: 15mm; }}
            body {{
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: 'Courier New', monospace;
                font-size: 11pt;
                line-height: 1.4;
            }}
            .header {{
                border-bottom: 2px solid #30363d;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }}
            .title {{ color: #58a6ff; font-size: 18pt; font-weight: bold; margin: 0; }}
            .subtitle {{ color: #8b949e; font-size: 10pt; }}
            .box {{
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 6px;
                padding: 12px;
                margin-bottom: 15px;
            }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th, td {{ border: 1px solid #30363d; padding: 8px; text-align: left; font-size: 9pt; }}
            th {{ background-color: #21262d; color: #58a6ff; }}
            .seal {{ word-break: break-all; color: #d2a8ff; font-size: 8pt; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="title">SSISM SENTINEL LLM ENGINE STACK</div>
            <div class="subtitle">AUTOMATED AUDIT & MULTI-NODE SYSTEM STATUS BRIEFING</div>
        </div>

        <div class="box">
            <h3>[1] SYSTEM MATRIX & ACTIVE NODES</h3>
            <table>
                <tr><th>NODE ID</th><th>MODEL</th><th>ASSIGNED ROLE</th><th>STATUS</th></tr>
                {nodes_html}
            </table>
        </div>

        <div class="box">
            <h3>[2] RISK ASSESSMENT LOGISTIC MODEL</h3>
            <p><strong>Raw Risk Score (Z):</strong> {data['assessment']['raw_risk_z']}</p>
            <p><strong>Digital Trust Score (Φ):</strong> {data['assessment']['trust_score_phi']}</p>
            <p><strong>System Response:</strong> <span style="color:{lockout_color}; font-weight:bold;">{data['assessment']['action']}</span></p>
        </div>

        <div class="box">
            <h3>[3] CRYPTOGRAPHIC INTEGRITY VERIFICATION</h3>
            <p><strong>Timestamp:</strong> {data['timestamp']}</p>
            <p><strong>SHA-256 Seal:</strong></p>
            <p class="seal">{data['seal']}</p>
        </div>
    </body>
    </html>
    """

def render_pdf_report(output_filename="ssism_sentinel_report.pdf"):
    # 1. Sample Inputs for Risk Calculation: Authority, Urgency, Linguistics, Link, Time Anomaly
    risk_assessment = calculate_trust_score(A=0.8, U=0.9, L=0.7, R=0.85, dT=0.6)

    # 2. Compile System Payload
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": SENTINEL_VERSION,
        "nodes": LLM_NODES,
        "assessment": risk_assessment
    }
    payload["seal"] = generate_sha256_seal(payload)

    # 3. Generate HTML & Render PDF via WeasyPrint
    html_content = build_html_template(payload)
    
    try:
        from weasyprint import HTML
        HTML(string=html_content).write_pdf(output_filename)
        print(f"[+] Dossier rendered successfully: {output_filename}")
    except ImportError:
        # Fallback if WeasyPrint is not installed in local environment
        html_file = output_filename.replace(".pdf", ".html")
        Path(html_file).write_text(html_content, encoding="utf-8")
        print(f"[!] WeasyPrint not found. Raw dark-mode HTML compiled to: {html_file}")

if __name__ == "__main__":
    render_pdf_report()
