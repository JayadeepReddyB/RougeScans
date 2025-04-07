function reverseChapters() {
    const chapterRowsContainer = document.getElementById("chapterRows");
    const chapterRows = Array.from(chapterRowsContainer.querySelectorAll(".chapter-row"));

    // Remove rows
    chapterRows.forEach(row => row.remove());

    // Reverse and append
    chapterRows.reverse().forEach(row => chapterRowsContainer.appendChild(row));
}

document.addEventListener("DOMContentLoaded", function () {
    const reverseIcon = document.getElementById("reverseIcon");
    if (reverseIcon) {
        reverseIcon.addEventListener("click", reverseChapters);
    }
});