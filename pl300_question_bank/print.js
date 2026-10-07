// Print out/pl300_test_sets.html to ../PL-300_Practice_Test_Sets.pdf with Chromium.
const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto("file://" + path.join(__dirname, "out", "pl300_test_sets.html"));
  const footer = `<div style="font:7.5pt 'DejaVu Sans',sans-serif;color:#5b6475;width:100%;padding:0 15mm;display:flex;justify-content:space-between">
    <span>PL-300 · Practice Test Sets</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`;
  await page.pdf({
    path: path.join(__dirname, "..", "PL-300_Practice_Test_Sets.pdf"),
    format: "A4",
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate: footer,
    margin: { top: "16mm", bottom: "18mm", left: "15mm", right: "15mm" },
  });
  await browser.close();
  console.log("pdf written");
})();
