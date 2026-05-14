# LQDOJ Edu Design System

> Tone: **Brilliant.org / Duolingo** — ấm áp, khuyến khích, dễ đọc lâu.
> Audience: HS cấp 3 ôn tin học, SV CS, GV ra đề, beginner.
> Theme: light, default cream + indigo. Không gamification rực rỡ.

Hướng dẫn này mô tả tokens và component anatomy của edu-theme. Source code:
- Tokens: [resources/vars.scss](../resources/vars.scss) (legacy + edu) và [resources/edu/_tokens.scss](../resources/edu/_tokens.scss) (re-export).
- Partials: [resources/edu/](../resources/edu/) (10 file).
- Entry: [resources/edu-theme.scss](../resources/edu-theme.scss).

---

## 1. Color tokens

### Surfaces

| Token | Hex | Use |
|-------|-----|-----|
| `$edu-bg-cream` | `#FBF8F3` | Trang chủ, body background — ấm, mắt không mỏi |
| `$edu-bg-paper` | `#FFFFFF` | Card, panel, table |
| `$edu-bg-soft` | `#F9FAFB` | Hover state, sample I/O block, table header |
| `$edu-bg-muted` | `#F3F4F6` | Disabled, progress track, neutral chip |

### Text

| Token | Hex | Use |
|-------|-----|-----|
| `$edu-text` | `#1F2937` | Body text |
| `$edu-text-strong` | `#111827` | Heading, link strong, value |
| `$edu-text-muted` | `#6B7280` | Secondary label, eyebrow, caption |
| `$edu-text-faint` | `#9CA3AF` | Placeholder, disabled, separator |
| `$edu-text-on-accent` | `#FFFFFF` | Text trên nền indigo |

### Accent (chỉ 1 cho action — tiết chế)

| Token | Hex | Use |
|-------|-----|-----|
| `$edu-accent` | `#4F46E5` | Primary button, link, active tab, focus ring |
| `$edu-accent-hover` | `#4338CA` | Hover state |
| `$edu-accent-soft` | `#EEF2FF` | Active sidebar item, pill bg, callout |
| `$edu-accent-border` | `#C7D2FE` | Border khi hover/active |
| `$edu-accent-strong` | `#3730A3` | Text trên indigo soft |

### Warm (cho streak / onboarding ấm áp)

| Token | Hex | Use |
|-------|-----|-----|
| `$edu-warm` | `#F97066` | Streak flame, beginner CTA |
| `$edu-warm-soft` | `#FEE4E2` | Beginner greeting bg, badge |
| `$edu-warm-border` | `#FECDCA` | Border của warm chip |

### Border / shadow

| Token | Hex | Use |
|-------|-----|-----|
| `$edu-border` | `#E5E7EB` | Card border, divider |
| `$edu-border-strong` | `#D1D5DB` | Hover border, input border |
| `$edu-border-focus` | `#A5B4FC` | Focus indigo light |
| `$edu-shadow-sm` | `0 1px 2px rgba(17,24,39,.04)` | Card resting |
| `$edu-shadow-md` | `0 4px 12px rgba(17,24,39,.06)` | Card hover, dropdown |
| `$edu-shadow-lg` | `0 12px 32px rgba(17,24,39,.08)` | Modal, sheet |
| `$edu-shadow-focus` | `0 0 0 3px rgba(79,70,229,.18)` | Focus ring |

### Verdicts (semantic, không glow)

Format: bg / text / border (3-tuple).

| Verdict | Tokens | Hex |
|---------|--------|-----|
| AC (success) | `$edu-ac-bg` / `$edu-ac-text` / `$edu-ac-border` | `#F0FDF4` / `#166534` / `#BBF7D0` |
| WA (error)   | `$edu-wa-bg` / `$edu-wa-text` / `$edu-wa-border` | `#FEF2F2` / `#991B1B` / `#FECACA` |
| TLE/MLE (warn) | `$edu-tle-bg` / `$edu-tle-text` / `$edu-tle-border` | `#FFFBEB` / `#92400E` / `#FDE68A` |
| CE (info)    | `$edu-ce-bg` / `$edu-ce-text` / `$edu-ce-border` | `#F5F3FF` / `#5B21B6` / `#DDD6FE` |
| IR/RTE (warn alt) | `$edu-ir-bg` / `$edu-ir-text` / `$edu-ir-border` | `#FFF7ED` / `#9A3412` / `#FED7AA` |

