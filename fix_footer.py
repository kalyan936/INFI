fix_css = """
<style>

/* Footer alignment fix */
.elementor-element-f977387 .e-con-inner {
  max-width: 1200px !important;
  margin: 0 auto !important;
}

.elementor-element-f977387 > .e-con-inner {
  display: grid !important;
  grid-template-columns: 1.6fr 1fr 1fr 1fr !important;
  gap: 60px !important;
  align-items: start !important;
}

.elementor-element-f977387 ul,
.elementor-element-f977387 li {
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
}

.elementor-element-f977387 a,
.elementor-element-f977387 li,
.elementor-element-f977387 .elementor-icon-list-text {
  white-space: nowrap !important;
  word-break: keep-all !important;
  overflow-wrap: normal !important;
  line-height: 1.7 !important;
}

.elementor-element-f977387 .elementor-widget-heading {
  margin-bottom: 22px !important;
}

@media (max-width: 900px) {
  .elementor-element-f977387 > .e-con-inner {
    grid-template-columns: 1fr 1fr !important;
    gap: 35px !important;
  }
}

@media (max-width: 600px) {
  .elementor-element-f977387 > .e-con-inner {
    grid-template-columns: 1fr !important;
  }

  .elementor-element-f977387 a,
  .elementor-element-f977387 li,
  .elementor-element-f977387 .elementor-icon-list-text {
    white-space: normal !important;
  }
}

</style>
"""
