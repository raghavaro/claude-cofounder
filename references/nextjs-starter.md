# The Next.js starter

The stack, the files, and the two pieces of motion code worth getting right.
Everything here is deliberately small — a landing page is one route, and a
starter that needs explaining is a starter that gets abandoned.

## Stack

```sh
npx create-next-app@latest my-page --typescript --app --tailwind --eslint
cd my-page
npm i lenis
```

- **Next.js App Router** — one route, static, deploys anywhere.
- **Lenis** for smooth scroll. The package is `lenis`; the old
  `@studio-freight/*` packages are retired and the imports have moved.
- **No component library.** shadcn and friends are designed to be pasted by
  agents, which is exactly why their defaults are recognisable. A landing page
  is a handful of sections, not an app.
- **No animation library** unless something genuinely needs it. An
  IntersectionObserver is about fifteen lines and doesn't ship a runtime.

## Tokens first

Put the filled-in `DESIGN.md` block into `app/globals.css` as custom
properties, before writing any markup. Everything else reads from these:

```css
:root {
  --ground: #faf9f7;
  --ink: #16150f;
  --ink-muted: #57544a;
  --accent: #1b4d3e;
  --rule: #e4e0d8;

  --step-0: 1.0625rem;   /* body */
  --step-1: 1.375rem;
  --step-2: 2.125rem;
  --step-3: 3.5rem;      /* headline */

  --space-1: 0.5rem;
  --space-2: 1rem;
  --space-3: 2rem;
  --space-4: 4rem;
  --space-5: 7.5rem;     /* between sections */

  --radius: 4px;
  --measure: 68ch;
}

@media (prefers-color-scheme: dark) { /* only if you actually want dark mode */ }
```

Swap the values. The ones above are an example of *committing* to values, not a
palette to adopt.

## Smooth scroll

`ReactLenis` is a client component, so it needs a wrapper before it can go in a
server-rendered layout.

```tsx
// app/smooth-scroll.tsx
'use client'

import { useEffect, useState } from 'react'
import { ReactLenis } from 'lenis/react'
import 'lenis/dist/lenis.css'

export default function SmoothScroll({ children }: { children: React.ReactNode }) {
  // Off until we know the visitor hasn't asked for less motion. Starting off
  // means someone with reduced-motion set never gets a frame of it; starting
  // on would give them one and then take it away.
  const [smooth, setSmooth] = useState(false)

  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)')
    const update = () => setSmooth(!mq.matches)
    update()
    mq.addEventListener('change', update)
    return () => mq.removeEventListener('change', update)
  }, [])

  if (!smooth) return <>{children}</>

  return (
    <ReactLenis root options={{ lerp: 0.1, smoothWheel: true }}>
      {children}
    </ReactLenis>
  )
}
```

```tsx
// app/layout.tsx
import SmoothScroll from './smooth-scroll'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <SmoothScroll>{children}</SmoothScroll>
      </body>
    </html>
  )
}
```

The `lenis.css` import is required — without it the scroll container is wrong
and the page behaves strangely on touch devices.

## Reveals

Fifteen lines, no dependency, and — the part that matters — **the content is in
the DOM and visible by default.** Motion is added to it, so a failed script
leaves a readable page rather than a blank one.

```tsx
// app/reveal.tsx
'use client'

import { useEffect, useRef, useState } from 'react'

export default function Reveal({
  children,
  delay = 0,
}: {
  children: React.ReactNode
  delay?: number
}) {
  const ref = useRef<HTMLDivElement>(null)
  const [shown, setShown] = useState(false)

  useEffect(() => {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduced || !ref.current) {
      setShown(true)
      return
    }

    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setShown(true)
          io.disconnect()   // reveal once, never again
        }
      },
      { rootMargin: '0px 0px -12% 0px' },
    )
    io.observe(ref.current)
    return () => io.disconnect()
  }, [])

  return (
    <div
      ref={ref}
      data-shown={shown}
      style={{ transitionDelay: `${delay}ms` }}
      className="reveal"
    >
      {children}
    </div>
  )
}
```

```css
/* one direction, one distance, one duration — the whole motion system.
   Visible by default; hidden only where scripting exists to un-hide it, so a
   page whose JavaScript never runs still reads instead of rendering blank. */
.reveal {
  transition: opacity 400ms ease-out, transform 400ms ease-out;
}

@media (scripting: enabled) {
  .reveal {
    opacity: 0;
    transform: translateY(16px);
  }
  .reveal[data-shown='true'] {
    opacity: 1;
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; transform: none; transition: none; }
}
```

`@media (scripting: enabled)` is the whole trick, and it's the difference
between a page that degrades and a page that disappears. If you need to support
browsers that don't have it, set a `js` class on `<html>` from a blocking inline
script and scope the hidden state to `.js .reveal` instead — same idea, more
moving parts.

Wrap sections, not individual words. Stagger siblings with `delay={80}`,
`delay={160}` — and stop there. **Never wrap the hero.** It renders immediately.

## Structure

```
app/
  layout.tsx        html shell + SmoothScroll
  page.tsx          the whole landing page, sections in order
  globals.css       tokens, reveal, base type
  smooth-scroll.tsx client wrapper
  reveal.tsx        client wrapper
  opengraph-image.png
public/
  [the product screenshot or demo loop]
DESIGN.md           the filled-in token block
```

One route. If a second page appears, it's a privacy policy.

## Before it goes public

- The form posts somewhere real and you have tested it end to end
- Success and error states exist and say what happens next
- `<title>`, meta description, and an OG image — the link gets shared before
  anyone visits it
- Real text in the HTML, not text baked into images
- Lighthouse on mobile: under two seconds, no layout shift on the hero
- Tab through it once — the CTA is reachable and focus is visible
- Turn off JavaScript: the page still reads
- The screenshot is of the actual product

## Deploy

```sh
npx vercel        # or: npm run build && npx serve out
```

Point the domain at it, then open the live URL on a phone before telling anyone
it's up.
