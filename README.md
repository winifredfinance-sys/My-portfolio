# Winifred Ukoh: portfolio website

A plain HTML/CSS site. There's no build step, no database and nothing to pay for. Every page is an ordinary file you can open and edit.

```
index.html                     Home page
work/movam/index.html          Case study (each lives at /work/<name>/)
work/health-insurance/index.html
work/shopta/index.html
work/trustesse/index.html
work/edswot/index.html
work/brainbox-ninja/index.html
cv/index.html                  CV page
cv.pdf                         Your CV (replace with your latest file, same name)
404.html                       "Page not found"
assets/css/site.css            All styling (colours are at the top)
assets/js/site.js              Theme toggle, mobile menu, contents highlight
assets/img/                    Portrait (WebP + JPEG)
assets/og.png                  Link-preview image for LinkedIn, Slack, etc.
favicon.svg, favicon-32.png, apple-touch-icon.png
sitemap.xml, robots.txt, vercel.json
```

---

## 1. Publish on Vercel (free)

You'll need a free Vercel account. You already have one from Brainbox Ninja.

### Option A: drag and drop (simplest)

1. Unzip `winifred-ukoh-portfolio.zip`. You'll get a folder called `site`.
2. Go to **vercel.com/drop** and sign in.
3. Drag the **`site` folder** onto the page.
4. When asked, choose your team and type the project name **`winifredukoh`**. Click **Deploy**.
5. When it finishes, your site is live at **https://winifredukoh.vercel.app**. If that name is taken, Vercel will suggest a variant. If you get a different address, see "If your address is different" below.

**To update later:** open the project in your Vercel dashboard and drag the updated `site` folder onto it. That creates a new live version.

### Option B: GitHub (best if you'll update often)

1. On github.com, create a new repository called `portfolio`.
2. Click **"uploading an existing file"** and drag in everything *inside* the `site` folder. Click **Commit changes**.
3. In Vercel, click **Add New → Project**, import the `portfolio` repository and click **Deploy**. You don't need to change any settings.
4. From now on, every time you edit a file on GitHub and commit, Vercel republishes automatically within about a minute.

### If your address is different

The site's link-preview image and sitemap point to `https://winifredukoh.vercel.app`. If your address differs, use your text editor's find-and-replace across the whole folder (VS Code: Edit → Replace in Files) to swap `winifredukoh.vercel.app` for your real address, then redeploy.

---

## 2. Connect a custom domain (optional, about $10–12 a year)

1. Buy a domain such as `winifredukoh.com` from Namecheap, Porkbun or Cloudflare Registrar.
2. In Vercel, open your project, then go to **Settings → Domains → Add**, type the domain and click **Add**.
3. Vercel shows one or two DNS records (usually an **A** record and a **CNAME** for `www`). Copy them into your registrar's DNS settings.
4. Wait 10 minutes to a few hours. Vercel adds HTTPS automatically.
5. Find-and-replace `winifredukoh.vercel.app` with your new domain (see above) and redeploy.
6. Update the link on your CV, LinkedIn "Featured" section and job applications so they all match.

---

## 3. Edit text later

Open any `.html` file in a plain text editor. VS Code is free and colour-codes the file, which makes it easier to read. Find the sentence you want to change, edit it, save the file and redeploy.

- **Placeholders** look like `[Add start date]` and show on the site as a pale yellow highlight. Search the files for `class="ph"` to find them all. Replace the whole `<span class="ph">[…]</span>` with your text.
- **Your CV:** replace `cv.pdf` with your new file, keeping the name `cv.pdf`.
- **Portrait:** replace both files in `assets/img/` and keep the same names. Use a 4:5 crop of about 760 × 950 px.
- **Colours:** at the top of `assets/css/site.css`. The accent is `--acc`.
- **Read times** ("5 min read") are typed into each page. If you add a lot of text, raise them at about 220 words a minute.
- **The "Next case study" order** runs Movam → Health insurer → Shopta → Trustesse → Edswot → Brainbox Ninja → Movam.

To check a change before publishing, double-click `index.html` to open it in your browser. Links between pages work best once deployed.

---

## 4. See which case studies employers read (free)

The analytics code is already in every page. You only need to switch it on:

1. In Vercel, open your project and click **Analytics**.
2. Click **Enable** and choose Web Analytics on the free Hobby plan.
3. Redeploy once (drag the folder again, or commit any small change on GitHub).

After that, the **Analytics** tab shows visits per page, for example `/work/movam/`, plus referrers such as LinkedIn and countries. It uses no cookies, so you don't need a cookie banner. The free plan has a monthly event limit, which is plenty for a portfolio.

**Tip:** link straight to a case study in applications, e.g. `winifredukoh.vercel.app/work/shopta/`, so you can see it was opened.

---

## 5. Printing

Case studies have a print layout. The menu and buttons are hidden, and the diagrams and the TL;DR box print on white. Use your browser's Print → Save as PDF to send one as a document.