Verdict ALWAYS pair colour + uppercase mono code (e.g. `AC`, `WA`) — colour-blind safe.

---

## 2. Typography

| Token | Value |
|-------|-------|
| `$edu-font-ui` | `"Inter", "Noto Sans", system-ui, -apple-system, sans-serif` |
| `$edu-font-code` | `"JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace` |
| `$edu-font-display` | `"Inter", system-ui, sans-serif` (heading, weight 600+) |

### Type scale (font-size / line-height)

| Token | Size | LH | Use |
|-------|------|----|----|
| display | 32 | 40 | Hero title, landing |
| h1 | 24 | 32 | Page title |
| h2 | 20 | 28 | Section heading |
| h3 | 18 | 26 | Card heading |
| body | 15 | 24 | Body text |
| small | 13 | 20 | Secondary text |
| caption | 12 | 16 | Eyebrow, label uppercase |
| code | 14 | 22 | JetBrains Mono code blocks |

Inline code dùng `0.92em` để không phá flow (giảm nhẹ so với surrounding text).

### Khi nào dùng monospace

Dùng `$edu-font-code` **chỉ cho**:
- Code thực sự (statement, editor, sample I/O)
- Số với tabular-nums (rating, points, time, AC%, score)
- Problem code identifier (e.g. `APLUSBTEST` pill)
- Verdict code (`AC`, `WA`, `TLE`)

KHÔNG dùng cho UI label, navigation, button text, prose.

---

## 3. Spacing / radius / motion

### Spacing (multiples of 4)

```
4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64
```

### Radius

| Token | Value | Use |
|-------|-------|-----|
| `$edu-radius-xs` | 4px | Inline code, small chip |
| `$edu-radius-sm` | 6px | Input, dropdown item |
| `$edu-radius-md` | 8px | Button, sample I/O block |
| `$edu-radius-lg` | 12px | Card, hero, large surface |
| `$edu-radius-pill` | 999px | Chip, badge, verdict pill |

### Motion

| Token | Value | Use |
|-------|-------|-----|
| `$edu-ease-out` | `cubic-bezier(.16,1,.3,1)` | Default easing |
| `$edu-duration-fast` | 150ms | Hover, focus |
| `$edu-duration-base` | 200ms | Enter/exit |
| `$edu-duration-slow` | 300ms | Progress fill, layout |

`@media (prefers-reduced-motion)` đã clamp tất cả về 0.01ms tự động (xem [_global.scss](../resources/edu/_global.scss)).

---

## 4. Component anatomy

### Button

```html
<button class="edu-btn edu-btn--primary">Nộp bài</button>
<button class="edu-btn edu-btn--secondary">Huỷ</button>
<button class="edu-btn edu-btn--ghost">Bỏ qua</button>
<button class="edu-btn edu-btn--danger">Xoá</button>

<!-- Sizes -->
<button class="edu-btn edu-btn--primary edu-btn--sm">Nhỏ</button>
<button class="edu-btn edu-btn--primary edu-btn--lg">Lớn</button>
```

- Primary = indigo solid
- Secondary = white + border slate
- Ghost = transparent, hover bg soft
- Danger = red dark + white text

Source: [_components.scss](../resources/edu/_components.scss).

### Card

```html
<article class="edu-card">
  <header class="edu-card-header">
    <h3>Tiêu đề</h3>
    <a class="edu-card-action" href="…">Xem tất cả →</a>
  </header>
  <p>Nội dung…</p>
</article>

<!-- Modifiers -->
<a class="edu-card edu-card--clickable" href="…">…</a>
<article class="edu-card edu-card--accent">…</article>
<article class="edu-card edu-card--flat">…</article>
```

- Bg `$edu-bg-paper`, border `$edu-border`, radius `$edu-radius-lg`, shadow `$edu-shadow-sm`.
- Clickable: hover `translateY(-1px)` + shadow md.
- Accent: gradient `$edu-accent-soft` → paper.

