import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_pdf():
    pdf_path = "SSISM_WAAE_2026_Masterclass_Classroom_9.pdf"
    
    # 1. Setup Document with Dark Theme Margins
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    # Color Palette Definitions
    BG_COLOR = colors.HexColor("#0b0f19")       # Dark Backdrop
    CYAN_ACCENT = colors.HexColor("#38bdf8")    # Accent Text / Borders
    GOLD_BADGE = colors.HexColor("#f59e0b")     # Header / Highlights
    PURPLE_HIGHLIGHT = colors.HexColor("#2e1065")# Callout Box BG
    TEXT_WHITE = colors.HexColor("#f8fafc")     # Primary Text
    TEXT_MUTED = colors.HexColor("#94a3b8")     # Subtitles / Secondary Text
    BORDER_COLOR = colors.HexColor("#1e293b")

    # Background Drawing Function for Page 1 & subsequent pages
    def draw_dark_bg(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(BG_COLOR)
        canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
        canvas.restoreState()

    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=CYAN_ACCENT,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        textColor=GOLD_BADGE,
        spaceAfter=12
    )

    meta_style = ParagraphStyle(
        'MetaText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        textColor=TEXT_MUTED,
        leading=12
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        textColor=TEXT_WHITE,
        leading=14,
        spaceAfter=8
    )

    quote_style = ParagraphStyle(
        'QuoteText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        textColor=colors.HexColor("#e2e8f0"),
        leading=13.5
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        textColor=CYAN_ACCENT,
        leading=11
    )

    table_body_style = ParagraphStyle(
        'TableBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        textColor=TEXT_WHITE,
        leading=11
    )

    story = []

    # --- HEADER SECTION ---
    story.append(Paragraph("SSISM WAAE-ENGINE-WIZAR MASTERCLASS CLASSROOM 9", title_style))
    story.append(Paragraph("Civil Intelligence Education Training Module • Bamar Enlightenment Journal Set", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=CYAN_ACCENT, spaceBefore=0, spaceAfter=10))

    # Metadata Panel
    meta_content = [
        [
            Paragraph("<b>Scheduled Date:</b> August 3, 2026<br/><b>Executive Editor:</b> U Ingar Soe (SSISM Sentinel)", meta_style),
            Paragraph("<b>License:</b> MIT Licensed Algorithm<br/><b>Framework:</b> Civil Intelligence Education", meta_style)
        ]
    ]
    meta_table = Table(meta_content, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#111827")),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 12))

    # --- EPISTEMOLOGICAL CORE (CALLOUT BOX) ---
    story.append(Paragraph("<b>MASTERCLASS OVERVIEW & EPISTEMOLOGICAL CORE</b>", ParagraphStyle('H2', parent=title_style, fontSize=12, textColor=GOLD_BADGE)))
    
    axiom_text = (
        "<b>Core Axiom:</b><br/>"
        "\"Intelligence organizations must resist the positivist temptation to treat codification as the sole path to knowledge quality. "
        "Polanyi's epistemology, as applied to intelligence by Ormerod and Robinson, demonstrates that the personal coefficient in knowledge is not "
        "a defect to be engineered away but an essential dimension of analytical competence.<br/><br/>"
        "The Civil Intelligence Education framework integrates tacit and explicit knowledge through curriculum design that balances both, decision-making "
        "protocols that require their convergence, and skill transfer cycles that move knowledge through all four SECI modes. The result is not the replacement "
        "of tacit knowledge by explicit codification, but the cultivation of their dynamic, interdependent interplay — the condition upon which intelligence "
        "cycle effectiveness ultimately depends.\""
    )
    
    quote_table = Table([[Paragraph(axiom_text, quote_style)]], colWidths=[540])
    quote_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), PURPLE_HIGHLIGHT),
        ('BOX', (0,0), (-1,-1), 1, GOLD_BADGE),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(quote_table)
    story.append(Spacer(1, 12))

    # --- MODULE SUMMARY TABLE ---
    story.append(Paragraph("<b>MODULE SUMMARY TABLE</b>", ParagraphStyle('H2_2', parent=title_style, fontSize=11, textColor=CYAN_ACCENT)))
    
    table_data = [
        [
            Paragraph("Module ID", table_header_style),
            Paragraph("Module Title", table_header_style),
            Paragraph("Knowledge Type Integration", table_header_style),
            Paragraph("Primary Focus & Outcomes", table_header_style)
        ],
        [
            Paragraph("<b>CIE-01</b>", table_body_style),
            Paragraph("Epistemological Foundations", table_body_style),
            Paragraph("Explicit-dominant with tacit bridge", table_body_style),
            Paragraph("Articulate Polanyi's tacit dimension, SECI model, and intelligence cycle dynamics.", table_body_style)
        ],
        [
            Paragraph("<b>CIE-02</b>", table_body_style),
            Paragraph("Collection & Source Evaluation", table_body_style),
            Paragraph("Balanced integration", table_body_style),
            Paragraph("Combine OSINT/HUMINT structured schemas with mentor-guided, intuitive source evaluation.", table_body_style)
        ],
        [
            Paragraph("<b>CIE-03</b>", table_body_style),
            Paragraph("Analytic Tradecraft & Codification", table_body_style),
            Paragraph("Tacit-dominant with explicit scaffold", table_body_style),
            Paragraph("Apply ACH, Key Assumptions Checks, and recognition-primed decision-making.", table_body_style)
        ],
        [
            Paragraph("<b>CIE-04</b>", table_body_style),
            Paragraph("Organizational Knowledge Transfer", table_body_style),
            Paragraph("Full SECI-cycle implementation", table_body_style),
            Paragraph("Institutionalize lessons-learned systems while capturing tacit wisdom via storytelling & exit interviews.", table_body_style)
        ]
    ]

    mod_table = Table(table_data, colWidths=[55, 120, 135, 230])
    mod_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e293b")),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#0f172a"), colors.HexColor("#111827")]),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(mod_table)
    story.append(Spacer(1, 12))

    # --- KEY EPISTEMOLOGICAL HIGHLIGHTS ---
    story.append(Paragraph("<b>KEY EPISTEMOLOGICAL HIGHLIGHTS</b>", ParagraphStyle('H2_3', parent=title_style, fontSize=11, textColor=GOLD_BADGE)))
    
    highlights = (
        "• <b>Polanyi's Epistemology in Intelligence:</b> Emphasizes that <i>'we know more than we can tell.'</i> The 'from-to' structure of subsidiary cues moving toward focal objects forms the backbone of intuitive pattern recognition and fraud detection.<br/>"
        "• <b>The Codification Continuum:</b> Navigates the risks of Context Loss, False Precision, and Tradecraft Secrecy/Institutional Silos.<br/>"
        "• <b>Intelligence Cycle Synthesis:</b> Demonstrates how over-codification renders analysis hollow and mechanical, whereas under-codification undermines institutional memory and accountability."
    )
    story.append(Paragraph(highlights, body_style))
    story.append(Spacer(1, 10))

    # --- VERIFICATION SEAL CARD ---
    seal_text = (
        "<b>VERIFICATION SEAL & PROOF OF AUTHENTICITY</b><br/>"
        "<b>Authenticity Verified:</b> SSISM-WAAE-CLASSROOM-9-20260803<br/>"
        "<b>Burmese Node Lineage:</b> <font color='#34d399'><b>မှန်ကန်ကြောင်း စစ်ဆေးပြီးစီးပါပြီ • Civil Intelligence Education Framework</b></font><br/>"
        "<b>Target Nodes:</b> OSINT Myanmar/Burma Civil Enlightenment Nodes"
    )
    seal_table = Table([[Paragraph(seal_text, ParagraphStyle('Seal', parent=body_style, fontSize=8.5, leading=12))]], colWidths=[540])
    seal_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#064e3b")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#10b981")),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(seal_table)

    # Build Document
    doc.build(story, onFirstPage=draw_dark_bg, onLaterPages=draw_dark_bg)
    print(f"PDF successfully generated: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
