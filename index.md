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
**On Wednesday, we'll be reviewing questions from [last quarter's final exam](https://practice.dsc10.com/fa23-final/index.html). Try out the questions before coming to class!**



[Jump to the current week](#week-10-review){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}