# Environment Setup

Setting up the right development environment is the foundation for everything you will build this summer and beyond. By installing the tools below, you will have a professional-grade workspace that mirrors what real developers use every day. This environment will allow you to write, run, and debug Python code efficiently, work with AI libraries and frameworks, and manage your projects like a software engineer. Whether you are writing your first script or building your first AI-powered application, these tools will support you every step of the way.

While we generally recommend using your issued laptop for this, you are more than welcome to set these components up on your personal devices.

---

## 1. Visual Studio Code (VS Code)

Visual Studio Code (VS Code) is a free, lightweight, and powerful code editor developed by Microsoft. It supports virtually every programming language and comes packed with features like syntax highlighting, intelligent code completion, an integrated terminal, and a rich library of extensions. For Python and AI development, VS Code is one of the most widely used editors in the industry — it makes writing and running code intuitive and efficient, whether you are a beginner or a seasoned developer.

**Download and installation instructions:** [VS Code Download](https://code.visualstudio.com/download)

---

## 2. Python

Python is one of the most popular and beginner-friendly programming languages in the world. Its clean, readable syntax makes it an excellent first language, and its vast ecosystem of libraries — including NumPy, pandas, and frameworks like LangChain and TensorFlow — makes it the go-to language for data science, machine learning, and AI development. Learning Python gives you a powerful, versatile skill that is in high demand across virtually every industry.

> **Note:** Please download **Python 3.14** specifically. This is the version we will use this summer. As you begin your courses at CMU, you may have to install different versions of Python to satisfy various project package dependencies.

**Download and installation instructions:** [Python Downloads](https://www.python.org/downloads/)

---

## 3. Git

Git is a free, open-source version control system that tracks changes to your code over time. It allows you to save snapshots of your work, collaborate with others, revert mistakes, and manage different versions of a project — all from the command line or within VS Code. Git is an essential tool for any developer, and learning it early will help you build good habits around organizing and protecting your work as your projects grow in complexity.

**Download and installation instructions:** [Git - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## 4. Windows Subsystem for Linux (WSL)

Windows Subsystem for Linux (WSL) allows you to run a full Linux environment directly on your Windows machine — no virtual machine or dual-boot required. This is particularly important for AI and software development because many tools, libraries, and workflows are built with Linux in mind. With WSL, Windows users can run Linux commands, install Linux-based packages, and work in an environment that closely mirrors professional development and cloud computing environments.

> **Important:** When following the installation instructions, make sure to open **PowerShell as an Administrator** before running any commands. Right-click the PowerShell icon and select *"Run as administrator"* to ensure the installation completes successfully.

**Download and installation instructions:** [Install WSL | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/install)

---

## 5. Docker Desktop

Docker is a container application platform that allows developers to build, run, and manage containers. Containers allow developers to create immutable, reusable systems for better reliability, reproducibility, and deployability. Most modern cloud systems utilize some sort of container runtime such as Docker.

**Download and installation instructions:** [Install Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)

---

## 6. Terraform

Terraform is an open-source infrastructure-as-code (IaC) tool developed by HashiCorp. It allows developers and engineers to define, provision, and manage cloud infrastructure using a declarative configuration language called HCL (HashiCorp Configuration Language). Rather than manually clicking through cloud provider dashboards, Terraform lets you describe your desired infrastructure in code, version it with Git, and apply it consistently across environments. It is widely used in the industry for managing resources on AWS, Azure, Google Cloud, and many other providers.

**Download and installation instructions:** [Install | Terraform | HashiCorp Developer](https://developer.hashicorp.com/terraform/install)

---

## 7. Azure CLI (az)

The Azure Command-Line Interface (Azure CLI) is a cross-platform tool that allows you to manage and interact with Microsoft Azure resources directly from your terminal. Using the `az` command, you can create and configure cloud services, manage subscriptions, deploy applications, and automate workflows — all without leaving the command line. The Azure CLI is an essential tool for anyone working with Azure-hosted applications or cloud infrastructure, and it integrates well with scripts and CI/CD pipelines.

> **Important:** Windows users should install the Azure CLI inside their WSL environment to ensure compatibility with Linux-based tooling and scripts used throughout this program.

**Download and installation instructions:** [Install the Azure CLI on Windows | Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows)

---

# Accounts

You will need the following accounts to help facilitate your work this summer and going into the CMU course.

## 1. GitHub

GitHub is a Microsoft web application that hosts git repositories. You will need an account to interact with remote repositories on GitHub such as this repository or your own code. If you have your own personal account already, you can use that as well.

**Sign Up:** [Sign up for GitHub](https://github.com/signup)

## 2. Docker Hub

Docker Hub is a platform for managing container images. Creating a Docker Hub account will remove certain rate limits for image downloads and other container operations. If you have your own personal account already, you can use that as well.

**Sign Up:** [Create your account](https://app.docker.com/signup)

> **Important:** After creating your account, [Sign in to Docker Desktop](https://docs.docker.com/desktop/setup/sign-in/).
