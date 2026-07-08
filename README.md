# [Shooni](https://shooni-frontend.onrender.com)

![shooni_logo](/frontend/app/src/assets/images/halffatbird.png)

**Live demo:** https://shooni-frontend.onrender.com

## Project status

Shooni was originally built in 2022-2023 by a 5-person team through Georgia Tech's CREATE-X program, including Firebase auth, listing search/filter, and a reviews system. The startup didn't continue past that, and the project sat untouched for about three years. In 2026 I revived it as a working portfolio demo: re-provisioned GCP infrastructure from scratch (the original project was gone), reconnected the existing auth and reviews code to it, and implemented favorites and sublease listings — features the original team had planned but never built. All of this is deployed and live at the link above. The original listing scraper (`backend/backend_scrape`, `backend/scraper`) no longer works — target sites changed their markup or started blocking the crawler — so the live demo seeds sample listings into Firestore instead (`backend/seed_firestore.py`, `backend/seed_subleases.py`) rather than silently faking a working pipeline.

## 1. What is Shooni?
**tldr: a website that helps college students find their desired housing much faster and easier**

Our objective is to simplify the housing search process by providing a centralized location to help college students find their desired housing. Research into existing solutions from competitors like Apartments.com, Zillow, and Facebook showed that the market lacked a single platform that effectively centralized all desirable aspects, leading to an inefficient and complex search process. To address this, we built a user-friendly forum that lets students filter their search based on preferences, with features like a two-way rating system (agency/homeowner <-> renter), favorites, and sublease listings.

A roommate matching system and a community forum were also part of the original plan; they remain on the roadmap and aren't built yet.

## 2. Shooni System Overview
![system_overview](/images/sys_overview.png)

## 3. Tech Stack

- **Frontend:** Vue 3 + Vite + TypeScript, deployed as a static site on Render
- **Backend:** Python, deployed as individual Google Cloud Functions
- **Database:** Firestore
- **Auth:** Firebase Authentication

## 4. Repository Outline

```
Shooni
├── frontend
│   └── app                  Vue3 + Vite frontend
│
├── backend                  Python, deployed as GCP Cloud Functions
│   ├── backend_fetch         serves listings from Firestore to the frontend
│   ├── backend_review        submit / fetch / delete reviews
│   ├── backend_favorites     toggle / fetch favorited listings
│   ├── backend_sublease      submit / fetch / delete sublease listings
│   ├── backend_scrape        original listing scraper (non-functional, kept for reference)
│   ├── scraper                per-site scraper modules used by backend_scrape
│   ├── mock_server           local mock API for frontend dev without GCP
│   ├── seed_firestore.py     seeds sample apartment listings into Firestore
│   └── seed_subleases.py     seeds sample sublease listings into Firestore
│
└── render.yaml               Render blueprint for the frontend static site
```

## 5. Running Locally

**Frontend**
```
cd frontend/app
npm install
npm run dev
```
Requires a `.env` file in `frontend/app` with Firebase config and backend endpoint URLs (`VITE_FIREBASE_*`, `VITE_*_ENDPOINT_URL`, etc.) — see `frontend/app/src/firebase.ts` and `store/index.ts` for the full list of variables read at build time.

**Backend (without GCP)**

`backend/mock_server/serve.py` serves the same response shape as the real Cloud Functions, using fixture data — useful for frontend development without any GCP setup.

**Backend (real deploy)**

Each `backend_*` directory is an independent Cloud Function with its own `deploy.sh` and `requirements.txt`. Deploy with `gcloud` configured for your project:
```
cd backend/backend_review
./deploy.sh
```
