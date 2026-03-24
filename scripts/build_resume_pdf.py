from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
)
from reportlab.lib import colors

OUT = '/Users/khizarkhan/projects/Portfolio/Resume_BA_KhizarKhan.pdf'

NAVY   = colors.HexColor('#1d4ed8')
DARK   = colors.HexColor('#1a2035')
DIM    = colors.HexColor('#5a6480')
WHITE  = colors.white

M = 0.75 * inch

doc = SimpleDocTemplate(
    OUT,
    pagesize=LETTER,
    leftMargin=M, rightMargin=M,
    topMargin=M, bottomMargin=M,
)

W = LETTER[0] - 2 * M  # usable width

# ── Styles ──────────────────────────────────────────────────────────
s_name = ParagraphStyle('name',
    fontName='Helvetica-Bold', fontSize=22,
    textColor=DARK, alignment=TA_CENTER,
    spaceAfter=10, spaceBefore=0,
)
s_contact = ParagraphStyle('contact',
    fontName='Helvetica', fontSize=9,
    textColor=DIM, alignment=TA_CENTER,
    spaceAfter=10, spaceBefore=0,
)
s_section = ParagraphStyle('section',
    fontName='Helvetica-Bold', fontSize=9,
    textColor=NAVY, alignment=TA_LEFT,
    spaceBefore=10, spaceAfter=2,
    leading=11,
)
s_body = ParagraphStyle('body',
    fontName='Helvetica', fontSize=10,
    textColor=DARK, alignment=TA_LEFT,
    spaceBefore=0, spaceAfter=4,
    leading=13,
)
s_bold = ParagraphStyle('bold',
    fontName='Helvetica-Bold', fontSize=10.5,
    textColor=DARK, alignment=TA_LEFT,
    spaceBefore=6, spaceAfter=2,
    leading=13,
)
s_date = ParagraphStyle('date',
    fontName='Helvetica', fontSize=9.5,
    textColor=DIM, alignment=TA_LEFT,
    spaceBefore=0, spaceAfter=2,
    leading=12,
)
s_bullet = ParagraphStyle('bullet',
    fontName='Helvetica', fontSize=9.5,
    textColor=DARK, alignment=TA_LEFT,
    leftIndent=14, firstLineIndent=-10,
    spaceBefore=0, spaceAfter=2,
    leading=12.5,
)
s_skill = ParagraphStyle('skill',
    fontName='Helvetica', fontSize=9.5,
    textColor=DARK, alignment=TA_LEFT,
    spaceBefore=0, spaceAfter=2,
    leading=12,
)
s_summary = ParagraphStyle('summary',
    fontName='Helvetica', fontSize=10,
    textColor=DARK, alignment=TA_LEFT,
    spaceBefore=4, spaceAfter=6,
    leading=14,
)

def section(title):
    return [
        Paragraph(title.upper(), s_section),
        HRFlowable(width=W, thickness=1, color=NAVY, spaceAfter=4),
    ]

def bullet_item(text):
    return Paragraph(f'\u2022\u00a0\u00a0{text}', s_bullet)

def job(title, company, date, bullets):
    items = [
        Paragraph(f'<b>{title}</b>', s_bold),
        Paragraph(f'{company} &nbsp;&nbsp;|&nbsp;&nbsp; {date}', s_date),
    ]
    for b in bullets:
        items.append(bullet_item(b))
    items.append(Spacer(1, 4))
    return KeepTogether(items)

def skill_row(label, detail):
    return Paragraph(f'<b>{label}:</b> {detail}', s_skill)

# ── Content ─────────────────────────────────────────────────────────
story = []

# Name
story.append(Paragraph('Khizar Khan', s_name))

# Contact
story.append(Paragraph(
    'khizarazakhan@gmail.com &nbsp;|&nbsp; +1 (437) 575-1079 &nbsp;|&nbsp; '
    'linkedin.com/in/khizarkhan1999/ &nbsp;|&nbsp; weareinsims.github.io/ba-portfolio',
    s_contact
))

# Summary
story += section('Professional Summary')
story.append(Paragraph(
    'Business analyst with a background in IT operations and hands-on experience translating '
    'technical complexity into structured requirements, process documentation, and stakeholder-ready '
    'deliverables. Comfortable working across the full BA lifecycle from discovery through to '
    'implementation support. Strong grasp of ITSM environments, having worked in and analyzed service '
    'desk operations from both the practitioner and analyst side.',
    s_summary
))

# Skills
story += section('Skills')
story.append(skill_row('Requirements Elicitation', 'Stakeholder interviews, workshops, gap analysis, user story writing'))
story.append(skill_row('Process Documentation', 'AS-IS/TO-BE mapping, BPMN, process flows, standard operating procedures'))
story.append(skill_row('BA Deliverables', 'BRD, functional specifications, use cases, user stories (Gherkin), personas'))
story.append(skill_row('Analysis', 'Data analysis, KPI reporting, dashboard design, Excel'))
story.append(skill_row('ITSM Platforms', 'ServiceNow, Jira Service Management, Freshservice'))
story.append(skill_row('Collaboration Tools', 'Confluence, Lucidchart, Microsoft 365, SharePoint'))
story.append(skill_row('Methodologies', 'Agile, Scrum, ITIL'))
story.append(skill_row('Other', 'SQL (basic), Python (basic), PowerShell (basic)'))

