---
title: Introduction to Open Source Software

---

---
title: Open Source Software, Licenses, Repositories, and Collaboration
tags: Talk
description: Understanding how modern software is built, shared, and used
---

# Introduction to Open Source Software

### Understanding how modern software is built, shared, and used

Leonardo Mingari
_Geosciences Barcelona (GEO3BCN-CSIC)_

<img src="https://hackmd.io/_uploads/r1zCLuDWzg.png" alt="qrcode" width="200"/>

---

## Introduction

### Content

> [TOC]

----

### What is this session about?

In this session, we will understand:
1) how code is shared and made reusable
2) what you are allowed and required to do with that code
3) how collaborative development is structured in practice

----

### Motivation

Modern software is produced through coordinated collaboration among multiple contributors, often across different organizations and domains.

These concepts matter for research, industry, and everyday tools you already use.

::: info
It matters for your work, even if you are not a developer!
:::

---

## Section 1: Open source software

### Why It Matters

Open source powers much of the modern digital world.

More importantly, it is something you will regularly encounter in:
- research and data science workflows
- software development in industry
- everyday tools and platforms

Understanding open source is essential to avoid legal, ethical, and practical risks when using software.

![](https://www.cobalt.io/hs-fs/hubfs/examples-of-open-sourced-software.jpeg)

----

### Can You Safely Use Code You Find Online?

If you find code online:
- Can you use it in your project?
- Can you modify it?
- Can you publish your results?

The answer is not always intuitive.

__It depends on the license__.

----

### Intuition: Think of it like a contract

Open source is not "free for all"

It works like:
- Terms & Conditions
- or a usage contract

The license tells you:
:white_check_mark: what you CAN do
:x: what you MUST do

----

### Why Open Source

People contribute to open source in order to:

* solve problems together
* learn from others
* improve tools they use
* share knowledge
* reduce dependence on one company

----

### Software copyright

It is a legal protection that treats source code as a literary work, protecting its expression from unauthorized copying, modification, or distribution while leaving underlying ideas unprotected.

* Before 1989: You had to strictly print a copyright notice on the medium, or you lost your rights.

* Automatic upon creation (in most jurisdictions worldwide): It automatically applies as soon as the code is fixed in a tangible medium, granting the creator exclusive rights to reproduce, distribute, and modify their intellectual property.

----

### Types of Software

| __Type__ | __Description__ |
| -------- | --------------- |
| Proprietary          | Source code is closed and controlled by the vendor            |
| Free Software        | Users can run, study, modify, and share the software          |
| Open Source Software | Source code is available under an open-source license         |
| Public Domain        | No copyright restrictions on use or distribution              |
| Source-Available	   | Source code is visible but subject to additional restrictions |

----

### Proprietary Software

Software whose source code is not publicly available and whose use, modification, and distribution are controlled by the owner. Normally accompanied by restrictive licenses that limit its use, modification and redistribution by users.

#### Examples

* Microsoft Windows,
* Microsoft Office,
* Adobe Photoshop,
* macOS

:::info
Focuses on commercial control, software is a product whose use is restricted to protect revenue and intellectual property
:::

----

### Proprietary Software and Its Limitations

With proprietary (closed-source) software, even if you have bought or licensed it:

- you cannot inspect how it works internally
- you cannot modify or adapt it to your needs
- you are dependent on the vendor for updates and fixes
- you cannot fix bugs yourself or audit behavior
- you may lose access or compatibility in the future if support ends

This limits transparency, control, and long-term flexibility.

Open source software addresses many of these limitations.

----

### Free software

Software that grants users the freedom to run, study, modify, and redistribute the program.
* VLC media player
* LibreOffice
* Inkscape
* GIMP

:::info
Focuses on user freedom, ensuring everyone has the right to run, study, modify, and share software
:::

----

### Public Domain Software

Software with no copyright restrictions (or where rights have been waived), allowing unrestricted use, modification, and distribution.
* SQLite
* Software in the early computer age (pre-1988): BLAS (1979), FFTPACK (1985)
* Many US federal agency works (e.g., NASA, NOAA), which are often in the public domain

:::info
Focuses on unrestricted use, removing ownership so software becomes a shared public resource with no legal barriers
:::

----

### Open source software

Software whose source code is publicly available and that can be modified and redistributed under an open-source license

* Linux Kernel,
* Mozilla Firefox, 
* Chromium
* Apache HTTP Server

:::info 
Focuses on collaborative development, making source code open to improve quality, transparency, and innovation through community contribution
:::

----

### Source-Available Software

Software whose source code is visible, but which does not meet the requirements of an open-source license because of additional restrictions.
* Redis
* MongoDB
* ElasticSearch
* Sentry

:::info 
Focuses on visibility with control, allowing code inspection while limiting certain uses to retain commercial advantage or governance control
:::

----

### Open Source Definition

__Open Source Software__ must meet a very specific, strict 10-point definition maintained by the Open Source Initiative (OSI): [Open Source Definition (OSD)](https://opensource.org/osd). 

* The OSI focuses less on ethical aspects and more on the development model.
* It requires that the underlying source code be completely public. 
* Additionally, the legal license must guarantee specific rights. 

#### Examples
* Anyone can view, modify, and redistribute the source code.
* The code can be used for any purpose, including commercial projects.
* It cannot discriminate against any specific group of people or field of research.

----

### Rights and restrictions

Open source software is distributed under licenses that grant users the right to:

* use, 
* modify, 
* and distribute software freely.

Open source licenses balance user freedoms with certain obligations.

#### Common Restrictions

* __Copyright__: Original owners retain rights, but grant specific permissions.
* __Patents__: Some licenses address patent rights.
* __Attribution__: Many require crediting the original authors (e.g. [EPOS Platform](https://www.ics-c.epos-eu.org/)).
* __Derivative Works__: Copyleft licenses often mandate that derived works use the same license.

---

## Section 2: Software Licenses

### What's a Software License?

A software license:
* answers a simple question: "What are you allowed to do with this code?"
* is the document that grants permissions and defines obligations for anyone who wants to use the code.
* is a legal instrument that can create rights and obligations recognized by law.

----

### Types of licenses

These licenses may vary in their precise terms, some being more permissive (such as the MIT License or the Apache License) and others imposing conditions to maintain the open source nature of the software in all derived versions (such as the GNU General Public License).

:::info
Open source licenses can be primarily categorized into two types: 
1. __permissive licenses__ and
2. __copyleft licenses__.
:::

----

### Permissive Licenses

* Permissive licenses offer __significant freedom__, allowing users to use, modify, and redistribute the software with __minimal restrictions__. 
* This flexibility makes permissive licenses popular among developers and enterprises.

#### Examples
* __MIT License__, 
* __Apache License 2.0__, and 
* __BSD License__. BSD license comes in two versions: 
    * 2-Clause and 
    * 3-Clause BSD licenses.

----

### Copyleft Licenses

* Copyleft licenses impose __stricter conditions__ on redistribution, ensuring that derivative works remain open source
* These licenses guarantee that the software's source code and any modifications will continue to be freely available, which fosters a collaborative development environment.

#### Examples
* __GNU General Public License (GPL)__: A widely used copyleft license that requires any derivative work to be licensed under the same terms, ensuring that the software remains open source.
* __GNU Lesser General Public License (LGPL)__: A weaker form of the GPL, it allows linking to the licensed software without requiring the entire linked program to be open source.

----

### Choosing a License

Different projects choose different licenses depending on their goals.

#### **Library or tool you want widely adopted**
> Use a **permissive license** (MIT, Apache)

_Example_: Many web libraries and developer tools use MIT or Apache to maximize usage.

#### Project that must remain open source
> Use a **copyleft license** (GPL family)

_Example_: The Linux kernel uses GPLv2 to guarantee long-term openness.

#### Protect against patent risk (important in industry)
> Use **Apache License 2.0**
> ( includes an explicit patent grant)

_Example_: Large-scale industry projects often choose Apache 2.0 to reduce legal and patent-related uncertainty.
    
#### Examples
1) Permissive licenses like MIT or Apache might be preferred in enterprise environments where proprietary solutions are developed alongside open source components.

2) Many Linux distributions use GPL-licensed software to ensure continued openness and collaboration. 
The Linux kernel itself is licensed under the GNU General Public License version 2 (GPLv2)

----

### Type of softwares: Examples

![software_license_flowchart](https://hackmd.io/_uploads/HkynH7IWGx.svg)

----

### Microsoft Windows: Proprietary Software

__Windows__ is a proprietary graphical operating system developed and marketed by Microsoft

Official website: [Windows](https://www.windows.com)

#### Key characteristics
* Source code is not publicly available
* Users receive compiled binaries (installer / system image)
* Internal implementation cannot be inspected or modified
* Redistribution and modification are restricted by the license

----

### GIMP: Free & Open Source Software with copyleft license

__GIMP__ is a cross-platform image editor available for GNU/Linux, macOS, Windows, and other operating systems

Website: [gimp.org](https://www.gimp.org/)
Repository: [gitlab](https://gitlab.gnome.org/GNOME/gimp)

#### Key characteristics
* License is GNU GPL (copyleft license)
* Source code is public
* License explicitly guarantees:
    * run the program
    * study the code
    * modify it
    * redistribute it (even modified versions)

----

### SciPy: Open Source Software with permissive license

__SciPy__ is an open-source software for mathematics, science, and engineering. 

Website: [scipy.org](https://scipy.org/)
Repository: [gitlab](https://github.com/scipy/scipy)

#### Key characteristics
* BSD-3-Clause license (permissive license)
* Source code is public
* License explicitly guarantees:
    * run the program
    * study the code
    * modify it
    * redistribute it (even modified versions)
    * no obligation to release modifications under the same license (unlike copyleft)

::: info
__BSD‑3‑Clause__ and __MIT__ are extremely similar
* Simple and flexible (minimal restrictions)
* Easy integration into proprietary/commercial products
* They are widely used in academia and national labs
* Encourages wider adoption and contributions
* It avoids copyleft, making it industry‑friendly
* Low legal overhead for companies and researchers
* BSD‑3‑Clause includes an extra "no endorsement" clause (MIT does not)
:::

----

### SQLite: Public Domain Software

__SQLite__ is a self-contained, serverless, and lightweight relational database engine

Website: [SQLite](https://sqlite.org/)
Repository: [github](https://github.com/sqlite/sqlite)

#### Key characteristics
* LICENSE file
* Official website: [copyright](https://sqlite.org/copyright.html)

> Note:
> Because SQLite is in the public domain, we do not normally accept pull requests, because if we did take a pull request, the changes in that pull request might carry a copyright and the SQLite source code would then no longer be fully in the public domain.

:::info
Copyleft (GPL) and permissive (MIT) licenses are actually better designed for collaboration precisely because they work with copyright rather than against it (they assume contributions carry copyright and handle it explicitly through license terms).
:::

----

### A fallback license for Europe

* While SQLite is functionally open source, some organizations prefer standard licenses (MIT/BSD/GPL) for legal clarity
* To address this, SQLite also offers a fallback license (a very permissive one) for jurisdictions where public domain is unclear

Some European countries do not allow authors to fully waive moral rights, meaning:

* You cannot legally "give up" all rights to your work.
* Therefore, "public domain" is not a legally recognized status.
* SQLite provides a backup license: the SQLite Blessing (a 0‑restriction, permissive license).
* This ensures that SQLite is legally usable everywhere, including the EU.
* If you are in a jurisdiction that does not recognize public domain (e.g., Germany, France, Spain), you may use SQLite under a permissive license provided by the authors.
* This fallback license is extremely permissive (more permissive than MIT or BSD) and imposes no obligations.

---

## Section 3: Collaborative Development

### From Open Source Code to Collaborative Development

For software to be developed collaboratively, projects need mechanisms to:
- organize code, documentation, and releases
- coordinate contributions from different people or organizations
- review, discuss, and approve changes
- maintain a transparent record of project evolution

These mechanisms are provided by __software repositories__ and __code hosting platforms__. 

----

### What Is a Repository?

A repository is a __version-controlled storage location__ for a software project that contains:

* Source code files
* Documentation
* Configuration files
* Metadata (e.g., license and contribution guidelines)
* Project assets
* The complete history of changes to the project

:::info
This mechanism is provided by version control systems.

**Git** is the most widely used version control system in modern software development.
:::

----

### Anatomy of a Repository

A repository contains all the files and information needed to define, build, and maintain a software project.

#### Typical elements

- `README`: project overview, setup instructions, and usage guide
- `LICENSE`: legal terms for use and distribution
- source code: the implementation of the software
- configuration files: build settings and environment setup
- documentation: technical explanations and guides
- assets: images, data files, or other project resources
- project history: recorded changes over time

__Key Features__
* __Version tracking__: Records every change made to the project.
* __Collaboration__: Allows multiple developers to work on the same codebase.
* __Branching and merging__: Enables parallel development and integration of changes.
* __History and recovery__: Makes it possible to review, compare, or restore previous versions.

----

### Example of Repository Structure

```text
my-project/
├── README.md
├── LICENSE
├── src/
│   ├── main.py
│   └── utils.py
├── docs/
│   └── usage.md
├── config/
│   └── settings.json
└── assets/
    └── logo.png
```

----

### From Repositories to Code Hosting Platforms

* A repository defines **what a project is** (its files and history).
* Modern software development also requires **coordination between people and teams**.

This is where code hosting platforms become essential:

- they store and manage repositories in the cloud
- they add collaboration features on top of repositories
- they provide tools for reviewing, discussing, and integrating changes
- they support automation for testing and deployment

#### Common Platforms

* GitHub, 
* GitLab, 
* Bitbucket, 
* institutional Git services.

::: info
* A **code hosting platform** is an online service that stores repositories and provides tools for collaborative software development.
* Code hosting platform make software development visible, structured, and collaborative.
:::

----

### Collaboration Workflow

Collaborative development follows a structured process for proposing, reviewing, and integrating changes.

#### Typical workflow
- identifying a problem, requirement, or improvement
- discussing possible solutions
- implementing a proposed change
- reviewing the proposed change before integration
- merging the accepted change into the project
- releasing updated versions of the software

This workflow makes project evolution **transparent, traceable, and reviewable**.

----

### Roles in a Collaborative Project

Collaborative software projects involve different levels of participation, each contributing in a different way to the project's evolution.

#### Typical roles
- users: use the software and may report problems or request improvements
- contributors: propose changes to code, documentation, tests, or examples
- reviewers: evaluate proposed changes before they are accepted
- maintainers: manage the project direction, quality standards, and integration of changes
- organizations: provide infrastructure, funding, governance, or long-term support

----

### Conclusion

Modern software development is built on **collaboration at scale**.

This is made possible by:
- structured **repositories** that store code and history
- **code hosting platforms** that enable collaboration and automation
- defined **workflows** that guide how changes are proposed and integrated
- clear **roles** that distribute responsibilities across contributors

Together, these elements transform individual code into **shared, evolving software systems**.