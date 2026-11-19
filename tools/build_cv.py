"""Build cv.pdf for Winifred Ukoh.

Edit the text in this file, then run from the repository root:

    pip install reportlab
    python3 tools/build_cv.py

It rewrites cv.pdf. Keep this text and the website saying the same thing.
"""
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (HRFlowable, KeepTogether, ListFlowable, ListItem,
                                Paragraph, SimpleDocTemplate, Spacer)

OUT = Path(__file__).resolve().parent.parent / "cv.pdf"

NAME = "WINIFRED UKOH"
TITLE = "Product Team Lead | Senior Product Manager"
CONTACT = ('Lagos, Nigeria | +234 808 666 1738 | '
           '<a href="mailto:winifredukoh3@gmail.com">winifredukoh3@gmail.com</a> | '
           '<a href="https://www.linkedin.com/in/winifred-ukohpm">linkedin.com/in/winifred-ukohpm</a> | '
           'Portfolio: <a href="https://winifredukoh.vercel.app">winifredukoh.vercel.app</a>')

SUMMARY = (
    "Senior Product Manager with 5+ years of professional experience, including product management since 2023, "
    "across logistics, e-commerce, education and health insurance. Currently Product Team Lead at Hadiel Health, "
    "leading a team of 20 (3 product managers, engineering and QA). I set product direction and roadmaps, ground "
    "decisions in research with users and operations teams, and turn insight into measurable outcomes: agency "
    "onboarding cut from up to two days to under 10 minutes, driver registration cut from up to two weeks to under "
    "one day, and an 18% lift in checkout conversion."
)

ACHIEVEMENTS = [
    "Cut agency onboarding from up to <b>two days</b> to <b>under 10 minutes</b> with a self-service client portal (Hadiel Health).",
    "Cut driver registration from up to <b>two weeks</b> to <b>under one day</b> with self-service partner onboarding (Movam).",
    "Increased checkout conversion by <b>18%</b>; mobile experience work contributed to a <b>20%</b> rise in daily active users (Shopta).",
    "Improved course completion by <b>22%</b> and NPS by <b>12 points</b> through a personalised learning dashboard and "
    "automated feedback loops (Edswot).",
    "Launched 7 high-impact features that contributed to a <b>15%</b> improvement in customer satisfaction and a "
    "<b>12%</b> improvement in user activation (Movam).",
    "Launched 30+ digital product features across roles and improved team efficiency by <b>20%</b> through workflow "
    "automation and sprint optimisation.",
]

SKILLS = [
    ("Strategy and Vision", "Product vision, roadmap ownership, outcome-based prioritisation, market research, go-to-market coordination."),
    ("Discovery", "User and client interviews, operations feedback, workflow reviews, funnel and friction-point analysis."),
    ("Execution", "Agile delivery, sprint planning, backlog prioritisation, UAT coordination, release documentation."),
    ("Analytics", "KPI and OKR tracking, funnel analysis, A/B testing, product performance metrics."),
    ("Leadership", "Cross-functional team leadership, weekly performance updates, sprint retrospectives, stakeholder management, workshop facilitation."),
    ("Tools and AI", "AI-assisted product workflows, Jira, Confluence, Figma, Miro, Google Analytics, Amplitude, SQL (basic), Excel."),
]

# (heading, sub-line, bullets)
EXPERIENCE = [
    ("Product Team Lead, Hadiel Health (health insurance / HMO)",
     "Lagos, Nigeria | Mar 2026 - Present | Full-time",
     ["Lead a cross-functional team of 20: 3 product managers, 2 senior back-end engineers, 2 senior front-end "
      "engineers, QA and others.",
      "Led a self-service client portal for HR teams and agencies (members, utilisation, health-data summaries and "
      "reconciliation) and a companion enrollee app for members.",
      "Cut agency onboarding from up to two days to under 10 minutes: agencies now upload their own members instead "
      "of emailing spreadsheets for manual upload.",
      "Confirmed client needs through client interviews and feedback from enrolment, customer service, case, "
      "provider relations and agency relations officers.",
      "Run weekly performance updates, daily stand-ups, sprint planning and sprint retrospectives."]),
    ("Movam Technologies Limited (logistics)",
     "Lagos, Nigeria | Jan 2023 - Mar 2026 | Full-time<br/>"
     "<b>Senior Product Manager</b>, Nov 2025 - Mar 2026 (promoted) | <b>Product Manager</b>, Jan 2023 - Oct 2025",
     ["Owned the product lifecycle for multi-platform B2B solutions serving 10,000+ users, from discovery and "
      "roadmap through launch and optimisation.",
      "Led self-service partner onboarding after discovery with 20+ drivers and operations staff, cutting driver "
      "registration from up to two weeks to under one day.",
      "Led alternative-route planning, which led to fewer route-deviation alerts and faster operations follow-up, "
      "followed by geofencing and remote locking.",
      "Launched 7 high-impact features that contributed to a 15% improvement in customer satisfaction.",
      "Built data-led experimentation and feedback loops that contributed to a 12% improvement in user activation."]),
    ("Product Manager, Shopta (e-commerce marketplace)",
     "Lagos, Nigeria | Jan 2025 - Jan 2026 | Contract",
     ["Found checkout friction through funnel analysis, product analytics and user feedback, prioritised fixes by "
      "value against effort, and drove an 18% increase in checkout conversion.",
      "Led a cross-functional team of 12 engineers and designers using Agile methods and bi-weekly releases.",
      "Partnered with UX/UI designers on the mobile experience, which contributed to a 20% increase in daily active users."]),
    ("Product Manager, Edswot (education technology)",
     "Lagos, Nigeria | Aug 2024 - Sep 2025 | Consulting | Team of 10-20",
     ["Led the launch of a personalised learning dashboard that improved course completion by 22%.",
      "Introduced automated student-instructor feedback loops, lifting NPS by 12 points.",
      "Prioritised the backlog from learner and instructor feedback and business value; coordinated go-to-market "
      "with marketing for new learning modules."]),
    ("Founder, Maloxe",
     "Apparel distribution (wholesale and retail) | Lagos, Nigeria | 2019 - 2022",
     ["Founded and ran an apparel brand supplying clothing to wholesale and retail buyers across Lagos.",
      "Owned the full commercial cycle: product sourcing, pricing, sales, customer relationships, inventory and cash flow.",
      "Built the commercial judgment I bring to product work: understanding what customers will pay for, managing "
      "margins, and making decisions with limited resources."]),
    ("Founder, Brainbox Ninja",
     'Independent product | 2026 - Present | <a href="https://brainbox-ninja.vercel.app">brainbox-ninja.vercel.app</a>',
     ["Defined, specified and shipped a free puzzle game for players of every age by directing AI-assisted "
      "development; launched to an initial group of 25 test players.",
      "Used player feedback to expand the question bank and plan adaptive difficulty."]),
]