Source: [_cards.scss](../resources/edu/_cards.scss).

### Verdict pill

```html
<span class="edu-verdict edu-verdict--ac">AC</span>
<span class="edu-verdict edu-verdict--wa">WA</span>
<span class="edu-verdict edu-verdict--tle">TLE</span>
<span class="edu-verdict edu-verdict--ce">CE</span>
<span class="edu-verdict edu-verdict--ir">IR</span>
<span class="edu-verdict edu-verdict--queued">QU</span>
```

Anatomy: dot prefix (current colour) + uppercase mono code 11px. DMOJ legacy classes (`.AC`, `.WA`, etc.) đã được map tự động — không cần thêm `edu-verdict` nếu template render legacy class.

Source: [_verdicts.scss](../resources/edu/_verdicts.scss).

### Tag / chip

```html
<span class="edu-chip">Mảng</span>
<span class="edu-chip edu-chip--accent">DP</span>
<span class="edu-chip edu-chip--warm">Streak</span>
```

### Stat block

```html
<div class="edu-stat">
  <div class="edu-stat-label">Rating</div>
  <div class="edu-stat-value">1842</div>
  <div class="edu-stat-delta">+24</div>
</div>
```

- Label: 12px uppercase muted
- Value: 28px JetBrains Mono tabular-nums slate strong
- Delta: 13px green AC (down → red WA via `.is-down`)

Source: [_dashboard.scss](../resources/edu/_dashboard.scss).

### Greeting hero (returning learner)

```html
<div class="edu-greeting">
  <div class="edu-greeting-eyebrow">Chào mừng trở lại</div>
  <h2 class="edu-greeting-title">
    Chào, <em>username</em>!
    <span class="edu-greeting-sub">Hôm nay bạn muốn học gì?</span>
  </h2>
  <div class="edu-dashboard-stats">
    <div class="edu-stat">…</div>
    …
  </div>
</div>
```

### Greeting hero (beginner)

```html
<div class="edu-greeting edu-greeting--beginner">
  <div class="edu-greeting-eyebrow">Bắt đầu hành trình</div>
  <h2 class="edu-greeting-title">
    Chào, <em>username</em>!
    <span class="edu-greeting-sub">Hãy giải bài đầu tiên của bạn nhé.</span>
  </h2>
  <p class="edu-greeting-meta">Mô tả ngắn…</p>
  <div class="edu-cluster">
    <a class="edu-btn edu-btn--primary" href="…">Khám phá khoá học</a>
    <a class="edu-btn edu-btn--secondary" href="…">Xem bài tập</a>
    <a class="edu-btn edu-btn--ghost" href="…">Hướng dẫn</a>
  </div>
</div>
```

Modifier `--beginner` chuyển background sang warm gradient `$edu-warm-soft`.

### Progress bar

```html
<div class="edu-progress" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100">
  <div class="edu-progress-fill" style="width: 60%"></div>
</div>
```

Variant ấm áp (streak):
```html
<div class="edu-progress edu-progress--warm">
  <div class="edu-progress-fill" style="width: 40%"></div>
</div>
```

### Streak chip

```html
<span class="edu-streak">
  <i class="fa fa-fire"></i>
  Streak <span class="edu-streak-count">12</span> ngày
</span>
```

### Course card

```html
<a class="edu-course-card" href="/course/nhap-mon-c">
  <div class="edu-course-cover" aria-hidden="true">
    <img src="…" alt="">
  </div>
  <h4 class="edu-course-title">Nhập môn lập trình C++</h4>
  <div class="edu-course-meta">
    <span>Khoá học</span>
    <span>→</span>
  </div>
</a>
```

### Problem row card

```html
<a class="edu-problem-card" href="…">
  <span class="edu-problem-status is-ac"><i class="fa fa-check"></i></span>
  <span class="edu-problem-title">A + B Test</span>
  <span class="edu-problem-difficulty">Cơ bản · ~15 phút</span>
</a>
```

### Tabs

