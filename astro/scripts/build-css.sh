#!/bin/bash
# Build optimized CSS bundles
# Usage: ./scripts/build-css.sh

STYLES_DIR="/home/hermes/www.burncloud.com/astro/public/styles"
PAGES_DIR="$STYLES_DIR/pages"

echo "Building optimized CSS bundles..."

# Common (base + components) - shared by all pages
cat "$STYLES_DIR/base.css" "$STYLES_DIR/components.css" > "$STYLES_DIR/common.css"
echo "✓ common.css ($(wc -c < "$STYLES_DIR/common.css" | awk '{print int($1/1024)"KB"}') KB)"

# Page-specific bundles (without common, will be loaded separately)
# Home page (index.astro)
cat "$PAGES_DIR/home.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/home.bundle.css"
echo "✓ home.bundle.css ($(wc -c < "$STYLES_DIR/pages/home.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

# Blog pages (blog/index.astro, blog/[slug].astro)
cat "$PAGES_DIR/blog.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/blog.bundle.css"
echo "✓ blog.bundle.css ($(wc -c < "$STYLES_DIR/pages/blog.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

# Models pages (models/index.astro, models/[slug].astro)
cat "$PAGES_DIR/models.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/models.bundle.css"
echo "✓ models.bundle.css ($(wc -c < "$STYLES_DIR/pages/models.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

# Pricing page (pricing.astro)
cat "$PAGES_DIR/pricing.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/pricing.bundle.css"
echo "✓ pricing.bundle.css ($(wc -c < "$STYLES_DIR/pages/pricing.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

# Compare pages (compare.astro, compare/*.astro)
cat "$PAGES_DIR/compare.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/compare.bundle.css"
echo "✓ compare.bundle.css ($(wc -c < "$STYLES_DIR/pages/compare.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

# Security page (security.astro)
cat "$PAGES_DIR/security.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/security.bundle.css"
echo "✓ security.bundle.css ($(wc -c < "$STYLES_DIR/pages/security.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

# Docs page (docs/quickstart.astro)
cat "$PAGES_DIR/docs.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/docs.bundle.css"
echo "✓ docs.bundle.css ($(wc -c < "$STYLES_DIR/pages/docs.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

# Alternatives page (alternatives/*.astro)
cat "$PAGES_DIR/alternatives.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/alternatives.bundle.css"
echo "✓ alternatives.bundle.css ($(wc -c < "$STYLES_DIR/pages/alternatives.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

# Use cases page (use-cases/*.astro)
cat "$PAGES_DIR/use-cases.css" "$STYLES_DIR/responsive.css" > "$STYLES_DIR/pages/use-cases.bundle.css"
echo "✓ use-cases.bundle.css ($(wc -c < "$STYLES_DIR/pages/use-cases.bundle.css" | awk '{print int($1/1024)"KB"}') KB)"

echo ""
echo "All CSS bundles built successfully!"
echo ""
echo "Bundle sizes:"
ls -la "$STYLES_DIR"/*.css "$STYLES_DIR/pages"/*.bundle.css | awk '{print $9, int($5/1024)"KB"}'