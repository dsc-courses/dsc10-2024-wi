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
**This site is currently under construction. This disclaimer will be removed when the site is finalized.**

[Jump to the current week](#week-10-review){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}