```html
<ul class="edu-tabs">
  <li class="active"><a href="…">Tổng quan</a></li>
  <li><a href="…">Bài học</a></li>
  <li><a href="…">Bài thi</a></li>
</ul>
```

Active tab: text `$edu-accent`, underline `$edu-accent` 2px.

### Pagination

```html
<ul class="pagination">
  <li class="disabled"><span>‹</span></li>
  <li><a href="?page=1">1</a></li>
  <li class="active"><span>2</span></li>
  <li><a href="?page=3">3</a></li>
  <li><a href="?page=3">›</a></li>
</ul>
```

### Callout

```html
<div class="edu-callout">Thông tin quan trọng cần lưu ý.</div>
<div class="edu-callout edu-callout--warm">Cảnh báo nhẹ nhàng.</div>
```

### Difficulty pill

5 mức theo `problem.points`. Render bằng Jinja function:

```jinja2
{{ difficulty_pill(problem.points) }}             {# full size #}
{{ difficulty_pill(problem.points, compact=True) }} {# inline với tên #}
```

Hoặc dùng filter để compose markup:

```jinja2
<span class="edu-difficulty edu-difficulty--{{ problem.points|difficulty_class }}">
  {{ problem.points|difficulty_label }}
</span>
```

| Range (points) | Slug | Label | Palette |
|---|---|---|---|
| `< 10`     | `helper`  | Trợ giúp     | Slate `#F1F5F9 / #475569 / #CBD5E1` |
| `< 30`     | `easy`    | Dễ           | Green AC tokens |
| `30–60`    | `medium`  | Trung bình   | Amber TLE tokens |
| `60–100`   | `hard`    | Khó          | Orange IR tokens |
| `≥ 100`    | `expert`  | Rất khó      | Red WA tokens |

Source: [_difficulty.scss](../resources/edu/_difficulty.scss), [judge/jinja2/difficulty.py](../judge/jinja2/difficulty.py).

### Toast / snackbar

Pop-up notification ở góc dưới-phải desktop (full-width mobile).

```js
window.eduToast.show({
  type: 'success',           // 'success' | 'error' | 'warning' | 'info'
  title: 'Đã nộp bài',       // optional
  message: 'Theo dõi tại mục Bài nộp',
  duration: 4000             // ms, 0 = không auto dismiss
});
```

Tự render Django messages framework qua block trong `base.html`. Container tạo lazy (không cần khai báo trong template).

Source: [_toast.scss](../resources/edu/_toast.scss), [resources/common.js](../resources/common.js) (cuối file).

### Skeleton loader

Placeholder shimmer trước khi data tới.

```html
<div class="edu-skeleton edu-skeleton--text"></div>
<div class="edu-skeleton edu-skeleton--text edu-skeleton--lg w-50"></div>
<div class="edu-skeleton edu-skeleton--card" style="height: 120px"></div>
<div class="edu-skeleton edu-skeleton--circle" style="width: 40px; height: 40px"></div>

<!-- Compose row -->
<div class="edu-skeleton--row">
  <div class="edu-skeleton edu-skeleton--circle"></div>
  <div class="edu-skeleton-row-body">
    <div class="edu-skeleton edu-skeleton--text w-75"></div>
    <div class="edu-skeleton edu-skeleton--text w-50"></div>
  </div>
</div>
```

`@media (prefers-reduced-motion)` → static muted bg.

Source: [_skeleton.scss](../resources/edu/_skeleton.scss).

### Modal / dialog

Edu chrome overlay với focus trap, ESC-to-close, click-outside-close.

```html
<button data-edu-modal-open="confirm-delete">Xoá</button>

<div class="edu-modal-backdrop" id="confirm-delete" data-edu-modal hidden>
  <div class="edu-modal" role="dialog" aria-modal="true" aria-labelledby="confirm-title">
    <header class="edu-modal-header">
      <h3 id="confirm-title">Xác nhận xoá</h3>
      <button class="edu-modal-close" data-edu-modal-close aria-label="Đóng">
        <i class="fa fa-times"></i>
      </button>
    </header>
    <div class="edu-modal-body">Hành động này không thể hoàn tác.</div>
    <footer class="edu-modal-footer">
      <button class="edu-btn edu-btn--secondary" data-edu-modal-close>Huỷ</button>
      <button class="edu-btn edu-btn--primary">Xoá</button>
    </footer>
  </div>
</div>
```

