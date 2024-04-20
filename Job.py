import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
import re

# Load the dataset (replace with your actual file path)
df = pd.read_excel('IPD Final Data Set (1) (2).xlsx')

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_pdf):
    text = ""
    pdf_reader = PdfReader(uploaded_pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract skills from text
def extract_skills(text):
    # This is a simple pattern matching for skill extraction, you may need to refine it based on your requirements
    pattern = r'\b(?:Python|Django|Flask|C|C\+\+|C#|DSA|Linux|Unix|Ubuntu|Cloud Computing|OpenCV|SQL|Git|API|Web Development|Problem Solving|Database Management|Data Modeling|ETL|Database Design|Query Optimization|Data Analysis|Data Visualization|Excel|Statistical Analysis|Data Cleaning|Java|Spring Framework|REST API|Object-Oriented Programming|Image Recognition|Machine Learning|TensorFlow|scikit-learn|Data Preprocessing|Model Evaluation|PHP|Laravel|MySQL|HTML|CSS|JavaScript|PHP Frameworks|React|Angular|VueJs|NodeJs|MongoDB|PostgreSQL|Version Control|Deep Learning|Neural Networks|Natural Language Processing|Responsive Design|Network Security|Penetration Testing|Firewall Management|Incident Response|Security Auditing|Continuous Integration/Continuous Deployment \(CI/CD\)|Docker|Kubernetes|AWS|Infrastructure as Code|Mobile App Development \(Android/iOS\)|Swift|React Native|Flutter|UI/UX Design|Mobile Platforms|Game Development|Game Engines \(Unity,Unreal Engine\)|3D Modeling|Physics|Game Design|Database Optimization|Backup and Recovery|Performance Tuning|R|Statistical Modeling|Big Data Technologies \(e.g Hadoop\)|Blockchain Technology|Solidity|Cryptography|Ethereum|Hyperledger|Software Testing|Test Automation|Bug Tracking|Quality Assurance|Testing Frameworks|User Interface Design|User Experience Design|Wireframing|Prototyping|Graphic Design|Usability Testing|PowerBI|MS Office|Communication Skills|Leadership|Teamwork|Time Management|Adaptability|Emotional Intelligence|Ethical Judgement|Hardware Design|Microcontroller|Requirement Analysis|UML|Business Analysis|Networking|TCP/IP|DNS|DHCP|Routing|Switching|Load Balancing|Wireless Networking|VPN|Wireshark|Cisco|CCNA|CCNP|ITIL|Scripting|Monitoring Tools|Troubleshooting|Embedded Systems|Microcontrollers|Digital Signal Processing|Analog Electronics|Verilog|VHDL|FPGA|Python Frameworks|Predictive Modeling|Feature Engineering|Time Series Analysis|Programming|Unity|Unreal Engine|Technical Knowledge|System Integration|Security|Project Management|Client Consultation|LAN/WAN|Router Configuration|Digital Marketing|SEO|SEM|Social Media Marketing|Content Marketing|Email Marketing|Google Analytics|Marketing Strategy|Marketing Analytics|Online Advertising|Copywriting|Brand Management|Public Relations|Market Research|Web Analytics|Conversion Rate Optimization|Social Media Management|Advertising|Content Strategy|Creative Thinking|Analytics|Product Development|Prototype Testing|User Feedback Analysis|Design Thinking|Agile Methodology|Collaboration|Innovative Thinking|Financial Analysis|Budgeting|Forecasting|Investment Planning|Risk Management|Financial Modeling|Accounting|Economics|Supply Chain Management|Logistics|Inventory Management|Procurement|Demand Planning|Vendor Management|Warehouse Management|SAP|ERP|Manufacturing Processes|Process Optimization|Quality Control|Lean Manufacturing|Six Sigma|CAD/CAM|Materials Science|Product Lifecycle Management \(PLM\)|Statistical Process Control \(SPC\)|Root Cause Analysis|Automation|Industrial Engineering|Safety Compliance|Environmental Science|Sustainability Practices|Climate Change Analysis|GIS|Remote Sensing|Environmental Policy|Research|Data Collection|Data Interpretation|Training|Presentation Skills|Legal Compliance|Regulatory Affairs|Contract Law|Corporate Governance|Ethics|Intellectual Property Law|Privacy Law|Legal Research|Legal Writing|Documentation|Policy Development|Dispute Resolution|Media Relations|Press Releases|Public Speaking|Crisis Communication|Content Creation|Editing|Analytical Skills|Event Planning|Marketing|ERP Implementation|Business Process Analysis|Data Migration|Customization|Technical Support|Valuation|Due Diligence|Investment Banking|Business Strategy|IT Knowledge|Risk Analysis|IT Governance|Compliance|Audit|Writing|Technical Writing|Grammar|Audit Procedures|Internal Controls|GAAP|SOX Compliance|Taxation|Financial Reporting|Negotiation|Contract Management|Supplier Relationship Management|Strategic Sourcing|E-commerce|Online Marketing|Content Management System \(CMS\)|Product Management|Customer Relationship Management \(CRM\)|Strategic Planning|Change Management|Decision Making|Innovation|Wellness Programs|Employee Assistance Programs \(EAP\)|Health Promotion|Training and Development|Employee Engagement|Performance Management|Learning Management Systems \(LMS\)|Instructional Design|Education Outreach|Language Proficiency|Translation|Cultural Awareness|Localization Tools|Business Continuity Planning|Scheduling|Investment Management|Portfolio Management|Quantitative Analysis|Asset Management|Tax Planning|Cash Management|Insurance Policies|Organizational Skills|Customer Service|IT Service Management|Social Media|Customer Engagement|Community Building|Conversion Optimization|A/B Testing|Keyword Research|Link Building|Search Engine Marketing \(SEM\)|Search Engine Optimization \(SEO\)|Digital Painting|Animation|Illustration|Photoshop|Adobe Illustrator|3D Studio Max|Maya|Blender|Video Editing|Motion Graphics|Adobe After Effects|Adobe Premiere Pro|Illustrator|Cinema 4D|3D Animation|Storyboarding|Virtual Reality|Augmented Reality|Computer Vision|ARKit|ARCore|Smart Contracts|DApp Development|Cryptocurrency|Algorithm Design|Data Structures|Mathematics|Software Development|Algorithm Optimization|Big O Notation|Pattern Recognition|Simulation|Engineering|Modeling|MATLAB|Simulink|Finite Element Analysis|CAD|Numerical Analysis|Aerodynamics|Aerospace Materials|Structural Analysis|Thermodynamics|Fluid Mechanics|Propulsion Systems|Control Systems|Spacecraft Systems|Avionics|Biomedical Imaging|Medical Device Design|Biosensors|Signal Processing|Programming \(e.g., Python\)|LabVIEW|Anatomy|Physiology|Regulatory Compliance|Chemical Engineering|Process Design|Material Science|Heat Transfer|Mass Transfer|Reaction Engineering|Safety Management|Environmental Compliance|Digital Electronics|Circuit Design|Power Systems|PLC Programming|Environmental Engineering|Water Quality Analysis|Air Quality Monitoring|Environmental Impact Assessment|Climate Change Mitigation|Sustainability|Renewable Energy|Environmental Regulations|Geotechnical Engineering|Soil Mechanics|Foundation Design|Slope Stability Analysis|Site Investigation|Civil Engineering|Construction Management|Metallurgy|Polymer Chemistry|Mechanical Testing|Research and Development|Mechanical Engineering|SolidWorks|Product Design|Finite Element Analysis \(FEA\)|Technical Drawing|Machine Design|Robotics|Geology|Reservoir Engineering|Drilling Engineering|Production Engineering|Well Testing|Oil and Gas Exploration|Petroleum Geophysics|Petrophysics|Oil and Gas Reserves Estimation|Oil and Gas Production Optimization|Risk Assessment|Mechatronics|ROS \(Robot Operating System\)|Motion Planning|Kinematics|Dynamics|Sensors and Actuators|Simulation Software|Algorithm Development|Revit|Steel Structures|Concrete Structures|Routing Protocols|Switching Technologies|VoIP|Wireless Communication|Telecommunication Systems|Data Networking|Spatial Analysis|Urban Design|Land Use Planning|Transportation Planning|Environmental Planning|Zoning|Community Development|Energy Analysis|Energy Efficiency|Energy Policy|Renewable Energy Systems|Solar Energy|Wind Energy|Energy Modeling|Nuclear Physics|Reactor Physics|Nuclear Engineering|Radiation Protection|Electrical Engineering|Instrumentation and Control|Nuclear Safety|Nuclear Regulatory Compliance|Criticality Safety|Radioactive Waste Management|Data Privacy|IT Compliance|Legal Knowledge|Patent Analysis|Trademark Management|Copyright Law|Contract Negotiation|Requirements Gathering|Integration|System Design|System Testing|Configuration Management|Network Configuration|Shell Scripting|Hardware Integration|Software Integration|Database Integration|API Integration|Budget Management|IT Asset Management|Cultural Sensitivity|Internationalization|Localization|Globalization|Linguistics|CAT Tools|Adobe Creative Suite|Chatbot Development|Process Improvement|Process Management|Conflict Resolution|Customer Relationship Management|Crisis Management|Community Management|Brand Development|Competitor Analysis|Business Development|Sales|Sales Strategy|Sales Training|CRM|Market Analysis|Channel Management|Product Knowledge|Merchandising|Retail|Sales Analysis|Technical Training|E-Learning|Curriculum Development|Learning Management Systems|Educational Technology|Content Development|Multimedia Design|Audio Editing|e-Learning Platforms|Curriculum Design|Online Assessment|Digital Learning|E-learning|Knowledge Management|Competitive Analysis|Market Intelligence|Business Intelligence|Financial Statement Analysis|Mergers and Acquisitions|Capital Markets|Corporate Finance|Equity Research|Business Valuation|DCF Analysis|Business Process Improvement|Tableau|Requirements Analysis|User Research|Optimization|Regulatory Requirements|Reporting|International Trade|Government Relations|Policy Analysis|Legislation|Political Science|Public Policy|Policy Writing|Report Writing|Qualitative Analysis|Critical Thinking|Statistics|Government Affairs|Legislative Advocacy|Stakeholder Engagement|Political Analysis|International Relations|Sustainable Development|Climate Modeling|GIS \(Geographic Information System\)|International Compliance|Global Workforce Management|Immigration Laws|Employee Benefits|Compensation Management|Benefits Administration|Job Evaluation|Salary Surveys|Employee Recognition|Incentive Programs|Total Rewards Strategy|HRIS \(Human Resources Information System\)|Employee Relations|HR Policies|Facilitation|Coaching|Organizational Development|Needs Analysis|Employee Onboarding|Recruitment|Interviewing|Human Resources|Talent Acquisition|Applicant Tracking System \(ATS\)|Branding|Onboarding Process|Public Health|Health Education|Community Outreach|Program Planning|Evaluation|Safety Procedures|Hazard Analysis|Occupational Health|Industrial Hygiene|Environmental Monitoring|Ergonomics|Chemical Exposure Assessment|Personal Protective Equipment|Property Management|Real Estate Law|Space Planning|Interior Design|Architectural Design|Visualization|Microsoft Office|File Management|Attention to Detail|Document Review|Litigation Support|Legal Project Management|Contract Review|Intellectual Property|Patent Law|Trademark Law|Licensing Agreements|Strategic Thinking|Patent Search|Analytical Thinking|Corporate Law|Environmental Laws and Regulations|Quality Management|FDA Regulations|ISO Standards|Clinical Trials|Pharmaceutical Regulations|Medical Device Regulations|Export/Import Regulations|Logistics Management|Cross-cultural Communication|International Trade Laws|Import/Export Regulations|Customs Documentation|Trade Compliance Management|Global Logistics|Cross-Border Trade|Compliance Auditing|Customs Regulations|Import/Export Documentation|Shipping Coordination|Tax Analysis|International Taxation|Tax Compliance|Transfer Pricing|Tax Reporting|International Tax|Probability and Statistics|Credit Scoring Models|Investment Analysis|Business Analytics|Credit Analysis|Loan Origination|Loan Processing|Mortgage Lending|Retirement Planning|Estate Planning|Financial Planning|Insurance Planning|Asset Allocation|Credit Scoring|Derivatives Trading|Investment Strategies|Derivatives|Financial Markets|Investment Evaluation|Financial Modelling|Actuarial Science|Cash Flow Analysis|IFRS)\b'
    skills = re.findall(pattern, text, flags=re.IGNORECASE)
    return list(set(map(lambda x: x.lower(), skills)))

# Function to recommend job roles based on student's skills
def recommend_job_roles(student_skills, df):
    # Filter job roles based on at least one matching skill with student's skills
    matching_roles = df.loc[:, student_skills].eq(1).any(axis=1)

    # If no matching roles found, return an empty DataFrame
    if not matching_roles.any():
        return pd.DataFrame(columns=['Preference No.', 'Job Roles', 'Matching Skills Percentage'])

    # Calculate the number of matching skills for each job role
    df['Matching Skills'] = df.loc[matching_roles, student_skills].sum(axis=1)

    # Calculate the total number of skills required for each job role
    df['Total Skills'] = df.loc[:, student_skills].sum(axis=1)

    # Calculate the matching skills percentage for each job role
    df['Matching Skills Percentage'] = (df['Matching Skills'] / len(student_skills)) * 100

    # Sort job roles by descending matching skills percentage
    sorted_roles = df[matching_roles].sort_values(by='Matching Skills Percentage', ascending=False)

    # Reset index to start preference number from 1
    sorted_roles.reset_index(drop=True, inplace=True)

    # Add preference number starting from 1
    sorted_roles['Preference No.'] = sorted_roles.index + 1

    # Display only the top 25 roles
    top_25_roles = sorted_roles.head(25)

    return top_25_roles[['Preference No.', 'Job Roles', 'Matching Skills Percentage']]


def main():
    st.title("Job Recommendation App")

    # Upload Resume
    st.header("Upload Resume")
    resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

    if resume_file is not None:
        # Extract skills from the uploaded resume
        resume_text = extract_text_from_pdf(resume_file)
        student_skills = extract_skills(resume_text)

        # Convert student skills to lowercase to match the column names in the dataset
        student_skills = [skill.lower() for skill in student_skills]

        # Display extracted skills
        st.header("Extracted Skills")
        st.write(student_skills)

        # Recommend job roles based on extracted skills
        recommended_roles = recommend_job_roles(student_skills, df)

        # Display recommended job roles
        st.header("Recommended Top 25 Job Roles")
        st.table(recommended_roles)

if __name__ == "__main__":
    main()
