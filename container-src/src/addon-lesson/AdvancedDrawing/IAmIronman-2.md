# I AM IRONMAN with animation

<video controls>
<source :src="$withBase('/AdvancedDrawing/ironman-animation/output.mkv')" type="video/mp4" >
</video>

## project structure
```
+-- ironman-animation
|    +-- ironman_helmet.py
|    +-- main.py
|    +-- points.py
```

ironman_helmet.py

<<< @/src/.vuepress/public/AdvancedDrawing/ironman-animation/ironman_helmet.py

points.py
```py
ankur1 = [
        [0, 120],
        ...
        [40, 120],
        [0, 120],
]

ankur2 = [
        [0, -30],
        ...
        [40, -30],
        [0, -30],
]

ankur3 = [
        [0, -220],
        ...
        [60, -220],
        [0, -220],
]
```
<a :href="$withBase('/AdvancedDrawing/ironman-animation/points.py')">download points.py</a>

main.py

<<< @/src/.vuepress/public/AdvancedDrawing/ironman-animation/main.py


## (Optional) Remove drawing animation

main.py

<<< @/src/.vuepress/public/AdvancedDrawing/ironman-animation/main-remove-drawing-animation.py{12,24,34}