JS API: `window.eduModal.open(idOrEl)`, `window.eduModal.close(idOrEl)`.

Source: [_modal.scss](../resources/edu/_modal.scss), `eduModal` trong [common.js](../resources/common.js).

### Theme toggle

Mounted trong `edu-nav-utility`:

```html
<button id="edu-theme-toggle" data-toggle-url="{{ url('toggle_darkmode_ajax') }}">
  <i class="fa-regular fa-moon edu-theme-icon-dark"></i>
  <i class="fa-regular fa-sun edu-theme-icon-light" style="display:none"></i>
</button>
```

Behaviour:
- Init: đọc `localStorage.getItem('edu-theme')`; fallback `body.dark` server-rendered; nếu cả hai trống thì giữ light.
- Click: toggle `body.dark`, swap icon, lưu localStorage, POST AJAX `/user/theme/toggle-darkmode/?mode=dark|light` (chỉ khi authenticated).
- Persist: localStorage cho cả guest, session backend cho user đăng nhập (lần render kế tiếp đã đúng class server-side).

Logic ở cuối [common.js](../resources/common.js) (`#edu-theme-toggle` IIFE).

---

## 5. Layouts

### Top navigation

- 56px fixed, bg paper, border-bottom `$edu-border`.
- Desktop: brand left, primary nav middle (icon + label), utility right (lang / theme toggle / profile).
- Mobile (≤1023px): hamburger trigger + brand + utility compact; nav-list slide-down panel.
- Active route: text indigo, bg indigo-soft, border indigo bottom 2px.

Source: [_navigation.scss](../resources/edu/_navigation.scss).

### Workspace shell (problem detail, common-content.html)

```html
<div class="edu-workspace-shell">
  <aside class="edu-workspace-sidebar">
    <div class="edu-workspace-sidebar-panel">…CTA + meta…</div>
  </aside>
  <section class="edu-workspace-main">
    <div class="edu-workspace-briefing">…statement prose…</div>
  </section>
</div>
```

- Desktop: 2-col `1fr 280px`, sidebar **sticky top:76px**.
- Mobile: 1-col, sidebar `order: -1` (CTA "Nộp bài" lên đầu).

### Three-column (home, blog, problem list)

Dùng `templates/three-column-content.html` — không thay đổi shell, chỉ override colour qua tokens.

---

## 6. Accessibility

- **Focus ring**: tất cả `:focus-visible` apply `$edu-shadow-focus` indigo 3px (xem [_global.scss](../resources/edu/_global.scss)).
- **Color contrast**: tokens đã được kiểm tra:
  - Body text `$edu-text` (`#1F2937`) trên cream `#FBF8F3` = 12.4:1 (AAA)
  - Muted text `$edu-text-muted` (`#6B7280`) trên cream = 4.5:1 (AA)
  - Indigo `$edu-accent` `#4F46E5` trên paper `#FFFFFF` = 6.8:1 (AAA cho text, AA cho UI)
- **Reduced motion**: `@media (prefers-reduced-motion)` đã clamp transitions/animations về 0.01ms.
- **Verdict**: pair colour + uppercase mono code — colour-blind safe.
- **Tap targets**: button ≥ 36px, top-nav icon 36×36, mobile filter chip min 32px.
- **ARIA**: progress bar dùng `role="progressbar"` + `aria-valuenow`. Mobile nav dùng `aria-label`.

---

## 7. Decision log

### Tại sao bỏ "Sci-Fi Arena"?

- Dark void + cyan/purple glow → mỏi mắt khi đọc đề lâu.
- HUD topbar "Programming Arena" → brand voice esports, không phù hợp cho HS/SV/GV/beginner.
- Glass cards với multi-shadow → over-decorated cho prose-heavy task.

### Tại sao Cream + Indigo?

