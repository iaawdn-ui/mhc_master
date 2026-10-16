# -*- coding: utf-8 -*-
"""Programmatic diagram/illustration generation for MHC 701 textbook.
All figures are rendered as vector-quality PNGs (200 dpi) into book/images/.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge, Rectangle
import numpy as np

IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(IMG, exist_ok=True)

NAVY = "#1f3b5c"
TEAL = "#2a9d8f"
GOLD = "#e9c46a"
CORAL = "#e76f51"
SLATE = "#4a6572"
LIGHT = "#f1f5f9"
INK = "#222222"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.edgecolor": SLATE,
})


def _box(ax, x, y, w, h, text, fc=LIGHT, ec=NAVY, fs=10, tc=INK, bold=False, style="round,pad=0.15"):
    p = FancyBboxPatch((x, y), w, h, boxstyle=style, linewidth=1.6,
                       facecolor=fc, edgecolor=ec)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, color=tc, fontweight="bold" if bold else "normal", wrap=True)
    return p


def _arrow(ax, x1, y1, x2, y2, color=NAVY, lw=2, style="-|>", conn="arc3,rad=0.0"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=16,
                        color=color, linewidth=lw, connectionstyle=conn)
    ax.add_patch(a)


def _canvas(w=10, h=6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    return fig, ax


def _save(fig, name):
    fig.savefig(os.path.join(IMG, name + ".png"), dpi=200, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Figure 1.1
def fig_1_1():
    fig, ax = _canvas()
    _box(ax, 3.4, 4.6, 3.2, 1.1, "MENTAL HEALTH\nCOUNSELING", fc=NAVY, ec=NAVY, tc="white", fs=13, bold=True)
    pillars = [("ASSESSMENT", "Intake, risk,\ndiagnosis, strengths"),
               ("TREATMENT", "Clinical change\ninterventions"),
               ("PREVENTION", "Early intervention,\noutreach programs"),
               ("WELLNESS\nPROMOTION", "Flourishing,\nresilience, growth")]
    xs = [0.2, 2.7, 5.2, 7.7]
    for (t, s), x in zip(pillars, xs):
        _box(ax, x, 2.6, 2.1, 1.2, t, fc=TEAL, ec=NAVY, tc="white", fs=10, bold=True)
        _box(ax, x, 1.2, 2.1, 1.2, s, fc=LIGHT, ec=SLATE, fs=9)
        _arrow(ax, 5.0, 4.6, x + 1.05, 3.8)
    _box(ax, 0.2, 0.05, 9.6, 0.85, "Foundation: behavioral-science research + ethical practice standards",
         fc=GOLD, ec=SLATE, fs=10)
    fig.suptitle("The Four Functional Pillars of Practice", fontsize=14, color=NAVY, y=1.0)
    _save(fig, "fig_1_1")


# ---------------------------------------------------------------- Figure 1.2
def fig_1_2():
    fig, ax = _canvas(11, 5.5)
    events = [(1900, "Lightner Witmer coins\n'clinical psychology';\nGuidance movement grows"),
              (1908, "Frank Parsons:\nVocational Bureau;\n'Choosing a Vocation'"),
              (1917, "WWI aptitude testing\n(Army Alpha/Beta);\npsychometrics boom"),
              (1935, "National Vocational\nGuidance Association\n(APA Division later)"),
              (1946, "National Mental\nHealth Foundation;\ncommunity mental\nhealth advocacy"),
              (1963, "Community Mental\nHealth Centers Act;\ndeinstitutionalization"),
              (1977, "ACES → ACCES;\ncounselor education\naccreditation (CACREP\nroots, 1981)"),
              (1984, "'80/20' identity debate;\nCounselors for Human\nDevelopment (CHD)"),
              (1992, "AMDC becomes\nAmerican Counseling\nAssociation (ACA)"),
              (2000, "APA recognizes\nDivision 42 (Psychologists\nin Independent Practice)\n& counseling momentum"),
              (2010, "20/20 One Voice;\n'clinical mental health\ncounseling' term adopted"),
              (2020, "Licensure in all 50 US\nstates; telehealth era;\ninterprofessional care")]
    ax.plot([0.3, 9.7], [3, 3], color=NAVY, lw=3, zorder=1)
    up = True
    for yr, txt in events:
        x = 0.3 + (yr - 1900) / (2025 - 1900) * 9.4
        ax.scatter([x], [3], s=60, color=CORAL, zorder=3)
        if up:
            ax.annotate(f"{yr}\n{txt}", xy=(x, 3), xytext=(x, 4.35), ha="center",
                        fontsize=7.2, color=INK,
                        arrowprops=dict(arrowstyle="-", color=SLATE, lw=1))
        else:
            ax.annotate(f"{yr}\n{txt}", xy=(x, 3), xytext=(x, 1.55), ha="center",
                        fontsize=7.2, color=INK,
                        arrowprops=dict(arrowstyle="-", color=SLATE, lw=1))
        up = not up
    ax.set_title("Historical Timeline of the Counseling Profession, 1900\u2013Present",
                 fontsize=14, color=NAVY)
    _save(fig, "fig_1_2")


# ---------------------------------------------------------------- Figure 1.3
def fig_1_3():
    fig, ax = _canvas(9, 7)
    labels = ["Developmental &\nStrength-Based", "Prevention &\nWellness Focus",
              "Short- to Medium-\nTerm Treatment", "Diverse Settings\n& Populations",
              "Relational &\nEclectic Practice"]
    colors = [TEAL, NAVY, CORAL, GOLD, SLATE]
    n = len(labels)
    for i, (lab, c) in enumerate(zip(labels, colors)):
        ang = 90 + i * 360 / n
        x = 5 + 1.55 * np.cos(np.radians(ang))
        y = 3.5 + 1.55 * np.sin(np.radians(ang))
        circ = Circle((x, y), 1.55, fill=True, facecolor=c, alpha=0.42,
                      edgecolor=c, lw=2.5)
        ax.add_patch(circ)
        ax.text(x, y + 0.55, lab, ha="center", va="center", fontsize=9.5,
                fontweight="bold", color=INK)
    ax.text(5, 3.5, "THE\nCOUNSELING\nPROFESSION", ha="center", va="center",
            fontsize=11, fontweight="bold", color=NAVY)
    ax.set_xlim(0.5, 9.5); ax.set_ylim(0.3, 7.0)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Five Defining Characteristics as Interlocking Rings", fontsize=14, color=NAVY)
    _save(fig, "fig_1_3")


# ---------------------------------------------------------------- Figure 1.4
def fig_1_4():
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.axhline(0, color=SLATE, lw=1.5); ax.axvline(0, color=SLATE, lw=1.5)
    quads = [(0.5, 0.5, "COMPLETE MENTAL HEALTH\nHigh wellness, low distress", TEAL),
             (-0.5, 0.5, "SYMPTOMATIC BUT WELL\n(Symptom-focused dx bias)", GOLD),
             (0.5, -0.5, "VULNERABLE\n(Low wellness, no disorder yet)", CORAL),
             (-0.5, -0.5, "INCOMPLETE MENTAL HEALTH\nLow wellness + high distress", NAVY)]
    for x, y, t, c in quads:
        ax.add_patch(Rectangle((x - 0.45, y - 0.45), 0.9, 0.9, facecolor=c, alpha=0.30,
                               edgecolor=c, lw=2))
        ax.text(x, y, t, ha="center", va="center", fontsize=10, fontweight="bold", color=INK)
    ax.set_xlim(-1, 1); ax.set_ylim(-1, 1)
    ax.set_xlabel("\u2190 Symptom Distress / Psychopathology \u2192", fontsize=11)
    ax.set_ylabel("\u2190 Emotional Well-Being / Flourishing \u2192", fontsize=11)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Dual-Factor Model: Complete Mental Health Across Two Continua",
                 fontsize=13, color=NAVY)
    _save(fig, "fig_1_4")


# ---------------------------------------------------------------- Figure 2.1
def fig_2_1():
    fig, ax = _canvas(11, 5)
    stages = ["STAGE 1\nNaive\nExpectations", "STAGE 2\nAccepting\nAmbiguity",
              "STAGE 3\nPersonalizing\nTheory", "STAGE 4\nIngesting\nSkills",
              "STAGE 5\nInternalizing\nProfessional Identity"]
    cols = [GOLD, CORAL, SLATE, TEAL, NAVY]
    x = 0.25
    for s, c in zip(stages, cols):
        _box(ax, x, 2.6, 1.75, 1.4, s, fc=c, ec=NAVY, tc="white" if c != GOLD else INK, fs=9, bold=True)
        if x < 8:
            _arrow(ax, x + 1.78, 3.3, x + 2.02, 3.3)
        x += 2.0
    _box(ax, 0.25, 1.0, 9.5, 1.1,
         "Driving forces: coursework \u2022 practicum feedback \u2022 supervision \u2022 personal therapy \u2022 critical incidents \u2022 role models",
         fc=LIGHT, ec=SLATE, fs=9)
    ax.set_title("Five-Stage Model of Counselor Professional Identity Formation",
                 fontsize=14, color=NAVY)
    _save(fig, "fig_2_1")


# ---------------------------------------------------------------- Figure 2.2
def fig_2_2():
    fig, ax = _canvas(9, 6.5)
    nodes = [(5, 5.2, "TRIGGER\nclient material activates\ncounselor theme"),
             (8.2, 3.6, "FEELING\nunexamined affect\n(anxiety, anger, rescue urge)"),
             (5, 2.0, "BEHAVIOR\nquestioning too fast, advice,\navoidance, over-disclosure"),
             (1.8, 3.6, "IMPACT ON\nSESSION\nrupture, compliance,\nwithdrawal"),
             (5, 3.6, "CLIENT\nRESPONSE\n(feedback signal)")]
    for x, y, t in nodes:
        _box(ax, x - 1.35, y - 0.62, 2.7, 1.24, t, fc=LIGHT, ec=NAVY, fs=8.5)
    pairs = [(6.3, 5.0, 8.0, 4.2), (7.4, 2.8, 6.2, 2.3), (3.7, 2.3, 2.1, 3.0),
             (2.6, 4.2, 3.8, 4.9), (5, 4.55, 5, 4.25)]
    for x1, y1, x2, y2 in pairs:
        _arrow(ax, x1, y1, x2, y2, color=CORAL)
    _box(ax, 3.3, 0.35, 3.4, 0.85, "BREAK LOOP: self-awareness, supervision,\npersonal therapy, mentalization",
         fc=TEAL, ec=NAVY, tc="white", fs=8.5, bold=True)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.set_title("The Countertransference Feedback Loop", fontsize=14, color=NAVY)
    _save(fig, "fig_2_2")


# ---------------------------------------------------------------- Figure 2.3
def fig_2_3():
    fig, ax = _canvas(9, 6.5)
    ax.add_patch(Circle((4.0, 3.6), 1.9, facecolor=NAVY, alpha=0.35, edgecolor=NAVY, lw=2))
    ax.add_patch(Circle((5.9, 3.6), 1.9, facecolor=CORAL, alpha=0.35, edgecolor=CORAL, lw=2))
    ax.add_patch(Circle((4.95, 2.1), 1.9, facecolor=TEAL, alpha=0.35, edgecolor=TEAL, lw=2))
    ax.text(2.7, 4.4, "BURNOUT\n(exhaustion,\ncynicism,\ninefficacy)", fontsize=9, ha="center", fontweight="bold")
    ax.text(7.2, 4.4, "COMPASSION\nFATIGUE\n(empathic\noverload)", fontsize=9, ha="center", fontweight="bold")
    ax.text(4.95, 0.75, "VICARIOUS TRAUMA\n(worldview changed by\nclient trauma material)", fontsize=9, ha="center", fontweight="bold")
    ax.text(4.9, 3.35, "OVERLAP:\nchronic\noccupational\nstress in\ncaring work", fontsize=8.5, ha="center", fontweight="bold", color=INK)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Burnout, Compassion Fatigue, and Vicarious Trauma", fontsize=14, color=NAVY)
    _save(fig, "fig_2_3")


# ---------------------------------------------------------------- Figure 3.1
def fig_3_1():
    fig, ax = _canvas(11, 6)
    _box(ax, 0.3, 4.3, 4.4, 1.3, "LINEAGE A \u2014 PSYCHIATRIC / MENTAL HYGIENE\nAsylum reform \u2192 mental hygiene (1908) \u2192\ncommunity mental health (1963) \u2192 clinical services", fc=CORAL, ec=NAVY, tc="white", fs=8.5, bold=True)
    _box(ax, 0.3, 1.4, 4.4, 1.3, "LINEAGE B \u2014 GUIDANCE / VOCATIONAL\nParsons' vocational bureau \u2192 school & career\nguidance \u2192 personnel & adjustment counseling", fc=TEAL, ec=NAVY, tc="white", fs=8.5, bold=True)
    _box(ax, 5.6, 2.6, 2.6, 1.6, "CONVERGENCE\n1960s\u201380s\n'80/20 debate,\nACA formation,\nlicensure drive", fc=GOLD, ec=NAVY, fs=9, bold=True)
    _box(ax, 8.6, 2.6, 1.3, 1.6, "MODERN\nCLINICAL\nMHC", fc=NAVY, ec=NAVY, tc="white", fs=9, bold=True)
    _arrow(ax, 4.75, 4.9, 5.7, 4.0); _arrow(ax, 4.75, 2.1, 5.7, 2.9)
    _arrow(ax, 8.25, 3.4, 8.6, 3.4)
    ax.set_title("Two Converging Lineages of the Counseling Profession", fontsize=14, color=NAVY)
    _save(fig, "fig_3_1")


# ---------------------------------------------------------------- Figure 3.2
def fig_3_2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    yrs = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    census = [550, 470, 300, 150, 90, 55, 40]
    ax1.plot(yrs, census, marker="o", color=NAVY, lw=2.5)
    ax1.set_title("State Psychiatric Hospital Inpatients\n(thousands, illustrative trend)", fontsize=10, color=NAVY)
    ax1.set_xlabel("Year"); ax1.set_ylabel("Inpatients (000s)")
    ax1.grid(alpha=0.3)
    cap = [10, 20, 45, 60, 70, 78, 85]
    dem = [12, 25, 55, 72, 82, 90, 96]
    ax2.fill_between(yrs, cap, dem, color=CORAL, alpha=0.35, label="Capacity gap")
    ax2.plot(yrs, dem, color=NAVY, lw=2, label="Need after deinstitutionalization")
    ax2.plot(yrs, cap, color=TEAL, lw=2, label="Community service capacity")
    ax2.set_title("Community Capacity vs. Population Need", fontsize=10, color=NAVY)
    ax2.set_xlabel("Year"); ax2.legend(fontsize=8)
    fig.suptitle("Deinstitutionalization: Census Decline vs. Community Capacity Gap", fontsize=13, color=NAVY)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    _save(fig, "fig_3_2")


# ---------------------------------------------------------------- Figure 4.1
def fig_4_1():
    fig, ax = _canvas(9, 6.5)
    pts = [(5, 5.1, "BEST AVAILABLE\nRESEARCH", TEAL), (1.9, 1.5, "CLINICAL\nEXPERTISE", NAVY),
           (8.1, 1.5, "CLIENT VALUES\n& PREFERENCES", CORAL)]
    tri = plt.Polygon([(p[0], p[1]) for p in pts], closed=True, facecolor=LIGHT,
                      edgecolor=SLATE, lw=2)
    ax.add_patch(tri)
    for x, y, t, c in pts:
        _box(ax, x - 1.3, y - 0.55, 2.6, 1.1, t, fc=c, ec=NAVY, tc="white", fs=9, bold=True)
    ax.text(5, 2.7, "EVIDENCE-BASED\nPRACTICE", ha="center", va="center",
            fontsize=12, fontweight="bold", color=NAVY)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("The Evidence-Based Practice Triangle", fontsize=14, color=NAVY)
    _save(fig, "fig_4_1")


# ============================================================ PART II FIGURES
def fig_5_1():
    fig, ax = _canvas(11, 5.5)
    steps = ["REFERRAL /\nINITIAL CONTACT", "INTAKE\nINTERVIEW", "COLLATERAL &\nRECORDS REVIEW",
             "RISK SCREENING\n(safety first)", "WORKING\nCONCEPTUALIZATION", "TREATMENT PLAN\n& CONSENT",
             "ONGOING\nRE-EVALUATION"]
    x = 0.15
    for s in steps:
        _box(ax, x, 2.7, 1.25, 1.3, s, fc=LIGHT, ec=NAVY, fs=7.6)
        if x < 8.5:
            _arrow(ax, x + 1.27, 3.35, x + 1.36, 3.35)
        x += 1.4
    _box(ax, 0.15, 1.0, 9.7, 1.2,
         "Throughout: cultural formulation, strengths inventory, diagnostic impressions (DSM-5-TR / ICD-11),\nand shared decision-making about goals, frequency, fees, and confidentiality limits.",
         fc=GOLD, ec=SLATE, fs=9)
    ax.set_title("The Intake and Case-Conceptualization Process Flow", fontsize=14, color=NAVY)
    _save(fig, "fig_5_1")


def fig_5_2():
    fig, ax = _canvas(10, 6.2)
    layers = [("PRESENTING PROBLEM\nsymptoms, complaints, triggers", CORAL),
              ("MAJOR THEMES\nshame, control, abandonment, safety", GOLD),
              ("PREDISPOSING FACTORS\ngenetics, attachment, trauma, learning history", SLATE),
              ("PRECIPITATING FACTORS\nrecent loss, transition, diagnosis, conflict", TEAL),
              ("PERPETUATING FACTORS\navoidance, reinforcement, beliefs, systems", NAVY),
              ("PROTECTIVE FACTORS\ninsight, supports, skills, motivation", "#7fb069")]
    y = 5.0
    for t, c in layers:
        _box(ax, 1.2, y, 7.6, 0.78, t, fc=c, ec=NAVY, tc="white", fs=8.5, bold=True)
        y -= 0.86
    _arrow(ax, 9.2, 5.4, 9.2, 0.9, color=SLATE, lw=1.5)
    ax.text(9.45, 3.1, "drilling\ndown", rotation=90, fontsize=8, color=SLATE, va="center")
    ax.set_title("Case Conceptualization House: The 5-P Structure (+ Protective Factors)",
                 fontsize=13, color=NAVY)
    _save(fig, "fig_5_2")


def fig_6_1():
    fig, ax = _canvas(10, 6)
    rows = [("BIOPSYCHO-SOCIAL-CULTURAL", "Genetic loading, neurochemistry, medical conditions;"
             " appraisals, core beliefs; family, work, culture, policy", NAVY),
            ("DIATHESIS-STRESS", "Vulnerability + precipitating stress \u2192 episode;\n"
             "diathesis can be genetic, psychological, or social", TEAL),
            ("LEARNING MODELS", "Classical conditioning (cue\u2013response), operant (reinforcement/"
             "punishment), observational (modeling)", CORAL),
            ("COGNITIVE MODELS", "Schema, distortion, attentional bias, intolerance of uncertainty", GOLD),
            ("SYSTEMIC / FAMILY", "Symptom as homeostatic signal; circular causality;\nroles and boundaries", SLATE)]
    y = 4.7
    for name, desc, c in rows:
        _box(ax, 0.3, y, 3.0, 0.95, name, fc=c, ec=NAVY, tc="white", fs=8.5, bold=True)
        _box(ax, 3.5, y, 6.2, 0.95, desc, fc=LIGHT, ec=SLATE, fs=8)
        y -= 1.05
    ax.set_title("Five Common Lenses of Etiological Theory", fontsize=14, color=NAVY)
    _save(fig, "fig_6_1")


def fig_7_1():
    fig, ax = _canvas(10, 6)
    rings = [("SOCIAL / POLICY\ninsurance parity, funding,\nlegislation, stigma campaigns", NAVY, 4.6),
             ("COMMUNITY / ORGANIZATIONAL\nschools, workplaces, faith-free civic orgs,\nprimary care integration", TEAL, 3.5),
             ("INDIVIDUAL / SKILLS\nscreening, brief interventions, resilience training,\nearly treatment", CORAL, 2.4)]
    for i, (t, c, r) in enumerate(rings):
        ax.add_patch(Circle((5, 3.0), r, facecolor="none", edgecolor=c, lw=3, alpha=0.8))
        ax.text(5, 3.0 + r - 0.45, t, ha="center", fontsize=8.5, fontweight="bold", color=c)
    ax.text(5, 3.0, "PERSON\nIN CONTEXT", ha="center", va="center", fontsize=10,
            fontweight="bold", color=INK)
    ax.set_xlim(0, 10); ax.set_ylim(0.2, 5.8); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Three Levels of Prevention Ecology (Caplan's Frame, Modernized)",
                 fontsize=13, color=NAVY)
    _save(fig, "fig_7_1")


def fig_8_1():
    fig, ax = _canvas(10, 6)
    cols = [("PSYCHIATRISTS\n(MD/DO)", "Medical degree;\nprescribe; psychotherapy\ntraining varies", NAVY),
            ("PSYCHOLOGISTS\n(PhD/PsyD)", "Assessment & therapy;\nsome prescribe in a few\nstates with extra training", TEAL),
            ("LIC. CLINICAL SOCIAL\nWORKERS (LCSW)", "Systems + therapy;\nlargest provider group\nin many regions", CORAL),
            ("LMHC / LPC\n(this profession)", "Counseling tradition;\ndiagnosis & therapy;\ncounseling identity", GOLD),
            ("PMHNP / APN", "Prescribing nurses;\nmed management\nin collaborative care", SLATE)]
    x = 0.25
    for t, d, c in cols:
        _box(ax, x, 3.3, 1.8, 1.5, t, fc=c, ec=NAVY, tc="white", fs=7.8, bold=True)
        _box(ax, x, 1.7, 1.8, 1.5, d, fc=LIGHT, ec=SLATE, fs=7.5)
        x += 1.95
    _box(ax, 0.25, 0.35, 9.5, 1.0,
         "Shared space: evidence-based psychotherapy. Distinguishing space: educational philosophy,\nlicensure exam route, and the profession's developmental/wellness emphasis.",
         fc="#dbeafe", ec=NAVY, fs=8.5)
    ax.set_title("The Behavioral Health Provider Ecosystem", fontsize=14, color=NAVY)
    _save(fig, "fig_8_1")


FIGGENS = {k[4:]: v for k, v in list(globals().items()) if k.startswith("fig_")}


# ---------------------------------------------------------------- Figure 4.2
def fig_4_2():
    fig, ax = _canvas(9, 7)
    levels = [("SYSTEMATIC REVIEWS /\nMETA-ANALYSES", 1.6, NAVY),
              ("RANDOMIZED CONTROLLED\nTRIALS (RCTs)", 2.8, TEAL),
              ("QUASI-EXPERIMENTAL,\nCOHORT & CASE-CONTROL", 4.0, CORAL),
              ("SINGLE-CASE / N-of-1,\nQUALITATIVE STUDIES", 5.2, GOLD),
              ("EXPERT OPINION, TEXTBOOKS,\nANECDOTES", 6.4, SLATE)]
    widths = [1.8, 3.0, 4.2, 5.4, 6.6]
    caveats = ["heterogeneity can hide\nclinically important differences",
               "publication bias; narrow\nsamples vs. real clinics",
               "confounding; direction\nof causality unclear",
               "high idiomographic value;\nlow generalizability",
               "use only when nothing\nbetter exists"]
    for (t, y, c), w, cav in zip(levels, widths, caveats):
        ax.add_patch(mpatches.Polygon([(5 - w / 2, y + 0.55), (5 + w / 2, y + 0.55),
                                       (5 + w / 2 + 0.3, y - 0.55), (5 - w / 2 - 0.3, y - 0.55)],
                                      closed=True, facecolor=c, edgecolor=NAVY, lw=1.5, alpha=0.85))
        ax.text(5, y, t, ha="center", va="center", fontsize=8, fontweight="bold", color="white")
        ax.annotate(cav, xy=(5 + w / 2 + 0.3, y), xytext=(7.0, y), fontsize=7, color=INK)
    ax.text(0.2, 3.5, "STRONGER\nDESIGN", rotation=90, fontsize=9, color=NAVY, fontweight="bold", va="center")
    ax.set_xlim(0, 10); ax.set_ylim(0.2, 7.4); ax.axis("off")
    ax.set_title("The Evidence Pyramid with Counseling-Specific Caveats", fontsize=13, color=NAVY)
    _save(fig, "fig_4_2")


# ============================================================ PART III FIGURES
def fig_9_1():
    fig, ax = _canvas(10, 6)
    _box(ax, 3.6, 4.8, 2.8, 1.0, "THE THERAPEUTIC\nALLIANCE", fc=NAVY, ec=NAVY, tc="white", fs=11, bold=True)
    parts = [("BOND\ntrust, liking, belief in\nthe method's fit", 0.4, TEAL),
             ("GOALS\nshared targets and\nagreed outcomes", 3.6, CORAL),
             ("TASKS\nconcrete activities both\naccept as reasonable", 6.8, GOLD)]
    for t, x, c in parts:
        _box(ax, x, 2.4, 2.8, 1.4, t, fc=c, ec=NAVY, tc="white" if c != GOLD else INK, fs=8.5, bold=True)
        _arrow(ax, x + 1.4, 3.85, 5.0, 4.75)
    _box(ax, 0.4, 0.6, 9.2, 1.2,
         "Alliance predicts outcome across modalities (robust 'common factor'); ruptures are normal \u2014\nwhat matters is detection and repair, which deepens the bond.",
         fc=LIGHT, ec=SLATE, fs=8.5)
    ax.set_title("Halloran's / Bordin's Three Components of the Working Alliance", fontsize=13, color=NAVY)
    _save(fig, "fig_9_1")


def fig_10_1():
    fig, ax = _canvas(10, 6)
    steps = [("EVENT", "triggering situation"), ("THOUGHT", "automatic cognition"),
             ("EMOTION", "feeling response"), ("BEHAVIOR", "action / avoidance"),
             ("CONSEQUENCE", "reinforcement loop")]
    cols = [TEAL, NAVY, CORAL, GOLD, SLATE]
    xs = [0.4, 4.0, 7.6, 6.2, 2.2]; ys = [4.6, 5.0, 3.6, 1.2, 1.2]
    for (t, d), c, x, y in zip(steps, cols, xs, ys):
        _box(ax, x, y, 2.1, 1.1, f"{t}\n{d}", fc=c, ec=NAVY, tc="white", fs=8, bold=True)
    order = [(2.5, 5.1, 4.0, 5.3), (6.1, 5.3, 7.8, 4.4), (8.4, 3.5, 7.6, 2.3),
             (6.2, 1.7, 4.3, 1.7), (2.2, 1.7, 1.4, 3.4), (1.6, 3.5, 1.5, 4.6)]
    for x1, y1, x2, y2 in order:
        _arrow(ax, x1, y1, x2, y2, color=SLATE, lw=1.6)
    ax.set_title("The Five-Part Cognitive-Behavioral Loop", fontsize=14, color=NAVY)
    _save(fig, "fig_10_1")


def fig_11_1():
    fig, ax = _canvas(10, 6)
    stages = ["PRECONTEMPLATION\nno intention to change\n(defense: minimization)",
              "CONTEMPLATION\nambivalence; weighing\ncosts and benefits",
              "PREPARATION\ncommitment + small steps;\nplanning begins",
              "ACTION\novert modification of\nbehavior & environment",
              "MAINTENANCE\nsustain change 6+ months;\nrelapse management"]
    cols = [SLATE, CORAL, GOLD, TEAL, NAVY]
    x = 0.25
    for s, c in zip(stages, cols):
        _box(ax, x, 2.8, 1.8, 1.6, s, fc=c, ec=NAVY, tc="white", fs=7.6, bold=True)
        if x < 8:
            _arrow(ax, x + 1.82, 3.6, x + 2.05, 3.6)
        x += 2.05
    _box(ax, 0.25, 1.0, 9.5, 1.2,
         "Counselor tasks shift by stage: raise awareness \u2192 resolve ambivalence (evocation, not\ninstallation) \u2192 support planning \u2192 reinforce action \u2192 consolidate gains. Relapse returns the person\nto an earlier stage \u2014 a learning loop, not a moral failure.",
         fc=LIGHT, ec=SLATE, fs=8.5)
    ax.set_title("Transtheoretical Model: Stages of Change Cycle", fontsize=14, color=NAVY)
    _save(fig, "fig_11_1")


def fig_12_1():
    fig, ax = _canvas(10, 6.4)
    _box(ax, 3.9, 5.1, 2.2, 0.9, "SETTLEMENT\n& TERMINATION", fc=NAVY, ec=NAVY, tc="white", fs=8.5, bold=True)
    stages = [("FORMING\norientation, politeness,\ntesting safety", TEAL, 0.3, 3.9),
              ("STORMING\nconflict, challenge to\nleader, subgroups", CORAL, 5.1, 3.9),
              ("NORMING\ncohesion, shared\nstandards, trust", GOLD, 0.3, 2.2),
              ("PERFORMING\nwork on goals;\nhere-and-now process", SLATE, 5.1, 2.2)]
    for t, c, x, y in stages:
        _box(ax, x, y, 2.4, 1.3, t, fc=c, ec=NAVY, tc="white" if c != GOLD else INK, fs=8, bold=True)
    _arrow(ax, 2.75, 4.55, 5.05, 4.55); _arrow(ax, 6.3, 3.85, 6.3, 3.55)
    _arrow(ax, 5.05, 2.85, 2.75, 2.85); _arrow(ax, 1.5, 3.6, 1.5, 2.2 - 0.0 + 1.32)
    _arrow(ax, 1.5, 3.55, 1.5, 3.52)  # placeholder no-op safe
    _box(ax, 0.3, 0.5, 7.2, 1.3,
         "Leadership levers: structuring, gatekeeping, linking, protecting, clarifying,\nsummarizing, blocking, and universalizing. Yalom's curative factors operate\nthrough these stages (instillation of hope, universality, altruism, feedback).",
         fc=LIGHT, ec=SLATE, fs=8)
    ax.set_title("Tuckman's Group Development Stages", fontsize=14, color=NAVY)
    _save(fig, "fig_12_1")


def fig_13_1():
    fig, ax = _canvas(10, 6.2)
    layers = [("SUPERVISOR\nrole modeling, teaching,\nevaluating, gatekeeping", NAVY),
              ("SUPERVISEE\nskills, theory, self-awareness,\nethical reasoning", TEAL),
              ("CLIENT\nwelfare is the organizing\npurpose of supervision", CORAL),
              ("CONTEXT\nagency, law, culture,\nreimbursement rules", GOLD)]
    y = 4.6
    for t, c in layers:
        _box(ax, 0.6, y, 4.2, 1.05, t, fc=c, ec=NAVY, tc="white", fs=8, bold=True)
        y -= 1.15
    _box(ax, 5.6, 1.2, 4.0, 3.6,
         "COMMON MODELS\n\nDevelopmental (Dreyer/Ronnestad):\nbeginner \u2192 intermediate \u2192 advanced\nself-authorship.\n\nDiscrimination model:\nskill, intervention, conceptualization,\nrelationship, systems, ethics.\n\nEmbedded CBT supervision:\nreview recorded sessions against\ncompetence scales.",
         fc=LIGHT, ec=SLATE, fs=8)
    ax.set_title("The Four-Pole Supervision System", fontsize=14, color=NAVY)
    _save(fig, "fig_13_1")


def fig_14_1():
    fig, ax = _canvas(10, 6)
    rows = [("PRIMARY\nprevent recurrence after\nrecovery; relapse prevention", NAVY),
            ("SECONDARY\nearly detection & short-\nterm treatment", TEAL),
            ("TERTIARY\nreduce disability from\nestablished disorder", CORAL)]
    y = 4.2
    for t, c in rows:
        _box(ax, 0.4, y, 3.1, 1.3, t, fc=c, ec=NAVY, tc="white", fs=8, bold=True)
        y -= 1.45
    _box(ax, 3.8, 0.6, 5.9, 5.0,
         "MODERN READING\n\nCaplan's triad was reinterpreted by Gordon (\n1987) as levels of prevention rather than levels\nof disorder:\n\n\u2022 Universal (all people; e.g., school social-\nemotional learning)\n\u2022 Selective (at-risk subgroups; e.g., children\nof parents with substance use disorder)\n\u2022 Indicated (high-risk individuals showing\nearly signs; e.g., attenuated psychosis\noutreach)\n\nCounselors work at every level \u2014 the\nprofession's founding promise.",
         fc=LIGHT, ec=SLATE, fs=8)
    ax.set_title("From Caplan's Levels to the Public-Health Prevention Matrix", fontsize=12.5, color=NAVY)
    _save(fig, "fig_14_1")


def fig_15_1():
    fig, ax = _canvas(10, 6)
    cols = [("DOCUMENTED\nRELIABILITY", "consistency of scores\nacross time, forms, raters", TEAL),
            ("DOCUMENTED\nVALIDITY", "does it measure what it\nclaims? construct, content,\ncriterion", NAVY),
            ("FAIRNESS &\nBIAS REVIEW", "differential item\nfunctioning; measurement\ninvariance across groups", CORAL),
            ("CLINICAL\nUTILITY", "adds information beyond\ninterview; actionable", GOLD),
            ("FEASIBILITY", "time, cost, training,\nburden on client", SLATE)]
    x = 0.25
    for t, d, c in cols:
        _box(ax, x, 3.4, 1.8, 1.5, t, fc=c, ec=NAVY, tc="white", fs=7.6, bold=True)
        _box(ax, x, 1.7, 1.8, 1.5, d, fc=LIGHT, ec=SLATE, fs=7.3)
        x += 1.95
    _box(ax, 0.25, 0.4, 9.5, 1.0,
         "Rule of thumb: tests inform the clinician; they do not replace the clinician.\nNo instrument diagnoses alone; no interview replaces measurement entirely.",
         fc="#dbeafe", ec=NAVY, fs=8.5)
    ax.set_title("Five Criteria for Selecting Any Assessment Instrument", fontsize=13, color=NAVY)
    _save(fig, "fig_15_1")



def generate_all(names=None):
    made = []
    for name, fn in sorted(globals().items()):
        if name.startswith("fig_") and callable(fn):
            if names is None or name in names:
                try:
                    fn()
                    made.append(name + ".png")
                except Exception as e:
                    print("FAILED", name, e)
    return made


if __name__ == "__main__":
    files = generate_all()
    print("Generated:", len(files))
    for f in files:
        print(" -", f)
