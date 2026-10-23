# HTML notes: books.toscrape.com

1. **Tag:** labels a piece of content with its type. An opening tag and a closing
   tag wrap the content into one element: `<p>£51.77</p>` marks the price as a paragraph.

2. **Attribute:** extra information about an element, written in the opening tag
   as name="value". `class` labels it (for CSS and for finding it), `href` says where
   a link goes, `src` where an image is, and `title` holds the full book title:
   title="A Light in the Attic".

3. **Class vs id:** a class is a group label many elements can share
   (product_pod appears 20 times, once per book). An id is a unique name that only
   one element may have (`<div id="messages">`). CSS selects them with .class and #id.

4. **Parent vs child:** a parent contains other elements, and a child sits directly
   inside its parent. `<article>` is the parent of `<h3>`, and `<h3>` is the parent
   of `<a>`, so `<a>` is the grandchild of `<article>`. It means "inside", not "is a kind of".

## Map for the scraper

- one book: <article class="product_pod">
- title: the title attribute of the <a> inside <h3>
- price: text of <p class="price_color">
- rating: second class word of <p class="star-rating ..."> (e.g. Three)
- stock: text of <p class="instock availability">, stripped of spaces