# Grid Layout


```html
...
<div class="layout">
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
</div>
...
```

```css{5-6}
.layout{
    height: 50vh;
    background-color: gray;

    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
}
.box{
    width: 100px;
    height: 100px;
    background-color: yellow;
}
```

<lv01-Grid-Grid gridTemplateColumns="1fr 1fr 1fr" />

## Spacing Layout

### FR

<br>
<lv01-Grid-FR gridTemplateColumns="1fr 1fr 1fr" />

<br>
<lv01-Grid-FR gridTemplateColumns="2fr 1fr 1fr" />

<br>
<lv01-Grid-FR gridTemplateColumns="2fr 1fr 2fr" />

<br>
<lv01-Grid-FR gridTemplateColumns="1fr 3fr 1fr" />

<br>
<lv01-Grid-FR gridTemplateColumns="2fr 2fr 2fr" />

<br>

### Gap

- column-gap
- row-gap

```css
.layout{
    ...
    column-gap: 1rem;
    ...
}
```

<lv01-Grid-FR gridTemplateColumns="1fr 1fr 1fr" columnGap="1rem" />

<br>

### Placing Items
- place-items = align-items + justify-items
- align-items (vertical axis), justify-items (horizontal axis)
  - start | center | end

```css{7-8}
.layout{
    height: 50vh;
    background-color: gray;

    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    align-items: end;
    justify-items: center;
    
}
.box{
    width: 100px;
    height: 100px;
    background-color: yellow;
}
```

<lv01-Grid-Grid gridTemplateColumns="1fr 1fr 1fr" justifyItems="center" alignItems="end" />

```css{7}
.layout{
    height: 50vh;
    background-color: gray;

    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    place-items:center;
    
}
.box{
    width: 100px;
    height: 100px;
    background-color: yellow;
}
```

<lv01-Grid-GridPlaceItems gridTemplateColumns="1fr 1fr 1fr" placeItems="center" />

## Try it yourself
- display: grid;
- grid-template-columns: {value}
- column-gap: {value}
- row-gap: {value}
- align-items: start | center | end
- justify-items: start | center | end

<hr>

<lv01-Grid-Index/>

## Workshops

### [CodeKids Classes Website](./08-01.md)

### [CodeKids Classes Website 2](./08-02.md)

