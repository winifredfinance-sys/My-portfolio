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
    "Senior Product Manager and Product Team Lead with 5 years in product management across health insurance, "
    "logistics, education and e-commerce, after founding an apparel distribution business. I set product strategy, lead cross-functional teams and use AI-assisted "
    "workflows to move from research to delivery faster. Currently Product Team Lead at Hadiel Health, leading a "
    "team of 20. Results include agency onboarding more than 99% faster, driver registration more than 90% faster, "
    "checkout conversion up 18%, course completion up 22%, 30+ product features delivered and team efficiency up "
    "20% through workflow automation and sprint optimisation."
)

SKILLS = [
    ("Strategy", "Product vision, roadmap ownership, outcome-based prioritisation, market research, go-to-market."),
    ("Discovery", "Client and user interviews, operations feedback, workflow reviews, funnel and friction analysis."),
    ("Delivery", "Agile and Scrum, sprint planning, backlog prioritisation, UAT, release planning."),
    ("Analytics", "KPIs and OKRs, funnel analysis, A/B testing, Google Analytics, Amplitude, SQL (basic), Excel."),
    ("Leadership", "Leading PMs and engineers, weekly performance updates, retrospectives, stakeholder management."),
    ("AI and tools", "AI-assisted research synthesis, requirements and test planning, Jira, Confluence, Figma, Miro."),
]

# (heading, sub-line, bullets)
EXPERIENCE = [
    ("Product Team Lead, Hadiel Health (health insurance / HMO)",
     "Lagos, Nigeria | 2026 - Present | Full-time",
     ["Lead product strategy for corporate clients and head a cross-functional team of 20: 3 product managers, "
      "4 senior engineers, QA and others.",
      "Built and launched a self-service client portal for HR teams and agencies, cutting agency onboarding time by "
      "more than 99%, from up to two days to under 10 minutes.",
      "Moved routine client requests for utilisation, member and reconciliation data into the portal, removing a "
      "steady stream of back-and-forth between clients and operations.",
      "Grounded the roadmap in client interviews and feedback from five operations teams, and deferred bulk "
      "dependant upload to protect the core launch.",
      "Established the team's operating rhythm: weekly performance updates, daily stand-ups, sprint planning and "
      "sprint retrospectives."]),
    ("Movam Technologies Limited (logistics)",
     "Lagos, Nigeria | 2024 - 2026 | Full-time<br/>"
     "<b>Senior Product Manager</b>, 2025 - 2026 (promoted) | <b>Product Manager</b>, 2024 - 2025",
     ["Owned product strategy and the roadmap for a B2B fleet-management platform serving 10,000+ users, spanning "
      "live tracking, trip management, electronic proof of delivery (EPOD), safety and activity reporting, and fleet "
      "maintenance and compliance.",
      "Identified onboarding friction, not demand, as the constraint on growth through research with 20+ drivers "
      "and operations staff, and made it the top roadmap priority.",
      "Led self-service partner onboarding, cutting driver registration time by more than 90%, from up to two weeks "
      "to under one day, and growing driver supply.",
      "Shipped 7 features, including partner onboarding, alternative-route planning, geofencing and remote locking, "
      "contributing to a 15% increase in customer satisfaction.",
      "Established data-led experimentation and feedback loops that contributed to a 12% increase in user activation.",
      "Introduced AI-assisted workflows for research synthesis, requirements, edge-case analysis and test planning, "
      "with human review before work entered the backlog."]),
    ("Product Manager, Edswot (education technology)",
     "Lagos, Nigeria | 2023 - 2024 | Consulting",
     ["Set backlog priorities for a team of 10-20 from learner and instructor feedback, weighed against business value.",
      "Launched a personalised learning dashboard that increased course completion by 22%.",
      "Introduced automated student-instructor feedback loops that raised NPS by 12 points.",
      "Coordinated go-to-market with marketing for new learning modules."]),
    ("Product Manager, Shopta, formerly WhipFix Hub (e-commerce marketplace)",
     "Lagos, Nigeria | 2021 - 2023 | Contract",
     ["Owned the end-to-end product lifecycle for a marketplace connecting buyers directly to sellers.",
      "Pinpointed checkout as the main conversion constraint through funnel analysis, journey analytics and user feedback.",
      "Prioritised fixes by value against effort and drove an 18% increase in checkout conversion.",
      "Partnered with UX/UI on the mobile experience, contributing to a 20% increase in daily active users.",
      "Led 12 engineers and designers on bi-weekly Agile releases."]),
    ("Founder, Maloxe",
     "Apparel distribution (wholesale and retail) | Lagos, Nigeria | 2019 - 2021",
     ["Founded and ran an apparel brand supplying clothing to wholesale and retail buyers across Lagos.",
      "Owned the full commercial cycle: product sourcing, pricing, sales, customer relationships, inventory and cash flow.",
      "Built the commercial judgment I bring to product work: understanding what customers will pay for, managing "
      "margins and making decisions with limited resources."]),
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
