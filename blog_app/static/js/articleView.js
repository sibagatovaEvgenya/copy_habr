function setView() {
    const cookie = document.cookie || "";
    const cookiesData = getCookieData(cookie);
    let viewingArticles = [];

    if (cookiesData.viewing_article) {
        viewingArticles = cookiesData.viewing_article.split(",");
    }

    const articleId = document.getElementById(
        "article_id"
    ).value;

    if (!viewingArticles.includes(articleId)) {
        viewingArticles.push(articleId);
        const ids = viewingArticles.join(",");
        document.cookie = `viewing_article=${ids}`;
    }

}
function getCookieData(cookieStr) {
    cookiesParts = cookieStr.split(";");
    result = {}

    cookiesParts.forEach((cookie) => {
        if (cookie.includes("=")) {
            oneCookiePart = cookie.split("=");
            result[oneCookiePart[0]] = oneCookiePart[1];
        }
    });

    return result;
}

document.addEventListener(
    "DOMContentLoaded",
    setView
)