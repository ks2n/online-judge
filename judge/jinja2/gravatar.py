import hashlib
from urllib.parse import quote

from django.utils.http import urlencode

from judge.utils.unicode import utf8bytes
from judge.models import Profile
from . import registry


# Edu palette — indigo / warm / mint / amber / rose / cyan family.
# Picked so that any single letter on bg renders with strong AA contrast (white text).
_MONOGRAM_PALETTE = (
    "#4F46E5",  # indigo-600
    "#7C3AED",  # violet-600
    "#EA580C",  # orange-600
    "#16A34A",  # green-600
    "#0891B2",  # cyan-600
    "#DC2626",  # red-600
    "#CA8A04",  # yellow-600
    "#DB2777",  # pink-600
)


def _monogram_svg(label: str, size: int, color: str) -> str:
    """Render a square SVG monogram avatar as a data URL.

    The label is centered with white text on `color` background; tspan
    `dominant-baseline=central` is well supported. Single-letter monograms
    only — fall back to '?' on empty.
    """
    text = (label[:1] if label else "?").upper()
    font_size = round(size * 0.5)
    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{size}' height='{size}' viewBox='0 0 {size} {size}'>"
        f"<rect width='{size}' height='{size}' fill='{color}'/>"
        f"<text x='50%' y='50%' fill='white' font-family='-apple-system,Segoe UI,Inter,sans-serif' "
        f"font-size='{font_size}' font-weight='600' text-anchor='middle' dominant-baseline='central'>"
        f"{text}</text></svg>"
    )
    return "data:image/svg+xml;utf8," + quote(svg)


def _monogram_for(profile: Profile, size: int) -> str:
    """Pick a deterministic palette colour for `profile` and render the monogram."""
    username = profile.get_username() or ""
    seed = username if username else profile.get_email() or str(profile.id or 0)
    digest = hashlib.md5(utf8bytes(seed.lower())).digest()
    color = _MONOGRAM_PALETTE[digest[0] % len(_MONOGRAM_PALETTE)]
    return _monogram_svg(username, size, color)


@registry.function
def gravatar(profile_id, size=80):
    profile = Profile(id=profile_id)
    is_muted = profile.get_mute()

    if not is_muted:
        profile_image_url = profile.get_profile_image_url()
        if profile_image_url:
            return profile_image_url

    # No uploaded avatar → render an inline monogram SVG. Avoids the external
    # gravatar.com round-trip and the noisy identicon pattern that doesn't fit
    # the edu palette.
    if not is_muted:
        return _monogram_for(profile, int(size))

    # Muted users: keep the legacy gravatar identicon so moderators can still
    # tell them apart by hash.
    email = profile.get_email()
    gravatar_url = (
        "//www.gravatar.com/avatar/"
        + hashlib.md5(utf8bytes(email.strip().lower())).hexdigest()
        + "?"
    )
    args = {"d": "identicon", "s": str(size), "f": "y"}
    gravatar_url += urlencode(args)
    return gravatar_url
