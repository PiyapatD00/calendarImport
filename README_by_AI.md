<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="calendarImport.git.png" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# CALENDARIMPORT.GIT

<em>Turn conversations into calendar events, effortlessly and instantly.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/PiyapatD00/calendarImport.git?style=flat-square&logo=opensourceinitiative&logoColor=white&color=ad5d91" alt="license">
<img src="https://img.shields.io/github/last-commit/PiyapatD00/calendarImport.git?style=flat-square&logo=git&logoColor=white&color=ad5d91" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/PiyapatD00/calendarImport.git?style=flat-square&color=ad5d91" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/PiyapatD00/calendarImport.git?style=flat-square&color=ad5d91" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black" alt="tqdm">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">

</div>
<br>

---

## ☀️ Table of Contents

1. [☀ ️ Table of Contents](#-table-of-contents)
2. [🌞 Overview](#-overview)
3. [🔥 Features](#-features)
4. [🌅 Project Structure](#-project-structure)
    4.1. [🌄 Project Index](#-project-index)
5. [🚀 Getting Started](#-getting-started)
    5.1. [🌟 Prerequisites](#-prerequisites)
    5.2. [⚡ Installation](#-installation)
    5.3. [🔆 Usage](#-usage)
    5.4. [🌠 Testing](#-testing)
6. [🌻 Roadmap](#-roadmap)
7. [🤝 Contributing](#-contributing)
8. [📜 License](#-license)
9. [✨ Acknowledgments](#-acknowledgments)

---

## 🌞 Overview



---

## 🔥 Features

|      | Component         | Details                                                                                                                                                                                                                   |
| :--- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ⚙️  | **Architecture**   | <ul><li>Python scripts (no package/module structure)</li><li>Single-repo, flat structure</li><li>CLI-driven usage</li><li>External config via <code>sample.txt</code></li></ul>                                                              |
| 🔩 | **Code Quality**    | <ul><li>No static typing enforcement</li><li>Python best practices vary</li><li>No linting config found</li><li>Some 3rd-party lib usage</li></ul>                                                                       |
| 📄 | **Documentation**   | <ul><li>README minimal/absent</li><li>In-code comments limited</li><li>No API docs</li><li>Sample config included</li></ul>                                                                                                |
| 🔌 | **Integrations**    | <ul><li>Google Calendar API (<code>google-api-python-client</code>)</li><li>PDF &amp; OCR parsing (<code>pdfminer</code>, <code>pytesseract</code>, <code>pdfplumber</code>, <code>pypdfium2</code>)</li><li>ICal (<code>ics</code>)</li></ul> |
| 🧩 | **Modularity**      | <ul><li>Monolithic scripts</li><li>Reusable utility functions</li><li>Loose coupling between modules</li></ul>                                                                     |
| 🧪 | **Testing**         | <ul><li>No test suite/framework detected</li><li>No CI/CD for testing</li></ul>                                                                                                     |
| ⚡️  | **Performance**    | <ul><li>Batch processing via CLI</li><li>Depends on external APIs &amp; file I/O</li><li>Not optimized for concurrency</li></ul>                                                  |
| 🛡️ | **Security**        | <ul><li>Uses OAuth 2.0 for Google APIs</li><li>No secrets management</li><li>No input validation hardening</li></ul>                                                                |
| 📦 | **Dependencies**    | <ul><li>Heavy (<code>requirements.txt</code>)</li><li>Google API, PDF, OCR, ICal, OpenAI</li><li><code>python-dotenv</code> for environment vars</li></ul>                          |

---

## 🌅 Project Structure

```sh
└── calendarImport.git/
    ├── README.md
    ├── app.py
    ├── authenAPI.py
    ├── file_parser.py
    ├── requirements.txt
    ├── sample_files
    │   └── sample.txt
    └── summarizer.py
```

### 🌄 Project Index

<details open>
	<summary><b><code>CALENDARIMPORT.GIT/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/PiyapatD00/calendarImport.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Dependency specification underpins the projects environment by defining all required third-party libraries and their versions, ensuring consistency and reproducibility across development, testing, and deployment<br>- Serves as a foundational layer within the overall architecture, enabling smooth integration of external services, APIs, and utilities while streamlining collaboration, automation, and onboarding for contributors working throughout the codebase.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/PiyapatD00/calendarImport.git/blob/master/summarizer.py'>summarizer.py</a></b></td>
					<td style='padding: 8px;'>- Enables the extraction and transformation of natural Thai language messages into structured Google Calendar events by leveraging AI-powered language understanding<br>- Acts as a bridge between unstructured text and standard calendar data formats, resolving relative time references and delivering well-formed event objects<br>- Plays a central role in automating event creation from conversational or free-form input within the overall project architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/PiyapatD00/calendarImport.git/blob/master/app.py'>app.py</a></b></td>
					<td style='padding: 8px;'>- Orchestrates the end-to-end workflow for extracting content from various file types, generating a natural language summary, and seamlessly creating a calendar event based on the summarized information<br>- Serves as the central entry point that integrates file parsing, text summarization, authentication, and event creation, enabling users to automate calendar scheduling from raw textual, PDF, or image-based sources within the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/PiyapatD00/calendarImport.git/blob/master/authenAPI.py'>authenAPI.py</a></b></td>
					<td style='padding: 8px;'>- Google Calendar API authentication is centralized in authenAPI.py, enabling secure and seamless access to calendar events throughout the project<br>- Centralizing credential management simplifies API usage for other modules, ensuring that user authentication and token storage are handled transparently<br>- This foundation supports robust integration with Google services while streamlining development and maintaining security across the codebase.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/PiyapatD00/calendarImport.git/blob/master/file_parser.py'>file_parser.py</a></b></td>
					<td style='padding: 8px;'>- Centralizes the extraction of text content from multiple file formats, including plain text, PDFs, and images, to support seamless ingestion and processing across the codebase<br>- Enables downstream modules to efficiently access textual data in a unified manner, serving as a foundational component for document analysis, search, or data transformation features within the broader project architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- sample_files Submodule -->
	<details>
		<summary><b>sample_files</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ sample_files</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/PiyapatD00/calendarImport.git/blob/master/sample_files/sample.txt'>sample.txt</a></b></td>
					<td style='padding: 8px;'>- Serves as a realistic conversational narrative that captures the informal team communication surrounding the BackOffice Flow Optimization project before its delivery deadline<br>- Provides insight into team dynamics, pending tasks, and the natural flow of collaboration, helping contextualize project deliverables and deadlines for both contributors and reviewers across the codebase<br>- Enhances overall understanding of real-world project workflows within the repository.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 🌟 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### ⚡ Installation

Build calendarImport.git from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/PiyapatD00/calendarImport.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd calendarImport.git
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r requirements.txt
	```

### 🔆 Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### 🌠 Testing

Calendarimport.git uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```

---

## 🌻 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

- **💬 [Join the Discussions](https://github.com/PiyapatD00/calendarImport.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/PiyapatD00/calendarImport.git/issues)**: Submit bugs found or log feature requests for the `calendarImport.git` project.
- **💡 [Submit Pull Requests](https://github.com/PiyapatD00/calendarImport.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/PiyapatD00/calendarImport.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/PiyapatD00/calendarImport.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=PiyapatD00/calendarImport.git">
   </a>
</p>
</details>

---

## 📜 License

Calendarimport.git is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
