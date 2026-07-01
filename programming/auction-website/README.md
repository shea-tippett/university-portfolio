# Auction Website

This project is a small auction website implemented using WebMatrix / Razor (C#) and SQL for data retrieval. The screenshots included in this folder show the key pages and the server-side view code used to populate and render auction catalogues and individual lots.

## Overview

- Tech: Razor (C#), HTML/CSS, SQL (WebMatrix.Data), Bootstrap for basic layout.
- Purpose: Display auction catalogues, list lots, and show lot details with images and status (current, passed, sold).

---

## Project Structure

- `website-screenshots/` - visual screenshots of pages and code:
    - `auction_home` - Home page showing current/future and past auctions.
    - `auction_catalogue` - Catalogue page listing lots filtered by category, with search and status filters.
    - `auction_lot` - Lot detail page with images, descriptions and sale status.
- `code-screenshots/` - screenshots of server-side Razor code used to build pages:
    - `code_home` - SQL query and Razor loop for the homepage.
    - `code_catalogue_p1` / `code_catalogue_p2` - Catalogue page code showing query composition, search and dropdown filters.
    - `code_lot` - Lot detail page code including image queries and conditional status badges.

---

## Key Features

- Server-side SQL queries are used to fetch catalogue and lot data at the top of each Razor page.
- Filtering and search: pages read query strings and form values to filter results (e.g., `type`, `search`, `dropDown`).
- Status handling: lots show `SOLD`, `PASSED IN`, or active state with distinct UI badges depending on `salePrice`, `bidderID`, and `auctDateTime`.
- Image handling: lot images are fetched via a `LotImages` query and displayed with constrained height and `object-fit` styling for consistent thumbnails.
- Defensive UI: pages check `data.Count()` or null results and render friendly fallbacks when no items are found.

---

## Code Notes

- SQL is assembled dynamically in the Razor view and often includes `JOIN` statements to collect catalogue, auction, and image data.
- The catalogue page uses logic like `var sold = row.salePrice != null && row.bidderID != null;` and `var auctionHasPassed = row.auctDateTime < DateTime.Now;` to decide which badge to show.
- Links preserve search and filter parameters when navigating between catalogue and lot pages to keep UX consistent.

---

## Running or Inspecting Locally

To run the site locally (table data can be provided to populate SQL tables):

1. Install a .NET/Mono environment compatible with Razor views (or use WebMatrix if available).
2. Configure a SQL database with tables used by the queries (`Catalogues`, `Lots`, `LotImages`, `Auctions`, etc.).
3. Place the Razor pages into a WebMatrix/ASP.NET project and update the `Database.Open("AuctionDB")` connection string to match your environment.
4. Start the site and navigate to the home/catalogue/lot pages to view results.

## Tips for Further Improvement

- Extract SQL queries into a repository or data-access layer instead of building them inline in Razor views.
- Add unit/integration tests around query results and page rendering logic.
- Replace string concatenation of SQL with parameterised commands to avoid injection risks.
- Add README links to the exact screenshot files for quicker reference.