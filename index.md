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

<!-- Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis. -->


{: .success }
**Welcome to DSC 10! To start, read the [syllabus](https://dsc10.com/syllabus) carefully, paying special attention to the ["Getting Started"](https://dsc10.com/syllabus/#-getting-started) section. Make sure to complete the [Welcome Survey](https://forms.gle/vw5RcYjjhiDAp5GD6) and [Pretest](https://practice.dsc10.com/pretest/) to get off to a good start!**


[Jump to the current week](#week-1-python-basics){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}