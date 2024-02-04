# README for DocuMentor

## Introduction

DocuMentor is a specialized tool designed for software development teams and individual developers to create a cloned directory specifically for documentation purposes. Rather than generating traditional documentation, DocuMentor focuses on creating a comprehensive directory tree of your entire codebase in Markdown format. This approach facilitates an organized structure for writing and maintaining documentation alongside your code, ensuring that all aspects of your project are well-documented and easily accessible.

## Features

- **Cross-Platform Compatibility**: Runs on Windows, Linux (Ubuntu), and macOS, ensuring that teams can use it regardless of their operating system.
- **Integrated with Virtual Environments**: Designed to run within a virtual environment, allowing for efficient management of dependencies without affecting global package installations.
- **Creates Directory Tree in Markdown**: DocuMentor generates a detailed directory tree of your entire codebase, presenting it in an easily navigable Markdown format. This feature aids in visualizing the project structure, making it simpler to organize and update documentation.

## Prerequisites

Ensure you have Python (version 3.6 or newer) installed on your system before running DocuMentor. It relies on several Python packages, which will be installed in a virtual environment to prevent any conflicts with other packages installed on your system.

## Installation

1. **Clone the Repository**: Start by cloning the DocuMentor repository to your local machine using Git.

    ```bash
    git clone https://example.com/DocuMentor.git
    cd DocuMentor
    ```

2. **Create a Virtual Environment**:

    - **Windows**:

        ```cmd
        python -m venv venv
        .\venv\Scripts\activate
        ```

    - **Linux (Ubuntu)/macOS**:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install Dependencies**:

    With the virtual environment activated, proceed to install the required Python packages using pip.

    ```bash
    pip install -r requirements.txt
    ```

## Running DocuMentor

After installation, you're set to use DocuMentor to generate the directory tree for your project.

1. **Prepare Your Project**: Make sure your project is ready and that you know which directories or files you wish to include or exclude from the documentation structure.

2. **Generate Directory Tree**:

    - **Windows**:

        ```cmd
        .\venv\Scripts\python -m DocuMentor
        ```

    - **Linux (Ubuntu)/macOS**:

        ```bash
        ./venv/bin/python -m DocuMentor
        ```

Adjust the command based on how DocuMentor is invoked, which might vary depending on its implementation. If DocuMentor is implemented as a script, you may need to use a different command like `./DocuMentor`.

## Deactivating the Virtual Environment

Once you're done with DocuMentor, you can deactivate the virtual environment to revert to your global Python setup.

- **All Platforms**:

    ```bash
    deactivate
    ```

## Support

For any issues, suggestions, or contributions, please refer to the GitHub repository's Issues and Pull Requests sections. We welcome contributions of all forms, be it through bug reports, code contributions, or documentation updates.

## License

DocuMentor is released under the GNU General Public License v3.0 (GPL-3.0), a popular free software license that guarantees end users the freedom to run, study, share, and modify the software.