# BA Projects
story += section('BA Projects')

projects = [
    (
        'IT Service Desk Process Improvement',
        [
            'Conducted gap analysis comparing current service desk operations against ITIL best practices across 6 process areas, scoring each gap by impact and effort.',
            'Produced a full Business Requirements Document covering incident management, change control, knowledge management, and onboarding workflows.',
            'Developed a future-state proposal with prioritized recommendations, KPI targets, and a phased implementation plan.',
        ]
    ),
    (
        'IT Help Desk Analytics Dashboard',
        [
            'Analyzed 1,847 simulated tickets across a 6-month period to identify operational trends and performance gaps.',
            'Built an interactive dashboard with KPI cards, trend charts, and breakdown tables covering volume, resolution time, SLA compliance, FCR, and CSAT.',
            'Produced 5 written recommendations with estimated impact, each directly tied to findings in the data.',
        ]
    ),
    (
        'ServiceNow ITSM Implementation BRD',
        [
            'Developed a full BRD for a ServiceNow ITSM Pro implementation based on discovery interviews with 5 stakeholder groups.',
            'Documented 40+ functional requirements across 6 modules: Incident Management, Service Requests, Change Management, Asset Management, Self-Service Portal, and Reporting.',
            'Included risk register, success criteria, constraints, assumptions, implementation timeline, and a 15-item service catalog appendix.',
        ]
    ),
    (
        'IT Onboarding Workflow - User Stories',
        [
            'Developed 4 user personas covering new hires, hiring managers, IT agents, and IT managers, each with situation, goals, and frustrations.',
            'Wrote 10 user stories in Agile format with full Gherkin acceptance criteria (Given/When/Then), covering the complete onboarding and offboarding lifecycle including edge cases.',
        ]
    ),
]

for title, bullets in projects:
    block = [Paragraph(f'<b>{title}</b>', s_bold)]
    for b in bullets:
        block.append(bullet_item(b))
    block.append(Spacer(1, 4))
    story.append(KeepTogether(block))

# Professional Experience
story += section('Professional Experience')

story.append(job(
    'Endpoint Technology Specialist',
    'Centennial College',
    'Sept 2025 - Feb 2026',
    [
        'Gathered operational requirements from IT and academic department stakeholders to define endpoint deployment standards and service expectations.',
        'Documented and maintained technical SOPs for patch deployment, endpoint imaging, and access provisioning workflows across 240+ managed devices.',
        'Analyzed deployment failure patterns and recurring incidents to identify root causes and recommend process improvements, reducing deployment lead time by 35 percent.',
        'Generated patch compliance and deployment status reports for IT leadership to support audit readiness, security reviews, and SLA accountability.',
        'Administered ServiceNow tickets and managed 50+ weekly incidents and service requests, maintaining 97 percent SLA compliance and a CSAT of 4.8 out of 5.',
        'Collaborated with infrastructure, security, networking, and AV teams on cross-functional issues, acting as a coordination point for escalated requests.',
    ]
))

story.append(job(
    'IT Support Desk',
    'Canadian National Institute for the Blind Foundation',
    'Apr 2025 - Aug 2025',
    [
        'Assessed accessibility requirements for end users relying on assistive technologies (NVDA, JAWS) and translated these into support and training workflows.',
        'Delivered structured one-on-one and group training, improving user adoption and reducing repeat incidents.',
    ]
))

story.append(job(
    'Service Desk Technician',
    'Business Intelligence Analytics Inc.',
    'Sept 2023 - Sept 2024',
    [
        'Conducted root cause analysis on recurring incidents and contributed to documentation and reporting improvements that raised first call resolution to 98 percent.',
        'Supported Azure Active Directory administration and policy-driven provisioning, documenting access workflows and control gaps.',
    ]
))

story.append(job(
    'IT Technician / eLearning CAL Developer',
    'Ontario Power Generation',
    'Jan 2021 - Aug 2021',
    [
        'Analyzed support ticket data to identify recurring issues and recommend preventive solutions to reduce incident volume.',
        'Assisted with system access, provisioning, and remote support documentation across multiple internal departments.',
    ]
))

# Education
story += section('Education')
story.append(Paragraph('<b>HBCom in Cybersecurity & Information Technology</b>', s_bold))
story.append(Paragraph('Toronto Metropolitan University &nbsp;&nbsp;|&nbsp;&nbsp; Sept 2019 - Oct 2024', s_date))
story.append(Spacer(1, 4))

# Certifications
story += section('Certifications')
for cert in [
    'CompTIA Security+',
    'ISC2 Certified in Cybersecurity (CC)',
    'Microsoft Azure Fundamentals (AZ-900)',
    'Microsoft Security Operations Analyst Associate',
    'Career Essentials in Cybersecurity by Microsoft & LinkedIn',
]:
    story.append(bullet_item(cert))

doc.build(story)
print(f'Saved: {OUT}')