EDUCATION = "Crawford University, Ogun State, Nigeria - BSc, Biochemistry (2015 - 2019)"

CERTIFICATIONS = [
    "AI for Product Management &amp; Innovation, Agile Enterprise Coach (Certificate of Completion)",
    "Artificial Intelligence for Product Managers, Product School (2024)",
    "Product Strategy Micro-Certification, Product School (2024)",
    "Product-Led Growth, Product School (2024)",
    "Product Road-Mapping, Product School (2024)",
    "Software Processes and Agile Practices, University of Alberta (2024)",
    "Client Needs and Software Requirements, University of Alberta (2024)",
]

INK = HexColor("#111111")
MUT = HexColor("#444444")
base = ParagraphStyle("base", fontName="Helvetica", fontSize=9.6, leading=12.6, textColor=INK, alignment=TA_LEFT)
S = {
    "name": ParagraphStyle("name", base, fontName="Helvetica-Bold", fontSize=21, leading=24),
    "title": ParagraphStyle("title", base, fontName="Helvetica-Bold", fontSize=11.5, leading=15),
    "contact": ParagraphStyle("contact", base, fontSize=8.8, leading=12, textColor=MUT),
    "h": ParagraphStyle("h", base, fontName="Helvetica-Bold", fontSize=10.5, leading=13, spaceBefore=9, spaceAfter=2),
    "role": ParagraphStyle("role", base, fontName="Helvetica-Bold", fontSize=10, leading=13, spaceBefore=6),
    "sub": ParagraphStyle("sub", base, fontSize=9, leading=12, textColor=MUT, spaceAfter=1),
    "body": base,
}
LINK = 'color="#1a4fa0"'


def links(t):
    return t.replace("<a href=", f"<a {LINK} href=")


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(links(i), S["body"]), leftIndent=11, value="•") for i in items],
        bulletType="bullet", start="•", leftIndent=11, bulletFontSize=8, spaceBefore=1)


def heading(t):
    return [Paragraph(t, S["h"]), HRFlowable(width="100%", thickness=0.6, color=INK, spaceBefore=0, spaceAfter=4)]


def build():
    story = [Paragraph(NAME, S["name"]), Paragraph(TITLE, S["title"]), Paragraph(links(CONTACT), S["contact"])]
    story += heading("PROFESSIONAL SUMMARY") + [Paragraph(SUMMARY, S["body"])]
    story += heading("KEY ACHIEVEMENTS") + [bullets(ACHIEVEMENTS)]
    story += heading("CORE SKILLS") + [bullets([f"<b>{k}:</b> {v}" for k, v in SKILLS])]
    story += heading("PROFESSIONAL EXPERIENCE")
    for role, sub, items in EXPERIENCE:
        story.append(KeepTogether([Paragraph(role, S["role"]), Paragraph(links(sub), S["sub"]), bullets(items)]))
    story += heading("EDUCATION") + [Paragraph(EDUCATION, S["body"])]
    story += heading("CERTIFICATIONS") + [bullets(CERTIFICATIONS)]

    doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=16 * mm, rightMargin=16 * mm,
                            topMargin=14 * mm, bottomMargin=14 * mm,
                            title="Winifred Ukoh - CV", author="Winifred Ukoh",
                            subject="Product Team Lead | Senior Product Manager")
    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
