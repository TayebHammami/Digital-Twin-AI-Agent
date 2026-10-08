"""Styling and frontend helpers for the Digital Twin Gradio app."""

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]


CSS = r"""
/* ============================================================
   DIGITAL TWIN — PREMIUM AI INTERFACE
   Gradio ChatInterface / Chatbot
   ============================================================ */

:root {
  --twin-accent: #7c6cff;
  --twin-accent-2: #2dd4bf;
  --twin-accent-soft: rgba(124, 108, 255, 0.12);
  --twin-accent-glow: rgba(124, 108, 255, 0.24);

  --twin-bg: #090a0f;
  --twin-surface: #101218;
  --twin-surface-2: #151821;
  --twin-surface-hover: #191c26;

  --twin-border: rgba(255, 255, 255, 0.08);
  --twin-border-hover: rgba(255, 255, 255, 0.14);

  --twin-text: #f4f5f7;
  --twin-muted: #9298a8;
  --twin-subtle: #626978;

  --twin-user: #6658f5;
  --twin-user-text: #ffffff;

  --twin-radius-sm: 8px;
  --twin-radius-md: 12px;
  --twin-radius-lg: 18px;
  --twin-radius-xl: 24px;

  --twin-column: 920px;

  --twin-font: Inter, "Instrument Sans", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --twin-heading: Inter, "Bricolage Grotesque", system-ui, sans-serif;
  --twin-mono: "SF Mono", "Cascadia Code", Consolas, monospace;
}


/* ============================================================
   LIGHT MODE
   ============================================================ */

body:not(.dark),
html[data-theme="light"] {
  --twin-bg: #f6f7fb;
  --twin-surface: #ffffff;
  --twin-surface-2: #f1f2f7;
  --twin-surface-hover: #eceef5;

  --twin-border: rgba(15, 23, 42, 0.08);
  --twin-border-hover: rgba(15, 23, 42, 0.14);

  --twin-text: #171923;
  --twin-muted: #687083;
  --twin-subtle: #8d94a5;

  --twin-accent: #5f54df;
  --twin-accent-soft: rgba(95, 84, 223, 0.09);

  --twin-user: #5f54df;
}


/* ============================================================
   GLOBAL
   ============================================================ */

html,
body,
gradio-app {
  margin: 0 !important;
  min-height: 100dvh !important;
  background: var(--twin-bg) !important;
}

body {
  font-family: var(--twin-font) !important;
  color: var(--twin-text) !important;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}


/* ============================================================
   MAIN CONTAINER
   ============================================================ */

.gradio-container {
  width: 100% !important;
  max-width: none !important;
  min-height: 100dvh !important;
  box-sizing: border-box !important;
  margin: 0 !important;
  padding: 24px clamp(16px, 4vw, 40px) 28px !important;
  background:
    radial-gradient(circle at 50% -20%, var(--twin-accent-soft), transparent 45%),
    var(--twin-bg) !important;
  color: var(--twin-text) !important;
}

.gradio-container .main {
  width: 100% !important;
  max-width: var(--twin-column) !important;
  margin: 0 auto !important;
}


/* ============================================================
   HIDE GRADIO DEFAULT ELEMENTS
   ============================================================ */

footer,
.built-with,
.show-api,
.api-docs {
  display: none !important;
}


/* ============================================================
   REMOVE DEFAULT GRADIO PANELS
   ============================================================ */

.block,
.form,
.contain {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}


/* ============================================================
   HEADER
   ============================================================ */

#twin-header {
  margin-bottom: 16px !important;
}

.gradio-container h1 {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  margin: 0 !important;
  padding: 0 !important;
  font-family: var(--twin-heading) !important;
  font-size: 22px !important;
  font-weight: 750 !important;
  line-height: 1.2 !important;
  letter-spacing: -0.035em !important;
  color: var(--twin-text) !important;
}

.gradio-container h1::before {
  content: "";
  width: 38px;
  height: 38px;
  flex: 0 0 38px;
  border-radius: 12px;
  background:
    radial-gradient(circle at 30% 50%, #8b7cff 0 26%, transparent 28%),
    radial-gradient(circle at 70% 50%, #32d6bd 0 26%, transparent 28%),
    linear-gradient(135deg, rgba(255, 255, 255, .04), rgba(255, 255, 255, 0));
  box-shadow:
    inset 0 0 0 1px var(--twin-border),
    0 8px 26px var(--twin-accent-glow);
}

.gradio-container h1 + p {
  margin: 7px 0 18px 50px !important;
  max-width: 680px !important;
  color: var(--twin-muted) !important;
  font-size: 13px !important;
  line-height: 1.55 !important;
}

/* A "# Heading" inside a reply is content, not the page title:
   no twin mark, no flex row, no subtitle styling. */
#twin-chatbot h1 {
  display: block !important;
  gap: 0 !important;
}

#twin-chatbot h1::before {
  content: none !important;
}

#twin-chatbot h1 + p {
  color: inherit !important;
  max-width: 74ch !important;
}


/* ============================================================
   CHAT CONTAINER
   ============================================================ */

#twin-chatbot {
  position: relative !important;
  height: calc(100dvh - 260px) !important;
  min-height: 430px !important;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.018), transparent 20%),
    var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-xl) !important;
  box-shadow:
    0 24px 80px rgba(0, 0, 0, .16),
    inset 0 1px 0 rgba(255, 255, 255, .02) !important;
  overflow: hidden !important;
}


/* ============================================================
   CHAT CONTENT
   ============================================================ */

#twin-chatbot .bubble-wrap,
#twin-chatbot .messages {
  padding: 24px !important;
  scrollbar-gutter: stable;
  overscroll-behavior: contain;
}


/* ============================================================
   MESSAGE ROW
   ============================================================ */

#twin-chatbot .message-row {
  margin-bottom: 8px !important;
}


/* ============================================================
   GLOBAL WRAPPER RESET
   ============================================================ */

#twin-chatbot .message-row > div,
#twin-chatbot .message-wrap,
#twin-chatbot .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}


/* ============================================================
   GENERIC MESSAGE
   ============================================================ */

#twin-chatbot .message,
#twin-chatbot .message-bubble,
#twin-chatbot .bubble {
  font-size: 15px !important;
  line-height: 1.7 !important;
  border: 0 !important;
  box-shadow: none !important;
}


/* ============================================================
   USER MESSAGE

   The bubble is capped with a FIXED length, never a percentage.
   The wrappers above it are width:auto (shrink-to-fit), and a
   percentage max-width inside a shrink-to-fit parent is circular:
   the parent is sized to the text, then the bubble is cut to a
   fraction of that. That made one-word messages wrap letter by
   letter and left phrases sitting in extra invisible space.
   ============================================================ */

/* Row: pushes the bubble to the right edge. */
#twin-chatbot .message-row.user-row,
#twin-chatbot .message-row[data-role="user"] {
  display: flex !important;
  justify-content: flex-end !important;
  align-items: flex-start !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 0 12px !important;
  padding: 0 !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* Wrappers between the row and the bubble: size to content, no chrome. */
#twin-chatbot .message-row.user-row > *,
#twin-chatbot .message-row[data-role="user"] > * {
  flex: 0 1 auto !important;
  width: auto !important;
  min-width: 0 !important;
  max-width: 100% !important;   /* % of the full-width row, so no cycle */
  margin: 0 !important;
  padding: 0 !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  outline: none !important;
}

/* The bubble itself. */
#twin-chatbot .message-row.user-row .message,
#twin-chatbot .message-row[data-role="user"] .message {
  display: block !important;
  position: relative !important;
  width: fit-content !important;
  min-width: 0 !important;
  max-width: min(680px, calc(100vw - 110px)) !important;
  margin: 0 !important;
  padding: 9px 14px !important;
  box-sizing: border-box !important;
  background: var(--twin-user) !important;
  color: var(--twin-user-text) !important;
  border: 0 !important;
  border-radius: 18px 18px 5px 18px !important;
  box-shadow: 0 6px 20px rgba(98, 85, 232, .16) !important;
  font-size: 15px !important;
  line-height: 1.45 !important;
  text-align: left !important;
  white-space: normal !important;
  overflow-wrap: break-word !important;
  word-break: normal !important;
}

/* Text wrappers inside the bubble: no extra padding, margin or background.
   Gradio's own wrappers are the usual source of a "big padding" look.
   Icon buttons (copy, edit) are deliberately left out. */
#twin-chatbot .message-row.user-row .message :where(.message-content, .prose, p),
#twin-chatbot .message-row[data-role="user"] .message :where(.message-content, .prose, p),
#twin-chatbot .message-row.user-row .message :where(.prose, p) span,
#twin-chatbot .message-row[data-role="user"] .message :where(.prose, p) span {
  min-width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  color: inherit !important;
  font: inherit !important;
  text-align: left !important;
}

#twin-chatbot .message-row.user-row .message p,
#twin-chatbot .message-row[data-role="user"] .message p {
  display: block !important;
  color: #ffffff !important;
  font-size: 15px !important;
  line-height: 1.45 !important;
}

#twin-chatbot .message-row.user-row .message a,
#twin-chatbot .message-row[data-role="user"] .message a {
  color: #ffffff !important;
  text-decoration: underline !important;
  border: 0 !important;
}

#twin-chatbot .message-row.user-row .message :where(ul, ol),
#twin-chatbot .message-row[data-role="user"] .message :where(ul, ol) {
  margin: 0 !important;
  padding-left: 1.2em !important;
}


/* ============================================================
   ASSISTANT ROW
   ============================================================ */

#twin-chatbot .message-row.bot-row,
#twin-chatbot .message-row[data-role="assistant"] {
  display: flex !important;
  justify-content: flex-start !important;
  align-items: flex-start !important;
  width: 100% !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}


/* ============================================================
   ASSISTANT MESSAGE
   ============================================================ */

#twin-chatbot .message-row.bot-row .message,
#twin-chatbot .message-row[data-role="assistant"] .message {
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 8px 8px 18px !important;
  background: transparent !important;
  color: var(--twin-text) !important;
  text-align: left !important;
  border: 0 !important;
  box-shadow: none !important;
}


/* ============================================================
   ASSISTANT CONTENT WIDTH
   ============================================================ */

#twin-chatbot .message-row[data-role="assistant"] .message :where(p, ul, ol, blockquote, h1, h2, h3, h4, pre, table) {
  max-width: 74ch;
}


/* ============================================================
   TEXT
   ============================================================ */

#twin-chatbot .message p {
  margin: 0 0 12px !important;
  font-size: 15.5px !important;
  line-height: 1.72 !important;
}

#twin-chatbot .message p:last-child {
  margin-bottom: 0 !important;
}


/* ============================================================
   HEADINGS
   ============================================================ */

#twin-chatbot .message h1,
#twin-chatbot .message h2,
#twin-chatbot .message h3 {
  font-family: var(--twin-heading) !important;
  font-weight: 750 !important;
  letter-spacing: -0.025em !important;
  color: var(--twin-text) !important;
}

#twin-chatbot .message h1 { font-size: 22px !important; }
#twin-chatbot .message h2 { font-size: 19px !important; }
#twin-chatbot .message h3 { font-size: 17px !important; }


/* ============================================================
   LISTS
   ============================================================ */

#twin-chatbot .message ul,
#twin-chatbot .message ol {
  padding-left: 22px !important;
}

#twin-chatbot .message li {
  margin: 5px 0 !important;
}


/* ============================================================
   LINKS
   ============================================================ */

#twin-chatbot .message a {
  color: var(--twin-accent) !important;
  text-decoration: none !important;
  border-bottom: 1px solid color-mix(in srgb, var(--twin-accent) 35%, transparent);
}

#twin-chatbot .message a:hover {
  border-color: var(--twin-accent);
  opacity: .82;
}


/* ============================================================
   QUOTES
   ============================================================ */

#twin-chatbot .message blockquote {
  margin: 14px 0 !important;
  padding: 8px 14px !important;
  border-left: 3px solid var(--twin-accent) !important;
  background: var(--twin-accent-soft) !important;
  color: var(--twin-muted) !important;
  border-radius: 0 10px 10px 0 !important;
}


/* ============================================================
   CODE
   ============================================================ */

#twin-chatbot .message code {
  font-family: var(--twin-mono) !important;
  font-size: .88em !important;
  padding: 3px 7px !important;
  background: var(--twin-surface-2) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 7px !important;
}

#twin-chatbot .message pre {
  margin: 14px 0 !important;
  padding: 16px !important;
  overflow-x: auto !important;
  background: #0b0d12 !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 14px !important;
}

body:not(.dark) #twin-chatbot .message pre {
  background: #171923 !important;
}

#twin-chatbot .message pre code {
  padding: 0 !important;
  background: transparent !important;
  border: 0 !important;
  color: #e7e9ee !important;
}


/* ============================================================
   INPUT
   ============================================================ */

#twin-input-area {
  margin-top: 12px !important;
}

#twin-input-area textarea,
#twin-input-area input[type="text"] {
  min-height: 52px !important;
  box-sizing: border-box !important;
  padding: 14px 16px !important;
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border-hover) !important;
  border-radius: var(--twin-radius-md) !important;
  color: var(--twin-text) !important;
  font-family: var(--twin-font) !important;
  font-size: 15px !important;
  line-height: 1.5 !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, .05) !important;
  transition: border-color .2s ease, box-shadow .2s ease !important;
}

#twin-input-area textarea:focus,
#twin-input-area input[type="text"]:focus {
  border-color: var(--twin-accent) !important;
  box-shadow:
    0 0 0 3px var(--twin-accent-soft),
    0 8px 30px rgba(0, 0, 0, .08) !important;
  outline: none !important;
}

#twin-input-area textarea::placeholder,
#twin-input-area input::placeholder {
  color: var(--twin-subtle) !important;
}


/* ============================================================
   SEND BUTTON
   ============================================================ */

#twin-input-area button {
  min-height: 52px !important;
  border-radius: var(--twin-radius-md) !important;
  font-family: var(--twin-font) !important;
}

#twin-input-area button.primary,
#twin-input-area button[variant="primary"],
#twin-input-area button.submit,
#twin-input-area button.submit-button {
  width: 52px !important;
  height: 52px !important;
  padding: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  align-self: flex-end !important;
  background: linear-gradient(135deg, #8a7dff, var(--twin-accent)) !important;
  border: 0 !important;
  color: #fff !important;
  box-shadow: 0 8px 25px var(--twin-accent-glow) !important;
  transition:
    transform .15s ease,
    box-shadow .15s ease,
    filter .15s ease !important;
}

#twin-input-area button.primary:hover,
#twin-input-area button.submit:hover,
#twin-input-area button.submit-button:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
  box-shadow: 0 12px 30px var(--twin-accent-glow) !important;
}

#twin-input-area button.primary:active,
#twin-input-area button.submit:active,
#twin-input-area button.submit-button:active {
  transform: translateY(1px) scale(.98);
}


/* ============================================================
   EXAMPLES
   ============================================================ */

.examples,
.examples-holder,
[data-testid="examples"] {
  margin-top: 12px !important;
  padding: 0 !important;
  background: transparent !important;
}

.examples table,
.examples-table {
  background: transparent !important;
  border: 0 !important;
}

.examples button,
.example,
.examples td button,
[data-testid="examples"] button {
  min-height: 42px !important;
  padding: 9px 14px !important;
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 12px !important;
  color: var(--twin-muted) !important;
  font-family: var(--twin-font) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  transition:
    color .15s ease,
    border-color .15s ease,
    background .15s ease,
    transform .15s ease !important;
}

.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover {
  color: var(--twin-text) !important;
  border-color: color-mix(in srgb, var(--twin-accent) 45%, var(--twin-border)) !important;
  background: var(--twin-accent-soft) !important;
  transform: translateY(-1px);
}


/* ============================================================
   SCROLLBAR
   ============================================================ */

* {
  scrollbar-width: thin;
  scrollbar-color: var(--twin-border-hover) transparent;
}

::-webkit-scrollbar { width: 7px; height: 7px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--twin-border-hover); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: var(--twin-accent); }


/* ============================================================
   ACCESSIBILITY
   ============================================================ */

:focus-visible {
  outline: 2px solid var(--twin-accent) !important;
  outline-offset: 3px !important;
}

::selection {
  background: var(--twin-accent) !important;
  color: #fff !important;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 640px) {

  .gradio-container {
    padding: 14px 12px 18px !important;
  }

  .gradio-container h1 {
    font-size: 18px !important;
  }

  .gradio-container h1::before {
    width: 34px;
    height: 34px;
    flex-basis: 34px;
    border-radius: 10px;
  }

  .gradio-container h1 + p {
    margin-left: 46px !important;
    margin-bottom: 12px !important;
  }

  #twin-chatbot {
    height: calc(100dvh - 245px) !important;
    min-height: 360px !important;
    border-radius: 16px !important;
  }

  #twin-chatbot .bubble-wrap,
  #twin-chatbot .messages {
    padding: 16px !important;
  }

  /* Fixed length, not a percentage (see USER MESSAGE above). */
  #twin-chatbot .message-row.user-row .message,
  #twin-chatbot .message-row[data-role="user"] .message {
    max-width: calc(100vw - 100px) !important;
    padding: 9px 13px !important;
  }

  #twin-chatbot .message {
    font-size: 15px !important;
  }

  .examples {
    display: flex !important;
    flex-wrap: nowrap !important;
    gap: 8px !important;
    overflow-x: auto !important;
    padding-bottom: 4px !important;
  }

  .examples button {
    flex: none !important;
    max-width: 78vw !important;
  }
}


/* ============================================================
   REDUCED MOTION
   ============================================================ */

@media (prefers-reduced-motion: reduce) {

  *,
  *::before,
  *::after {
    animation: none !important;
    transition: none !important;
  }
}
"""


JS = r"""() => {
  document.title = "Digital Twin";

  let meta = document.querySelector('meta[name="theme-color"]');

  if (!meta) {
    meta = document.createElement("meta");
    meta.name = "theme-color";
    document.head.appendChild(meta);
  }

  meta.setAttribute("content", "#090a0f");
}"""