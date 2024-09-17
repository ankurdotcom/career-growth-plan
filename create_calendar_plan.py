import csv
from datetime import datetime, timedelta

# 16-week detailed plan with a focus on one goal at a time
weekly_plan = [
    # Week 1: Focus on Cloud-Native Architecture
    [
        {"task": "Cloud-Native Architecture Basics", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Cloud-Native Design Patterns", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Exploring Kubernetes", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Containerization with Docker", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Cloud Strategy", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Hands-On Kubernetes Practice", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 2: Focus on Cloud-Native (Continuation)
    [
        {"task": "Kubernetes Deep Dive", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Cloud-Native Deployment Strategies", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Service Mesh in Kubernetes", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Session: Architecting Cloud Systems", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Scalability Techniques", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Cloud-Native Architecture POC", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 3: Focus on DevOps
    [
        {"task": "DevOps Introduction", "duration": 60, "start_time": "09:00 AM"},
        {"task": "CI/CD Pipeline Overview", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Jenkins CI Setup", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Automating Jenkins CI/CD", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: DevOps Culture", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Jenkins Pipeline Hands-On", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 4: Focus on DevOps (Advanced)
    [
        {"task": "Container Orchestration with Kubernetes", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Advanced CI/CD Pipelines", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Deploying Microservices using CI/CD", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Monitoring and Alerting in DevOps", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Session: DevOps Transformation", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: CI/CD Pipeline Optimization", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 5: Focus on Microservices Design
    [
        {"task": "Introduction to Microservices", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Microservices Design Patterns", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Spring Cloud for Microservices", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Microservices Case Study", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Microservices Strategy", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Implementing Microservices", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 6: Focus on Microservices (Advanced)
    [
        {"task": "Advanced Microservices Architecture", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Resilient Microservices with Netflix OSS", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Microservices Monitoring and Security", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Event-Driven Architecture in Microservices", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Scaling Microservices", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Advanced Microservices Hands-On", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 7: Focus on AI/ML Basics
    [
        {"task": "Introduction to AI/ML", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Machine Learning on AWS", "duration": 60, "start_time": "09:00 AM"},
        {"task": "AI/ML POC Planning", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Cloud Architecture with AI/ML", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: AI Trends", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: AI/ML Proof of Concept", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 8: Focus on AI/ML (Advanced)
    [
        {"task": "Deep Learning Basics", "duration": 60, "start_time": "09:00 AM"},
        {"task": "AI/ML Model Deployment on Cloud", "duration": 60, "start_time": "09:00 AM"},
        {"task": "TensorFlow for AI", "duration": 60, "start_time": "09:00 AM"},
        {"task": "AI/ML Performance Tuning", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: AI Ethics", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Deploying AI Models", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 9: Focus on Public Speaking & Leadership
    [
        {"task": "Public Speaking Practice", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Skills Enhancement", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Advanced Public Speaking", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Influence & Leadership Podcast", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership in Technology Reading", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Public Speaking Event Simulation", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
  # Week 10: Focus on Cloud Security
   [
        {"task": "Introduction to Cloud Security", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Identity & Access Management", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Data Encryption in Cloud", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Cloud Security Best Practices", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Cloud Security Trends", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Cloud Security Hands-On", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 11: Focus on Networking and API Security
    [
        {"task": "Networking Basics for Architects", "duration": 60, "start_time": "09:00 AM"},
        {"task": "API Security Essentials", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Securing Microservices APIs", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Networking with Cloud Platforms", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Security Policies", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Implementing API Security", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 12: Focus on Advanced Leadership Skills
    [
        {"task": "Developing Emotional Intelligence", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Communication Skills", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Conflict Resolution in Teams", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Advanced Decision-Making Strategies", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Leadership Philosophy", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Leadership Workshop", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 13: Focus on Cloud-Native Infrastructure
    [
        {"task": "Introduction to Infrastructure as Code", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Setting up Terraform", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Infrastructure Automation in Cloud", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Cloud Cost Management", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Cloud Infrastructure", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Deploying Infrastructure with Terraform", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 14: Focus on Cloud Networking
    [
        {"task": "Introduction to Cloud Networking", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Networking Solutions in AWS", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Setting up VPC and Subnets", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Advanced Cloud Networking Strategies", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Network Management", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Networking in Cloud Hands-On", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 15: Focus on AI/ML and Data Engineering (Advanced)
    [
        {"task": "Data Engineering for AI/ML", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Big Data Processing in Cloud", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Building Data Pipelines", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Optimizing AI/ML Models with Big Data", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Big Data Strategy", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Data Engineering POC", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ],
    # Week 16: Focus on Networking, Final Reflection, and Review
    [
        {"task": "Networking in Architect Roles", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Final Reflection on Learning", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Final Presentation Preparation", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Leadership Reading: Future Career Plans", "duration": 60, "start_time": "09:00 AM"},
        {"task": "Weekend: Final Review and Reflection", "duration": 120, "start_time": "10:00 AM"},
        {"task": "Cheat Day", "duration": 0, "start_time": "All Day"}
    ]
    # Add remaining weeks for deeper dives or new topics...
    # Week 10 - 16 can focus on additional areas like Security, Networking, Advanced Leadership, etc.
]

# Function to generate the CSV for the plan
def create_plan_csv(start_date, weeks_plan, filename='career_growth_plan_16_weeks.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Start Date', 'Start Time', 'Duration (Minutes)'])

        current_date = start_date
        for week in weeks_plan:
            for task in week:
                # Skip cheat days
                if task['duration'] > 0:
                    writer.writerow([task['task'], current_date.strftime("%Y-%m-%d"), task['start_time'], task['duration']])
                current_date += timedelta(days=1)

# Setting the start date for the plan
start_date = datetime.today()

# Calling the function to create the CSV file with the full 16-week plan
create_plan_csv(start_date, weekly_plan)

print("Career growth plan CSV has been created successfully.")
