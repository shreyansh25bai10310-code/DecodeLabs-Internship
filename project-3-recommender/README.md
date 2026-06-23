# Project 3 — AI Tech Stack Recommender

**DecodeLabs AI Internship | Batch 2026**

## Overview
A content-based filtering recommendation engine that maps user skills
to the most relevant tech career paths using TF-IDF and Cosine Similarity.
Fully browser-based — zero dependencies, zero backend.

## Key Concepts
- Content-based filtering (no historical user data needed)
- TF-IDF weighting (penalizes generic skills, rewards specific ones)
- Cosine similarity (orientation-based matching, magnitude-invariant)
- IPO model: Input → Process → Output
- Cold start handling via onboarding skill selection
- Top-N ranked recommendations

## How to Use
Open `index.html` directly in any browser — no server needed.

## Live Demo
[View Live on GitHub Pages](https://shreyansh25bai10310-code.github.io/DecodeLabs-Internship/project-3-recommender/)

## Pipeline
1. User selects 3+ skills
2. Skills are encoded into TF-IDF weighted vectors
3. Cosine similarity is calculated against 15 job role catalogues
4. Top 3 matching career paths returned with match percentage

## Tech Stack
- HTML5 / CSS3 / Vanilla JavaScript
- No frameworks, no libraries, no backend
