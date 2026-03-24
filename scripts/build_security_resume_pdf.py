"""
Generates the updated BaseResume_KhizarKhan.pdf (security-focused resume)
with added Projects section, GitHub/portfolio links, categorized skills,
and tightened experience bullets. Target: 2 pages.
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether, Table, TableStyle
)
from reportlab.lib import colors

OUT = '/Users/khizarkhan/projects/Portfolio/BaseResume_KhizarKhan.pdf'

BLACK = colors.HexColor('#111111')
DARK  = colors.HexColor('#1a2035')
DIM   = colors.HexColor('#5a6480')
NAVY  = colors.HexColor('#1d4ed8')

M = 0.60 * inch
doc = SimpleDocTemplate(
    OUT, pagesize=LETTER,
    leftMargin=M, rightMargin=M,
    topMargin=0.55 * inch, bottomMargin=0.55 * inch,
)
W = LETTER[0] - 2 * M  # ~7.3 inch usable width

# ── Styles ──────────────────────────────────────────────────────────
s_name = ParagraphStyle('name',
    fontName='Helvetica-Bold', fontSize=20,
    textColor=DARK, alignment=TA_CENTER,
    spaceAfter=10, spaceBefore=0)

s_contact = ParagraphStyle('contact',
    fontName='Helvetica', fontSize=8.5,
    textColor=DIM, alignment=TA_CENTER,
    spaceAfter=5, spaceBefore=0)

s_section = ParagraphStyle('section',
    fontName='Helvetica-Bold', fontSize=9.5,
    textColor=NAVY, alignment=TA_LEFT,
    spaceBefore=7, spaceAfter=2, leading=11)

s_jobtitle = ParagraphStyle('jobtitle',
    fontName='Helvetica-Bold', fontSize=9.2,
    textColor=DARK, spaceBefore=5, spaceAfter=0, leading=11)

s_company = ParagraphStyle('company',
    fontName='Helvetica-Oblique', fontSize=8.8,
    textColor=DIM, spaceBefore=1, spaceAfter=2, leading=11)

s_date = ParagraphStyle('date',
    fontName='Helvetica', fontSize=8.8,
    textColor=DIM, alignment=TA_RIGHT, leading=11)

s_bullet = ParagraphStyle('bullet',
    fontName='Helvetica', fontSize=8.7,
    textColor=DARK, leftIndent=12, firstLineIndent=0,
    spaceBefore=0, spaceAfter=1.5, leading=11.5)

s_skill_label = ParagraphStyle('skill_label',
    fontName='Helvetica-Bold', fontSize=8.7,
    textColor=DARK, leading=11.5, spaceAfter=0)

s_skill_val = ParagraphStyle('skill_val',
    fontName='Helvetica', fontSize=8.7,
    textColor=DARK, leading=11.5, spaceAfter=0)

s_proj_title = ParagraphStyle('proj_title',
    fontName='Helvetica-Bold', fontSize=8.8,
    textColor=DARK, spaceBefore=4, spaceAfter=1, leading=11)

s_proj_desc = ParagraphStyle('proj_desc',
    fontName='Helvetica', fontSize=8.6,
    textColor=DARK, spaceBefore=0, spaceAfter=1.5, leading=11.5)

s_cert = ParagraphStyle('cert',
    fontName='Helvetica', fontSize=8.7,
    textColor=DARK, alignment=TA_CENTER,
    spaceAfter=3, leading=11.5)

s_edu = ParagraphStyle('edu',
    fontName='Helvetica', fontSize=8.8,
    textColor=DARK, leading=11.5)

s_edu_r = ParagraphStyle('edu_r',
    fontName='Helvetica', fontSize=8.8,
    textColor=DIM, alignment=TA_RIGHT, leading=11.5)


def section(title):
    return [
        Paragraph(title.upper(), s_section),
        HRFlowable(width=W, thickness=0.7, color=NAVY, spaceAfter=4),
    ]


def skill_row(label, value):
    t = Table(
        [[Paragraph(f'<b>{label}:</b>', s_skill_label), Paragraph(value, s_skill_val)]],
        colWidths=[1.55 * inch, W - 1.55 * inch]
    )
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
        ('TOPPADDING',    (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    return t


def row_table(left_para, right_para, left_w=4.2 * inch):
    t = Table([[left_para, right_para]], colWidths=[left_w, W - left_w])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
        ('TOPPADDING',    (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    return t


def bullet_item(text):
    return Paragraph(f'\u2022 \u00a0{text}', s_bullet)


def job_block(title, company, date, bullets):
    items = [
        row_table(Paragraph(f'<b>{title}</b>', s_jobtitle), Paragraph(date, s_date)),
        Paragraph(company, s_company),
    ]
    for b in bullets:
        items.append(bullet_item(b))
    return KeepTogether(items)


# ── Build story ──────────────────────────────────────────────────────
story = []

# Header
story.append(Paragraph('Khizar Khan', s_name))
story.append(Paragraph(
    'khizarazakhan@gmail.com &nbsp;|&nbsp; +1 (437) 575-1079 &nbsp;|&nbsp;'
    ' linkedin.com/in/khizarkhan1999 &nbsp;|&nbsp;'
    ' github.com/weareinsims &nbsp;|&nbsp;'
    ' weareinsims.github.io',
    s_contact
))
story.append(HRFlowable(width=W, thickness=1.2, color=DARK, spaceAfter=5))

# Skills
story += section('Skills')
for label, value in [
    ('Endpoint & Systems',    'SCCM/MECM, Microsoft Intune, Autopilot, KACE SDA, MDT, Windows 10/11, Windows Server 2016/2019/2022, Active Directory, Group Policy, BitLocker, JAMF'),
    ('Security & Compliance', 'Microsoft Defender XDR, Microsoft Sentinel, Nessus, Vulnerability Management, Patch Compliance, Security Baselines, Azure MFA, Threat Mitigation'),
    ('Cloud & Infrastructure','Microsoft Azure, Azure AD, AWS, Exchange Online, Office 365, SharePoint, VMware, Citrix'),
    ('Scripting & Automation','PowerShell, Python, Microsoft Graph API, Patch Automation, Compliance Reporting'),
    ('ITSM & Networking',     'ServiceNow, Jira Service Management, Freshservice, ITIL, TCP/IP, DNS/DHCP, LAN, Wireshark, Cisco'),
]:
    story.append(skill_row(label, value))

# Certifications
story.append(Spacer(1, 2))
story += section('Certifications')
story.append(Paragraph(
    'CompTIA Security+ &nbsp; | &nbsp; ISC2 CC &nbsp; | &nbsp;'
    ' Microsoft Azure Fundamentals AZ-900 &nbsp; | &nbsp;'
    ' SC-200 Security Operations Analyst &nbsp; | &nbsp;'
    ' Career Essentials in Cybersecurity (Microsoft)',
    s_cert
))

# Education
story += section('Education')
story.append(row_table(
    Paragraph('<b>HBCom, Cybersecurity &amp; Information Technology</b> &nbsp;&nbsp; Toronto Metropolitan University', s_edu),
    Paragraph('Sept 2019 - Oct 2024', s_edu_r),
    left_w=5.1 * inch,
))

# Projects
story.append(Spacer(1, 2))
story += section('Projects')

for title, tech, desc in [
    (
        'Azure Sentinel SIEM Lab',
        'Azure Sentinel, KQL, Logic Apps, Bicep/ARM',
        'Deployed Microsoft Sentinel on Azure with 4 custom KQL detection rules covering brute force, impossible travel, '
        'privilege escalation, and suspicious PowerShell. Automated incident response via Logic App playbook with full '
        'IaC deployment using Bicep templates.',
    ),
    (
        'PowerShell Patch Compliance Dashboard',
        'PowerShell, Microsoft Graph API, Intune',
        'Pulls device patch compliance data from Intune via Microsoft Graph API and generates a self-contained HTML '
        'dashboard with charts, non-compliant device tables, and stale device tracking. Replaced manual Excel reporting.',
    ),
    (
        'Intune Autopilot Automation Suite',
        'PowerShell, Intune, Microsoft Graph API, Azure AD',
        'Scripts managing the full Autopilot device lifecycle: registration from CSV or local hash capture, profile '
        'creation and group assignment, status checking with color-coded output, and bulk device removal.',
    ),
    (
        'Vulnerability Scanner and Report Generator',
        'Python, nmap, CVE Analysis',
        'Python network scanner with port scanning, banner grabbing, and CVE matching (EternalBlue, BlueKeep, Apache '
        'path traversal). Generates a self-contained HTML report with severity charts and per-finding remediation steps.',
    ),
    (
        'Active Directory Security Audit Tool',
        'PowerShell, Active Directory, Security Hardening',
        'PowerShell audit script running 10 AD security checks: Kerberoastable accounts, unconstrained delegation, '
        'AS-REP roasting, privileged group sprawl, stale accounts, and weak password policies. Exports HTML report '
        'with severity breakdown.',
    ),
]:
    story.append(KeepTogether([
        Paragraph(
            f'<b>{title}</b>'
            f'<font name="Helvetica" size="8" color="#888888"> &nbsp; {tech}</font>',
            s_proj_title
        ),
        Paragraph(desc, s_proj_desc),
    ]))

# Experience
story.append(Spacer(1, 2))
story += section('Professional Experience')

story.append(job_block(
    'Endpoint Technology Specialist', 'Centennial College', 'Sept 2025 - Feb 2026',
    [
        'Administered <b>SCCM/MECM and Intune</b> across a large enterprise environment managing Windows endpoints for academic and administrative departments.',
        'Built, tested, and deployed Windows 10/11 images using <b>MECM, KACE SDA, MDT, and Intune Autopilot</b>, rolling out <b>240+ endpoints</b>.',
        'Automated driver, firmware, and configuration updates via <b>PowerShell</b>, reducing post-deployment incidents by <b>28%</b>.',
        'Enforced BitLocker, security baselines, and endpoint policies via Intune and Group Policy, achieving <b>98% patch and asset compliance</b>.',
        'Performed root cause analysis on recurring endpoint issues, contributing to a <b>35% reduction in deployment lead time</b>.',
        'Resolved <b>50+ tickets/week</b> via ServiceNow with 97% SLA compliance, 94% first call resolution, and 4.8/5 CSAT.',
    ]
))

story.append(job_block(
    'IT Support Desk', 'Canadian National Institute for the Blind Foundation', 'Apr 2025 - Aug 2025',
    [
        'Supported Windows and macOS environments with a focus on accessibility and system compatibility alongside assistive technologies.',
        'Delivered training on NVDA and JAWS, improving user adoption and reducing repeat support incidents.',
    ]
))

story.append(job_block(
    'Service Desk Technician', 'Business Intelligence Analytics Inc.', 'Sept 2023 - Sept 2024',
    [
        'Supported enterprise Windows and SaaS environments focused on system stability, access control, and troubleshooting.',
        'Assisted with <b>Azure Active Directory</b> administration, including user access troubleshooting and policy-driven provisioning.',
        'Supported security patching and vulnerability response, including remediation workflows for phishing and endpoint threats.',
        'Maintained <b>98% first call resolution</b> across network connectivity, remote desktop, and SaaS platform support.',
    ]
))

story.append(job_block(
    'IT Technician / eLearning CAL Developer', 'Ontario Power Generation', 'Jan 2021 - Aug 2021',
    [
        'Supported enterprise Windows and Citrix environments, ensuring system availability and SLA adherence.',
        'Analyzed support tickets and operational data to identify recurring issues and recommend preventive solutions.',
    ]
))

doc.build(story)
print(f'Saved: {OUT}')