- **Cream `#FBF8F3`**: ấm hơn pure white, gợi cảm giác giấy/sách giáo khoa, đọc lâu không mỏi mắt.
- **Indigo `#4F46E5`**: tin cậy, học thuật, không quá "fun" như xanh lá Duolingo. Phù hợp cho ngữ cảnh "ôn thi tin học" của HS cấp 3.
- **Coral `#F97066`** chỉ dùng cho streak / beginner CTA → ấm áp khi cần khuyến khích nhưng không lan ra UI chính.

### Tại sao Inter + JetBrains Mono?

- Inter: free, nhiều weight (400/500/600/700), x-height cao → đọc body 15px comfortable.
- JetBrains Mono: ligature đẹp khi xem code (`==`, `=>`, `!=`), tabular-nums hỗ trợ score/rating cột thẳng.
- Bỏ DM Sans (cũ ở arena) — DM Sans tracking thoáng tạo cảm giác tactical HUD, không phù hợp giáo dục.

### Tại sao token-first refactor (không rewrite)?

- 6000+ dòng SCSS legacy ở `course.scss`, `problem.scss`, `contest.scss`, `blog.scss`, `comments.scss`...
- Token swap trong `vars.scss` lan tỏa tự động qua tất cả file legacy.
- Edu partials chỉ override các affordance đặc thù (button color, card chrome, verdict pill).
- Diff nhỏ, ít regression hơn rewrite from scratch.

### Tại sao SCSS-only cho problem-list / problem-detail / course?

- Templates phức tạp (contest mode, types, editorial, locked lessons).
- Sửa template → blast radius cao + risk vỡ feature.
- SCSS với `body.edu` specificity đã đủ override mọi affordance hiện tại.
- Khi cần redesign template thật sự (ví dụ thêm difficulty pill cho problem list), sẽ làm sau ở sprint riêng.

---

## 8. Files & artifacts

### Source

- [resources/vars.scss](../resources/vars.scss) — legacy + edu palette tokens
- [resources/edu-theme.scss](../resources/edu-theme.scss) — entry, `@use` 11 partials
- [resources/edu/](../resources/edu/) — 11 partials (tokens / global / typography / navigation / components / cards / data-display / verdicts / forms / utilities / dashboard / problem-list / problem-detail / course)
- [resources/style.scss](../resources/style.scss) — root entry, `@use "edu-theme"`

### Templates touched

- [templates/base.html](../templates/base.html) — body class `edu`, nav classes `edu-nav-*`, `edu-page`, `edu-main`, `edu-footer`, theme-color, fonts
- [templates/common-content.html](../templates/common-content.html) — `edu-workspace-*` classes
- [templates/chat/chat.html](../templates/chat/chat.html) — `bare` opt-out (was `arena_bare`)
- [templates/home.html](../templates/home.html) — include `home/learning-dashboard.html`
- [templates/home/learning-dashboard.html](../templates/home/learning-dashboard.html) (new) — greeting hero + courses

### Backend touched

- [judge/views/feed.py](../judge/views/feed.py) — `edu_dashboard` + `edu_courses` context.

### Audit artifacts

- [audit-screenshots/baseline-2026-05/](../audit-screenshots/baseline-2026-05/) — before
- [audit-screenshots/phase-1-de-arena/](../audit-screenshots/phase-1-de-arena/) — token swap
- [audit-screenshots/phase-2-foundation/](../audit-screenshots/phase-2-foundation/) — edu modules
- [audit-screenshots/phase-3-dashboard/](../audit-screenshots/phase-3-dashboard/) — learning home
- [audit-screenshots/phase-4-problem-list/](../audit-screenshots/phase-4-problem-list/) — problem list
- [audit-screenshots/phase-5-problem-detail/](../audit-screenshots/phase-5-problem-detail/) — problem detail + submit
- [audit-screenshots/phase-6-course/](../audit-screenshots/phase-6-course/) — course
- [audit-screenshots/sprint1-verify-2026-05-02/](../audit-screenshots/sprint1-verify-2026-05-02/) — sprint 1 baseline (12 surfaces × 2 VP)
- [audit-screenshots/round2-2026-05-03/](../audit-screenshots/round2-2026-05-03/) — round 2 audit + `findings.md`
- [audit-screenshots/round2-final-2026-05-03/](../audit-screenshots/round2-final-2026-05-03/) — after-fix subset (5 surfaces × 2 VP)
- [audit-screenshots/footer-check-2026-05-04/](../audit-screenshots/footer-check-2026-05-04/) — sprint 3 footer audit (12 surfaces × 2 VP) + findings
- [audit-screenshots/sprint3-2026-05-04/](../audit-screenshots/sprint3-2026-05-04/) — sprint 3 light + dark (12 × 2 × 2 = 48 screenshots) + findings

