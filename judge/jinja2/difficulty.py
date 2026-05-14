"""Difficulty pill — map a problem's points value to a 5-tier label.

Used by the edu theme to render `<span class="edu-difficulty edu-difficulty--X">…</span>`
in problem lists and detail sidebars. Thresholds match the ones agreed for
sprint 3 (2026-05-04):

   <  10  → helper   (Trợ giúp)
   < 30   → easy     (Dễ)
   30–60  → medium   (Trung bình)
   60–100 → hard     (Khó)
   ≥100   → expert   (Rất khó)

The threshold logic lives here (one place to edit) so templates stay dumb.
"""

from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from . import registry


def _bucket(points):
    if points is None:
        return None
    try:
        p = float(points)
    except (TypeError, ValueError):
        return None
    if p < 10:
        return ("helper", _("Trợ giúp"))
    if p < 30:
        return ("easy", _("Dễ"))
    if p < 60:
        return ("medium", _("Trung bình"))
    if p < 100:
        return ("hard", _("Khó"))
    return ("expert", _("Rất khó"))


@registry.function("difficulty_pill")
def difficulty_pill(points, compact=False):
    bucket = _bucket(points)
    if bucket is None:
        return ""
    slug, label = bucket
    classes = "edu-difficulty edu-difficulty--%s" % slug
    if compact:
        classes += " edu-difficulty--sm"
    return mark_safe(
        '<span class="%s" title="%s điểm">%s</span>'
        % (classes, points, label)
    )


@registry.filter("difficulty_class")
def difficulty_class(points):
    """Filter form: `{{ problem.points|difficulty_class }}` → `easy`/`medium`/…"""
    bucket = _bucket(points)
    return bucket[0] if bucket else ""


@registry.filter("difficulty_label")
def difficulty_label(points):
    """Filter form: `{{ problem.points|difficulty_label }}` → `Dễ`/`Trung bình`/…"""
    bucket = _bucket(points)
    return bucket[1] if bucket else ""
