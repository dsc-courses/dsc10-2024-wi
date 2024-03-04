---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }


{{ site.staffersnobio }}

<!--
{: .success }
**Tip: When working on assignments, use Ctrl+F on this page to search for a keyword and quickly find the relevant lecture. Click the ✏️ emoji to open a static version of the lecture for reference, which is much faster than loading it on DataHub. Also, make sure to use the [reference sheet](https://drive.google.com/file/d/1ky0Np67HS2O4LO913P-ing97SJG0j27n/view?usp=sharing)!**
-->


{: .success }
**Announcement: Janine is out of town on Friday 3/8 and there will be no live lecture that day. Instead, you will watch a recording of the lecture asynchronously. This message will be updated when that recording is available.**



[Jump to the current week](#week-9-prediction){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}