## 9. Phase log

### Round 2 — 2026-05-03 (polish & fix)

Audit 12 surfaces × 2 viewports (desktop 1440 / mobile 390). 0 P0, 7 P1, 9 P2, 9 P3/defer. Fixes landed:

- **#4 Course grid** (`_course.scss`): bỏ `max-width: 960px`, đổi grid sang `repeat(auto-fill, minmax(280px, 1fr))` để 1-2 card stretch fill middle column thay vì cụm trái.
- **#5 Course thumbnail icon** (`course/list.html` + `organization/course_list.html`): thay `{{ course.name|first|upper }}` bằng `<i class="fa fa-graduation-cap edu-course-thumb-icon">`. Style icon trong `_course.scss .course-image .edu-course-thumb-icon`.
- **#6 Users table mobile overflow** (`_ranklist.scss`): thêm `@media (max-width: 519px)` ẩn cột Problems để table chỉ còn rank · avatar · username · points.
- **#13 Problem-detail middle stretch** (`_problem-detail.scss`): cap `.edu-workspace-main { max-width: 820px @1280+ }` để briefing card không bị stretch quá rộng so với prose, sidebar phải không còn lơ lửng.
- **#16 Submissions pie chart legend** (`submission/list.html`): bật `legend.display = true, position = 'bottom'`, boxWidth 12. Verdict labels (Accepted / WA / TLE / IR / CE) render dưới chart.

Defer P2 (#2, #7, #8, #10, #14, #18, #24) sang sprint sau. WONTFIX #1 (DPR scaling), #25 (content-driven).

`!important` count: 439 (không tăng).

### Sprint 3 — 2026-05-04 (polish + dark mode + components)

Step 0 footer audit (12 surfaces × 2 VP): tất cả pass sticky-to-bottom (chat = bare, intended). Không có lỗi footer thực — `_global.scss` flex shell + `min-height:100vh` rule giữ footer đáy mọi trang.

Step 1 — close 7 OPEN từ round 2: #2 (heatmap legend wrap), #3 (mobile day labels visible), #7 + #14 (verified, không cần thêm rule), #8 (mobile select padding 12px), #10 (sidebox bg paper + edu chrome), #18 (pie chart cap 240px center).

Step 2 — Dark mode mở rộng (`_dark.scss` từ ~400 → ~600 dòng): course/contest/blog/chat/comments + generic tables + sidebox + heatmap dark counterparts + difficulty pill / toast / modal / skeleton dark variants + theme toggle UI.

Step 2.2 — Theme toggle button trong `edu-nav-utility` (`base.html:196-203`). Light/dark dual icon, localStorage persist, AJAX sync `/user/theme/toggle-darkmode/`.

Step 3 — 4 components mới:
- `edu-difficulty` 5 mức (helper/easy/medium/hard/expert) — Jinja `difficulty_pill(points)` từ `judge/jinja2/difficulty.py`. Wired vào `problem/list.html` + `problem/problem.html`.
- `edu-toast` snackbar — `window.eduToast.show({type, title, message, duration})`. Auto-render Django messages framework qua `base.html` script.
- `edu-skeleton` shimmer — CSS only, honour `prefers-reduced-motion`.
- `edu-modal` dialog — `window.eduModal.open(idOrEl)`, focus trap, ESC + click-outside close.

Verify: `e2e-audit/sprint3-audit.mjs` snapshot 48 screenshot (light + dark × desktop + mobile × 12 surface). Output `audit-screenshots/sprint3-2026-05-04/`. `findings.md` cùng folder.

`!important` count: ~500 (tăng do dark mode coverage thêm partial + sidebar widget legacy specificity).
